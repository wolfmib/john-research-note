---
title: "Math Material — Summation Formulas"
topic: basic-math
example: math-material-summation-formulas
course: AP Precalculus
status: material
created: 2026-10-23
author: Wei-Che Hung
---

# Math Material — Summation Formulas

**Sigma notation** is a short way to write a long sum:

$$
\sum_{k=1}^{n} a_k = a_1 + a_2 + \dots + a_n
$$

- $k$ counts from the bottom number to the top number.
- Seven formulas below give the total without adding every term.
- Cards 5–7 are the sums of the arithmetic (linear) and geometric (exponential) sequences from 2.1–2.2.

Type your answers in each table and tap **Check**.

## Rules

### 1. Sum rules: split, pull out, count

Three rules let you break any sum into pieces you already know:

$$
\sum_{k=1}^{n} c = nc
$$

- Adding the same number $c$ exactly $n$ times.

$$
\sum_{k=1}^{n} c\,a_k = c\sum_{k=1}^{n} a_k
$$

- A constant factor comes out of the sum.

$$
\sum_{k=1}^{n} (a_k + b_k) = \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} b_k
$$

- A sum of two sequences splits into two sums.

**Practice:** you are given

$$
\sum_{k=1}^{10} a_k = 40
$$

and

$$
\sum_{k=1}^{10} b_k = 15
$$

Find each sum (every sum runs from $k=1$ to $10$):

- **(a)** $\displaystyle \sum 5$
- **(b)** $\displaystyle \sum 3a_k$
- **(c)** $\displaystyle \sum (a_k + b_k)$
- **(d)** $\displaystyle \sum (a_k - 2b_k)$
- **(e)** $\displaystyle \sum (2a_k + 3)$

| Sum | Rule | Value |
|---:|---:|---:|
| \text{(a)} | \text{count} | ? |
| \text{(b)} | \text{pull out} | ? |
| \text{(c)} | \text{split} | ? |
| \text{(d)} | \text{split, pull} | ? |
| \text{(e)} | \text{all three} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** find $\displaystyle\sum_{k=1}^{10} (3a_k - 2b_k + 1)$.

- Split into three sums.
- Pull the constants out.
- The $1$ is added 10 times.

$$
\begin{aligned}
\sum (3a_k - 2b_k + 1) &= 3\sum a_k - 2\sum b_k + \sum 1 \\
&= 3(40) - 2(15) + 10 \\
&= 120 - 30 + 10 \\
&= \boxed{100}
\end{aligned}
$$

**Example 2:** find $\displaystyle\sum_{k=1}^{10} (3k + 2)$, using $\displaystyle\sum_{k=1}^{10} k = 55$ (card 2).

$$
\begin{aligned}
\sum_{k=1}^{10} (3k + 2) &= 3\sum_{k=1}^{10} k + \sum_{k=1}^{10} 2 \\
&= 3(55) + 10(2) \\
&= 165 + 20 \\
&= \boxed{185}
\end{aligned}
$$

**Common mistake:** $\displaystyle\sum_{k=1}^{10} 2 = 2$ is wrong.

- The 2 is added once for every $k$, so the sum is $10 \times 2 = 20$.

</details>

## Powers of k

### 2. Sum of k: 1 + 2 + 3 + … + n

$$
\sum_{k=1}^{n} k = \frac{n(n+1)}{2}
$$

**Where it comes from (Gauss):**

- Write the sum forwards and backwards.
- Each column adds to $n+1$, and there are $n$ columns.
- That is twice the sum, so divide by 2.

**Practice:** find each sum. Sum (e) starts at $k = 11$, not at 1.

- **(a)** $\displaystyle \sum_{k=1}^{10} k$
- **(b)** $\displaystyle \sum_{k=1}^{30} k$
- **(c)** $\displaystyle \sum_{k=1}^{50} k$
- **(d)** $\displaystyle \sum_{k=1}^{100} k$
- **(e)** $\displaystyle \sum_{k=11}^{20} k$

| Sum | $n$ | Value |
|---:|---:|---:|
| \text{(a)} | 10 | ? |
| \text{(b)} | 30 | ? |
| \text{(c)} | 50 | ? |
| \text{(d)} | 100 | ? |
| \text{(e)} | 20 - 10 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $1 + 2 + 3 + \dots + 100$.

