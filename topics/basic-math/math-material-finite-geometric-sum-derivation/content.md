---
title: "Math Material — Finite Geometric Sum: Where Sₙ Comes From"
topic: basic-math
example: math-material-finite-geometric-sum-derivation
course: AP Precalculus
status: material
created: 2026-10-30
author: Wei-Che Hung
---

# Math Material — Finite Geometric Sum: Where Sₙ Comes From

$$
S_n = \frac{a_1\,(1 - r^{\,n})}{1 - r}, \qquad r \ne 1
$$

- $a_1$ = first term, $r$ = ratio, $n$ = number of terms.
- Card 1 derives it. Cards 2–4 use it; type your answers and tap **Check**.

## Derivation

### 1. How the formula is derived

A geometric series: first term $a_1$, each term is the one before times $r$, and there are $n$ terms.

Tap **Show working** to see the five lines that give $S_n$.

<details>
<summary><b>Working</b></summary>

**1. Write the sum.**

$$
S_n = a_1 + a_1 r + a_1 r^2 + \dots + a_1 r^{\,n-1}
$$

**2. Multiply every term by $r$.**

$$
r\,S_n = a_1 r + a_1 r^2 + \dots + a_1 r^{\,n-1} + a_1 r^{\,n}
$$

**3. Subtract line 2 from line 1.** All the middle terms cancel.

$$
S_n - r\,S_n = a_1 - a_1 r^{\,n}
$$

**4. Factor both sides.**

$$
S_n\,(1 - r) = a_1\,(1 - r^{\,n})
$$

**5. Divide by $(1 - r)$.**

$$
S_n = \frac{a_1\,(1 - r^{\,n})}{1 - r}, \qquad r \ne 1
$$

- $r \ne 1$ because we divided by $1 - r$.
- If $r = 1$ every term is $a_1$, so $S_n = n\,a_1$.

</details>

## Examples

### 2. Example 1: use the formula

Find

$$
2 + 6 + 18 + 54
$$

**Practice:** find each sum with the formula.

- **(a)** $1 + 2 + 4 + 8 + 16$
- **(b)** $3 + 12 + 48$
- **(c)** $5 + 10 + 20 + 40 + 80 + 160$

| Sum | $a_1,\ r,\ n$ | $S_n$ |
|---:|---:|---:|
| \text{(a)} | 1,\ 2,\ 5 | ? |
| \text{(b)} | 3,\ 4,\ 3 | ? |
| \text{(c)} | 5,\ 2,\ 6 | ? |

<details>
<summary><b>Working</b></summary>

Read off the three numbers: $a_1 = 2$, $r = 6 \div 2 = 3$, $n = 4$.

$$
\begin{aligned}
S_4 &= \frac{2\,(1 - 3^4)}{1 - 3} \\
&= \frac{2\,(1 - 81)}{-2} \\
&= \frac{-160}{-2} \\
&= \boxed{80}
\end{aligned}
$$

Check by adding: $2 + 6 + 18 + 54 = 80$.

</details>

### 3. Example 2: ratio smaller than 1

Find

$$
16 + 8 + 4 + 2 + 1
$$

**Practice:** find each sum with the formula.

- **(a)** $81 + 27 + 9 + 3$
- **(b)** $64 + 16 + 4$
- **(c)** $100 + 10 + 1$

| Sum | $a_1,\ r,\ n$ | $S_n$ |
|---:|---:|---:|
| \text{(a)} | 81,\ \tfrac{1}{3},\ 4 | ? |
| \text{(b)} | 64,\ \tfrac{1}{4},\ 3 | ? |
| \text{(c)} | 100,\ \tfrac{1}{10},\ 3 | ? |

<details>
<summary><b>Working</b></summary>

Read off: $a_1 = 16$, $r = 8 \div 16 = \tfrac{1}{2}$, $n = 5$.

$$
\begin{aligned}
S_5 &= \frac{16\,\big(1 - (\tfrac{1}{2})^5\big)}{1 - \tfrac{1}{2}} \\
&= \frac{16\,(1 - \tfrac{1}{32})}{\tfrac{1}{2}} \\
&= \frac{16 \cdot \tfrac{31}{32}}{\tfrac{1}{2}} \\
&= \frac{\tfrac{31}{2}}{\tfrac{1}{2}} \\
&= \boxed{31}
\end{aligned}
$$

Check by adding: $16 + 8 + 4 + 2 + 1 = 31$.

</details>

### 4. Example 3: written with sigma

Find

$$
\sum_{k=1}^{6} 3 \cdot 2^{\,k-1}
$$

**Practice:** find each sum with the formula.

- **(a)** $\displaystyle\sum_{k=1}^{4} 4 \cdot 3^{\,k-1}$
- **(b)** $\displaystyle\sum_{k=1}^{3} 2 \cdot 5^{\,k-1}$
- **(c)** $\displaystyle\sum_{k=1}^{8} 2^{\,k-1}$

| Sum | $a_1,\ r,\ n$ | $S_n$ |
|---:|---:|---:|
| \text{(a)} | 4,\ 3,\ 4 | ? |
| \text{(b)} | 2,\ 5,\ 3 | ? |
| \text{(c)} | 1,\ 2,\ 8 | ? |

<details>
<summary><b>Working</b></summary>

Read off: $a_1 = 3$ (the number in front), $r = 2$ (the base), $n = 6$ (the top number).

$$
\begin{aligned}
S_6 &= \frac{3\,(1 - 2^6)}{1 - 2} \\
&= \frac{3\,(1 - 64)}{-1} \\
&= \frac{-189}{-1} \\
&= \boxed{189}
\end{aligned}
$$

Check by adding: $3 + 6 + 12 + 24 + 48 + 96 = 189$.

</details>
