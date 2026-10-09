---
title: "SAT Math 3 — Systems of Linear Equations"
topic: basic-math
example: sat-math-3-systems-of-linear-equations
course: SAT Math
status: material
created: 2026-10-09
author: Wei-Che Hung
---

# SAT Math 3 — Systems of Linear Equations

**SAT domain:** Algebra (13–15 of the 44 math questions).

**Key ideas**
- **Substitution:** solve one equation for a variable and put it into the other.
- **Elimination:** add or subtract the equations (after scaling) so one variable cancels.
- **Graph:** the solution is the intersection point. Desmos finds it in seconds.
- Number of solutions for $ax + by = c$ and $dx + ey = f$:
  - one solution: different slopes, $\dfrac{a}{d} \ne \dfrac{b}{e}$
  - no solution: parallel lines, $\dfrac{a}{d} = \dfrac{b}{e} \ne \dfrac{c}{f}$
  - infinitely many: the same line, $\dfrac{a}{d} = \dfrac{b}{e} = \dfrac{c}{f}$
- When the question asks for $x + y$ or $x - y$, try adding or subtracting the two equations first.

**Watch out**
- Answer the question asked: the value of $x$, $y$, or an expression in both.

## 1. Exam 1 — Ticket sales

A school play sold 230 tickets. Adult tickets cost €8 and student tickets cost €5. The total was €1,450.

How many adult tickets were sold?

**A.** $100$

**B.** $130$

**C.** $150$

**D.** $80$

<details>
<summary><b>Working</b></summary>

Let $a$ be adult tickets and $s$ student tickets:

$$
\begin{aligned} a + s &= 230 \\ 8a + 5s &= 1450 \end{aligned}
$$

Substitute $s = 230 - a$:

$$
\begin{aligned} 8a + 5(230 - a) &= 1450 \\ 3a + 1150 &= 1450 \\ a &= 100 \end{aligned}
$$

$$
\boxed{a = 100}
$$

**Answer: A** — 130 is the number of student tickets.

</details>

## 2. Exam 2 — No solution

In the system below, $k$ is a constant. The system has no solution.

$$
\begin{aligned} kx + 6y &= 9 \\ 2x + 3y &= 5 \end{aligned}
$$

What is the value of $k$? (Type the answer.)

<details>
<summary><b>Working</b></summary>

No solution means parallel lines: the $x$ and $y$ coefficients are in the same ratio.

$$
\frac{k}{2} = \frac{6}{3}
$$

$$
\begin{aligned} \frac{k}{2} &= 2 \\ k &= 4 \end{aligned}
$$

Check the constants are **not** in that ratio: $\tfrac{9}{5} \ne 2$, so the lines are parallel, not the same line.

$$
\boxed{k = 4}
$$

</details>
