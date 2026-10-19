---
title: "Math Material — Composition of Functions"
topic: basic-math
example: math-material-composition-of-functions
course: AP Precalculus
status: material
created: 2026-10-19
author: Wei-Che Hung
---

# Math Material — Composition of Functions

**Composition** means feeding the output of one function into another:

$$
(f\circ g)(x)=f\big(g(x)\big)
$$

- Work from the **inside** out: first $g(x)$, then use that as the input of $f$.
- Order matters: $f\big(g(x)\big)$ and $g\big(f(x)\big)$ are usually different.

Type your answers in the tables and tap **Check**.

## 1. Evaluate from formulas

Given

$$
f(x)=2x+3
$$

and

$$
g(x)=x^2-1
$$

Find $f\big(g(x)\big)$ for each $x$ below.

- Work from the inside out: first find $g(x)$, then put that result into $f$.

| $x$ | $g(x)$ | $f(g(x))$ |
|---:|---:|---:|
| -2 | 3 | ? |
| -1 | 0 | ? |
| 0 | -1 | ? |
| 1 | 0 | ? |
| 2 | 3 | ? |

<details>
<summary><b>Working</b></summary>

**Method:** compute $g(x)$ first, then use the result as the input of $f$.

**Example with $x = -2$:**

$$
\begin{aligned}
g(-2) &= (-2)^2-1 \\
&= 4-1 \\
&= 3
\end{aligned}
$$

Now put $3$ into $f$:

$$
\begin{aligned}
f\big(g(-2)\big) &= f(3) \\
&= 2(3)+3 \\
&= \boxed{9}
\end{aligned}
$$

**With $x = 0$:**

$$
\begin{aligned}
g(0) &= 0^2-1 \\
&= -1
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(0)\big) &= f(-1) \\
&= 2(-1)+3 \\
&= \boxed{1}
\end{aligned}
$$

**With $x = 2$:**

$$
\begin{aligned}
g(2) &= 2^2-1 \\
&= 3
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(2)\big) &= f(3) \\
&= 2(3)+3 \\
&= \boxed{9}
\end{aligned}
$$

Notice: $f\big(g(-2)\big) = f\big(g(2)\big) = 9$ because $(-2)^2 = 2^2$.

</details>

## 2. Evaluate from a table

$$
\begin{array}{c|ccccc}
x & 1 & 2 & 3 & 4 & 5\\
\hline
f(x) & 5 & 3 & 1 & 4 & 2\\
g(x) & 2 & 4 & 5 & 3 & 1
\end{array}
$$

Use the table to find $f\big(g(x)\big)$ for each $x$.

- Read $g(x)$ first, then use that number to look up $f$.

| $x$ | $g(x)$ | $f(g(x))$ |
|---:|---:|---:|
| 1 | 2 | ? |
| 2 | 4 | ? |
| 3 | 5 | ? |
| 4 | 3 | ? |
| 5 | 1 | ? |

<details>
<summary><b>Working</b></summary>

**Method:** two look-ups.

- First read $g(x)$ in the $g$ row.
- Then use that output to read $f$ in the $f$ row.

**Example with $x = 1$:**

$$
\begin{aligned}
g(1) &= 2
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(1)\big) &= f(2) \\
&= \boxed{3}
\end{aligned}
$$

**With $x = 3$:**

$$
\begin{aligned}
g(3) &= 5
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(3)\big) &= f(5) \\
&= \boxed{2}
\end{aligned}
$$

**With $x = 5$:**

$$
\begin{aligned}
g(5) &= 1
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(5)\big) &= f(1) \\
&= \boxed{5}
\end{aligned}
$$

</details>

## 3. Build the composed formula

Let

$$
f(x)=x^2+1
$$

and

$$
g(x)=3x-2
$$

Write $f\big(g(x)\big)$ as a single formula and simplify.

<details>
<summary><b>Working</b></summary>

**Step 1:** write $f$ with its input left blank:

$$
f(\Box)=\Box^2+1
$$

**Step 2:** replace $\Box$ with $g(x)=3x-2$:

$$
\begin{aligned}
f\big(g(x)\big) &= (3x-2)^2+1
\end{aligned}
$$

**Step 3:** expand $(3x-2)^2$:

$$
\begin{aligned}
(3x-2)^2 &= (3x)^2 - 2(3x)(2) + 2^2 \\
&= 9x^2-12x+4
\end{aligned}
$$

**Step 4:** add 1:

$$
\begin{aligned}
f\big(g(x)\big) &= 9x^2-12x+4+1 \\
&= \boxed{9x^2-12x+5}
\end{aligned}
$$

**Check at $x=1$:**

$$
\begin{aligned}
g(1) &= 3(1)-2 = 1 \\
f(1) &= 1^2+1 = \boxed{2}
\end{aligned}
$$

and $9(1)-12(1)+5 = 9-12+5 = 2$. It matches.

</details>

## 4. Real world: fuel cost of a trip

A car uses

$$
L(d)=0.08d
$$

litres of fuel to drive $d$ km.

Fuel costs

$$
C(L)=1.50L
$$

euros for $L$ litres.

Use composition $C\big(L(d)\big)$ to find the cost of each trip.

- Kilometres go into $L$ first, then litres go into $C$.

| $d$ km | $L(d)$ litres | Cost (euros) |
|---:|---:|---:|
| 50 | 4.0 | ? |
| 75 | 6.0 | ? |
| 150 | 12.0 | ? |
| 200 | 16.0 | ? |
| 300 | 24.0 | ? |

<details>
<summary><b>Working</b></summary>

**Method:** kilometres $\to$ litres $\to$ euros.

Compose: $C\big(L(d)\big)$.

**Example with $d = 150$ km:**

$$
\begin{aligned}
L(150) &= 0.08(150) \\
&= 12 \text{ litres}
\end{aligned}
$$

Then:

$$
\begin{aligned}
C\big(L(150)\big) &= C(12) \\
&= 1.50(12) \\
&= \boxed{18 \text{ euros}}
\end{aligned}
$$

**In one formula:**

$$
\begin{aligned}
C\big(L(d)\big) &= 1.50(0.08d) \\
&= 0.12d
\end{aligned}
$$

So the cost is simply $0.12$ euros per km.

- $d=50$: $0.12(50) = 6$ euros
- $d=300$: $0.12(300) = 36$ euros

</details>
