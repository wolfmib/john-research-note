"""Classical reference solution for the 2D affine mapping problem.

    Y = Z B          Z (5x3) homogeneous source points
                     Y (5x2) transformed target points
                     B (3x2) the unknown affine transform

This is PRD section 3. It is the baseline the quantum path is checked against, and
nothing here is quantum -- it exists so that every number the circuit produces has a
known-correct value to be compared with.
"""

import numpy as np

# Source points in homogeneous form: row i is [x_i, y_i, 1].
Z = np.array(
    [
        [0.0, 0.0, 1.0],
        [1.0, 0.0, 1.0],
        [0.0, 1.0, 1.0],
        [1.0, 1.0, 1.0],
        [2.0, -1.0, 1.0],
    ]
)

# Hidden ground truth. Used ONLY to generate Y; treated as unknown from then on.
#     B = [[a, d],
#          [b, e],
#          [c, f]]      so that  [x', y'] = [x, y, 1] B
B_TRUE = np.array(
    [
        [1.2, -0.4],
        [0.5, 1.1],
        [2.0, -1.0],
    ]
)


def generate_targets(Z=Z, B=B_TRUE):
    """Y = Z B -- the observed data. After this call, forget B."""
    return Z @ B


def solve_affine(Z, Y):
    """Ordinary least squares fit of B in Y = Z B.

    Uses lstsq rather than the explicit normal-equation form inv(Z.T @ Z) @ Z.T @ Y:
    same answer, but it goes through an SVD/QR internally instead of squaring the
    condition number. The quantum path is a different route to this same B.
    """
    B, *_ = np.linalg.lstsq(Z, Y, rcond=None)
    return B


def solve_column(Z, y):
    """Least squares fit of a single column: beta = pinv(Z) @ y."""
    beta, *_ = np.linalg.lstsq(Z, y, rcond=None)
    return beta


def report(stream=None):
    """PRD section 3 diagnostic block. Returns (Y, B_classical, residual)."""
    out = []
    Y = generate_targets()
    B = solve_affine(Z, Y)
    Y_pred = Z @ B
    residual = np.linalg.norm(Y - Y_pred)

    out.append("=" * 46)
    out.append("Classical reference: least-squares affine fit")
    out.append("=" * 46)
    out.append("")
    out.append(f"Z shape: {Z.shape}")
    out.append(f"Y shape: {Y.shape}")
    out.append(f"Recovered B shape: {B.shape}")
    out.append("")
    out.append("Z =")
    out.append(str(Z))
    out.append("")
    out.append("Y = Z B_true =")
    out.append(str(Y))
    out.append("")
    out.append("B =")
    out.append(str(np.round(B, 12) + 0.0))  # +0.0 kills "-0." display artefacts
    out.append("")
    out.append("Y_pred = Z B =")
    out.append(str(Y_pred))
    out.append("")
    out.append(f"||Y - Y_pred||_F = {residual:.6e}")
    out.append(f"||B - B_true||_F = {np.linalg.norm(B - B_TRUE):.6e}")
    out.append("")

    text = "\n".join(out)
    print(text, file=stream)
    return Y, B, residual


if __name__ == "__main__":
    report()
