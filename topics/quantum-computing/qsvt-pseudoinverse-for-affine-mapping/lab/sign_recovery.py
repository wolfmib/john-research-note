"""Recovering the signs of beta from shots (PRD section 14).

A computational-basis measurement of |beta> returns |beta_i|^2. The signs are gone.
For the X column that hardly matters -- beta_x = (1.2, 0.5, 2.0) is all positive -- but
for the Y column beta_y = (-0.4, 1.1, -1.0) collapses to the ratio 0.16 : 1.21 : 1, which
is equally consistent with (+, +, +). Reporting a histogram and calling it "the affine
parameters" would be wrong.

The fix is interference. Insert, just before measurement, the unitary that Hadamard-mixes
one pair of basis states and leaves the rest alone:

    G_ij : |i> -> (|i> + |j>)/sqrt(2)
           |j> -> (|i> - |j>)/sqrt(2)

Then the success amplitudes a_i become (a_i + a_j)/sqrt(2) and (a_i - a_j)/sqrt(2), so

    P(i) - P(j) = 2 a_i a_j

and the sign of that difference is the sign of the product a_i a_j -- observable from
counts alone, no statevector needed. Two pairs, (0,1) and (0,2), fix every relative sign.
The overall global sign is genuinely unobservable: |beta> and -|beta> are the same
physical state, and the classical least-squares answer is what fixes the convention.

Because i and j are both inside the parameter subspace {0,1,2}, G_ij only redistributes
amplitude within the success branch. The success probability itself is untouched.
"""

import numpy as np


def pair_mixer(dim, i, j):
    """Identity on dim dimensions except a Hadamard acting on span{|i>, |j>}."""
    G = np.eye(dim)
    r = 1.0 / np.sqrt(2.0)
    G[i, i] = r
    G[i, j] = r
    G[j, i] = r
    G[j, j] = -r
    return G


def recover_signs(solver, y, shots=40000, seed=99, pairs=((0, 1), (0, 2))):
    """Shot-based relative signs of beta. Returns a dict per pair plus the assembled signs.

    The reported z-score is for the null hypothesis a_i a_j = 0, using the binomial
    variance of the difference of two multinomial cells.
    """
    dim = solver.enc.dim
    results = {}
    for (i, j) in pairs:
        s = solver.sample(y, shots=shots, seed=seed, basis_change=pair_mixer(dim, i, j))
        n_i, n_j = int(s["success_counts"][i]), int(s["success_counts"][j])
        n_s = s["n_success"]
        # conditional on success, P(i) - P(j) estimates 2 a_i a_j / P_S
        diff = (n_i - n_j) / max(n_s, 1)
        var = (n_i + n_j - (n_i - n_j) ** 2 / max(n_s, 1)) / max(n_s, 1) ** 2
        z = diff / np.sqrt(var) if var > 0 else np.inf
        results[(i, j)] = {
            "n_i": n_i,
            "n_j": n_j,
            "n_success": n_s,
            "diff": diff,
            "z": float(z),
            "sign": int(np.sign(diff)) if abs(z) > 3 else 0,
            "product_estimate": diff * s["P_S_measured"] / 2.0,
        }

    signs = np.ones(solver.enc.n, dtype=int)  # convention: beta_0 taken positive
    for (i, j), r in results.items():
        if i == 0:
            signs[j] = r["sign"] if r["sign"] != 0 else 1
    return {"pairs": results, "signs": signs}


def report(solver, y, label, shots=40000, seed=99):
    out = recover_signs(solver, y, shots=shots, seed=seed)
    exact = solver.solve_statevector(y)
    beta_c = exact["beta_classical"]
    true_signs = np.sign(beta_c / np.sign(beta_c[0]))  # same convention: beta_0 positive

    print(f"--- sign recovery, {label} ---")
    print(f"  computational basis alone gives only |beta_i|^2 = "
          f"{np.array2string(beta_c**2 / np.sum(beta_c**2), precision=4)}")
    for (i, j), r in out["pairs"].items():
        print(
            f"  mix |{i}>,|{j}> : n_{i}={r['n_i']:<6d} n_{j}={r['n_j']:<6d}  "
            f"P({i})-P({j})={r['diff']:+.4f}  z={r['z']:+8.1f}  "
            f"=> sign(b{i}*b{j}) = {r['sign']:+d}   (true {int(np.sign(beta_c[i]*beta_c[j])):+d})"
        )
    ok = np.array_equal(out["signs"], true_signs.astype(int))
    print(f"  recovered signs (b0 taken +) : {out['signs']}")
    print(f"  true signs      (b0 taken +) : {true_signs.astype(int)}")
    print(f"  match: {ok}")
    print()
    return ok, out


if __name__ == "__main__":
    from block_encoding import RectangularBlockEncoding
    from classical_affine import Z, generate_targets
    from qsvt_polynomial import QSPPhases, SingularValuePolynomial
    from quantum_solver import QuantumPseudoInverse

    enc = RectangularBlockEncoding(Z)
    poly = SingularValuePolynomial(enc.singular_values)
    solver = QuantumPseudoInverse(enc, poly, QSPPhases(poly).solve())
    Y = generate_targets()
    report(solver, Y[:, 0], "X output")
    report(solver, Y[:, 1], "Y output")
