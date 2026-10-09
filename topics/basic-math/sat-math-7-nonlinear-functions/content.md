---
title: "SAT Math 7 — Nonlinear Functions"
topic: basic-math
example: sat-math-7-nonlinear-functions
course: SAT Math
status: material
created: 2026-10-09
author: Wei-Che Hung
---

# SAT Math 7 — Nonlinear Functions

**SAT domain:** Advanced Math (13–15 of the 44 math questions).

**Key ideas**
- Exponential model $f(t) = a \cdot b^{t}$:
  - $a$ is the starting value
  - growth of $r\%$: $b = 1 + \tfrac{r}{100}$
  - decay of $r\%$: $b = 1 - \tfrac{r}{100}$
- Doubling every 3 years: $a \cdot 2^{t/3}$.
- Quadratic forms:
  - vertex form $f(x) = a(x - h)^2 + k$: vertex $(h, k)$
  - factored form $f(x) = a(x - p)(x - q)$: $x$-intercepts $p$ and $q$
  - the vertex is halfway between $p$ and $q$
- $a > 0$: opens up (a minimum); $a < 0$: opens down (a maximum).
- Shifts:
  - $f(x) + k$: up $k$
  - $f(x - h)$: right $h$

**Watch out**
- A 15% loss keeps 85%: the factor is 0.85, not 0.15.
- $f(x - 3)$ moves the graph **right** 3, not left.

## 1. Exam 1 — Depreciation

A car bought for €24,000 loses 15% of its value each year.

Which function gives its value $V$, in euros, after $t$ years?

**A.** $V(t) = 24000(0.15)^t$

**B.** $V(t) = 24000(0.85)^t$

**C.** $V(t) = 24000(1.15)^t$

**D.** $V(t) = 24000 - 0.15t$

<details>
<summary><b>Working</b></summary>

Losing 15% each year keeps 85% of the value:

$$
b = 1 - 0.15 = 0.85
$$

Starting value $a = 24000$:

$$
\boxed{V(t) = 24000(0.85)^t}
$$

**Answer: B** — $0.15^t$ keeps only 15% each year.

</details>

## 2. Exam 2 — Minimum from factored form

$$
f(x) = 2(x - 3)(x + 5)
$$

What is the minimum value of $f$? (Type the answer.)

<details>
<summary><b>Working</b></summary>

The zeros are $x = 3$ and $x = -5$. The vertex is halfway between them:

$$
\begin{aligned} x &= \frac{3 + (-5)}{2} \\ &= -1 \end{aligned}
$$

$$
\begin{aligned} f(-1) &= 2(-1 - 3)(-1 + 5) \\ &= 2(-4)(4) \\ &= -32 \end{aligned}
$$

$a = 2 > 0$, so the vertex is a minimum.

$$
\boxed{-32}
$$

</details>
