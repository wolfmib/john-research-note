---
title: "Math Material — Logarithm Rules"
topic: basic-math
example: math-material-logarithm-rules
course: AP Precalculus
status: material
created: 2026-10-23
author: Wei-Che Hung
---

# Math Material — Logarithm Rules

**A logarithm is an exponent:**

$$
\log_b c = a \iff b^{a} = c
$$

- Cards 1–2: what a log means.
- Cards 3–6: the three rules, then all of them together.
- Cards 7–10: using the rules (calculator, cancelling, the main trap, solving).
- Cards 11–12: advanced.

Type your answers in each table and tap **Check**.

## Basics

### 1. Definition: a log is an exponent

$$
\log_b c = a \iff b^{a} = c
$$

- Ask: **$b$ to what power gives $c$?**
- No base written means base $10$.
- Two values for every base: $\log_b 1 = 0$ and $\log_b b = 1$.

**Practice:** find each value.

- **(a)** $\displaystyle \log_2 8$
- **(b)** $\displaystyle \log_3 81$
- **(c)** $\displaystyle \log 1000$
- **(d)** $\displaystyle \log_5 1$
- **(e)** $\displaystyle \log_7 7$

| Log | Base | Value |
|---:|---:|---:|
| \text{(a)} | 2 | ? |
| \text{(b)} | 3 | ? |
| \text{(c)} | 10 | ? |
| \text{(d)} | 5 | ? |
| \text{(e)} | 7 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\log_5 25$.

- $5$ to what power gives $25$?

$$
\begin{aligned}
5^2 &= 25 \\
\log_5 25 &= \boxed{2}
\end{aligned}
$$

**Example 2:** $\log 10000$ (base $10$).

$$
\begin{aligned}
10^4 &= 10000 \\
\log 10000 &= \boxed{4}
\end{aligned}
$$

**Example 3:** the two special values.

$$
\begin{aligned}
6^0 &= 1 \\
\log_6 1 &= \boxed{0}
\end{aligned}
$$

$$
\begin{aligned}
6^1 &= 6 \\
\log_6 6 &= \boxed{1}
\end{aligned}
$$

</details>

### 2. Fraction and negative answers

- Input **below 1** (like $\tfrac{1}{8}$): the answer is **negative**.

$$
b^{-n} = \frac{1}{b^n}
$$

- Input is a **root** of the base (like $2 = \sqrt{4}$): the answer is a **fraction**.

$$
\sqrt[n]{b} = b^{1/n}
$$

**Practice:** find each value. Type fractions like 1/2.

- **(a)** $\displaystyle \log_2 \tfrac{1}{8}$
- **(b)** $\displaystyle \log_3 \tfrac{1}{9}$
- **(c)** $\displaystyle \log 0.01$
- **(d)** $\displaystyle \log_4 2$
- **(e)** $\displaystyle \log_{27} 3$

| Log | Base | Value |
|---:|---:|---:|
| \text{(a)} | 2 | ? |
| \text{(b)} | 3 | ? |
| \text{(c)} | 10 | ? |
| \text{(d)} | 4 | ? |
| \text{(e)} | 27 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\log_5 \tfrac{1}{25}$.

$$
\begin{aligned}
\frac{1}{25} &= \frac{1}{5^2} \\
&= 5^{-2}
\end{aligned}
$$

$$
\begin{aligned}
\log_5 \tfrac{1}{25} &= \boxed{-2}
\end{aligned}
$$

**Example 2:** $\log_9 3$.

$$
\begin{aligned}
3 &= \sqrt{9} \\
&= 9^{1/2}
\end{aligned}
$$

$$
\begin{aligned}
\log_9 3 &= \boxed{\tfrac{1}{2}}
\end{aligned}
$$

**Common mistake:** $\log_9 3 = 3$ is wrong.

- $9^3 = 729$, not $3$. The base is bigger than the input, so the answer is below $1$.

</details>

## Rules

### 3. Product rule: add logs, multiply inside

$$
\log_b m + \log_b n = \log_b (mn)
$$

- Same base on both logs.
- Adding the logs **multiplies** the inputs.

$$
\log 2 + \log 3 = \log 6
$$

**Practice:** write each as one log. Type the number inside the log.

- **(a)** $\displaystyle \log 2 + \log 5$
- **(b)** $\displaystyle \log_3 4 + \log_3 5$
- **(c)** $\displaystyle \log_2 3 + \log_2 6$
- **(d)** $\displaystyle \log 4 + \log 25$
- **(e)** $\displaystyle \log_6 4 + \log_6 9$

