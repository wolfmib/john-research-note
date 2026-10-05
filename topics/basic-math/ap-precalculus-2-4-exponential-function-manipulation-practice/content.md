---
title: "AP Precalculus 2.4 — Exponential Function Manipulation Practice"
topic: basic-math
example: ap-precalculus-2-4-exponential-function-manipulation-practice
course: AP Precalculus
unit: "2.4"
status: quiz
created: 2026-10-05
author: Wei-Che Hung
---

# AP Precalculus 2.4 — Exponential Function Manipulation Practice

**Quick recap:**

- Product property:

$$
b^{x+k}=b^k\cdot b^x
$$

- Power property:

$$
b^{cx}=\left(b^c\right)^x
$$

- Negative exponent:

$$
b^{-n}=\frac{1}{b^n}
$$

- Fractional exponent:

$$
b^{1/k}=\sqrt[k]{b}
$$

**Show your calculation before choosing A–D.**

---

## 1. Shift to dilation

Rewrite in the form $a\,b^x$:

$$
2^{x+4}
$$

- **A.** $8\cdot2^x$
- **B.** $2^x+16$
- **C.** $16\cdot2^x$
- **D.** $4\cdot2^x$

## 2. Shift with a minus

Rewrite in the form $a\,b^x$:

$$
5^{x-2}
$$

- **A.** $5^x-25$
- **B.** $\dfrac{1}{25}\cdot5^x$
- **C.** $25\cdot5^x$
- **D.** $\dfrac{1}{10}\cdot5^x$

## 3. Shift with a coefficient

Rewrite in the form $a\,b^x$:

$$
3\cdot2^{x+1}
$$

- **A.** $5\cdot2^x$
- **B.** $12\cdot2^x$
- **C.** $6^{x+1}$
- **D.** $6\cdot2^x$

## 4. Change the base

Rewrite with a single base and exponent $x$:

$$
27^{x/3}
$$

- **A.** $3^x$
- **B.** $9^x$
- **C.** $81^x$
- **D.** $27^x$

## 5. Root, then power

Rewrite with a single base and exponent $x$:

$$
16^{3x/4}
$$

- **A.** $12^x$
- **B.** $64^x$
- **C.** $4^x$
- **D.** $8^x$

## 6. Fifth root, then square

Rewrite with a single base and exponent $x$:

$$
32^{2x/5}
$$

- **A.** $2^x$
- **B.** $16^x$
- **C.** $4^x$
- **D.** $12.8^x$

## 7. Negative exponent and root

Rewrite with a single base and exponent $x$:

$$
9^{-x/2}
$$

- **A.** $\left(\dfrac13\right)^x$
- **B.** $3^x$
- **C.** $\left(\dfrac{1}{4.5}\right)^x$
- **D.** $\left(\dfrac{1}{81}\right)^x$

## 8. Exponential in the denominator

Rewrite in the form $a\,b^x$:

$$
\frac{12}{3^{x-1}}
$$

- **A.** $4\left(\dfrac13\right)^x$
- **B.** $36\left(\dfrac13\right)^x$
- **C.** $36\cdot3^x$
- **D.** $4\cdot3^x$

## 9. Both rules together

Rewrite in the form $a\,b^x$:

$$
2^{3x+1}
$$

- **A.** $2\cdot6^x$
- **B.** $8\cdot2^x$
- **C.** $2\cdot8^x$
- **D.** $6\cdot2^x$

## 10. Shift and change of base

Rewrite in the form $a\,b^x$:

$$
5\cdot4^{(x-3)/2}
$$

- **A.** $40\cdot2^x$
- **B.** $\dfrac{5}{64}\cdot2^x$
- **C.** $\dfrac58\cdot4^x$
- **D.** $\dfrac58\cdot2^x$

---

<details>
<summary><b>Answers</b></summary>

**1. C — Split the sum in the exponent**

$$
\begin{aligned}
2^{x+4} &= 2^4\cdot2^x \\
&= \boxed{16\cdot2^x}
\end{aligned}
$$

- The shift $+4$ becomes the factor $2^4$.
- Not $2^x+16$: the rule multiplies $2^4\cdot2^x$, it never adds.

**2. B — A negative shift gives a fraction**

