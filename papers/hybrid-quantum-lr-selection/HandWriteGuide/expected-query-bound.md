---
title: "HandWriteGuide P2 — Why E(Q) ≤ 45/4 √N"
paper: hybrid-quantum-lr-selection
page: 2
status: handwritten-guide
created: 2026-09-30
author: Wei-Che Hung
---

# P2 — Why $\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N}$

<details open>
<summary>P2 — the expected cost as a sum over threshold ranks, the visiting probability 1/r, and the sum that gives 45/4</summary>

![Handwritten page P2: E[Q] written as a sum over the possible threshold ranks r of the probability of visiting rank r, equal to 1/r, times the expected Grover work of a BBHT search from that threshold, 9/2 root of N over r-1, with that factor marked "later P3"; a strip of N sorted ranks with arrows jumping to better ranks; a boxed calculation that sums the two factors, substitutes s = r - 1, bounds the tail by an integral of x to the minus 3/2 that stays below 2, and boxes E at most 45/4 root N; a large region explaining the 1/r: the example N = 11, r = 10 giving 1/10, the general case with a recursion P_k equal to 1/(k-1) times 1 plus the sum of P_j, which gives k P_(k+1) = k P_k and so P_(k+1) = P_k; and a blue region that averages over the uniform starting rank to get P_N(r) = 1/N + (1/N)(N - r)/r = 1/r](media/handwrite-p2-expected-query-bound.jpg)

</details>

The page proves the bound quoted at the end of [P1](concept.md). The idea is to
split the expected number of Grover iterations by the thresholds the search passes
through: every threshold rank $r$ contributes *the probability that the search ever
sits at rank $r$* times *the expected Grover work of one BBHT search started from
there*. The first factor is $1/r$ and is proved on this page; the second factor
comes from BBHT and is the subject of page 3.

## Setting

Sort the $N$ profiles by score, rank $1$ being the best. The threshold $y$ starts
at a uniformly random rank. From a threshold of rank $k$, a BBHT search returns
one of the $k-1$ better profiles, and each of them is equally likely, so the next
threshold rank is uniform over $\{1, \dots, k-1\}$.

## The decomposition

```math
\mathbb{E}[Q] = \sum_{r=2}^{N} \underbrace{P(\text{visit rank } r)}_{\text{(1)}}
\times \underbrace{\mathbb{E}_{\mathrm{BBHT}}(\text{Grover work at } r)}_{\text{(2)}} .
```

Rank $1$ contributes nothing: once the threshold is the minimum there is nothing
left to find (deciding *when to stop* is a separate question, see the paper's
termination criteria).

## Factor (1): the visiting probability is $1/r$

Write $P_k(r)$ for the probability that rank $r$ is ever visited when the current
threshold has rank $k > r$.

**(A) One step above.** From $k = r+1$ the next threshold is uniform over
$\{1, \dots, r\}$, so it lands on $r$ with probability $1/r$. The page's example is
$N = 11$, $r = 10$: $P_{11}(10) = 1/10$. In general

```math
P_{r+1}(r) = \frac{1}{r}.
```

**(B) Any start above $r$.** From rank $k$, the next threshold either lands on $r$
directly, or on some $j$ between $r$ and $k$ from where $r$ is still ahead:

```math
P_k = \frac{1}{k-1}\Big(1 + \sum_{j=r+1}^{k-1} P_j\Big).
```

Writing the same line for $k+1$ and subtracting,

```math
k P_{k+1} = 1 + \sum_{j=r+1}^{k} P_j = \underbrace{1 + \sum_{j=r+1}^{k-1} P_j}_{(k-1) P_k} + P_k = k P_k
\quad\Longrightarrow\quad P_{k+1} = P_k .
```

So $P_k(r) = 1/r$ for every start $k > r$.

**Average over the uniform start.** The first threshold is uniform over all $N$
ranks: below $r$ (rank $r$ is never visited), exactly $r$ (visited), or above $r$
(visited with probability $1/r$):

```math
P_N(r) = 0 + \frac{1}{N} + \frac{1}{N}\sum_{k=r+1}^{N} \frac{1}{r}
= \frac{1}{N} + \frac{N-r}{N r} = \frac{r + N - r}{N r} = \frac{1}{r}.
```

## Factor (2): one BBHT search from rank $r$

From a threshold of rank $r$ there are $r-1$ better profiles. The BBHT bound on
the expected number of Grover iterations to find one of $t$ marked items among
$N$, used here with $t = r - 1$, is

```math
\mathbb{E}_{\mathrm{BBHT}}(r) \le \frac{9}{2}\sqrt{\frac{N}{r-1}} .
```

Its derivation is the subject of page 3 (to come).

## The sum

Combining (1) and (2):

```math
\mathbb{E}[Q] \le \frac{9}{2}\sqrt{N}\, \sum_{r=2}^{N} \frac{1}{r\sqrt{r-1}}
= \frac{9}{2}\sqrt{N}\, \sum_{s=1}^{N-1} \frac{1}{(s+1)\sqrt{s}}, \qquad s = r - 1 .
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
\sum_{s=2}^{N-1} s^{-3/2} \le \int_{1}^{N-1} x^{-3/2}\, dx
= \Big[-2x^{-1/2}\Big]_{1}^{N-1} = 2\Big(1 - \frac{1}{\sqrt{N-1}}\Big) \le 2 .
```

Therefore, with the $s = 1$ term and the $s \ge 2$ bound together,

```math
\mathbb{E}[Q] \le \frac{9}{2}\Big(\frac{1}{2} + 2\Big)\sqrt{N} = \frac{45}{4}\sqrt{N} .
```

<!--
Audit note on the handwritten page (kept as a comment, not shown):
**A correction to one line of the page.** The page replaces $\frac{1}{r}\cdot\frac{1}{\sqrt{r-1}}$
by $r^{-3/2}$. Since $r^{-3/2} < \frac{1}{r\sqrt{r-1}}$, that step goes the wrong way for
an upper bound. The line above uses $s^{-3/2} = (r-1)^{-3/2}$ instead, which is larger,
and reaches the same constant $\tfrac{1}{2} + 2 = \tfrac{5}{2}$, so the page's result
$\frac{45}{4}\sqrt{N}$ stands.
-->

**How tight is 5/2?** The sum converges: $\sum_{s \ge 1} \frac{1}{(s+1)\sqrt{s}} \approx 1.86$
(1.26 at $N = 11$, 1.86 at $N = 2^{18}$), so $\frac{45}{4}$ is a safe round constant rather
than the exact one. The computation and a simulation of the $1/r$ law are in the topic
note [Dürr–Høyer expected query bound](../../../topics/quantum-computing/durr-hoyer-expected-query-bound/content.md).

---

[Back to the HandWriteGuide index](main.md)
