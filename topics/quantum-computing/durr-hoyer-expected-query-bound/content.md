---
title: "Dürr–Høyer Expected Query Bound"
topic: quantum-computing
example: threshold-ranks-and-the-45-over-4-constant
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-30
author: Wei-Che Hung
---

# Dürr–Høyer Expected Query Bound

## Working Notes

<details open>
<summary>1 / 1 — the expected cost as a sum over threshold ranks, the visiting probability 1/r, and the sum that gives 45/4</summary>

![Handwritten note: E[Q] written as a sum over the possible threshold ranks r of the probability of visiting rank r, equal to 1/r, times the expected Grover work of a BBHT search from that threshold, 9/2 root of N over r-1; a strip of N sorted ranks with arrows jumping to better ranks; a boxed calculation that substitutes s = r - 1, bounds the tail by an integral of x to the minus 3/2 that stays below 2, and boxes E at most 45/4 root N; a region explaining the 1/r with the example N = 11, r = 10, a recursion that gives P_(k+1) = P_k, and an average over the uniform starting rank that gives P_N(r) = 1/r](media/durr-hoyer-expected-query-bound-note-1-proof.jpg)

</details>

The page proves where the constant in Dürr and Høyer's bound comes from. Minimum
finding lowers a threshold through a chain of better and better candidates, and
its expected cost splits over the ranks that chain can pass through: the chance of
passing through rank $r$, times the cost of one quantum search started there. The
chance turns out to be exactly $1/r$, the cost is a BBHT bound, and a short sum
turns the two into $\frac{45}{4}\sqrt{N}$. The sections below write each step out
and check the two ingredients numerically.

## Research Question

Dürr–Høyer minimum finding (Dürr and Høyer, 1996) finds the smallest of $N$ values
with an expected number of Grover iterations $Q$ that grows like $\sqrt{N}$, against
$N$ evaluations for a classical scan. The question of this note is where the
constant comes from:

```math
\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N} .
```

Dürr and Høyer's statement carries a second, lower-order term,
$\frac{7}{10}(\log_2 N)^2$, on top of the part derived here.

## Setting

Sort the $N$ values, rank $1$ being the minimum. The algorithm keeps a threshold
$y$, starting at a uniformly random index. Each stage runs a BBHT search
(Boyer, Brassard, Høyer and Tapp, 1998) for an index whose value is below the
threshold's; when one is found, it becomes the new threshold. A BBHT search returns
each marked index with equal probability, so from a threshold of rank $k$ the next
threshold rank is uniform over $\{1, \dots, k-1\}$.

The cost then splits over the ranks the threshold visits:

```math
\mathbb{E}[Q] = \sum_{r=2}^{N} P(\text{visit rank } r) \times \mathbb{E}_{\mathrm{BBHT}}(\text{Grover work at } r) .
```

## The Visiting Probability Is $1/r$

Let $P_k$ be the probability that rank $r$ is ever visited when the current
threshold has rank $k > r$. From $k = r+1$ the next threshold is uniform over
$\{1, \dots, r\}$, so $P_{r+1} = 1/r$. From a general $k$, the next threshold lands on
$r$ directly or on a rank $j$ between them:

```math
P_k = \frac{1}{k-1}\Big(1 + \sum_{j=r+1}^{k-1} P_j\Big).
```

The same line written for $k+1$ gives

```math
k P_{k+1} = 1 + \sum_{j=r+1}^{k} P_j = (k-1)P_k + P_k = k P_k ,
```

so $P_{k+1} = P_k = \dots = P_{r+1} = 1/r$. Averaging over the uniform start
(below $r$: never; at $r$: always; above $r$: with probability $1/r$),

```math
P(\text{visit rank } r) = \frac{1}{N} + \frac{1}{N}\sum_{k=r+1}^{N}\frac{1}{r} = \frac{1}{N} + \frac{N-r}{N r} = \frac{1}{r} .
```

The probability does not depend on $N$: the second-best value is visited half of
the time, the tenth-best one run in ten, whatever the size of the list.

## The Cost of One Search

