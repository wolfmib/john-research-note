---
title: "AP Precalculus 2.7 — Composition of Functions"
topic: basic-math
example: ap-precalculus-2-7-composition-of-functions
course: AP Precalculus
unit: "2.7"
status: quiz
created: 2026-10-16
author: Wei-Che Hung
---

# AP Precalculus 2.7 — Composition of Functions

**Quick recap:**

- Composition:

$$
(f\circ g)(x)=f\big(g(x)\big)
$$

- Work from the inside out: first $g(x)$, then use that output as the input of $f$.
- Order matters: $f\big(g(x)\big)$ and $g\big(f(x)\big)$ are usually different.
- Domain of $f\big(g(x)\big)$: the $x$ for which $g(x)$ is a valid input of $f$.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Formulas · Evaluate a composition

Let

$$
f(x)=x^2-1
$$

and

$$
g(x)=2x+1
$$

Find $f\big(g(3)\big)$.

- **A.** $17$
- **B.** $56$
- **C.** $48$
- **D.** $36$

## 2. Table · Composition from a table

$$
\begin{array}{c|ccccc}
x & 1 & 2 & 3 & 4 & 5\\
\hline
f(x) & 4 & 1 & 5 & 2 & 3\\
g(x) & 3 & 5 & 2 & 1 & 4
\end{array}
$$

Find $f\big(g(4)\big)$.

- **A.** $1$
- **B.** $5$
- **C.** $2$
- **D.** $4$

## 3. Formulas · Build f(g(x))

Let

$$
f(x)=3x-2
$$

and

$$
g(x)=x^2
$$

Which expression is $f\big(g(x)\big)$?

- **A.** $(3x-2)^2$
- **B.** $3x^2-2$
- **C.** $9x^2-2$
- **D.** $3x^2-2x$

## 4. Fuel · Cost of a trip

A car uses

$$
L(m)=0.06m
$$

litres of fuel to drive $m$ km.

Fuel costs

$$
C(L)=1.7L
$$

euros for $L$ litres.

Use $C\big(L(m)\big)$ to find the fuel cost of a $250$ km trip.

- **A.** €25.50
- **B.** €15.00
- **C.** €425.00
- **D.** €0.10

## 5. Domain · Square root of 6 − x

Let

$$
f(x)=\sqrt{x}
$$

and

$$
g(x)=6-x
$$

What is the domain of $f\big(g(x)\big)$?

- **A.** $x\ge6$
- **B.** $x\le6$
- **C.** $x\ge0$
- **D.** all real numbers

---

<details>
<summary><b>Answers</b></summary>

**1. C — Inside first: g(3), then f**

$$
\begin{aligned}
g(3) &= 2(3)+1 \\
&= 7
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(3)\big) &= f(7) \\
&= 7^2-1 \\
&= \boxed{48}
\end{aligned}
$$

- Not $17$: that is $g\big(f(3)\big)=g(8)$, the other order.
- Not $56$: that is $f(3)\cdot g(3)=8\cdot7$. Composition feeds one output in; it does not multiply.
- Not $36$: $(2x+1)^2$ is not $4x^2+1$. Work out $g(3)=7$ first, then square.

**2. D — Read g first, then use its output in f**

$$
\begin{aligned}
g(4) &= 1
\end{aligned}
$$

$$
\begin{aligned}
f\big(g(4)\big) &= f(1) \\
&= \boxed{4}
\end{aligned}
$$

- Not $5$: that is $g\big(f(4)\big)=g(2)$, the other order.
- Not $2$ or $1$: those are $f(4)$ and $g(4)$, only one step of the two.

**3. B — Replace every x in f with g(x)**

$$
\begin{aligned}
f\big(g(x)\big) &= 3\,g(x)-2 \\
&= \boxed{3x^2-2}
\end{aligned}
$$

- Not $(3x-2)^2$: that is $g\big(f(x)\big)$, the other order.
- Not $9x^2-2$: only $x$ is squared, not the $3$. $9x^2$ would be $(3x)^2$.

**4. A — Kilometres → litres → euros**

$$
\begin{aligned}
L(250) &= 0.06(250) \\
&= 15 \text{ litres}
\end{aligned}
$$

$$
\begin{aligned}
C\big(L(250)\big) &= C(15) \\
&= 1.7(15) \\
&= \boxed{25.50\text{ euros}}
\end{aligned}
$$

- Not €15.00: $15$ is the number of **litres**, the output of the inside function only.
- Not €425.00: $C(250)$ prices $250$ litres. The $250$ km must go into $L$ first.

In one formula, in euros:

$$
\begin{aligned}
C\big(L(m)\big) &= 1.7(0.06m) \\
&= 0.102m
\end{aligned}
$$

**5. B — The output of g must be in the domain of f**

$$
\begin{aligned}
f\big(g(x)\big) &= \sqrt{6-x}
\end{aligned}
$$

The square root needs

$$
\begin{aligned}
6-x &\ge 0
\end{aligned}
$$

Add $x$ to both sides:

$$
\begin{aligned}
6 &\ge x
\end{aligned}
$$

So the domain is

$$
\boxed{x\le6}
$$

- Not $x\ge6$: at $x=10$, $\sqrt{6-10}=\sqrt{-4}$ is not a real number.
- Not $x\ge0$: that is the domain of $f$ alone. The input of $f$ is $6-x$, not $x$.

In a composition the output of the inside function is the input of the outside function, so the order matters.

</details>