| Sum | Base | Inside |
|---:|---:|---:|
| \text{(a)} | 10 | ? |
| \text{(b)} | 3 | ? |
| \text{(c)} | 2 | ? |
| \text{(d)} | 10 | ? |
| \text{(e)} | 6 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\log 2 + \log 3$.

$$
\begin{aligned}
\log 2 + \log 3 &= \log (2 \times 3) \\
&= \boxed{\log 6}
\end{aligned}
$$

**Example 2:** $\log_2 4 + \log_2 8$, checked both ways.

$$
\begin{aligned}
\log_2 4 + \log_2 8 &= \log_2 32 \\
&= 5
\end{aligned}
$$

- Check: $\log_2 4 = 2$ and $\log_2 8 = 3$, and $2 + 3 = 5$.

**Why it works:** logs are exponents, and exponents add when powers multiply.

$$
\begin{aligned}
2^2 \times 2^3 &= 2^{2+3} \\
4 \times 8 &= 32
\end{aligned}
$$

</details>

### 4. Quotient rule: subtract logs, divide inside

$$
\log_b m - \log_b n = \log_b \frac{m}{n}
$$

- Subtracting the logs **divides** the inputs.
- The first input goes on top.

$$
\log 12 - \log 3 = \log 4
$$

**Practice:** write each as one log. Type the number inside (a fraction like 1/25 is fine).

- **(a)** $\displaystyle \log 20 - \log 2$
- **(b)** $\displaystyle \log_2 40 - \log_2 5$
- **(c)** $\displaystyle \log_3 54 - \log_3 2$
- **(d)** $\displaystyle \log 500 - \log 5$
- **(e)** $\displaystyle \log_5 3 - \log_5 75$

| Diff | Base | Inside |
|---:|---:|---:|
| \text{(a)} | 10 | ? |
| \text{(b)} | 2 | ? |
| \text{(c)} | 3 | ? |
| \text{(d)} | 10 | ? |
| \text{(e)} | 5 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\log 12 - \log 3$.

$$
\begin{aligned}
\log 12 - \log 3 &= \log \frac{12}{3} \\
&= \boxed{\log 4}
\end{aligned}
$$

**Example 2:** $\log_3 54 - \log_3 2$, then find its value.

$$
\begin{aligned}
\log_3 54 - \log_3 2 &= \log_3 27 \\
&= \boxed{3}
\end{aligned}
$$

**Common mistake:** $\log 12 - \log 3 = \log 9$ is wrong.

- Subtracting logs divides: $12 \div 3 = 4$, not $12 - 3$.

</details>

### 5. Power rule: the exponent comes out in front

$$
\log_b m^{k} = k\log_b m
$$

- Read it both ways:
- **Out:** $\log 2^5 = 5\log 2$
- **In:** $3\log 2 = \log 2^3 = \log 8$

**Practice:** move the number in front back inside. Type the number inside the log.

- **(a)** $\displaystyle 3\log 2$
- **(b)** $\displaystyle 2\log 5$
- **(c)** $\displaystyle 4\log_3 2$
- **(d)** $\displaystyle \tfrac{1}{2}\log 49$
- **(e)** $\displaystyle -\log 2$

| Expr | Base | Inside |
|---:|---:|---:|
| \text{(a)} | 10 | ? |
| \text{(b)} | 10 | ? |
| \text{(c)} | 3 | ? |
| \text{(d)} | 10 | ? |
| \text{(e)} | 10 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1 (out):** $\log_2 8^5$.

$$
\begin{aligned}
\log_2 8^5 &= 5\log_2 8 \\
&= 5 \times 3 \\
&= \boxed{15}
\end{aligned}
$$

**Example 2 (in):** $3\log 2$.

$$
\begin{aligned}
3\log 2 &= \log 2^3 \\
&= \boxed{\log 8}
\end{aligned}
$$

**Example 3:** a half in front means a square root.

$$
\begin{aligned}
\tfrac{1}{2}\log 9 &= \log 9^{1/2} \\
&= \log \sqrt{9} \\
&= \boxed{\log 3}
\end{aligned}
$$

**A minus in front** means one over:

$$
\begin{aligned}
-\log 5 &= \log 5^{-1} \\
&= \log \tfrac{1}{5}
\end{aligned}
$$

</details>

### 6. Combine into one log

Use the rules in this order:

- **Power** first: move every number in front inside.
- **Product:** each $+$ multiplies.
- **Quotient:** each $-$ divides.

