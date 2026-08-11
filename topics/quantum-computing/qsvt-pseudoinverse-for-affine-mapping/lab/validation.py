"""Independent validation layers (PRD section 17, plus the checks that section misses).

The PRD asks for four validations. Four is not enough to catch the ways this lab can be
silently wrong, so six more are here:

  * the QSP phase gate, checked in pure 2x2 arithmetic BEFORE any circuit is built --
    this is the only step that can genuinely fail to converge, so it is isolated;
  * the circuit-vs-numpy amplitude comparison, which catches gate-ordering and
    qubit-ordering mistakes that leave the maths intact but the circuit wrong;
  * the index convention itself, asserted at runtime rather than trusted to a comment;
  * the phase ancilla actually uncomputing;
  * the full normalization identity of PRD section 11;
  * the scale recovery of PRD section 19.
"""

import numpy as np
from scipy.stats import chisquare

from block_encoding import RectangularBlockEncoding
from classical_affine import B_TRUE, Z, generate_targets, solve_affine
from qsvt_polynomial import QSPPhases, SingularValuePolynomial, qsp_scalar
from quantum_solver import QuantumPseudoInverse
from sign_recovery import recover_signs


class Check:
    def __init__(self):
        self.rows = []

    def add(self, name, ok, measured, threshold):
        self.rows.append((name, bool(ok), measured, threshold))
        return ok

    def report(self):
        width = max(len(r[0]) for r in self.rows) + 2
        print("=" * (width + 42))
        print("VALIDATION")
        print("=" * (width + 42))
        for name, ok, measured, threshold in self.rows:
            print(f"{'PASS' if ok else 'FAIL'}  {name:<{width}} {measured:<20} {threshold}")
        n_ok = sum(r[1] for r in self.rows)
        print("-" * (width + 42))
        print(f"{n_ok}/{len(self.rows)} checks pass")
        return n_ok == len(self.rows)


def check_index_convention(checks):
    """Qiskit's statevector index must equal our numpy matrix index.

    Everything in this lab depends on "basis state |j>" meaning the same thing to numpy
    and to Qiskit. Qiskit is little-endian: passing [sys[0], sys[1], sys[2]] makes sys[0]
    the least significant bit, which is the convention numpy indexing already uses. That
    is easy to get wrong and invisible when it is wrong, so it gets a real test.
    """
    from qiskit import QuantumCircuit
    from qiskit.circuit.library import StatePreparation, UnitaryGate
    from qiskit.quantum_info import Statevector

    errs = []
    for j in range(8):
        v = np.zeros(8)
        v[j] = 1.0
        qc = QuantumCircuit(3)
        qc.append(StatePreparation(v), [0, 1, 2])
        errs.append(np.max(np.abs(np.asarray(Statevector(qc).data) - v)))

    # and a non-symmetric unitary, which catches transposes that basis states cannot
    rng = np.random.default_rng(7)
    M = np.linalg.qr(rng.normal(size=(8, 8)))[0]
    v = rng.normal(size=8)
    v /= np.linalg.norm(v)
    qc = QuantumCircuit(3)
    qc.append(StatePreparation(v), [0, 1, 2])
    qc.append(UnitaryGate(M), [0, 1, 2])
    errs.append(np.max(np.abs(np.asarray(Statevector(qc).data) - M @ v)))

    err = float(max(errs))
    checks.add("index convention (Qiskit LE == numpy)", err < 1e-12, f"{err:.3e}", "< 1e-12")