$$
\begin{aligned}
S &= 1 + 2 + \dots + 99 + 100 \\
S &= 100 + 99 + \dots + 2 + 1 \\
2S &= 101 + 101 + \dots + 101 \\
2S &= 100 \times 101 \\
S &= \boxed{5050}
\end{aligned}
$$

**Example 2:** $\displaystyle\sum_{k=1}^{20} k$ with the formula, $n = 20$:

$$
\begin{aligned}
\sum_{k=1}^{20} k &= \frac{20 \times 21}{2} \\
&= \frac{420}{2} \\
&= \boxed{210}
\end{aligned}
$$

**Example 3:** a sum that does not start at 1: $\displaystyle\sum_{k=11}^{20} k$.

- Take everything up to 20, then remove 1 to 10.

$$
\begin{aligned}
\sum_{k=11}^{20} k &= \sum_{k=1}^{20} k - \sum_{k=1}^{10} k \\
&= 210 - 55 \\
&= \boxed{155}
\end{aligned}
$$

</details>

### 3. Sum of squares: 1² + 2² + … + n²

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

- Three factors on top: $n$, the next number $n+1$, and $2n+1$.
- The top is always a multiple of 6, so the answer is a whole number.

**Practice:** the **Top** column gives $n(n+1)(2n+1)$. Divide by 6.

- **(a)** $\displaystyle \sum_{k=1}^{3} k^2$
- **(b)** $\displaystyle \sum_{k=1}^{5} k^2$
- **(c)** $\displaystyle \sum_{k=1}^{6} k^2$
- **(d)** $\displaystyle \sum_{k=1}^{10} k^2$
- **(e)** $\displaystyle \sum_{k=1}^{12} k^2$

| Sum | Top | Value |
|---:|---:|---:|
| \text{(a)} | 84 | ? |
| \text{(b)} | 330 | ? |
| \text{(c)} | 546 | ? |
| \text{(d)} | 2310 | ? |
| \text{(e)} | 3900 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\displaystyle\sum_{k=1}^{4} k^2$, checked term by term first:

$$
\begin{aligned}
1^2 + 2^2 + 3^2 + 4^2 &= 1 + 4 + 9 + 16 \\
&= 30
\end{aligned}
$$

Now with the formula, $n = 4$:

$$
\begin{aligned}
\sum_{k=1}^{4} k^2 &= \frac{4 \times 5 \times 9}{6} \\
&= \frac{180}{6} \\
&= \boxed{30}
\end{aligned}
$$

**Example 2:** $\displaystyle\sum_{k=1}^{10} k^2$, $n = 10$:

$$
\begin{aligned}
\sum_{k=1}^{10} k^2 &= \frac{10 \times 11 \times 21}{6} \\
&= \frac{2310}{6} \\
&= \boxed{385}
\end{aligned}
$$

**Common mistake:** $\displaystyle\sum k^2 \ne \Big(\sum k\Big)^2$.

- For $n = 4$: $30 \ne 10^2 = 100$.

</details>

### 4. Sum of cubes: 1³ + 2³ + … + n³

$$
\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2
$$

- The sum of cubes is the **square of the sum of k** (card 2).
- So: find $1 + 2 + \dots + n$ first, then square it.

**Practice:** the middle column gives $\displaystyle\sum k$. Square it.

- **(a)** $\displaystyle \sum_{k=1}^{3} k^3$
- **(b)** $\displaystyle \sum_{k=1}^{5} k^3$
- **(c)** $\displaystyle \sum_{k=1}^{6} k^3$
- **(d)** $\displaystyle \sum_{k=1}^{10} k^3$
- **(e)** $\displaystyle \sum_{k=1}^{20} k^3$

| Sum | $\sum k$ | Value |
|---:|---:|---:|
| \text{(a)} | 6 | ? |
| \text{(b)} | 15 | ? |
| \text{(c)} | 21 | ? |
| \text{(d)} | 55 | ? |
| \text{(e)} | 210 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\displaystyle\sum_{k=1}^{4} k^3$, checked term by term first:

