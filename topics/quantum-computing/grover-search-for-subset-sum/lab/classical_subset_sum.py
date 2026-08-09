"""
Part 1 - Classical reference for the 6-bit subset-sum problem.

Rule:
    18*x0 + 36*x1 + 34*x2 + 32*x3 + 19*x4 + 23*x5 == 75      x_i in {0,1}

This module is the ground truth the quantum run is checked against.
It is deliberately dumb: enumerate all 2^6 = 64 binary combinations,
evaluate the rule, keep whatever satisfies it.

Run standalone:
    python3 classical_subset_sum.py
"""

from itertools import product

# The only two things the problem (and later the oracle) is allowed to know.
WEIGHTS = [18, 36, 34, 32, 19, 23]
TARGET = 75
N_BITS = len(WEIGHTS)


def weighted_sum(bits):
    """S(x) = sum_i w_i * x_i, with bits given as (x0, x1, ..., x5)."""
    return sum(w * x for w, x in zip(WEIGHTS, bits))


def bits_to_int(bits):
    """(x0, ..., x5) -> integer, x_i is the coefficient of 2^i (little-endian)."""
    return sum(x << i for i, x in enumerate(bits))


def bits_to_qiskit_string(bits):
    """(x0, ..., x5) -> the string Qiskit prints, which is x5 x4 x3 x2 x1 x0."""
    return "".join(str(b) for b in reversed(bits))


def brute_force(verbose=True):
    """Enumerate all 64 candidates. Returns (solutions, n_candidates_checked)."""
    solutions = []
    checked = 0

    for bits in product([0, 1], repeat=N_BITS):
        total = weighted_sum(bits)
        checked += 1
        if total == TARGET:
            solutions.append(bits)
            if verbose:
                print(
                    f"  hit: x={bits}  S(x)={total}  "
                    f"int={bits_to_int(bits)}  qiskit='{bits_to_qiskit_string(bits)}'"
                )

    return solutions, checked


def main():
    print("=" * 68)
    print("PART 1 - CLASSICAL BRUTE FORCE")
    print("=" * 68)
    print(f"weights = {WEIGHTS}")
    print(f"target  = {TARGET}")
    print(f"search space = 2^{N_BITS} = {2 ** N_BITS} candidates")
    print(f"max possible sum = {sum(WEIGHTS)}  ->  sum register needs "
          f"{sum(WEIGHTS).bit_length()} bits\n")

    print("Scanning all binary combinations:")
    solutions, checked = brute_force()

    print(f"\ncandidates checked : {checked}")
    print(f"solutions found    : {len(solutions)}")

    # Check A - exactly one satisfying combination.
    assert len(solutions) == 1, f"expected exactly 1 solution, got {len(solutions)}"
    sol = solutions[0]

    print("\nCHECK A PASSED - exactly one satisfying combination.")
    print(f"  tuple (x0..x5)  : {sol}")
    print(f"  integer         : {bits_to_int(sol)}")
    print(f"  qiskit bitstring: {bits_to_qiskit_string(sol)}")
    print(f"  verification    : " + " + ".join(
        f"{w}*{x}" for w, x in zip(WEIGHTS, sol)) + f" = {weighted_sum(sol)}")

    print(f"\nClassical cost: {checked} rule evaluations (worst case O(N), N=64).")
    print("Grover will need about sqrt(N) ~ 6 oracle calls for the same answer.")
    return sol


if __name__ == "__main__":
    main()
