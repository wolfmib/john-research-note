"""Singular-value polynomial and QSP phase factors (PRD sections 9, 16).

Two objects live here.

`SingularValuePolynomial` picks the odd real polynomial p with

    p(sigma) ~ C / sigma       and       |p(x)| <= 1 on [-1, 1]

The bound is not optional: p(x) has to be realizable as the (0,0) entry of a product of
2x2 unitaries, and no such entry can exceed 1 in modulus. The reciprocal 1/sigma blows up
at 0, so the whole game is to scale it down by C and approximate what is left.

`QSPPhases` finds the phase angles Phi that make a quantum signal processing sequence
reproduce p. There is no library for this here (pyqsp is not installed, and the point of
the lab is to build the tooling), so it is solved directly: evaluate the 2x2 sequence,
least-squares fit the phases against p on Chebyshev nodes.

Two design choices worth reading before the code.

1.  Which polynomial. The obvious target is a minimax approximation of C/x over the whole
    interval [sigma_min, sigma_max]. That is the textbook framing and it is expensive:
    with kappa = 3.9 it takes degree ~19 to get relative error to 1.4%, which caps the
    achievable fidelity. But Z has exactly THREE singular values. Nothing the polynomial
    does anywhere else can affect beta. So the default mode pins p(sigma_i) = C/sigma_i
    as hard equality constraints and spends the remaining freedom on keeping |p| small.
    Degree 9 then gives an exact singular-value transform. `interval_minimax` mode keeps
    the textbook version available for comparison -- see the sweep at the bottom.

2.  Why the result is complex. A QSP sequence produces a complex polynomial in the block;
    only its real part is p. For this matrix the imaginary part at the three singular
    values is (-0.99, -0.15, 0.54), which is not negligible. A complex p(sigma_i) would
    put a DIFFERENT phase on each singular component and scramble beta, so the circuit
    has to project onto the real part. That is handled in quantum_solver.py.
"""

import numpy as np
from numpy.polynomial import chebyshev as Ch
from scipy.optimize import linprog, least_squares