**Practice:** write each as one log. Type the number inside the log.

- **(a)** $\displaystyle 2\log 3 + \log 2$
- **(b)** $\displaystyle \log 8 + \log 5 - \log 4$
- **(c)** $\displaystyle 3\log 2 - \log 4$
- **(d)** $\displaystyle 2\log_2 6 - \log_2 9$
- **(e)** $\displaystyle \log 50 + 2\log 2 - \log 2$

| Expr | Base | Inside |
|---:|---:|---:|
| \text{(a)} | 10 | ? |
| \text{(b)} | 10 | ? |
| \text{(c)} | 10 | ? |
| \text{(d)} | 2 | ? |
| \text{(e)} | 10 | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $2\log 3 + \log 4 - \log 6$.

- Power first: $2\log 3 = \log 9$.

$$
\begin{aligned}
2\log 3 + \log 4 - \log 6 &= \log 9 + \log 4 - \log 6 \\
&= \log \frac{9 \times 4}{6} \\
&= \log \frac{36}{6} \\
&= \boxed{\log 6}
\end{aligned}
$$

**Example 2:** $2\log_2 6 - \log_2 9$, then its value.

$$
\begin{aligned}
2\log_2 6 - \log_2 9 &= \log_2 36 - \log_2 9 \\
&= \log_2 \frac{36}{9} \\
&= \log_2 4 \\
&= \boxed{2}
\end{aligned}
$$

**Common mistake:** $2\log 3 + \log 4 = \log 24$ is wrong.

- The $2$ must go inside first: $\log 9 + \log 4 = \log 36$.

</details>

## Using the rules

### 7. Change of base: any log on a calculator

$$
\log_b c = \frac{\log c}{\log b}
$$

- The calculator has $\log$ (base $10$), so divide two base-10 logs.
- The input goes on **top**, the base on the **bottom**.

**Practice:** use a calculator. Give each value to 2 decimal places.

- **(a)** $\displaystyle \log_2 7$
- **(b)** $\displaystyle \log_3 20$
- **(c)** $\displaystyle \log_5 100$
- **(d)** $\displaystyle \log_4 10$
- **(e)** $\displaystyle \log_6 50$

| Log | Calculator | Value |
|---:|---:|---:|
| \text{(a)} | \frac{\log 7}{\log 2} | ? |
| \text{(b)} | \frac{\log 20}{\log 3} | ? |
| \text{(c)} | \frac{\log 100}{\log 5} | ? |
| \text{(d)} | \frac{\log 10}{\log 4} | ? |
| \text{(e)} | \frac{\log 50}{\log 6} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\log_2 7$.

$$
\begin{aligned}
\log_2 7 &= \frac{\log 7}{\log 2} \\
&= \frac{0.8451}{0.3010} \\
&\approx \boxed{2.81}
\end{aligned}
$$

**Check:** it should sit between two whole powers.

- $2^2 = 4$ and $2^3 = 8$, so $\log_2 7$ is between $2$ and $3$. It fits.

**Example 2:** an exact answer with change of base, $\log_8 32$.

$$
\begin{aligned}
\log_8 32 &= \frac{\log 2^5}{\log 2^3} \\
&= \frac{5\log 2}{3\log 2} \\
&= \boxed{\tfrac{5}{3}}
\end{aligned}
$$

**Common mistake:** $\dfrac{\log 2}{\log 7}$ is upside down.

- That gives $0.36$, which is $\log_7 2$.

</details>

### 8. Inverse pair: a log and its power cancel

$$
b^{\log_b x} = x
$$

$$
\log_b b^{x} = x
$$

- $b^x$ and $\log_b x$ undo each other (inverse functions, 2.10).
- The bases must match.

**Practice:** find each value. For (e), use the power rule first.

- **(a)** $\displaystyle 2^{\log_2 5}$
- **(b)** $\displaystyle 10^{\log 7}$
- **(c)** $\displaystyle \log_3 3^{4}$
- **(d)** $\displaystyle \log 10^{-2}$
- **(e)** $\displaystyle 5^{2\log_5 3}$

| Expr | Rule | Value |
|---:|---:|---:|
| \text{(a)} | \text{cancel} | ? |
| \text{(b)} | \text{cancel} | ? |
| \text{(c)} | \text{cancel} | ? |
| \text{(d)} | \text{cancel} | ? |
| \text{(e)} | \text{power} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $3^{\log_3 11}$.

