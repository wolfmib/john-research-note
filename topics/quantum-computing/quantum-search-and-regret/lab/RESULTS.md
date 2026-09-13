# Results

Output of `regret_toy.py` (seed 20260913).

```
Part A -- probability of finding the best set
  trials = 1000, found best = 999
  P = 999/1000 = 0.999

Part B -- regret of three misses
  L(best) = 0, L(misses) = [3, 4, 23]
  regret = [(3 - 0) + (4 - 0) + (23 - 0)] / 3 = 10

Part C -- toy search, seeded
  N = 64 sets, trials = 1000, L(best) = 10.00
  found best = 944  ->  P = 0.944
  misses = 56  ->  regret = 7.19
  miss gaps: min 2.26, median 6.15, max 26.70
  histogram -> media/quantum-search-and-regret-regret-histogram.png

```