From a threshold of rank $r$ there are $t = r-1$ better indices. BBHT finds one of
$t$ marked items among $N$ with an expected number of Grover iterations bounded as

```math
\mathbb{E}_{\mathrm{BBHT}}(r) \le \frac{9}{2}\sqrt{\frac{N}{r-1}} .
```

The fewer indices are left below the threshold, the longer the search: the last
stages, close to the minimum, are the expensive ones.

## The Sum and the Constant

```math
\mathbb{E}[Q] \le \frac{9}{2}\sqrt{N}\sum_{r=2}^{N}\frac{1}{r\sqrt{r-1}}
= \frac{9}{2}\sqrt{N}\sum_{s=1}^{N-1}\frac{1}{(s+1)\sqrt{s}}, \qquad s = r-1 .
```

Split the sum into the $s = 1$ term and the terms with $s \ge 2$:

```math
\sum_{s=1}^{N-1}\frac{1}{(s+1)\sqrt{s}}
= \underbrace{\frac{1}{2}}_{s\,=\,1} + \underbrace{\sum_{s=2}^{N-1}\frac{1}{(s+1)\sqrt{s}}}_{s\,\ge\,2}
\le \frac{1}{2} + \sum_{s=2}^{N-1} s^{-3/2} ,
```

because $\frac{1}{(s+1)\sqrt{s}} \le s^{-3/2}$. The $s \ge 2$ part is a decreasing sum, so it stays below its
integral, and the integral has the upper bound $2$:

```math
\sum_{s=2}^{N-1} s^{-3/2} \le \int_{1}^{N-1} x^{-3/2}\,dx = 2\Big(1 - \frac{1}{\sqrt{N-1}}\Big) \le 2 .
```

Hence, with the $s = 1$ term and the $s \ge 2$ bound together,

```math
\mathbb{E}[Q] \le \frac{9}{2}\Big(\frac{1}{2} + 2\Big)\sqrt{N} = \frac{45}{4}\sqrt{N} .
```

The bound must compare each term with something *larger*. Replacing
$\frac{1}{r\sqrt{r-1}}$ by $r^{-3/2}$, as the handwritten page does in one line, compares
it with something smaller; using $(r-1)^{-3/2} = s^{-3/2}$ keeps the direction right
and gives the same constant.

## Numeric Check

The script [`lab/check_visit_probability.py`](lab/check_visit_probability.py)
simulates the threshold chain (uniform start, uniform jump to a strictly better
rank) $100{,}000$ times and evaluates the sum
$S(N) = \sum_{r=2}^{N} \frac{1}{r\sqrt{r-1}}$.

| Check | Result |
|---|---|
| Visit frequency vs $1/r$, $N = 11$ | largest difference over all ranks $0.0018$ |
| Visit frequency vs $1/r$, $N = 64$ | largest difference over all ranks $0.0022$ |
| $S(11)$ | $1.2615$ |
| $S(64)$ | $1.6103$ |
| $S(1024)$ | $1.7975$ |
| $S(2^{18})$ | $1.8561$ |
| $S(10^7)$ | $1.8594$ |

$S(N)$ approaches about $1.86$, below the $\tfrac{5}{2}$ used in the proof, so the
rounded constant $\frac{45}{4} = 11.25$ is safe; the sum itself gives about
$\frac{9}{2}\times 1.86 \approx 8.4$.

## Reproducing These Results

```bash
cd topics/quantum-computing/durr-hoyer-expected-query-bound/lab
python check_visit_probability.py      # NumPy only, about 2 s
```

## Reference Reading

