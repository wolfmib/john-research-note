---
title: "AP Precalculus 2.13 — Exponential and Logarithmic Equations and Inequalities"
topic: basic-math
example: ap-precalculus-2-13-exponential-and-logarithmic-equations-and-inequalities
course: AP Precalculus
unit: "2.13"
status: quiz
created: 2026-11-17
author: Wei-Che Hung
---

# AP Precalculus 2.13 — Exponential and Logarithmic Equations and Inequalities

**Quick recap:**

$$
b^{M}=b^{N}\iff M=N
$$

$$
\log_b x=k\iff x=b^{k}
$$

$$
\ln A=B\iff A=e^{B}
$$

- Same base on both sides: set the exponents equal.
- Different bases: take $\ln$ of both sides.
- Log equations: check every root; the input of a log must be positive.
- Inequalities: dividing by a negative number flips the sign.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Same base

Solve:

$$
4^{x+1}=8^{x-1}
$$

- **A.** $x=3$
- **B.** $x=-5$
- **C.** $x=5$
- **D.** $x=1$

## 2. Take a logarithm

Use a calculator. To two decimal places, solve:

$$
3^{x}=20
$$

- **A.** $x\approx2.73$
- **B.** $x\approx6.67$
- **C.** $x\approx1.90$
- **D.** $x\approx0.37$

## 3. A log equation

Solve:

$$
\log_2 x+\log_2(x-2)=3
$$

- **A.** $x=4$ or $x=-2$
- **B.** $x=-2$
- **C.** $x=5$
- **D.** $x=4$

## 4. An inequality with a base below 1

Solve:

$$
\left(\tfrac12\right)^{x+2}<8
$$

- **A.** $x<-5$
- **B.** $x>-5$
- **C.** $x>1$
- **D.** $x<1$

## 5. Inverse of a log function

Find the inverse of

$$
g(x)=\ln(x-1)+4
$$

- **A.** $g^{-1}(x)=e^{x-4}-1$
- **B.** $g^{-1}(x)=e^{x+4}+1$
- **C.** $g^{-1}(x)=e^{x-4}+1$
- **D.** $g^{-1}(x)=\dfrac{1}{\ln(x-1)+4}$

---

<details>
<summary><b>Answers</b></summary>

**1. C — Write both sides as powers of 2**

- $4=2^{2}$ and $8=2^{3}$.
- Same base on both sides, so the exponents are equal.

$$
\begin{aligned}
\left(2^{2}\right)^{x+1} &= \left(2^{3}\right)^{x-1} \\
2^{2x+2} &= 2^{3x-3} \\
2x+2 &= 3x-3 \\
x &= 5
\end{aligned}
$$

Check: $4^{6}=4096$ and $8^{4}=4096$.

$$
\boxed{x=5}
$$

- Not $x=-5$: the powers $2$ and $3$ were swapped.
- Not $x=3$: the $3$ must multiply the whole bracket $x-1$.

**2. A — Take ln of both sides, then divide**

- $20$ is not a whole power of $3$, so take $\ln$ of both sides.
- The power property brings $x$ down to the front.

$$
\begin{aligned}
3^{x} &= 20 \\
x\ln3 &= \ln20 \\
x &= \frac{\ln20}{\ln3} \\
x &\approx 2.73
\end{aligned}
$$

Sanity check: $3^{2}=9<20<27=3^{3}$, so $x$ is between $2$ and $3$.

$$
\boxed{x\approx2.73}
$$

- Not $6.67$: $20\div3$ is not a logarithm.
- Not $0.37$: the fraction is upside down; $\ln20$ goes on top.

**3. D — Combine, rewrite as a power, then check the domain**

- Product property: a sum of logs is the log of a product.
- Then rewrite the log equation as a power of $2$.

$$
\begin{aligned}
\log_2\big(x(x-2)\big) &= 3 \\
x(x-2) &= 2^{3} \\
x^{2}-2x-8 &= 0 \\
(x-4)(x+2) &= 0
\end{aligned}
$$

- $x=4$: $\log_2 4+\log_2 2=2+1=3$. It works.
- $x=-2$: $\log_2(-2)$ has no value. Reject it.

$$
\boxed{x=4}
$$

- Not $x=4$ or $x=-2$: always check each root in the original logs.
- Not $x=5$: $\log_2 x+\log_2(x-2)$ is not $\log_2(x+x-2)$.

**4. B — Write both sides as powers of 2, then compare**

- $\tfrac12=2^{-1}$ and $8=2^{3}$.
- Base $2>1$, so the exponents keep the same order.

$$
\begin{aligned}
2^{-(x+2)} &< 2^{3} \\
-x-2 &< 3 \\
-x &< 5 \\
x &> -5
\end{aligned}
$$

Dividing by $-1$ flips the sign.

Check: $x=0$ gives $\tfrac14<8$, true. $x=-6$ gives $16<8$, false.

$$
\boxed{x>-5}
$$

- Not $x<-5$: the sign must flip when you divide by $-1$.
- Not $x>1$ or $x<1$: $\tfrac12$ is $2^{-1}$, so the exponent gets a minus sign.

**5. C — Swap x and y, then undo ln with e**

- Swap $x$ and $y$, then solve for $y$.
- $\ln A=B$ means $A=e^{B}$.

$$
\begin{aligned}
x &= \ln(y-1)+4 \\
x-4 &= \ln(y-1) \\
e^{x-4} &= y-1 \\
y &= e^{x-4}+1
\end{aligned}
$$

Check: $g(2)=\ln1+4=4$ and $g^{-1}(4)=e^{0}+1=2$.

$$
\boxed{g^{-1}(x)=e^{x-4}+1}
$$

- Not $e^{x-4}-1$: the $-1$ inside the log becomes $+1$ when you add it back.
- Not $\dfrac{1}{g(x)}$: an inverse function is not one over the function.

Make the bases match or take a log, rewrite logs as powers, reject roots that make a log input negative, and flip the sign when you divide by a negative.

</details>
