"""The quantum pseudoinverse circuit (PRD sections 10-13, 16).

Register layout -- 5 qubits, not the 3 the block encoding alone would suggest:

    sys[0..2]   the 8-dimensional dilation. Holds |y> on input, |beta> on success.
    anc         scratch for the projector-controlled phase shifts. Always returns
                to |0>; it is computed and uncomputed inside every phase block.
    lcu         selects the real part of the QSVT polynomial. Post-selected on |0>.

What the circuit computes. Writing V(Phi) for the alternating phase sequence and
M = Pi_R Re[V(Phi)] Pi_L for the 3x5 map it block-encodes:

    |Psi_out> = |success> M|y>  +  |failure> |phi_F>

with the success branch being exactly the three amplitudes at
sys in {0,1,2}, anc = 0, lcu = 0 -- which are global statevector indices 0, 1, 2.
M is not unitary (it stretches small singular values and shrinks large ones), so it
cannot be all of a quantum evolution. The failure branch carries the missing norm.

Because the polynomial is exact at every singular value of A,

    M = C * alpha * pinv(Z)

so the success amplitudes are proportional to beta itself, and

    P_S = || C * alpha * pinv(Z) |y> ||^2 = ( C * alpha * ||beta|| / ||y|| )^2

which inverts to give ||beta|| back -- the overall scale is NOT lost. See
`solve_statevector`.

Real-part projection. A QSP sequence yields a complex polynomial in the block; only its
real part is the p we designed. Rather than controlling the whole sequence, note that
V(-Phi) = conj(V(Phi)) because U_A is real, so H . [V(Phi) (+) V(-Phi)] . H with a
post-selection on lcu = 0 gives (V(Phi) + conj(V(Phi)))/2 = Re V(Phi). Only the phase
angles need to see lcu, and a single RZZ(anc, lcu) flips their sign. U_A itself is never
controlled, which keeps the circuit cheap.
"""

import numpy as np
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit.circuit.library import StatePreparation, UnitaryGate, XGate
from qiskit.quantum_info import Statevector

from qsvt_polynomial import sequence_factors


def _reflection(projector, phi):
    """exp(i phi (2 Pi - I)) for a diagonal projector."""
    return np.diag(np.exp(1j * phi * (2.0 * np.diag(projector) - 1.0)))


