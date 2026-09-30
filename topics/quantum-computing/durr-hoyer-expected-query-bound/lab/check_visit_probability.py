"""Numeric check of the two ingredients of the Durr-Hoyer bound E[Q] <= (45/4) sqrt(N).

1. Visiting probability. The threshold starts at a uniformly random rank and, at every success, jumps to a
   uniformly random strictly better rank (rank 1 = minimum). The probability that rank r is ever the threshold
   is 1/r. The chain is simulated and the visit frequency of each rank is compared with 1/r.
2. The sum. With the BBHT cost (9/2) sqrt(N/(r-1)) per visit of rank r, the bound is
   (9/2) sqrt(N) * S(N),  S(N) = sum_{r=2}^{N} 1 / (r sqrt(r-1)),
   and S(N) <= 1/2 + 2 = 5/2 for every N, which gives 45/4.

Run:  python check_visit_probability.py
"""
import numpy as np

rng = np.random.default_rng(2026)


def visit_frequencies(n, trials):
    counts = np.zeros(n + 1)
    for _ in range(trials):
        r = rng.integers(1, n + 1)          # uniform start over ranks 1..n
        counts[r] += 1
        while r > 1:
            r = rng.integers(1, r)          # uniform over the strictly better ranks 1..r-1
            counts[r] += 1
    return counts[1:] / trials


def s_sum(n):
    r = np.arange(2, n + 1, dtype=float)
    return float(np.sum(1.0 / (r * np.sqrt(r - 1.0))))


if __name__ == "__main__":
    trials = 100_000
    for n in (11, 64):
        freq = visit_frequencies(n, trials)
        exact = 1.0 / np.arange(1, n + 1)
        err = np.max(np.abs(freq - exact))
        print(f"N = {n}: max |frequency - 1/r| over all ranks = {err:.4f} ({trials:,} chains)")
        show = [1, 2, 3, n // 2, n - 1, n] if n > 11 else list(range(1, n + 1))
        for r in show:
            print(f"   r = {r:3d}   frequency {freq[r - 1]:.4f}   1/r {1 / r:.4f}")
    print()
    print("   N        S(N)     bound 5/2   (9/2)*S(N)   45/4")
    for n in (11, 64, 1024, 262_144, 10**7):
        s = s_sum(n)
        print(f"{n:>9,}   {s:.4f}   2.5000      {4.5 * s:.4f}      11.2500")
