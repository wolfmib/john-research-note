"""Custom rectangular block encoding (PRD sections 6, 7, 8, 16).

We do not use a ready-made block-encoding primitive. We build the Halmos unitary
dilation of a rectangular matrix by hand, so the 5-dimensional data space and the
3-dimensional parameter space stay visible as two distinct subspaces of one 8-dimensional
(3-qubit) register.

For A (m x n) with ||A||_2 <= 1:

    U_A = [[ A                  ,  sqrt(I_m - A A^T) ],
           [ sqrt(I_n - A^T A)  , -A^T               ]]      -- (m+n) x (m+n)

Unitarity comes from the intertwining identity  A^T f(A A^T) = f(A^T A) A^T:
    column block 1 Gram : A^T A + (I_n - A^T A) = I_n
    column block 2 Gram : (I_m - A A^T) + A A^T = I_m
    cross term          : A^T sqrt(I_m - A A^T) - sqrt(I_n - A^T A) A^T = 0

Index layout for m = 5, n = 3 (8 = 2^3, so one 3-qubit register holds everything):

    basis state |0> |1> |2> |3> |4> | |5> |6> |7>
    data space   *   *   *   *   *              <- H_L, dimension 5, holds |y>
    param space  *   *   *                      <- H_R, dimension 3, holds |beta>

The two subspaces OVERLAP on |0>,|1>,|2>. That is fine and is exactly why the
success/failure split later is a statement about which subspace the output lands in,
not about a separate flag qubit.

Note on "do not use Z^T Z" (PRD section 5): that rule is about the *algorithm* -- the
quantum path must never solve the normal equations (Z^T Z) beta = Z^T y. Building the
dilation does need A^T A for one matrix square root, and alpha = ||Z||_2 needs a
classical SVD. Those are construction-time preprocessing of the encoding, not the solve.
A real application would get U_A from a data-structure oracle instead.
"""

import numpy as np
from scipy.linalg import sqrtm


def _psd_sqrt(M):
    """Principal square root of a symmetric PSD matrix, forced real.

    Gotcha worth stating: because alpha = ||Z||_2 exactly, A has a singular value of
    exactly 1, so I - A A^T is exactly singular. Rounding puts that eigenvalue at some
    +-1e-17, and sqrt(1e-17) = 3e-9 -- nine orders of magnitude larger than the dust it
    came from, which then shows up as a 1e-10 unitarity error in U_A. So eigenvalues
    below a relative floor are snapped to exactly zero before the square root.
    """
    S = (M + M.T) / 2.0
    w, V = np.linalg.eigh(S)
    floor = len(w) * np.finfo(float).eps * max(np.max(np.abs(w)), 1.0)
    w = np.where(w <= floor, 0.0, w)
    return (V * np.sqrt(w)) @ V.T


