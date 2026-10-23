---
title: "AP Precalculus 2.9 — Logarithmic Expressions"
topic: basic-math
example: ap-precalculus-2-9-logarithmic-expressions
course: AP Precalculus
unit: "2.9"
status: quiz
created: 2026-10-23
author: Wei-Che Hung
---

# AP Precalculus 2.9 — Logarithmic Expressions

**Quick recap:**

- A logarithm is an exponent:

$$
\log_b c=a \iff b^{a}=c
$$

- No base written means base $10$: $\log 1000=3$.
- $\log_b 1=0$ and $\log_b b=1$.
- The input must be positive: $\log_b 0$ and $\log_b(-4)$ have no value.
- On a log scale each step multiplies by the base.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Definition · Exponential form

Which equation means the same as

$$
\log_2 32=5
$$

- **A.** $5^2=32$
- **B.** $32^5=2$
- **C.** $2^5=32$
- **D.** $2^{32}=5$

## 2. Evaluate · Fraction exponent

Find the value of

$$
\log_8 2
$$

- **A.** $\dfrac{1}{3}$
- **B.** $4$
- **C.** $3$
- **D.** $-3$

## 3. Domain · Which log does not exist?

Which of these has **no** value?

- **A.** $\log_3 1$
- **B.** $\log_5 \dfrac{1}{5}$
- **C.** $\log 0.1$
- **D.** $\log_2 0$

## 4. Estimate · Between two powers

Without a calculator, where is

$$
\log_2 50
$$

- **A.** Between $4$ and $5$
- **B.** Between $5$ and $6$
- **C.** Between $6$ and $7$
- **D.** Equal to $25$

## 5. pH · A log scale

The pH of a drink is

$$
\text{pH}=-\log[\text{H}^+]
$$

where $[\text{H}^+]$ is the acid concentration.

- Lemon juice has pH $2$.
- Black coffee has pH $5$.

How many times more acid is in lemon juice than in coffee?

- **A.** $3$
- **B.** $2.5$
- **C.** $1000$
- **D.** $30$

---

<details>
<summary><b>Answers</b></summary>

**1. C — The base stays the base, the answer is the exponent**

$$
\log_b c=a \iff b^{a}=c
$$

- Base $b=2$
- Answer $a=5$ is the exponent
- Input $c=32$ is the result

$$
\boxed{2^5=32}
$$

Check:

$$
\begin{aligned}
2^5 &= 2\cdot2\cdot2\cdot2\cdot2 \\
&= 32
\end{aligned}
$$

- Not $5^2=32$: the base of the log stays the base of the power, and $5^2$ is $25$.
- Not $2^{32}=5$: the $32$ is the result, not the exponent.

**2. A — Which power of 8 gives 2?**

Ask: $8$ to what power is $2$?

- $2$ is the cube root of $8$.

$$
\begin{aligned}
2 &= \sqrt[3]{8} \\
&= 8^{1/3}
\end{aligned}
$$

So

$$
\begin{aligned}
\log_8 2 &= \log_8 8^{1/3} \\
&= \boxed{\frac{1}{3}}
\end{aligned}
$$

- Not $4$: that is $8\div2$. A log asks for an exponent, not a division.
- Not $3$: that is $\log_2 8$, the base and input swapped.
- Not $-3$: the input $2$ is bigger than $1$, so the answer is positive.

**3. D — A power of a positive base is never 0**

$\log_2 0$ asks for $a$ with

$$
2^{a}=0
$$

- Every power of $2$ is positive, so no $a$ works.
- The input of a logarithm must be **positive**.

$$
\boxed{\log_2 0 \text{ has no value}}
$$

The others exist:

$$
\begin{aligned}
\log_3 1 &= 0 \\
\log_5 \tfrac{1}{5} &= -1 \\
\log 0.1 &= -1
\end{aligned}
$$

- $\log_3 1=0$ because $3^0=1$. An answer of $0$ is fine.
- A negative answer is fine too: $5^{-1}=\tfrac15$ and $10^{-1}=0.1$.

**4. B — Place 50 between two powers of 2**

List powers of $2$:

$$
\begin{aligned}
2^5 &= 32 \\
2^6 &= 64
\end{aligned}
$$

$50$ sits between them:

$$
32<50<64
$$

So the exponent sits between $5$ and $6$:

$$
\boxed{5<\log_2 50<6}
$$

- A calculator gives $\log_2 50\approx5.64$.
- Not $25$: that is $50\div2$. A log asks for an exponent.

**5. C — Each pH step is a factor of 10**

Undo the log for each drink:

$$
\begin{aligned}
[\text{H}^+]_{\text{lemon}} &= 10^{-2} \\
[\text{H}^+]_{\text{coffee}} &= 10^{-5}
\end{aligned}
$$

Divide:

$$
\begin{aligned}
\frac{10^{-2}}{10^{-5}} &= 10^{-2-(-5)} \\
&= 10^{3} \\
&= \boxed{1000}
\end{aligned}
$$

- $5-2=3$ steps on the pH scale, and each step multiplies by $10$.
- Not $3$: that is the number of steps, not the factor.
- Not $2.5$: that is $5\div2$. On a log scale the gap is what counts.

A logarithm answers one question: which exponent turns the base into this number?

</details>