# --------------------------------------------------------------------------- polynomial
class SingularValuePolynomial:
    """Odd real polynomial approximating C/x, bounded by 1 on [-1, 1].

    Parameters
    ----------
    singular_values : array
        The normalized singular values of A. Used as exact interpolation points in
        `exact` mode, and to set the interval in `interval` mode.
    scale : float or None
        C. Defaults to 0.85 * sigma_min, which keeps sup|p| = 0.85 -- a safe margin
        under the hard bound of 1 -- while keeping the success probability usable.
        Raising C raises the success probability as C^2 but pushes p toward the bound.
    degree : int
        Odd. The polynomial has (degree+1)/2 free coefficients.
    mode : {"exact", "interval"}
        "exact"    -- pin p(sigma_i) = C/sigma_i exactly, minimize sup|p| on [-1,1].
        "interval" -- minimize max relative error to C/x over [sigma_min, sigma_max],
                      subject to |p| <= 1 - margin.
    """

    def __init__(self, singular_values, scale=None, degree=9, mode="exact", margin=0.02):
        self.singular_values = np.asarray(singular_values, dtype=float)
        if degree % 2 == 0:
            raise ValueError("degree must be odd -- the pseudoinverse map is odd in sigma")
        self.degree = degree
        self.mode = mode
        self.margin = margin
        self.sigma_min = float(self.singular_values.min())
        self.sigma_max = float(self.singular_values.max())
        self.C = float(0.85 * self.sigma_min if scale is None else scale)

        self._odd_powers = list(range(1, degree + 1, 2))
        self._coef, self.objective = self._fit()
        self.sup_norm = self.verify_bound()[1]

    # -------------------------------------------------------------- internal fitting
    def _basis(self, xs):
        """Chebyshev design matrix restricted to odd degrees: rows x, cols T_k(x)."""
        xs = np.atleast_1d(np.asarray(xs, dtype=float))
        return np.stack([Ch.chebval(xs, [0] * k + [1]) for k in self._odd_powers], axis=1)

    def _fit(self):
        nc = len(self._odd_powers)
        # p is odd, so bounding it on [0, 1] bounds it on [-1, 1].
        x_bound = np.linspace(0.0, 1.0, 2001)
        T_bound = self._basis(x_bound)

        if self.mode == "exact":
            # min t  s.t.  |p(x)| <= t on [0,1],  p(sigma_i) = C/sigma_i exactly
            A_ub = np.vstack(
                [
                    np.hstack([T_bound, -np.ones((len(x_bound), 1))]),
                    np.hstack([-T_bound, -np.ones((len(x_bound), 1))]),
                ]
            )
            b_ub = np.zeros(2 * len(x_bound))
            A_eq = np.hstack([self._basis(self.singular_values), np.zeros((len(self.singular_values), 1))])
            b_eq = self.C / self.singular_values
        elif self.mode == "interval":
            # min t  s.t.  |p(x) - C/x| * (x/C) <= t on [sigma_min, sigma_max]
            #              |p(x)| <= 1 - margin on [0,1]
            x_fit = np.linspace(self.sigma_min, self.sigma_max, 400)
            T_fit = self._basis(x_fit)
            target = self.C / x_fit
            w = (x_fit / self.C)[:, None]  # relative-error weighting
            A_ub = np.vstack(
                [
                    np.hstack([T_fit * w, -np.ones((len(x_fit), 1))]),
                    np.hstack([-T_fit * w, -np.ones((len(x_fit), 1))]),
                    np.hstack([T_bound, np.zeros((len(x_bound), 1))]),
                    np.hstack([-T_bound, np.zeros((len(x_bound), 1))]),
                ]
            )
            b_ub = np.concatenate(
                [
                    target * w[:, 0],
                    -target * w[:, 0],
                    np.full(len(x_bound), 1.0 - self.margin),
                    np.full(len(x_bound), 1.0 - self.margin),
                ]
            )
            A_eq = b_eq = None
        else:
            raise ValueError(f"unknown mode {self.mode!r}")

        res = linprog(
            np.r_[np.zeros(nc), 1.0],
            A_ub=A_ub,
            b_ub=b_ub,
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=[(None, None)] * (nc + 1),
            method="highs",
        )
        if not res.success:
            raise RuntimeError(f"polynomial LP failed: {res.message}")
        coef = np.zeros(self.degree + 1)
        coef[self._odd_powers] = res.x[:nc]
        return coef, float(res.x[-1])

    # -------------------------------------------------------------------- accessors
    def coefficients(self):
        """Chebyshev coefficients, index k holding the coefficient of T_k."""
        return self._coef

    def evaluate(self, x):
        return Ch.chebval(np.asarray(x, dtype=float), self._coef)

    def target(self, x):
        """The ideal reciprocal transform C/x, for side-by-side comparison."""
        return self.C / np.asarray(x, dtype=float)

    def verify_bound(self, n=4001, tol=1.0):
        """PRD requirement |p(x)| <= 1 on the QSVT domain. Returns (ok, sup|p|)."""
        sup = float(np.max(np.abs(self.evaluate(np.linspace(-1.0, 1.0, n)))))
        return sup <= tol, sup

    def singular_value_errors(self):
        """|p(sigma_i) - C/sigma_i| -- PRD Validation C."""
        return np.abs(self.evaluate(self.singular_values) - self.target(self.singular_values))

    def report(self):
        s = self.singular_values
        print("=" * 46)
        print(f"Singular-value polynomial  (mode={self.mode}, degree={self.degree})")
        print("=" * 46)
        print()
        print("normalized singular values:")
        for i, v in enumerate(s, 1):
            print(f"  sigma{i} = {v:.10f}")
        print()
        print(f"chosen C = {self.C:.10f}   ( = {self.C / self.sigma_min:.4f} * sigma_min )")
        print()
        print("target:")
        for i, v in enumerate(s, 1):
            print(f"  C/sigma{i} = {self.C / v:.10f}")
        print()
        print("polynomial:")
        for i, v in enumerate(s, 1):
            print(f"  p(sigma{i}) = {self.evaluate(v):.10f}")
        print()
        print(f"max |p(sigma_i) - C/sigma_i| = {self.singular_value_errors().max():.3e}")
        print(f"sup |p(x)| on [-1,1]         = {self.sup_norm:.6f}   (must be <= 1)")
        print()