class RectangularBlockEncoding:
    """Halmos dilation of a rectangular real matrix into one unitary.

    Parameters
    ----------
    matrix : (m, n) array
        The raw matrix, e.g. Z. It is normalized internally.
    expected_shape : tuple or None
        If given, asserted against matrix.shape. This lab passes (5, 3).
    """

    def __init__(self, matrix, expected_shape=(5, 3)):
        M = np.asarray(matrix, dtype=float)
        if expected_shape is not None and M.shape != expected_shape:
            raise ValueError(f"expected matrix of shape {expected_shape}, got {M.shape}")
        self.raw = M
        self.m, self.n = M.shape
        self.dim = self.m + self.n
        if self.dim & (self.dim - 1):
            raise ValueError(
                f"m + n = {self.dim} is not a power of two, so it does not fill a "
                "qubit register exactly"
            )
        self.num_qubits = int(np.log2(self.dim))

        # ---- normalization (PRD section 6): alpha >= ||Z||_2, here taken as equality
        self.singular_values_raw = np.linalg.svd(M, compute_uv=False)
        self.alpha = float(self.singular_values_raw[0])
        self.A = M / self.alpha
        self.singular_values = self.singular_values_raw / self.alpha
        if self.singular_values[0] > 1.0 + 1e-12:
            raise ValueError("||A||_2 > 1 after normalization")

        # ---- the dilation
        A = self.A
        top = np.hstack([A, _psd_sqrt(np.eye(self.m) - A @ A.T)])
        bottom = np.hstack([_psd_sqrt(np.eye(self.n) - A.T @ A), -A.T])
        self.U = np.vstack([top, bottom])

    # ------------------------------------------------------------------ accessors
    def normalized_matrix(self):
        """A = Z / alpha, with every singular value in [0, 1]."""
        return self.A

    def unitary(self):
        """The (m+n) x (m+n) block unitary U_A."""
        return self.U

    def left_projector(self):
        """Pi_L -- projector onto the data space H_L (dimension m). Holds |y>."""
        d = np.zeros(self.dim)
        d[: self.m] = 1.0
        return np.diag(d)

    def right_projector(self):
        """Pi_R -- projector onto the parameter space H_R (dimension n). Holds |beta>."""
        d = np.zeros(self.dim)
        d[: self.n] = 1.0
        return np.diag(d)

    def left_indices(self):
        return list(range(self.m))

    def right_indices(self):
        return list(range(self.n))

    def embed_left(self, y):
        """Embed an m-vector into the full dim-dimensional register, normalized."""
        y = np.asarray(y, dtype=float)
        if y.shape != (self.m,):
            raise ValueError(f"expected a {self.m}-vector, got {y.shape}")
        v = np.zeros(self.dim)
        v[: self.m] = y / np.linalg.norm(y)
        return v

    # ---------------------------------------------------------------- verification
    def verify(self, tol=1e-12, verbose=True):
        """PRD Validation B. Returns a dict of measured errors."""
        U = self.U
        errs = {
            "unitarity": float(np.linalg.norm(U.T @ U - np.eye(self.dim))),
            "left_block": float(
                np.linalg.norm((self.left_projector() @ U @ self.right_projector())[: self.m, : self.n] - self.A)
            ),
            # the adjoint direction is what the QSVT sequence actually uses
            "adjoint_block": float(
                np.linalg.norm((self.right_projector() @ U.T @ self.left_projector())[: self.n, : self.m] - self.A.T)
            ),
            "imaginary_part": float(np.max(np.abs(np.imag(U)))) if np.iscomplexobj(U) else 0.0,
        }
        if verbose:
            print(f"||U^T U - I||       = {errs['unitarity']:.3e}")
            print(f"||Pi_L U Pi_R - A|| = {errs['left_block']:.3e}")
            print(f"||Pi_R U^T Pi_L - A^T|| = {errs['adjoint_block']:.3e}")
        ok = errs["unitarity"] < tol and errs["left_block"] < tol and errs["adjoint_block"] < tol
        return ok, errs

    def report(self):
        print("=" * 46)
        print("Custom rectangular block encoding")
        print("=" * 46)
        print()
        print(f"raw matrix shape      : {self.raw.shape}")
        print(f"alpha = ||Z||_2       : {self.alpha:.10f}")
        print(f"singular values of Z  : {np.array2string(self.singular_values_raw, precision=6)}")
        print(f"singular values of A  : {np.array2string(self.singular_values, precision=6)}")
        print(f"condition number      : {self.singular_values[0] / self.singular_values[-1]:.6f}")
        print(f"dilation dimension    : {self.dim}  ->  {self.num_qubits} qubits")
        print(f"data subspace  H_L    : dimension {self.m}, basis states {self.left_indices()}")
        print(f"param subspace H_R    : dimension {self.n}, basis states {self.right_indices()}")
        print()
        print("U_A =")
        print(np.array2string(self.U, precision=5, suppress_small=True))
        print()
        self.verify()
        print()


if __name__ == "__main__":
    from classical_affine import Z

    RectangularBlockEncoding(Z).report()
