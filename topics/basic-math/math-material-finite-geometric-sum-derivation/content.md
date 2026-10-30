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

The finite geometric sum formula is

$$
S_n = \frac{a_1\,(1 - r^{\,n})}{1 - r}, \qquad r \ne 1
$$

- $a_1$ is the first term, $r$ the ratio, $n$ the number of terms.
- These five cards show **where it comes from**, one move each, with $2 + 6 + 18 + 54$ as the running example.
- Cards 4 and 5 show the other-sign form and how the infinite sum $\frac{a_1}{1 - r}$ falls out.

Type your answers in each table and tap **Check**.

## The derivation

### 1. Move 1: write the sum, then multiply every term by r

A **geometric** sequence multiplies by the same ratio $r$ each time. Its first $n$ terms add up to $S_n$:

$$
S_n = a_1 + a_1 r + a_1 r^2 + \dots + a_1 r^{\,n-1}
$$

- The $k$-th term is $a_1 r^{\,k-1}$: the exponent is one less than the position.
- Now multiply **every term** by $r$. Each term turns into the next one:

$$
r\,S_n = a_1 r + a_1 r^2 + a_1 r^3 + \dots + a_1 r^{\,n}
$$

- The two lines share every term except the first of $S_n$ and the last of $rS_n$. That is the trick for Move 2.

**Practice:** the middle column gives $a_1,\ r,\ k$. Find the $k$-th term $a_1 r^{\,k-1}$.

- **(a)** $a_1 = 2,\ r = 3,\ k = 4$
- **(b)** $a_1 = 5,\ r = 2,\ k = 6$
- **(c)** $a_1 = 1,\ r = 10,\ k = 5$
- **(d)** $a_1 = 81,\ r = \tfrac{1}{3},\ k = 4$
- **(e)** $a_1 = 3,\ r = -2,\ k = 5$

| Term | $a_1,\ r,\ k$ | $a_k$ |
|---:|---:|---:|
| \text{(a)} | 2,\ 3,\ 4 | ? |
| \text{(b)} | 5,\ 2,\ 6 | ? |
| \text{(c)} | 1,\ 10,\ 5 | ? |
| \text{(d)} | 81,\ \tfrac{1}{3},\ 4 | ? |
| \text{(e)} | 3,\ -2,\ 5 | ? |

<details>
<summary><b>Working</b></summary>

**Example:** $2 + 6 + 18 + 54$ has $a_1 = 2$, $r = 3$, $n = 4$.

$$
\begin{aligned}
S_4 &= 2 + 6 + 18 + 54 \\
3\,S_4 &= 6 + 18 + 54 + 162
\end{aligned}
$$

- Line 2 is line 1 shifted one place to the right.
- $6, 18, 54$ appear in both lines.
- Only the $2$ (first term of $S_4$) and the $162$ (last term of $3S_4$) stand alone.

**The 4th term by the exponent rule:**

$$
\begin{aligned}
a_4 &= a_1 r^{\,4-1} \\
&= 2 \cdot 3^3 \\
&= 2 \cdot 27 \\
&= \boxed{54}
\end{aligned}
$$

**Common mistake:** $a_4 = 2 \cdot 3^4 = 162$.

- That is the 5th term. The exponent is $k - 1$, not $k$.

</details>

### 2. Move 2: subtract, and the middle cancels

Subtract the second line from the first:

$$
\begin{aligned}
S_n &= a_1 + a_1 r + \dots + a_1 r^{\,n-1} \\
r\,S_n &= a_1 r + \dots + a_1 r^{\,n-1} + a_1 r^{\,n}
\end{aligned}
$$

- Every shared term cancels: $a_1 r$ against $a_1 r$, $a_1 r^2$ against $a_1 r^2$, and so on.
- Only two terms survive, the first of the top line and the last of the bottom line:

$$
S_n - r\,S_n = a_1 - a_1 r^{\,n}
$$

**Practice:** the middle column gives $a_1,\ r,\ n$. Find $a_1 - a_1 r^{\,n}$ (the right-hand side).

- **(a)** $a_1 = 2,\ r = 3,\ n = 4$
- **(b)** $a_1 = 1,\ r = 2,\ n = 5$
- **(c)** $a_1 = 5,\ r = 2,\ n = 3$
- **(d)** $a_1 = 4,\ r = \tfrac{1}{2},\ n = 3$
- **(e)** $a_1 = 3,\ r = -2,\ n = 4$

| Series | $a_1,\ r,\ n$ | $a_1 - a_1 r^{\,n}$ |
|---:|---:|---:|
| \text{(a)} | 2,\ 3,\ 4 | ? |
| \text{(b)} | 1,\ 2,\ 5 | ? |
| \text{(c)} | 5,\ 2,\ 3 | ? |
| \text{(d)} | 4,\ \tfrac{1}{2},\ 3 | ? |
| \text{(e)} | 3,\ -2,\ 4 | ? |

<details>
<summary><b>Working</b></summary>