$$
\begin{aligned}
5^{x-2} &= 5^{-2}\cdot5^x \\
&= \boxed{\frac{1}{25}\cdot5^x}
\end{aligned}
$$

- The factor is $5^{-2}$, which is $\dfrac{1}{5^2}$.
- Not $\dfrac{1}{10}$: the exponent $-2$ means divide by $5$ twice, not by $5\cdot2$.

**3. D — Pull out $2^1$, then multiply**

$$
\begin{aligned}
3\cdot2^{x+1} &= 3\cdot2^1\cdot2^x \\
&= \boxed{6\cdot2^x}
\end{aligned}
$$

- Not $6^{x+1}$: the $3$ is outside the power, so it cannot join the base $2$.

**4. A — Take the cube root of the base**

$$
\begin{aligned}
27^{x/3} &= \left(27^{1/3}\right)^x \\
&= \boxed{3^x}
\end{aligned}
$$

- $27^{1/3}$ is the cube root of $27$, which is $3$.
- Not $9^x$: that divides $27$ by $3$ instead of taking the cube root.

**5. D — Fourth root first, then cube**

$$
\begin{aligned}
16^{3x/4} &= \left(16^{3/4}\right)^x \\
16^{3/4} &= \left(16^{1/4}\right)^3 \\
&= 2^3 \\
&= 8
\end{aligned}
$$

So

$$
16^{3x/4}=\boxed{8^x}
$$

- Not $12^x$: that multiplies $16$ by $\tfrac34$ instead of raising $16$ to the power $\tfrac34$.

**6. C — Fifth root first, then square**

$$
\begin{aligned}
32^{2x/5} &= \left(32^{2/5}\right)^x \\
32^{2/5} &= \left(32^{1/5}\right)^2 \\
&= 2^2 \\
&= 4
\end{aligned}
$$

So

$$
32^{2x/5}=\boxed{4^x}
$$

- Not $2^x$: it takes the fifth root of $32$ but forgets the square.

**7. A — Square root, then flip**

$$
\begin{aligned}
9^{-x/2} &= \left(9^{-1/2}\right)^x \\
9^{-1/2} &= \frac{1}{9^{1/2}} \\
&= \frac13
\end{aligned}
$$

So

$$
9^{-x/2}=\boxed{\left(\frac13\right)^x}
$$

- Not $3^x$: it drops the minus sign, so it grows where the function decays.

**8. B — Move the power up: the exponent changes sign**

$$
\begin{aligned}
\frac{12}{3^{x-1}} &= 12\cdot3^{-(x-1)} \\
&= 12\cdot3^{1-x} \\
&= 12\cdot3\cdot3^{-x} \\
&= \boxed{36\left(\frac13\right)^x}
\end{aligned}
$$

- Check $x=1$: the original gives $\dfrac{12}{3^0}$, which is $12$.
- The answer gives $36\cdot\dfrac13$, which is also $12$.
- Not $4\left(\frac13\right)^x$: dividing by $3^{-1}$ multiplies by $3$, it does not divide.

**9. C — Split the sum, then change the base**

$$
\begin{aligned}
2^{3x+1} &= 2^1\cdot2^{3x} \\
&= 2\cdot\left(2^3\right)^x \\
&= \boxed{2\cdot8^x}
\end{aligned}
$$

- The initial value is $2$ and the growth factor per unit is $8$.
- Not $2\cdot6^x$: $2^{3x}$ is $(2^3)^x$, so the base is $8$, not $2\cdot3$.

**10. D — Halve the exponent: base $4$ becomes base $2$**

$$
\begin{aligned}
5\cdot4^{(x-3)/2} &= 5\cdot\left(4^{1/2}\right)^{x-3} \\
&= 5\cdot2^{x-3} \\
&= 5\cdot2^{-3}\cdot2^x \\
&= \boxed{\frac58\cdot2^x}
\end{aligned}
$$

- The factor is $4^{-3/2}$, which is $\dfrac18$.
- Not $\dfrac{5}{64}\cdot2^x$: that uses $4^{-3}$ and forgets the $\tfrac12$ in the exponent.

A shift in the exponent becomes a constant factor, and a multiplier on $x$ in the exponent becomes a new base.

</details>