def run_all(shots=20000, verbose=True):
    checks = Check()
    Y = generate_targets()

    # ---------------------------------------------------------- A: classical baseline
    B_cls = solve_affine(Z, Y)
    err_A = float(np.linalg.norm(B_cls - B_TRUE))
    checks.add("A  classical affine fit", err_A < 1e-12, f"{err_A:.3e}", "< 1e-12")

    # -------------------------------------------------------------- B: block unitary
    enc = RectangularBlockEncoding(Z)
    ok_B, errs_B = enc.verify(verbose=False)
    checks.add("B  block unitary U^T U = I", ok_B, f"{errs_B['unitarity']:.3e}", "< 1e-12")
    checks.add("B  adjoint block = A^T", errs_B["adjoint_block"] < 1e-12,
               f"{errs_B['adjoint_block']:.3e}", "< 1e-12")

    # ------------------------------------------------------ C: singular-value function
    poly = SingularValuePolynomial(enc.singular_values)
    err_C = float(poly.singular_value_errors().max())
    checks.add("C  p(sigma_i) = C/sigma_i", err_C < 1e-10, f"{err_C:.3e}", "< 1e-10")
    ok_bound, sup = poly.verify_bound()
    checks.add("C  sup|p| <= 1 on [-1,1]", ok_bound, f"{sup:.6f}", "<= 1")

    # --------------------------------------------- QSP phase gate (before any circuit)
    qsp = QSPPhases(poly)
    qsp.solve()
    checks.add("   QSP phase fit (2x2, pre-circuit)", qsp.error < 1e-10, f"{qsp.error:.3e}", "< 1e-10")

    # ------------------------------------------------------------- index convention
    check_index_convention(checks)

    # ---------------------------------------------------------------- QSVT operator
    solver = QuantumPseudoInverse(enc, poly, qsp.phases)
    ok_op, errs_op = solver.verify_operator(verbose=False)
    checks.add("   QSVT block = C*alpha*pinv(Z)", ok_op,
               f"{errs_op['vs_scaled_pseudoinverse']:.3e}", "< 1e-10")

    # ------------------------------------------------------- D: per-column quantum run
    for name, col in (("X", 0), ("Y", 1)):
        y = Y[:, col]
        ok_c, errs_c = solver.verify_circuit(y, verbose=False)
        checks.add(f"   circuit == numpy ({name})", ok_c, f"{errs_c['amplitude_error']:.3e}", "< 1e-10")
        checks.add(f"   phase ancilla uncomputes ({name})", errs_c["ancilla_leak"] < 1e-12,
                   f"{errs_c['ancilla_leak']:.3e}", "< 1e-12")

        r = solver.solve_statevector(y)
        checks.add(f"D  fidelity vs classical beta ({name})", r["fidelity"] > 0.999,
                   f"{r['fidelity']:.12f}", "> 0.999")

        total = float(np.sum(np.abs(r["success_amplitudes"]) ** 2) + r["P_F"])
        checks.add(f"   |A1|^2+|A2|^2+|A3|^2 + P_F = 1 ({name})", abs(total - 1.0) < 1e-12,
                   f"{abs(total - 1.0):.3e}", "< 1e-12")

        scale_err = abs(r["beta_norm"] - np.linalg.norm(r["beta_classical"]))
        checks.add(f"   ||beta|| scale recovery ({name})", scale_err < 1e-6, f"{scale_err:.3e}", "< 1e-6")

        # ------------------------------------------------------------- shot histogram
        s = solver.sample(y, shots=shots)
        beta = r["beta_classical"]
        expected = beta**2 / np.sum(beta**2)
        obs = s["success_counts"]
        stat, p = chisquare(obs, expected * obs.sum())
        checks.add(f"   shot histogram chi2 ({name}, n={obs.sum()})", p > 0.001,
                   f"chi2={stat:.2f} p={p:.3f}", "p > 0.001")

        sg = recover_signs(solver, y, shots=2 * shots)
        true_signs = np.sign(beta / np.sign(beta[0])).astype(int)
        checks.add(f"   sign recovery from shots ({name})", np.array_equal(sg["signs"], true_signs),
                   f"{sg['signs']} vs {true_signs}", "exact")

    ok = checks.report()
    return ok, checks


if __name__ == "__main__":
    import sys

    ok, _ = run_all()
    sys.exit(0 if ok else 1)
