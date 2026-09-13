"""Probability of finding the best set, and the regret of the misses.

A search over N candidate sets is repeated for many trials. Each trial returns
one set. Two numbers summarise the run:

    P       = (# trials that returned the best set) / (# trials)
    regret  = mean over the missed trials of  L(returned set) - L(best set)

L is a loss, so the best set is the minimiser and every regret term is >= 0.

Part A and Part B reproduce the two hand-worked examples from the note.
Part C runs a seeded toy search and draws the histogram of miss regrets.
"""

from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
MEDIA = HERE.parent / "media"
SLUG = "quantum-search-and-regret"


def probability_of_best(n_found_best: int, n_trials: int) -> float:
    return n_found_best / n_trials


def regret_of_misses(loss_of_misses: np.ndarray, loss_best: float) -> float:
    """Average of L(S_i) - L(best) over the trials that did not return best."""
    misses = np.asarray(loss_of_misses, dtype=float)
    if misses.size == 0:
        return 0.0
    return float(np.sum(misses - loss_best) / np.sum(np.ones_like(misses)))


def part_a() -> None:
    print("Part A -- probability of finding the best set")
    n_trials, n_best = 1000, 999
    p = probability_of_best(n_best, n_trials)
    print(f"  trials = {n_trials}, found best = {n_best}")
    print(f"  P = {n_best}/{n_trials} = {p:.3f}")
    print()


def part_b() -> None:
    print("Part B -- regret of three misses")
    # The page scores the best set at 100 and the misses at 97, 96, 77.
    # In loss form the best set has the lowest loss; the gaps are the same.
    loss_best = 0.0
    loss_misses = np.array([3.0, 4.0, 23.0])
    r = regret_of_misses(loss_misses, loss_best)
    terms = " + ".join(f"({m:.0f} - {loss_best:.0f})" for m in loss_misses)
    print(f"  L(best) = {loss_best:.0f}, L(misses) = {loss_misses.astype(int).tolist()}")
    print(f"  regret = [{terms}] / 3 = {r:.0f}")
    print()


def part_c(n_sets: int = 64, n_trials: int = 1000, p_best: float = 0.95,
           temperature: float = 6.0, seed: int = 20260913) -> None:
    print("Part C -- toy search, seeded")
    rng = np.random.default_rng(seed)

    # One loss per set. Set 0 is the unique minimiser; the rest sit above it
    # at random gaps, so a miss can be a near miss or a bad one.
    loss = np.empty(n_sets)
    loss[0] = 10.0
    loss[1:] = loss[0] + rng.uniform(1.0, 30.0, size=n_sets - 1)
    best = int(np.argmin(loss))

    # The search returns the best set with probability p_best. Otherwise it
    # returns one of the other sets, with lower-loss sets favoured.
    others = np.arange(n_sets) != best
    w = np.exp(-(loss[others] - loss[best]) / temperature)
    w /= w.sum()
    other_ids = np.flatnonzero(others)

    hit = rng.random(n_trials) < p_best
    returned = np.where(hit, best, rng.choice(other_ids, size=n_trials, p=w))

    n_found = int(np.sum(returned == best))
    loss_misses = loss[returned[returned != best]]
    p = probability_of_best(n_found, n_trials)
    r = regret_of_misses(loss_misses, loss[best])

    print(f"  N = {n_sets} sets, trials = {n_trials}, L(best) = {loss[best]:.2f}")
    print(f"  found best = {n_found}  ->  P = {p:.3f}")
    print(f"  misses = {loss_misses.size}  ->  regret = {r:.2f}")
    if loss_misses.size:
        gaps = loss_misses - loss[best]
        print(f"  miss gaps: min {gaps.min():.2f}, median {np.median(gaps):.2f}, "
              f"max {gaps.max():.2f}")
        save_histogram(gaps, r)
    print()


def save_histogram(gaps: np.ndarray, regret: float) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    MEDIA.mkdir(exist_ok=True)
    out = MEDIA / f"{SLUG}-regret-histogram.png"
    fig, ax = plt.subplots(figsize=(6.0, 3.4), dpi=150)
    ax.hist(gaps, bins=np.arange(0, np.ceil(gaps.max()) + 2, 2), color="#4C72B0",
            edgecolor="white")
    ax.axvline(regret, color="#C44E52", linestyle="--", linewidth=1.5,
               label=f"regret (mean gap) = {regret:.2f}")
    ax.set_xlabel("L(returned set) - L(best set)")
    ax.set_ylabel("misses")
    ax.set_title(f"Gap to the best set over {gaps.size} missed trials")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out)
    plt.close(fig)
    print(f"  histogram -> {out.relative_to(HERE.parent)}")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
