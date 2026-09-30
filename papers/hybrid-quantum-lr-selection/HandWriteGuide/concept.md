---
title: "HandWriteGuide P1 — The General Concept"
paper: hybrid-quantum-lr-selection
page: 1
status: handwritten-guide
created: 2026-09-30
author: Wei-Che Hung
---

# P1 — The General Concept

<details open>
<summary>P1 — from per-group learning rates to the quantum search and its expected cost</summary>

![Handwritten page P1: the paper title with G = 6 groups and K = 8 rates marked; step 1, a learning rate applied at every layer group, w_g updated by minus eta_g times d_g for g from 1 to G; step 2, the learning-rate space E of K values, a profile z as one choice per group, and the count N = K to the power G; step 3, the profiles encoded into a quantum register of ceiling log2 N qubits and the uniform initial state; step 4, Grover asks how many profiles beat the current one, M = the number of z with f(z) below f(y), with the success probability sine squared of (2j+1) theta and theta = arcsin of root M over N, a small-angle form crossed out; step 5, M is unknown so BBHT varies j: 5-1 the depth j drawn uniformly below the ceiling of m, 5-2 success resets m to 1 and moves the threshold, failure multiplies m by lambda = 6/5 (5/4 crossed out) capped at root N, 5-3 the expected query count E(Q) at most 45/4 root N from Dürr–Høyer; a small sketch nests E(Q), BBHT and DH; a margin line reads "the sun will shine once again"](media/handwrite-p1-concept.jpg)

</details>

The page walks through the method of the paper in five steps: where the learning
rates act, how the candidate profiles are counted, how they enter a quantum
register, what one Grover search asks, and how the BBHT schedule turns that
question into a search with an expected cost. The sections below type out each
step with the paper's symbols.

## 1. A learning rate for every layer group

The model's layers are split into $G$ groups ($G = 6$ in the paper). Group $g$ has
its own learning rate $\eta_g$, and an optimizer step updates the group's weights
$w_g$ with the group's descent direction $d_g$:

```math
w_g \leftarrow w_g - \eta_g\, d_g, \qquad g = 1, \dots, G .
```

## 2. The learning-rate space and the profiles

Each group chooses its rate from the same menu of $K$ values ($K = 8$ in the paper):

```math
E = \{\eta^{(1)}, \eta^{(2)}, \dots, \eta^{(K)}\}.
```

A *profile* is one choice per group, $z = (\eta_1, \dots, \eta_G) \in E^G$, so the
number of profiles is

```math
N = K^G ,
```

which is $8^6 = 262{,}144$ for the paper's design.

## 3. Encoding the profiles into a quantum register

Every profile gets an integer index, and the index is written in binary on a
search register of

```math
q_{\mathrm{srch}} = \lceil \log_2 N \rceil
```

qubits ($q_{\mathrm{srch}} = 18$ for $N = 2^{18}$). The search starts from the
uniform superposition over all $N$ profiles:

```math
|\psi_0\rangle = \frac{1}{\sqrt{N}} \sum_{z} |z\rangle .
```

## 4. What one Grover search asks

The current best profile $y$ is the *threshold*. One Grover search asks for a
profile that beats it; the number of such profiles is

```math
M = \#\{\, z : f(z) < f(y) \,\},
```

where $f$ is the profile's score. After $j$ Grover iterations a measurement
returns a better profile with probability

```math
P_j(M) = \sin^2\!\big((2j+1)\,\theta\big), \qquad \theta = \arcsin\sqrt{M/N} .
```

The page crosses out the form $(2j+1)^2 \sin^2\theta$: it is only the small-angle
approximation of the same expression.

## 5. $M$ is unknown, so BBHT varies $j$

The best number of iterations depends on $M$, and $M$ is not known during the
search. The BBHT schedule (Boyer, Brassard, Høyer and Tapp) replaces the fixed $j$
by a random one drawn from a growing range $m$.

**5-1. Choosing $j$.** The depth is drawn uniformly below the current range:

```math
j \sim \mathcal{U}\{0, 1, \dots, \lceil m \rceil - 1\}.
```

**5-2. Updating the range.** A success moves the threshold and resets the range; a
failure enlarges the range, up to $\sqrt{N}$:

```math
\text{success: } y \leftarrow z,\; m \leftarrow 1, \qquad
\text{failure: } m \leftarrow \min(\lambda m, \sqrt{N}), \quad \lambda = 6/5 .
```

The page first wrote $\lambda = 5/4$ and corrected it to the paper's $6/5$.

**5-3. The expected number of Grover iterations.** Dürr and Høyer's minimum finding
repeats BBHT searches, each against the latest threshold, until the minimum is
reached. The expected total number of Grover iterations $Q$ satisfies

```math
\mathbb{E}[Q] \le \frac{45}{4}\sqrt{N} .
```

The small sketch at the bottom of the page shows how the pieces nest: the bound on
$\mathbb{E}[Q]$ comes from Dürr–Høyer, which is built on BBHT. Page 2 derives the
bound: [P2 — why E(Q) ≤ 45/4 √N](expected-query-bound.md).

---

[Back to the HandWriteGuide index](main.md)