**Example:** the same $2 + 6 + 18 + 54$.

$$
\begin{aligned}
S_4 &= 2 + 6 + 18 + 54 \\
3\,S_4 &= 6 + 18 + 54 + 162 \\
S_4 - 3\,S_4 &= 2 - 162 \\
-2\,S_4 &= -160
\end{aligned}
$$

**The same thing with the formula** $a_1 - a_1 r^{\,n}$:

$$
\begin{aligned}
a_1 - a_1 r^{\,n} &= 2 - 2 \cdot 3^4 \\
&= 2 - 2 \cdot 81 \\
&= 2 - 162 \\
&= \boxed{-160}
\end{aligned}
$$

**Check with the numbers:** $S_4 = 80$, so $S_4 - 3S_4 = 80 - 240 = -160$. Same answer.

**Common mistake:** subtracting $a_1 r^{\,n-1}$ instead of $a_1 r^{\,n}$.

- The last term of $rS_n$ has exponent $n$: it is one step past the last term of $S_n$.

</details>

### 3. Move 3: factor both sides, then divide

Both sides of Move 2 have a common factor. Take it out:

$$
\begin{aligned}
S_n - r\,S_n &= a_1 - a_1 r^{\,n} \\
(1 - r)\,S_n &= a_1\,(1 - r^{\,n})
\end{aligned}
$$

Divide by $(1 - r)$:

$$
S_n = \frac{a_1\,(1 - r^{\,n})}{1 - r}, \qquad r \ne 1
$$

**Why $r \ne 1$:**

- If $r = 1$, then $1 - r = 0$ and we cannot divide by it.
- But $r = 1$ is the easy case anyway: every term equals $a_1$, so $S_n = n\,a_1$.

**Practice:** the middle column gives $a_1,\ r,\ n$. Find $S_n$. Row (e) has $r = 1$.

- **(a)** $2 + 6 + 18 + 54$
- **(b)** $1 + 2 + 4 + 8 + 16$
- **(c)** $5 + 10 + 20$
- **(d)** $4 + 2 + 1$
- **(e)** $7 + 7 + 7 + 7 + 7 + 7$

| Series | $a_1,\ r,\ n$ | $S_n$ |
|---:|---:|---:|
| \text{(a)} | 2,\ 3,\ 4 | ? |
| \text{(b)} | 1,\ 2,\ 5 | ? |
| \text{(c)} | 5,\ 2,\ 3 | ? |
| \text{(d)} | 4,\ \tfrac{1}{2},\ 3 | ? |
| \text{(e)} | 7,\ 1,\ 6 | ? |

<details>
<summary><b>Working</b></summary>

**Example:** $2 + 6 + 18 + 54$ with $a_1 = 2$, $r = 3$, $n = 4$.

$$
\begin{aligned}
S_4 &= \frac{2\,(1 - 3^4)}{1 - 3} \\
&= \frac{2\,(1 - 81)}{-2} \\
&= \frac{2\,(-80)}{-2} \\
&= \frac{-160}{-2} \\
&= \boxed{80}
\end{aligned}
$$

**Check by adding:** $2 + 6 + 18 + 54 = 80$. Same answer.

**Finishing Move 2 directly** (no formula needed for one series):

$$
\begin{aligned}
-2\,S_4 &= -160 \\
S_4 &= \frac{-160}{-2} \\
&= 80
\end{aligned}
$$

**The $r = 1$ case:** $7 + 7 + 7 + 7 + 7 + 7$.

$$
\begin{aligned}
S_6 &= 6 \times 7 \\
&= \boxed{42}
\end{aligned}
$$

- The formula would give $\frac{7(1 - 1)}{1 - 1} = \frac{0}{0}$: no information. Count the terms instead.

**Common mistake:** $\frac{2(1 - 81)}{1 - 3} = \frac{-160}{2}$.

- The bottom is $1 - 3 = -2$, not $2$. Two negatives give the positive $80$.

</details>

## Using it

### 4. Move 4: the same formula with the signs flipped

Multiply the top and the bottom by $-1$. The value does not change:

$$
\begin{aligned}
S_n &= \frac{a_1\,(1 - r^{\,n})}{1 - r} \\
&= \frac{a_1\,(r^{\,n} - 1)}{r - 1}
\end{aligned}
$$

- Use the **second** form when $r > 1$: top and bottom are both positive, no double negative.
- Use the **first** form when $r < 1$ (fractions): $1 - r^{\,n}$ and $1 - r$ are both positive.
- Either form always gives the right answer. Pick the one with fewer minus signs.

**Practice:** the middle column gives $a_1,\ r,\ n$. Find $S_n$ with the form you prefer.

- **(a)** $3 + 6 + 12 + 24 + 48$
- **(b)** $1 + 3 + 9 + 27$
- **(c)** $2 + 10 + 50$
- **(d)** $10 + 20 + 40 + \dots \text{ (6 terms)}$
- **(e)** $1 - 2 + 4 - 8$