$$
\begin{aligned}
1^3 + 2^3 + 3^3 + 4^3 &= 1 + 8 + 27 + 64 \\
&= 100
\end{aligned}
$$

With the formula, $n = 4$:

$$
\begin{aligned}
1 + 2 + 3 + 4 &= 10 \\
\sum_{k=1}^{4} k^3 &= 10^2 \\
&= \boxed{100}
\end{aligned}
$$

**Example 2:** $\displaystyle\sum_{k=1}^{10} k^3$, $n = 10$:

$$
\begin{aligned}
\sum_{k=1}^{10} k &= \frac{10 \times 11}{2} \\
&= 55 \\
\sum_{k=1}^{10} k^3 &= 55^2 \\
&= \boxed{3025}
\end{aligned}
$$

</details>

## Sequences (2.1–2.2)

### 5. Arithmetic series: add a linear pattern

An **arithmetic** sequence adds the same $d$ each time (linear, topic 2.2).

$$
a_n = a_1 + (n-1)d
$$

The sum of its first $n$ terms:

$$
S_n = \frac{n\,(a_1 + a_n)}{2}
$$

- Number of terms × the average of the first and last term.
- Same pairing idea as $1 + 2 + \dots + n$.

**Practice:** the middle column gives the number of terms $n$.

- **(a)** $\displaystyle 2 + 4 + \dots + 20$
- **(b)** $\displaystyle 5 + 8 + \dots + 32$
- **(c)** $\displaystyle \sum_{n=1}^{8} (3n + 1)$
- **(d)** $\displaystyle 100 + 95 + \dots + 55$
- **(e)** $\displaystyle \sum_{k=1}^{20} (2k - 1)$

| Series | $n$ | Sum |
|---:|---:|---:|
| \text{(a)} | 10 | ? |
| \text{(b)} | 10 | ? |
| \text{(c)} | 8 | ? |
| \text{(d)} | 10 | ? |
| \text{(e)} | 20 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\displaystyle\sum_{n=1}^{5} (2n - 1) = 1 + 3 + 5 + 7 + 9$.

- First term 1, last term 9, $n = 5$ terms.

$$
\begin{aligned}
S_5 &= \frac{5\,(1 + 9)}{2} \\
&= \frac{50}{2} \\
&= \boxed{25}
\end{aligned}
$$

**Example 2:** $3 + 7 + 11 + \dots + 39$.

- First find how many terms: $d = 4$.

$$
\begin{aligned}
39 &= 3 + (n-1)(4) \\
36 &= (n-1)(4) \\
n - 1 &= 9 \\
n &= 10
\end{aligned}
$$

Then the sum:

$$
\begin{aligned}
S_{10} &= \frac{10\,(3 + 39)}{2} \\
&= \frac{420}{2} \\
&= \boxed{210}
\end{aligned}
$$

**Common mistake:** counting terms as $(39 - 3) \div 4 = 9$.

- That counts the gaps. There is one more term than gaps: $n = 10$.

</details>

### 6. Finite geometric series: add an exponential pattern

A **geometric** sequence multiplies by the same $r$ each time (exponential, topic 2.2).

$$
a_n = a_1 r^{\,n-1}
$$

The sum of its first $n$ terms ($r \ne 1$):

$$
S_n = \frac{a_1\,(1 - r^n)}{1 - r}
$$

**Where it comes from:**

- Write $S_n$ and $rS_n$ one under the other.
- Subtract: every middle term cancels, leaving $a_1 - a_1 r^n$.

**Practice:** the middle column gives $a_1,\ r,\ n$. Fractions like 155/16 are fine.

- **(a)** $\displaystyle 1 + 2 + 4 + 8 + 16$
- **(b)** $\displaystyle 3 + 6 + 12 + \dots$
- **(c)** $\displaystyle \sum_{n=1}^{4} 2 \cdot 5^{\,n-1}$
- **(d)** $\displaystyle 81 + 27 + 9 + 3 + 1$
- **(e)** $\displaystyle \sum_{n=0}^{4} 5\left(\tfrac{1}{2}\right)^{n}$