- Base $3$ and $\log_3$ match, so they cancel.

$$
\begin{aligned}
3^{\log_3 11} &= \boxed{11}
\end{aligned}
$$

**Example 2:** $\log_2 2^7$.

$$
\begin{aligned}
\log_2 2^7 &= \boxed{7}
\end{aligned}
$$

**Example 3:** a number in front, $10^{2\log 4}$.

- Move the $2$ inside first (power rule).

$$
\begin{aligned}
10^{2\log 4} &= 10^{\log 16} \\
&= \boxed{16}
\end{aligned}
$$

</details>

### 9. The trap: there is no rule for log(a + b)

These two look alike but are **not** equal:

$$
\log (a + b) \ne \log a + \log b
$$

- $\log a + \log b$ is $\log (ab)$, the product rule.
- $\log (a + b)$ cannot be split. Add inside first, then take the log.

$$
\frac{\log a}{\log b} \ne \log \frac{a}{b}
$$

- A fraction of two logs is change of base, not the quotient rule.

**Practice:** find each value. (d) needs a calculator, 2 decimal places.

- **(a)** $\displaystyle \log_2 4 + \log_2 4$
- **(b)** $\displaystyle \log_2 (4 + 4)$
- **(c)** $\displaystyle \log 20 + \log 5$
- **(d)** $\displaystyle \log (20 + 5)$
- **(e)** $\displaystyle \frac{\log 100}{\log 10}$

| Expr | Rule | Value |
|---:|---:|---:|
| \text{(a)} | \text{product} | ? |
| \text{(b)} | \text{add first} | ? |
| \text{(c)} | \text{product} | ? |
| \text{(d)} | \text{add first} | ? |
| \text{(e)} | \text{divide} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** compare (a) and (b).

$$
\begin{aligned}
\log_2 4 + \log_2 4 &= 2 + 2 \\
&= \boxed{4}
\end{aligned}
$$

$$
\begin{aligned}
\log_2 (4 + 4) &= \log_2 8 \\
&= \boxed{3}
\end{aligned}
$$

- Different answers, so the two are not the same thing.

**Example 2:** $\log 2 + \log 3$.

$$
\begin{aligned}
\log 2 + \log 3 &= \log 6
\end{aligned}
$$

- Not $\log 5$: adding logs multiplies the inputs, it never adds them.

**Example 3:** compare a fraction of logs with the log of a fraction.

$$
\begin{aligned}
\frac{\log 100}{\log 10} &= \frac{2}{1} \\
&= 2
\end{aligned}
$$

$$
\begin{aligned}
\log \frac{100}{10} &= \log 10 \\
&= 1
\end{aligned}
$$

</details>

### 10. Solve an exponential with logs

To get $x$ down from the exponent, take $\log$ of both sides:

$$
b^{x} = c
$$

$$
x\log b = \log c
$$

$$
x = \frac{\log c}{\log b}
$$

- If a number multiplies the power, divide it away first.

**Practice:** solve for $x$. Give $x$ to 2 decimal places.

- **(a)** $\displaystyle 2^x = 10$
- **(b)** $\displaystyle 3^x = 50$
- **(c)** $\displaystyle 5^x = 0.2$
- **(d)** $\displaystyle 1.05^x = 2$
- **(e)** $\displaystyle 4 \cdot 3^x = 100$

| Eq | $x =$ | $x$ |
|---:|---:|---:|
| \text{(a)} | \frac{\log 10}{\log 2} | ? |
| \text{(b)} | \frac{\log 50}{\log 3} | ? |
| \text{(c)} | \frac{\log 0.2}{\log 5} | ? |
| \text{(d)} | \frac{\log 2}{\log 1.05} | ? |
| \text{(e)} | \frac{\log 25}{\log 3} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $7^x = 30$.

$$
\begin{aligned}
7^x &= 30 \\
\log 7^x &= \log 30 \\
x\log 7 &= \log 30 \\
x &= \frac{\log 30}{\log 7} \\
x &\approx \boxed{1.75}
\end{aligned}
$$

**Check:** $7^1 = 7$ and $7^2 = 49$, so $x$ is between $1$ and $2$. It fits.

**Example 2:** money growing $5\%$ a year. When does it double?

$$
\begin{aligned}
1.05^x &= 2 \\
x &= \frac{\log 2}{\log 1.05} \\
x &\approx \boxed{14.2 \text{ years}}
\end{aligned}
$$

**Example 3:** divide first, $4 \cdot 3^x = 100$.