- C. Dürr and P. Høyer, "A quantum algorithm for finding the minimum,"
  [arXiv:quant-ph/9607014](https://arxiv.org/abs/quant-ph/9607014) (1996).
- M. Boyer, G. Brassard, P. Høyer and A. Tapp, "Tight bounds on quantum
  searching," *Fortschritte der Physik* 46, 493–505 (1998),
  [arXiv:quant-ph/9605034](https://arxiv.org/abs/quant-ph/9605034).
- Related notes: [Dürr–Høyer runtime accounting formula](../../animations/durr-hoyer-runtime-three-terms/content.md),
  [Dürr–Høyer minimum finding, part 1](../../animations/durr-hoyer-stop-part1-ladder-clock-one-climb-budget/content.md),
  and the handwritten paper guide
  [P2 — why E(Q) ≤ 45/4 √N](../../../papers/hybrid-quantum-lr-selection/HandWriteGuide/expected-query-bound.md).

## Concepts

- The cost of a chain of searches splits over the states the chain visits: how
  likely each state is, times what one search from it costs.
- A threshold that always jumps to a uniformly random better value visits rank $r$
  with probability exactly $1/r$, independent of $N$.
- The last few thresholds dominate: the search from rank $r$ costs about
  $\sqrt{N/(r-1)}$, but the $1/r$ weighting keeps the total at order $\sqrt{N}$.

## Summary

Dürr–Høyer minimum finding lowers a threshold through better and better values, so
its expected number of Grover iterations is a sum over the ranks the threshold can
visit. Rank $r$ is visited with probability exactly $1/r$, one BBHT search from it
costs at most $\frac{9}{2}\sqrt{N/(r-1)}$ iterations, and the resulting sum stays below
$\tfrac{5}{2}$, which gives $\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N}$. A simulation confirms the
$1/r$ law, and the exact sum approaches about $1.86$, so the constant is a safe upper
bound.

### 繁體中文

Dürr–Høyer 最小值搜尋會把門檻一路降到越來越好的值，因此它的 Grover 迭代期望次數可以寫成「門檻可能經過的各個名次」的總和。第 $r$ 名被經過的機率恰好是 $1/r$，從該名次出發的一次 BBHT 搜尋最多花 $\frac{9}{2}\sqrt{N/(r-1)}$ 次迭代，而整個總和不超過 $\tfrac{5}{2}$，於是得到 $\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N}$。模擬驗證了 $1/r$ 規律，實際總和趨近約 $1.86$，所以這個常數是安全的上界。

### Français

La recherche du minimum de Dürr–Høyer abaisse un seuil à travers des valeurs de plus en plus petites ; son nombre moyen d'itérations de Grover est donc une somme sur les rangs que le seuil peut visiter. Le rang $r$ est visité avec une probabilité exactement égale à $1/r$, une recherche BBHT partant de ce rang coûte au plus $\frac{9}{2}\sqrt{N/(r-1)}$ itérations, et la somme obtenue reste inférieure à $\tfrac{5}{2}$, ce qui donne $\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N}$. Une simulation confirme la loi en $1/r$, et la somme exacte tend vers environ $1{,}86$ : la constante est donc une borne supérieure sûre.

### Deutsch

Die Minimumsuche nach Dürr–Høyer senkt eine Schwelle über immer bessere Werte ab; ihre erwartete Zahl an Grover-Iterationen ist daher eine Summe über die Ränge, die die Schwelle besuchen kann. Rang $r$ wird mit Wahrscheinlichkeit genau $1/r$ besucht, eine BBHT-Suche von dort kostet höchstens $\frac{9}{2}\sqrt{N/(r-1)}$ Iterationen, und die entstehende Summe bleibt unter $\tfrac{5}{2}$, was $\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N}$ ergibt. Eine Simulation bestätigt das $1/r$-Gesetz, und die exakte Summe nähert sich etwa $1{,}86$, sodass die Konstante eine sichere obere Schranke ist.

### Русский

Алгоритм поиска минимума Дюрра–Хойера понижает порог через всё лучшие значения, поэтому ожидаемое число итераций Гровера есть сумма по рангам, которые может посетить порог. Ранг $r$ посещается с вероятностью ровно $1/r$, один поиск BBHT из этого ранга стоит не более $\frac{9}{2}\sqrt{N/(r-1)}$ итераций, а получающаяся сумма не превышает $\tfrac{5}{2}$, что даёт $\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N}$. Моделирование подтверждает закон $1/r$, а точная сумма стремится примерно к $1{,}86$, так что константа является надёжной верхней оценкой.
