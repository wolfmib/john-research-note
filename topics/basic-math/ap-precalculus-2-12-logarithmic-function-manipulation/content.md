---
title: "AP Precalculus 2.12 — Logarithmic Function Manipulation"
topic: basic-math
example: ap-precalculus-2-12-logarithmic-function-manipulation
course: AP Precalculus
unit: "2.12"
status: quiz
created: 2026-11-16
author: Wei-Che Hung
---

# AP Precalculus 2.12 — Logarithmic Function Manipulation

**Quick recap:** for $x>0$, $y>0$:

$$
\log_b(xy)=\log_b x+\log_b y
$$

$$
\log_b\frac{x}{y}=\log_b x-\log_b y
$$

$$
\log_b\!\left(x^{n}\right)=n\log_b x
$$

$$
\log_b x=\frac{\ln x}{\ln b}
$$

- Count the factors inside the log: each factor becomes its own log term.
- Power pairs give fractional logs: $2^{3}=8$ means $\log_8 2=\tfrac13$.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Expand a product with a power

For $x>0$, which expression is equal to

$$
\log_2\!\left(32x^{4}\right)?
$$

- **A.** $20\log_2 x$
- **B.** $32+4\log_2 x$
- **C.** $5+4\log_2 x$
- **D.** $9\log_2 x$

## 2. Expand three factors

For $x>0$ and $y>0$, expand:

$$
\log_3\!\left(27xy^{2}\right)
$$

- **A.** $3+\log_3 x+2\log_3 y$
- **B.** $3+2\log_3(xy)$
- **C.** $27+\log_3 x+2\log_3 y$
- **D.** $3+\log_3 x+\log_3(2y)$

## 3. Condense to a number

Find the value of

$$
3\log_2 4-\log_2 8
$$

- **A.** $2$
- **B.** $3$
- **C.** $6$
- **D.** $-1$

## 4. A fractional log

Find the value of

$$
\log_{64} 4
$$

- **A.** $3$
- **B.** $16$
- **C.** $\dfrac{1}{16}$
- **D.** $\dfrac13$

## 5. Change of base

Use a calculator. To two decimal places, what is

$$
\log_5 40?
$$

- **A.** $8$
- **B.** $2.29$
- **C.** $0.44$
- **D.** $1.60$

---

<details>
<summary><b>Answers</b></summary>

**1. C — Split the product, then bring the power down**

- Product property: a log of a product is a sum of logs.
- Power property: the exponent $4$ moves to the front.

$$
\begin{aligned}
\log_2\!\left(32x^{4}\right) &= \log_2 32+\log_2 x^{4} \\
&= 5+4\log_2 x
\end{aligned}
$$

because $2^{5}=32$, so $\log_2 32=5$.

$$
\boxed{5+4\log_2 x}
$$

- Not $32+4\log_2 x$: $32$ is inside the log; it becomes $\log_2 32=5$.
- Not $20\log_2 x$: the $5$ and the $4$ are **added** as separate terms, never multiplied.

**2. A — Three factors give three log terms**

- The argument has **three** factors: $27$, $x$ and $y^{2}$. So there are three log terms.
- Only the $y$ is squared, so only $\log_3 y$ gets the $2$.

$$
\begin{aligned}
\log_3\!\left(27xy^{2}\right) &= \log_3 27+\log_3 x+\log_3 y^{2} \\
&= 3+\log_3 x+2\log_3 y
\end{aligned}
$$

because $3^{3}=27$.

$$
\boxed{3+\log_3 x+2\log_3 y}
$$

- Not $3+2\log_3(xy)$: that would square the $x$ as well.
- Not $\log_3(2y)$: the power $2$ comes to the front; it does not multiply $y$.

**3. B — Power first, then the quotient**

- Power property: $3\log_2 4=\log_2 4^{3}=\log_2 64$.
- Quotient property: a difference of logs is the log of a quotient.

$$
\begin{aligned}
3\log_2 4-\log_2 8 &= \log_2 64-\log_2 8 \\
&= \log_2\frac{64}{8} \\
&= \log_2 8 \\
&= 3
\end{aligned}
$$

Quick check: $\log_2 4=2$ and $\log_2 8=3$, so $3(2)-3=3$.

$$
\boxed{3}
$$

- Not $2$: $3\cdot4-8=4$ treats the log like a bracket. The $3$ is a power of $4$.
- Not $-1$: the factor $3$ was dropped.

**4. D — Which power of 64 gives 4?**

- Start from the power pair you know: $4^{3}=64$.
- Read it backwards: $4$ is the **cube root** of $64$.

$$
\begin{aligned}
4^{3} &= 64 \\
64^{1/3} &= 4 \\
\log_{64} 4 &= \frac13
\end{aligned}
$$

$$
\boxed{\tfrac13}
$$

- Not $3$: that is $\log_4 64$, base and input swapped.
- Not $16$ or $\tfrac1{16}$: a log is an exponent, not $64\div4$.
- The input $4$ is smaller than the base $64$, so the answer is between $0$ and $1$.

**5. B — Divide ln of the input by ln of the base**

$$
\log_b x=\frac{\ln x}{\ln b}
$$

$$
\begin{aligned}
\log_5 40 &= \frac{\ln 40}{\ln 5} \\
&\approx \frac{3.689}{1.609} \\
&\approx 2.29
\end{aligned}
$$

Sanity check: $5^{2}=25<40<125=5^{3}$, so the answer is between $2$ and $3$.

$$
\boxed{2.29}
$$

- Not $0.44$: the fraction is upside down; the **input** goes on top.
- Not $1.60$: that is $\log 40$, base $10$, not base $5$.
- Not $8$: $40\div5$ is not a logarithm.

Products become sums, quotients become differences, powers come to the front; change of base is ln of the input over ln of the base.

</details>