# ------------------------------------------------------------------- QSVT sequence shape
def sequence_factors(phases):
    """Factors of the QSVT product V, in MATRIX order (leftmost factor first).

        V = R(Pi_R, phi_0) . M . prod_{k=1}^{(d-1)/2} [ R(Pi_L, phi_{2k-1}) . M^dag
                                                        . R(Pi_R, phi_{2k}) . M ]

    with M = U_A^T. Note the direction: the sequence is driven by U_A^T, not U_A, and
    the projectors are swapped relative to the naive reading of the block encoding.
    That is deliberate. QSVT on (U_A, Pi_L, Pi_R) applies p to the singular values in
    the FORWARD direction and yields W p(Sigma) V^T -- the same direction as A itself.
    The pseudoinverse needs the adjoint direction V p(Sigma) W^T, which is what running
    the sequence on Pi_R U_A^T Pi_L = A^T produces.

    Returned as (kind, which, value) triples so that the numpy reference operator and the
    Qiskit circuit consume one shared description and cannot drift apart:
        ("phase",   "L"|"R", phi)   -> exp(i phi (2 Pi - I))
        ("unitary", "T"|"N", None)  -> M = U^T  |  M^dag = U
    """
    phases = np.asarray(phases, dtype=float)
    d = len(phases)
    if d % 2 == 0:
        raise ValueError("need an odd number of phases")
    factors = [("phase", "R", phases[0]), ("unitary", "T", None)]
    for k in range(1, (d + 1) // 2):
        factors += [
            ("phase", "L", phases[2 * k - 1]),
            ("unitary", "N", None),
            ("phase", "R", phases[2 * k]),
            ("unitary", "T", None),
        ]
    return factors


def qsp_scalar(x, phases):
    """<0| V |0> for the 1x1 case, evaluated for a whole array of x at once.

    The 1x1 Halmos dilation of the scalar x is W = [[x, sqrt(1-x^2)], [sqrt(1-x^2), -x]],
    which is Hermitian, so M and M^dag coincide and the same factor list applies. By the
    QSVT singular-value decomposition theorem, phases that work here work unchanged on
    the full 8-dimensional block encoding -- which is why the expensive fit is done on
    2x2 matrices.
    """
    x = np.atleast_1d(np.asarray(x, dtype=float))
    sq = np.sqrt(np.clip(1.0 - x * x, 0.0, None))
    W = np.zeros((len(x), 2, 2), dtype=complex)
    W[:, 0, 0] = x
    W[:, 0, 1] = sq
    W[:, 1, 0] = sq
    W[:, 1, 1] = -x
    V = np.tile(np.eye(2, dtype=complex), (len(x), 1, 1))
    for kind, _which, value in sequence_factors(phases):
        V = V @ (np.diag([np.exp(1j * value), np.exp(-1j * value)]) if kind == "phase" else W)
    return V[:, 0, 0]


class QSPPhases:
    """Phase angles Phi reproducing a target polynomial through a QSP sequence.

    Solved by least squares against Re<0|V|0> on Chebyshev nodes. The zero vector turns
    out to be a good starting point for this problem; extra random restarts are kept as
    insurance and stop as soon as the fit is at machine precision.
    """

    def __init__(self, polynomial, degree=None):
        self.polynomial = polynomial
        self.degree = int(polynomial.degree if degree is None else degree)
        self.phases = None
        self.error = None

    def solve(self, n_starts=12, n_nodes=80, tol=1e-10, seed=0, verbose=False):
        xs = np.cos(np.pi * (np.arange(n_nodes) + 0.5) / n_nodes)
        target = self.polynomial.evaluate(xs)

        def residual(phi):
            return qsp_scalar(xs, phi).real - target

        best = None
        for trial in range(n_starts):
            x0 = (
                np.zeros(self.degree)
                if trial == 0
                else np.random.default_rng(seed + trial).uniform(-np.pi, np.pi, self.degree)
            )
            res = least_squares(residual, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15)
            if best is None or res.cost < best.cost:
                best = res
            if verbose:
                print(f"  start {trial:2d}: cost {res.cost:.3e}")
            if best.cost < 1e-26:
                break

        self.phases = best.x
        self.error = float(np.max(np.abs(residual(best.x))))
        if self.error > tol:
            raise RuntimeError(
                f"QSP phase fit did not converge: max error {self.error:.3e} > {tol:.0e}. "
                "Try more restarts or a lower polynomial degree."
            )
        return self.phases

    def evaluate(self, x):
        return qsp_scalar(x, self.phases)

    def report(self):
        s = self.polynomial.singular_values
        vals = self.evaluate(s)
        print("=" * 46)
        print(f"QSP phase factors  (degree {self.degree}, {self.degree} angles)")
        print("=" * 46)
        print()
        print(f"max |Re<0|V|0> - p(x)| over 80 nodes = {self.error:.3e}")
        print()
        print("Phi =")
        print(np.array2string(self.phases, precision=8))
        print()
        print("at the singular values:")
        for i, (v, c) in enumerate(zip(s, vals), 1):
            print(f"  sigma{i}={v:.6f}   Re<0|V|0> = {c.real:+.8f}   Im<0|V|0> = {c.imag:+.8f}")
        print()
        print("The imaginary parts are large, and they differ across singular values.")
        print("Left alone they would rotate each singular component by a different")
        print("phase and scramble beta -- hence the real-part projection in the circuit.")
        print()


if __name__ == "__main__":
    from block_encoding import RectangularBlockEncoding
    from classical_affine import Z

    enc = RectangularBlockEncoding(Z)
    poly = SingularValuePolynomial(enc.singular_values)
    poly.report()

    phases = QSPPhases(poly)
    phases.solve()
    phases.report()

    print("=" * 46)
    print("Why not the textbook interval approximation")
    print("=" * 46)
    print()
    print("Minimax approximation of C/x over the whole interval, for comparison:")
    print(f"{'degree':>7}{'max rel err':>14}{'sup|p|':>10}")
    for deg in (5, 9, 13, 19, 25):
        p_int = SingularValuePolynomial(enc.singular_values, degree=deg, mode="interval")
        print(f"{deg:>7}{p_int.objective:>14.3e}{p_int.sup_norm:>10.4f}")
    print()
    print("Degree 19 still leaves ~1% relative error, which caps the achievable")
    print("fidelity. The exact mode reaches machine precision at degree 9 because it")
    print("only has to be right at the three singular values Z actually has.")