| Series | $a_1,\ r,\ n$ | Sum |
|---:|---:|---:|
| \text{(a)} | 1,\ 2,\ 5 | ? |
| \text{(b)} | 3,\ 2,\ 6 | ? |
| \text{(c)} | 2,\ 5,\ 4 | ? |
| \text{(d)} | 81,\ \tfrac{1}{3},\ 5 | ? |
| \text{(e)} | 5,\ \tfrac{1}{2},\ 5 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\displaystyle\sum_{n=1}^{3} 4 \cdot 3^{\,n-1} = 4 + 12 + 36$.

- $a_1 = 4$, $r = 3$, $n = 3$.

$$
\begin{aligned}
S_3 &= \frac{4\,(1 - 3^3)}{1 - 3} \\
&= \frac{4\,(1 - 27)}{-2} \\
&= \frac{-104}{-2} \\
&= \boxed{52}
\end{aligned}
$$

**Example 2:** $1 + 2 + 4 + \dots + 2^9$.

- $a_1 = 1$, $r = 2$, and $2^0$ to $2^9$ is $n = 10$ terms.

$$
\begin{aligned}
S_{10} &= \frac{1\,(1 - 2^{10})}{1 - 2} \\
&= \frac{1 - 1024}{-1} \\
&= \boxed{1023}
\end{aligned}
$$

**Why it works** (with $a_1 = 4$, $r = 3$):

$$
\begin{aligned}
S &= 4 + 12 + 36 \\
3S &= 12 + 36 + 108 \\
S - 3S &= 4 - 108 \\
-2S &= -104 \\
S &= 52
\end{aligned}
$$

</details>

### 7. Infinite geometric series: when the sum stops growing

If the ratio is small, $|r| < 1$, the terms shrink towards 0 and the sum settles at

$$
S_\infty = \frac{a_1}{1 - r}
$$

- It is card 6 with $n \to \infty$: $r^n \to 0$, so $1 - r^n \to 1$.
- If $|r| \ge 1$ the terms do not shrink, and there is **no** finite sum.

**Practice:** the middle column gives $a_1,\ r$. Fractions like 20/3 are fine.

- **(a)** $\displaystyle 1 + \tfrac{1}{2} + \tfrac{1}{4} + \dots$
- **(b)** $\displaystyle 6 + 2 + \tfrac{2}{3} + \dots$
- **(c)** $\displaystyle 10 - 5 + 2.5 - \dots$
- **(d)** $\displaystyle \sum_{n=1}^{\infty} 4(0.2)^{n-1}$
- **(e)** $\displaystyle 0.9 + 0.09 + 0.009 + \dots$

| Series | $a_1,\ r$ | Sum |
|---:|---:|---:|
| \text{(a)} | 1,\ \tfrac{1}{2} | ? |
| \text{(b)} | 6,\ \tfrac{1}{3} | ? |
| \text{(c)} | 10,\ -\tfrac{1}{2} | ? |
| \text{(d)} | 4,\ 0.2 | ? |
| \text{(e)} | 0.9,\ 0.1 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\displaystyle\sum_{n=1}^{\infty} \left(\tfrac{1}{2}\right)^n = \tfrac{1}{2} + \tfrac{1}{4} + \tfrac{1}{8} + \dots$

- $a_1 = \tfrac{1}{2}$, $r = \tfrac{1}{2}$.

$$
\begin{aligned}
S_\infty &= \frac{\tfrac{1}{2}}{1 - \tfrac{1}{2}} \\
&= \frac{\tfrac{1}{2}}{\tfrac{1}{2}} \\
&= \boxed{1}
\end{aligned}
$$

**Example 2:** the repeating decimal $0.333\ldots = 0.3 + 0.03 + 0.003 + \dots$

- $a_1 = 0.3$, $r = 0.1$.

$$
\begin{aligned}
S_\infty &= \frac{0.3}{1 - 0.1} \\
&= \frac{0.3}{0.9} \\
&= \boxed{\tfrac{1}{3}}
\end{aligned}
$$

**Check first:** $2 + 4 + 8 + \dots$ has $r = 2$.

- $|r| \ge 1$: the terms grow, so there is no sum.
- The formula would give $\frac{2}{1 - 2} = -2$, which is nonsense for positive terms.

</details>