| Series | $a_1,\ r,\ n$ | $S_n$ |
|---:|---:|---:|
| \text{(a)} | 3,\ 2,\ 5 | ? |
| \text{(b)} | 1,\ 3,\ 4 | ? |
| \text{(c)} | 2,\ 5,\ 3 | ? |
| \text{(d)} | 10,\ 2,\ 6 | ? |
| \text{(e)} | 1,\ -2,\ 4 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $2 + 6 + 18 + 54$ again, second form, $r = 3 > 1$.

$$
\begin{aligned}
S_4 &= \frac{2\,(3^4 - 1)}{3 - 1} \\
&= \frac{2\,(81 - 1)}{2} \\
&= \frac{160}{2} \\
&= \boxed{80}
\end{aligned}
$$

- Same $80$ as Move 3, with no negative numbers on the way.

**Example 2:** $3 + 6 + 12 + 24 + 48$, $a_1 = 3$, $r = 2$, $n = 5$.

$$
\begin{aligned}
S_5 &= \frac{3\,(2^5 - 1)}{2 - 1} \\
&= \frac{3\,(32 - 1)}{1} \\
&= 3 \times 31 \\
&= \boxed{93}
\end{aligned}
$$

**Example 3, a negative ratio:** $1 - 2 + 4 - 8$, $a_1 = 1$, $r = -2$, $n = 4$.

$$
\begin{aligned}
S_4 &= \frac{1\,\big((-2)^4 - 1\big)}{-2 - 1} \\
&= \frac{16 - 1}{-3} \\
&= \frac{15}{-3} \\
&= \boxed{-5}
\end{aligned}
$$

- Check: $1 - 2 + 4 - 8 = -5$.

**Common mistake:** $(-2)^4 = -16$.

- An even power of a negative number is positive: $(-2)^4 = 16$.

</details>

### 5. Move 5: check small cases, then let n grow

A formula should agree with what you can add by hand.

$$
\begin{aligned}
S_1 &= \frac{a_1\,(1 - r)}{1 - r} \\
&= a_1
\end{aligned}
$$

and

$$
\begin{aligned}
S_2 &= \frac{a_1\,(1 - r^2)}{1 - r} \\
&= \frac{a_1\,(1 - r)(1 + r)}{1 - r} \\
&= a_1 + a_1 r
\end{aligned}
$$

- Both match the first one and two terms. Good sign.

**Let $n$ grow.** If $|r| < 1$, the power $r^{\,n}$ shrinks towards $0$:

$$
\begin{aligned}
S_n &= \frac{a_1\,(1 - r^{\,n})}{1 - r} \\
&\to \frac{a_1\,(1 - 0)}{1 - r} \\
&= \frac{a_1}{1 - r}
\end{aligned}
$$

- That is the infinite geometric sum $S_\infty$. It only exists when $|r| < 1$.

**Practice:** $a_1 = 8$, $r = \tfrac{1}{2}$, so the series is $8 + 4 + 2 + 1 + \tfrac{1}{2} + \dots$. Find each sum. Decimals are fine (15.984 is accepted for (d)).

- **(a)** $S_1$
- **(b)** $S_2$
- **(c)** $S_5$
- **(d)** $S_{10}$
- **(e)** $S_\infty$

| Sum | $a_1 = 8,\ r = \tfrac{1}{2}$ | Value |
|---:|---:|---:|
| \text{(a)} | n = 1 | ? |
| \text{(b)} | n = 2 | ? |
| \text{(c)} | n = 5 | ? |
| \text{(d)} | n = 10 | ? |
| \text{(e)} | n \to \infty | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $S_5$ for $a_1 = 8$, $r = \tfrac{1}{2}$.

$$
\begin{aligned}
S_5 &= \frac{8\,\big(1 - (\tfrac{1}{2})^5\big)}{1 - \tfrac{1}{2}} \\
&= \frac{8\,(1 - \tfrac{1}{32})}{\tfrac{1}{2}} \\
&= 16 \cdot \tfrac{31}{32} \\
&= \boxed{15.5}
\end{aligned}
$$

- Check by adding: $8 + 4 + 2 + 1 + 0.5 = 15.5$.

**Example 2:** $S_\infty$ for the same series.

$$
\begin{aligned}
S_\infty &= \frac{8}{1 - \tfrac{1}{2}} \\
&= \frac{8}{\tfrac{1}{2}} \\
&= \boxed{16}
\end{aligned}
$$

- $S_5 = 15.5$ and $S_{10} \approx 15.98$: the sums creep up to $16$ and never pass it.

**Why $|r| < 1$ matters:** $2 + 4 + 8 + \dots$ has $r = 2$.

- $2^{\,n}$ grows without limit, so $1 - 2^{\,n}$ does not settle. No infinite sum.
- The finite formula still works for any $n$: $S_5 = \frac{2(1 - 32)}{1 - 2} = 62$.

</details>
