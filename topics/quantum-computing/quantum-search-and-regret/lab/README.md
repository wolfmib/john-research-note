# Reproducible Lab — Probability of the Best Set and Regret of the Misses

Runnable code behind [the write-up](../content.md). Read the write-up for the
concepts; read this for the calculation and the raw numbers.

**The two numbers**

```
P       = (# trials that returned the best set) / (# trials)
regret  = mean over missed trials of  L(returned set) - L(best set)
```

`L` is a loss, so the best set is the minimiser and every regret term is non-negative.

## Files

| File | Purpose |
|---|---|
| `regret_toy.py` | Part A: `999 / 1000 = 0.999`. Part B: three misses `3, 4, 23` → regret `10`. Part C: seeded toy search over 64 sets, 1000 trials, histogram of miss gaps. |
| `RESULTS.md` | Captured output of the script. |

## Run

```bash
/Users/john/.venv-llm/bin/python3 regret_toy.py
```

Requires `numpy` and `matplotlib`. Part C writes
`../media/quantum-search-and-regret-regret-histogram.png`. The random seed is fixed
(`20260913`), so the printed numbers and the figure are reproducible.

## What Part C does

- Sixty-four candidate sets, one loss each. Set 0 is the unique minimiser at loss 10; the
  others sit 1 to 30 units above it at random gaps.
- Each trial returns the best set with probability 0.95. Otherwise it returns one of the
  other sets, with lower-loss sets more likely (weights `exp(-gap / 6)`), so misses are
  usually near misses with an occasional bad one.
- `P` is the hit count over 1000. Regret is the mean gap over the misses. The histogram
  shows the gap distribution with the regret marked as a dashed line.