$$
\begin{aligned}
4 \cdot 3^x &= 100 \\
3^x &= 25 \\
x &= \frac{\log 25}{\log 3} \\
x &\approx \boxed{2.93}
\end{aligned}
$$

**Common mistake:** $\log 12^x$ from $4 \cdot 3^x$ is wrong.

- $4 \cdot 3^x$ is not $12^x$. Divide by $4$ first.

</details>

## Advanced

### 11. Expand one log into pieces

Run the rules backwards:

$$
\log \frac{x^2 y}{z} = 2\log x + \log y - \log z
$$

- Each factor on top becomes $+\log$.
- Each factor on the bottom becomes $-\log$.
- Each power comes out in front.

**Practice:** you are given

$$
\begin{aligned}
\log_b x &= 2 \\
\log_b y &= 5 \\
\log_b z &= 3
\end{aligned}
$$

Expand, then find each value:

- **(a)** $\displaystyle \log_b (xy)$
- **(b)** $\displaystyle \log_b \frac{x}{z}$
- **(c)** $\displaystyle \log_b x^3$
- **(d)** $\displaystyle \log_b \frac{x y^2}{z}$
- **(e)** $\displaystyle \log_b (\sqrt{x}\, z)$

| Log | Rule | Value |
|---:|---:|---:|
| \text{(a)} | \text{product} | ? |
| \text{(b)} | \text{quotient} | ? |
| \text{(c)} | \text{power} | ? |
| \text{(d)} | \text{all three} | ? |
| \text{(e)} | \text{root} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** expand $\log \dfrac{x^2 y}{z}$.

$$
\begin{aligned}
\log \frac{x^2 y}{z} &= \log x^2 + \log y - \log z \\
&= \boxed{2\log x + \log y - \log z}
\end{aligned}
$$

**Example 2:** the same with the given values.

$$
\begin{aligned}
\log_b \frac{x^2 y}{z} &= 2(2) + 5 - 3 \\
&= \boxed{6}
\end{aligned}
$$

**A square root is a power of one half:**

$$
\begin{aligned}
\log_b \sqrt{x} &= \log_b x^{1/2} \\
&= \tfrac{1}{2}\log_b x
\end{aligned}
$$

**Common mistake:** $\log_b \dfrac{x}{z} = \dfrac{\log_b x}{\log_b z}$ is wrong.

- It is a subtraction: $2 - 3 = -1$, not $\tfrac{2}{3}$.

</details>

### 12. Solve a log equation

Three steps:

- **Combine** into one log on each side (product / quotient rule).
- **Undo** the log with the definition:

$$
\log_b M = k \iff M = b^{k}
$$

- **Check** every answer: the input of each log must be positive.

**Practice:** solve for $x$.

- **(a)** $\displaystyle \log_2 x = 5$
- **(b)** $\displaystyle \log_3 (x - 1) = 2$
- **(c)** $\displaystyle \log x + \log 4 = 2$
- **(d)** $\displaystyle \log_2 x - \log_2 3 = 2$
- **(e)** $\displaystyle \log_6 x + \log_6 (x - 1) = 1$

| Eq | Step | $x$ |
|---:|---:|---:|
| \text{(a)} | \text{undo} | ? |
| \text{(b)} | \text{undo} | ? |
| \text{(c)} | \text{combine} | ? |
| \text{(d)} | \text{combine} | ? |
| \text{(e)} | \text{check} | ? |

<details>
<summary><b>Working</b></summary>

**Example 1:** $\log_3 x = 4$.

$$
\begin{aligned}
\log_3 x &= 4 \\
x &= 3^4 \\
x &= \boxed{81}
\end{aligned}
$$

**Example 2:** $\log_2 x + \log_2 (x - 2) = 3$.

- Combine with the product rule, then undo the log.

$$
\begin{aligned}
\log_2 \big(x(x - 2)\big) &= 3 \\
x(x - 2) &= 2^3 \\
x^2 - 2x &= 8 \\
x^2 - 2x - 8 &= 0 \\
(x - 4)(x + 2) &= 0
\end{aligned}
$$

Two candidates: $x = 4$ or $x = -2$.

- $x = -2$ gives $\log_2 (-2)$, which has no value. Reject it.

$$
\begin{aligned}
x &= \boxed{4}
\end{aligned}
$$

**Check $x = 4$:**

$$
\begin{aligned}
\log_2 4 + \log_2 2 &= 2 + 1 \\
&= 3
\end{aligned}
$$

</details>
