---
title: "SAT Math 6 — Quadratic and Nonlinear Equations"
topic: basic-math
example: sat-math-6-quadratic-and-nonlinear-equations
course: SAT Math
status: material
created: 2026-10-09
author: Wei-Che Hung
---

# SAT Math 6 — Quadratic and Nonlinear Equations

**SAT domain:** Advanced Math (13–15 of the 44 math questions).

**Key ideas**
- Solve $ax^2 + bx + c = 0$ by factoring, the quadratic formula, or a graph:
  - $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- The discriminant $D = b^2 - 4ac$ counts the real solutions:
  - $D > 0$: two
  - $D = 0$: one
  - $D < 0$: none
- Sum and product of the solutions:
  - sum $= -\dfrac{b}{a}$
  - product $= \dfrac{c}{a}$
- A line and a parabola: set them equal, get a quadratic. The discriminant says 0, 1 or 2 intersection points.
- Radical and rational equations can produce **extraneous** solutions: check every answer in the original equation.

**Watch out**
- Move everything to one side ($= 0$) before factoring.

## 1. Exam 1 — Exactly one solution

In the equation below, $c$ is a constant. The equation has exactly one real solution.

$$
x^2 - 6x + c = 0
$$

What is the value of $c$?

**A.** $9$

**B.** $36$

**C.** $3$

**D.** $-9$

<details>
<summary><b>Working</b></summary>

Exactly one solution means the discriminant is 0:

$$
b^2 - 4ac = 0
$$

$$
\begin{aligned} (-6)^2 - 4(1)(c) &= 0 \\ 36 - 4c &= 0 \\ c &= 9 \end{aligned}
$$

Check: $x^2 - 6x + 9 = (x - 3)^2$, one solution $x = 3$.

$$
\boxed{c = 9}
$$

**Answer: A**

</details>

## 2. Exam 2 — Radical equation

What is the solution of the equation?

$$
\sqrt{x + 7} = x - 5
$$

(Type the answer.)

<details>
<summary><b>Working</b></summary>

Square both sides:

$$
\begin{aligned} x + 7 &= (x - 5)^2 \\ x + 7 &= x^2 - 10x + 25 \\ 0 &= x^2 - 11x + 18 \\ 0 &= (x - 2)(x - 9) \end{aligned}
$$

Check $x = 2$ in the original: $\sqrt{9} = 3$, but $2 - 5 = -3$. Extraneous.

Check $x = 9$: $\sqrt{16} = 4$, and $9 - 5 = 4$. ✓

$$
\boxed{x = 9}
$$

</details>