class QuantumPseudoInverse:
    """Builds and runs the QSVT pseudoinverse circuit for one right-hand side."""

    def __init__(self, block_encoding, polynomial, phases):
        self.enc = block_encoding
        self.poly = polynomial
        self.phases = np.asarray(phases, dtype=float)
        self.factors = sequence_factors(self.phases)
        self.n_sys = block_encoding.num_qubits
        self._U = block_encoding.unitary()

    # ------------------------------------------------------------ numpy reference
    def sequence_matrix(self):
        """V(Phi) as an explicit (m+n) x (m+n) matrix -- the classical mirror of the circuit."""
        U = self._U
        V = np.eye(self.enc.dim, dtype=complex)
        PiL, PiR = self.enc.left_projector(), self.enc.right_projector()
        for kind, which, value in self.factors:
            if kind == "phase":
                V = V @ _reflection(PiL if which == "L" else PiR, value)
            else:
                V = V @ (U.T if which == "T" else U)
        return V

    def reference_operator(self):
        """M = Pi_R Re[V] Pi_L as an n x m matrix. Should equal C * alpha * pinv(Z)."""
        V = self.sequence_matrix()
        return np.real((V + V.conj()) / 2.0)[: self.enc.n, : self.enc.m]

    def ideal_operator(self):
        """C * alpha * pinv(Z) -- what the block is supposed to be."""
        return self.poly.C * self.enc.alpha * np.linalg.pinv(self.enc.raw)

    # ----------------------------------------------------------------- the circuit
    def _c_pi_not(self, qc, sys, anc, which):
        """Flip anc iff sys lies in the chosen subspace.

        Pi_R is {|0>,|1>,|2>} -- three controlled flips, one per basis state.
        Pi_L is {|0>..|4>}, whose complement {|5>,|6>,|7>} is smaller, so it is cheaper
        to flip on the complement and then invert anc.
        """
        if which == "R":
            states = self.enc.right_indices()
            invert = False
        else:
            states = [j for j in range(self.enc.dim) if j not in self.enc.left_indices()]
            invert = True
        for j in states:
            qc.append(XGate().control(self.n_sys, ctrl_state=j), [*sys, anc[0]])
        if invert:
            qc.x(anc[0])

    def build_circuit(self, y, measure=False, basis_change=None, barriers=True):
        """Full circuit for one right-hand side y (an m-vector, normalized internally)."""
        sys = QuantumRegister(self.n_sys, "sys")
        anc = QuantumRegister(1, "anc")
        lcu = QuantumRegister(1, "lcu")
        qc = QuantumCircuit(sys, anc, lcu)

        qc.append(StatePreparation(self.enc.embed_left(y), label="prep |y>"), list(sys))
        if barriers:
            qc.barrier()
        qc.h(lcu[0])

        gate_T = UnitaryGate(self._U.T, label="U_A^T")
        gate_N = UnitaryGate(self._U, label="U_A")

        # The factor list is in matrix order (leftmost factor first); a circuit applies
        # the rightmost factor to the state first, so it is consumed in reverse.
        for kind, which, value in reversed(self.factors):
            if kind == "phase":
                self._c_pi_not(qc, sys, anc, which)
                qc.rzz(2.0 * value, anc[0], lcu[0])
                self._c_pi_not(qc, sys, anc, which)
            else:
                qc.append(gate_T if which == "T" else gate_N, list(sys))

        qc.h(lcu[0])
        if basis_change is not None:
            if barriers:
                qc.barrier()
            qc.append(UnitaryGate(basis_change, label="basis"), list(sys))

        if measure:
            creg = ClassicalRegister(self.n_sys + 2, "c")
            qc.add_register(creg)
            qc.measure(list(sys) + [anc[0], lcu[0]], list(creg))
        return qc

    # -------------------------------------------------------------- statevector path
    def solve_statevector(self, y, basis_change=None):
        """Run the circuit exactly and unpack the success/failure decomposition."""
        y = np.asarray(y, dtype=float)
        qc = self.build_circuit(y, measure=False, basis_change=basis_change)
        sv = np.asarray(Statevector(qc).data)

        # global index = sys + 8*anc + 16*lcu, so the success branch is indices 0,1,2
        success_amps = sv[: self.enc.n]
        P_S = float(np.sum(np.abs(success_amps) ** 2))
        P_F = 1.0 - P_S

        norm_y = float(np.linalg.norm(y))
        scale = self.poly.C * self.enc.alpha
        beta_norm = np.sqrt(P_S) * norm_y / scale
        direction = success_amps.real / np.linalg.norm(success_amps)
        beta_classical = np.linalg.lstsq(self.enc.raw, y, rcond=None)[0]

        # fix the global sign against the classical solution before reporting a vector;
        # a quantum state is only defined up to global phase and the sign is not
        # observable in the computational basis (see sign_recovery.py)
        sign = np.sign(direction @ (beta_classical / np.linalg.norm(beta_classical)))
        beta_quantum = direction * sign * beta_norm

        overlap = direction @ (beta_classical / np.linalg.norm(beta_classical))
        return {
            "statevector": sv,
            "success_amplitudes": success_amps,
            "P_S": P_S,
            "P_F": P_F,
            "ancilla_leak": float(np.sum(np.abs(sv[8:16]) ** 2)),
            "beta_direction": direction * sign,
            "beta_norm": float(beta_norm),
            "beta_quantum": beta_quantum,
            "beta_classical": beta_classical,
            "beta_classical_normalized": beta_classical / np.linalg.norm(beta_classical),
            "fidelity": float(overlap**2),
            "norm_y": norm_y,
        }

    # -------------------------------------------------------------------- shot path
    def sample(self, y, shots=20000, seed=1234, basis_change=None):
        """Run with measurement. Each shot restarts the circuit; failures are discarded."""
        from qiskit_aer import AerSimulator
        from qiskit import transpile

        qc = self.build_circuit(y, measure=True, basis_change=basis_change)
        backend = AerSimulator(seed_simulator=seed)
        counts = backend.run(transpile(qc, backend), shots=shots).result().get_counts()

        success = np.zeros(self.enc.n, dtype=int)
        n_success = n_fail = 0
        for key, c in counts.items():
            val = int(key.replace(" ", ""), 2)
            sys_val, anc_val, lcu_val = val & 7, (val >> 3) & 1, (val >> 4) & 1
            if lcu_val == 0 and anc_val == 0 and sys_val < self.enc.n:
                success[sys_val] += c
                n_success += c
            else:
                n_fail += c
        return {
            "counts": counts,
            "success_counts": success,
            "n_success": int(n_success),
            "n_fail": int(n_fail),
            "shots": int(shots),
            "P_S_measured": n_success / shots,
            "distribution": success / max(n_success, 1),
        }

    # ---------------------------------------------------------------- verification
    def verify_operator(self, tol=1e-10, verbose=True):
        """The numpy sequence really is C*alpha*pinv(Z), in the pseudoinverse direction."""
        M = self.reference_operator()
        ideal = self.ideal_operator()
        WA, sA, VtA = np.linalg.svd(self.enc.A, full_matrices=False)
        svt = VtA.T @ np.diag(self.poly.evaluate(sA)) @ WA.T
        errs = {
            "vs_singular_value_transform": float(np.linalg.norm(M - svt)),
            "vs_scaled_pseudoinverse": float(np.linalg.norm(M - ideal)),
        }
        if verbose:
            print(f"||Pi_R Re[V] Pi_L  -  V p(Sigma) W^T||  = {errs['vs_singular_value_transform']:.3e}")
            print(f"||Pi_R Re[V] Pi_L  -  C*alpha*pinv(Z)|| = {errs['vs_scaled_pseudoinverse']:.3e}")
        return max(errs.values()) < tol, errs

    def verify_circuit(self, y, tol=1e-10, verbose=True):
        """The Qiskit circuit reproduces the numpy sequence, amplitude by amplitude."""
        sv = self.solve_statevector(y)["statevector"]
        expected = self.reference_operator() @ self.enc.embed_left(y)[: self.enc.m]
        err = float(np.max(np.abs(sv[: self.enc.n] - expected)))
        leak = float(np.sum(np.abs(sv[8:16]) ** 2))
        if verbose:
            print(f"max |circuit amplitude - numpy amplitude| = {err:.3e}")
            print(f"probability left on the phase ancilla     = {leak:.3e}  (must uncompute to 0)")
        return err < tol and leak < tol, {"amplitude_error": err, "ancilla_leak": leak}


if __name__ == "__main__":
    from block_encoding import RectangularBlockEncoding
    from classical_affine import Z, generate_targets
    from qsvt_polynomial import QSPPhases, SingularValuePolynomial

    enc = RectangularBlockEncoding(Z)
    poly = SingularValuePolynomial(enc.singular_values)
    phi = QSPPhases(poly).solve()
    solver = QuantumPseudoInverse(enc, poly, phi)

    solver.verify_operator()
    Y = generate_targets()
    solver.verify_circuit(Y[:, 0])
    print()
    r = solver.solve_statevector(Y[:, 0])
    print("P_S      =", r["P_S"])
    print("beta_q   =", r["beta_quantum"])
    print("beta_cls =", r["beta_classical"])
    print("fidelity =", r["fidelity"])
