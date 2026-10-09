---
title: "SAT Math 4 — Linear Inequalities"
topic: basic-math
example: sat-math-4-linear-inequalities
course: SAT Math
status: material
created: 2026-10-09
author: Wei-Che Hung
---

# SAT Math 4 — Linear Inequalities

**SAT domain:** Algebra (13–15 of the 44 math questions).

**Key ideas**
- Solve an inequality like an equation.
- Multiplying or dividing by a **negative** number flips the sign:
  - $-2x > 6$ becomes $x < -3$
- Word clues:
  - "at least", "no less than": $\ge$
  - "at most", "no more than": $\le$
  - "more than": $>$, "fewer than": $<$
- A point solves a system of inequalities only if it makes **every** inequality true.
- Whole-number answers: the greatest number allowed rounds **down**; the least number needed rounds **up**.

**Watch out**
- Include every fixed amount (fees, the weight of the driver) before dividing.

## 1. Exam 1 — Delivery van

A delivery van can carry at most 1,250 kg. The driver weighs 80 kg, and each box weighs 35 kg.

What is the greatest number of boxes the van can carry with the driver?

**A.** $33$

**B.** $34$

**C.** $35$

**D.** $37$

<details>
<summary><b>Working</b></summary>

Total weight at most 1,250 kg:

$$
80 + 35b \le 1250
$$

$$
\begin{aligned} 35b &\le 1170 \\ b &\le 33.4\ldots \end{aligned}
$$

The number of boxes is a whole number, so round **down**:

$$
\boxed{b = 33}
$$

**Answer: A** — 35 forgets the driver ($1250 \div 35 \approx 35.7$).

</details>

## 2. Exam 2 — A point in a system

Which point $(x, y)$ is a solution of the system?

$$
\begin{aligned} y &> 2x - 3 \\ x + y &\le 4 \end{aligned}
$$

**A.** $(3, 2)$

**B.** $(0, 5)$

**C.** $(1, 2)$

**D.** $(4, 4)$

<details>
<summary><b>Working</b></summary>

Test each point in **both** inequalities.

$(3, 2)$: $2 > 3$ is false.

$(0, 5)$: $5 > -3$ is true, but $5 \le 4$ is false.

$(4, 4)$: $4 > 5$ is false.

$(1, 2)$: $2 > -1$ is true, and $3 \le 4$ is true.

$$
\boxed{(1, 2)}
$$

**Answer: C**

</details>
