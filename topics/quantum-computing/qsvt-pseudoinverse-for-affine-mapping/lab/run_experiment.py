"""End-to-end run: classical baseline, quantum solve for both columns, reconstruction.

    python3 run_experiment.py            # the two column reports + reconstruction
    python3 run_experiment.py --all      # the above plus every validation layer
    python3 run_experiment.py --shots 50000
    python3 run_experiment.py --scale 0.5      # C as a fraction of sigma_min
"""

import argparse

import numpy as np

from block_encoding import RectangularBlockEncoding
from classical_affine import B_TRUE, Z, generate_targets, report as classical_report, solve_affine
from qsvt_polynomial import QSPPhases, SingularValuePolynomial
from quantum_solver import QuantumPseudoInverse
from sign_recovery import report as sign_report

np.set_printoptions(precision=6, suppress=True, linewidth=120)


def column_report(solver, y, label, shots):
    """PRD section 18 diagnostic block for one output column."""
    enc, poly = solver.enc, solver.poly
    r = solver.solve_statevector(y)
    s = solver.sample(y, shots=shots)
    _, unit_err = enc.verify(verbose=False)

    bar = "=" * 46
    print(bar)
    print(f"Affine quantum solve: {label} output")
    print(bar)
    print()
    print("Input y:")
    print(y)
    print(f"||y|| = {r['norm_y']:.10f}")
    print()
    print(f"Matrix normalization alpha: {enc.alpha:.10f}")
    print(f"Normalized singular values: {np.array2string(enc.singular_values, precision=8)}")
    print(f"Polynomial scale C:         {poly.C:.10f}")
    print(f"p(sigma):                   {np.array2string(poly.evaluate(enc.singular_values), precision=8)}")
    print(f"C/sigma:                    {np.array2string(poly.target(enc.singular_values), precision=8)}")
    print(f"Block-unitary error:        {unit_err['unitarity']:.3e}")
    print()

    # -------------------------------------------------- PRD section 11, in full
    print("Complete normalization BEFORE postselection")
    print("-" * 46)
    print("The circuit output is a single normalized state spread over the whole")
    print("register. Writing the success amplitudes as A1, A2, A3:")
    print()
    amps = r["success_amplitudes"].real
    for i, a in enumerate(amps):
        print(f"  A{i+1} = <S,{i}|Psi>  = {a:+.10f}     |A{i+1}|^2 = {a**2:.10f}")
    tot = float(np.sum(amps**2))
    print(f"  {'':<26}sum |Ai|^2 = {tot:.10f}   <- this is P_S")
    print(f"  {'':<26}       P_F = {r['P_F']:.10f}   <- everything else")
    print(f"  {'':<26}   P_S+P_F = {tot + r['P_F']:.10f}")
    print()
    print("The failure branch is not a bug or a leak. p(sigma) rescales each singular")
    print("component by a different factor, so the desired branch cannot keep unit norm;")
    print("unitarity forces the missing norm to live somewhere, and that somewhere is")
    print("the failure subspace.")
    print()
    print(f"Success probability: {r['P_S']:.10f}")
    print(f"Failure probability: {r['P_F']:.10f}")
    print(f"Success + failure:   {r['P_S'] + r['P_F']:.6f}")
    print()

    print("Postselected beta state:    " + np.array2string(r["beta_direction"], precision=8))
    print("Classical normalized beta:  " + np.array2string(r["beta_classical_normalized"], precision=8))
    print(f"State fidelity:             {r['fidelity']:.12f}")
    print()

    print(f"Shot distribution conditioned on success ({s['n_success']} of {s['shots']} shots):")
    beta_c = r["beta_classical"]
    theory = beta_c**2 / np.sum(beta_c**2)
    for i in range(enc.n):
        bits = format(i, f"0{enc.num_qubits}b")
        print(
            f"  {bits}: {s['distribution'][i]:.4f}    theory |beta_{i}|^2/sum = {theory[i]:.4f}"
            f"    ({s['success_counts'][i]} counts)"
        )
    print(f"  measured P_S = {s['P_S_measured']:.4f}   exact P_S = {r['P_S']:.4f}")
    print()

    print("Scale recovery (PRD section 19):")
    print("  A quantum state carries no absolute scale, but P_S does:")
    print("      P_S = || C*alpha*pinv(Z) |y> ||^2 = ( C*alpha*||beta|| / ||y|| )^2")
    print("  so  ||beta|| = sqrt(P_S) * ||y|| / (C*alpha), all of which is known.")
    print(f"      sqrt({r['P_S']:.8f}) * {r['norm_y']:.6f} / ({poly.C:.6f} * {enc.alpha:.6f})")
    print(f"      = {r['beta_norm']:.10f}     (classical ||beta|| = {np.linalg.norm(beta_c):.10f})")
    print()
    print("Recovered beta:  " + np.array2string(r["beta_quantum"], precision=8))
    print("Classical beta:  " + np.array2string(beta_c, precision=8))
    print()
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="also run every validation layer")
    ap.add_argument("--shots", type=int, default=20000)
    ap.add_argument("--degree", type=int, default=9)
    ap.add_argument("--scale", type=float, default=0.85, help="C as a fraction of sigma_min")
    args = ap.parse_args()

    Y, B_cls, _ = classical_report()

    enc = RectangularBlockEncoding(Z)
    enc.report()

    poly = SingularValuePolynomial(
        enc.singular_values, scale=args.scale * float(enc.singular_values.min()), degree=args.degree
    )
    poly.report()

    qsp = QSPPhases(poly)
    qsp.solve()
    qsp.report()

    solver = QuantumPseudoInverse(enc, poly, qsp.phases)
    print("=" * 46)
    print("QSVT operator check")
    print("=" * 46)
    print()
    solver.verify_operator()
    print()
    print("Circuit size:")
    qc = solver.build_circuit(Y[:, 0])
    print(f"  qubits {qc.num_qubits}   depth {qc.depth()}   ops {sum(qc.count_ops().values())}")
    print(f"  {dict(qc.count_ops())}")
    print()

    results = {}
    for label, col in (("X", 0), ("Y", 1)):
        results[label] = column_report(solver, Y[:, col], label, args.shots)

    print("=" * 46)
    print("Sign recovery from shots (PRD section 14)")
    print("=" * 46)
    print()
    sign_report(solver, Y[:, 0], "X output")
    sign_report(solver, Y[:, 1], "Y output")

    # ------------------------------------------------------------ PRD section 19
    B_q = np.column_stack([results["X"]["beta_quantum"], results["Y"]["beta_quantum"]])
    print("=" * 46)
    print("Final reconstruction")
    print("=" * 46)
    print()
    print("B_quantum = [beta_x, beta_y] =")
    print(np.array2string(B_q, precision=8))
    print()
    print("B_classical =")
    print(np.array2string(B_cls, precision=8))
    print()
    print("B_true =")
    print(np.array2string(B_TRUE, precision=8))
    print()
    print(f"||B_quantum - B_true||_F    = {np.linalg.norm(B_q - B_TRUE):.6e}")
    print(f"||B_classical - B_true||_F  = {np.linalg.norm(B_cls - B_TRUE):.6e}")
    print()
    print("Note on what was and was not recovered by measurement:")
    print("  - magnitudes |beta_i|  : from the shot histogram")
    print("  - relative signs       : from the interference experiment above")
    print("  - overall scale ||beta||: from P_S, via the identity in each column report")
    print("  - global sign          : NOT observable. |beta> and -|beta> are the same")
    print("    physical state; the convention here is fixed against the classical fit.")
    print()

    if args.all:
        import validation

        validation.run_all(shots=args.shots)


if __name__ == "__main__":
    main()
