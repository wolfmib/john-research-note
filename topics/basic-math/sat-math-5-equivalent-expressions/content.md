---
title: "SAT Math 5 — Equivalent Expressions"
topic: basic-math
example: sat-math-5-equivalent-expressions
course: SAT Math
status: material
created: 2026-10-09
author: Wei-Che Hung
---

# SAT Math 5 — Equivalent Expressions

**SAT domain:** Advanced Math (13–15 of the 44 math questions).

**Key ideas**
- Expand brackets and combine like terms.
- Special products:
  - $(a + b)^2 = a^2 + 2ab + b^2$
  - $(a - b)^2 = a^2 - 2ab + b^2$
  - $a^2 - b^2 = (a - b)(a + b)$
- Exponent rules:
  - $x^m \cdot x^n = x^{m + n}$
  - $(x^m)^n = x^{mn}$
  - $x^{-n} = \dfrac{1}{x^n}$
  - $x^{m/n} = \sqrt[n]{x^m}$
- Rational expressions: factor first, then cancel; add fractions over a common denominator.
- If two polynomials are equal for **all** $x$, their matching coefficients are equal.
- Completing the square: $x^2 + bx + c = \left(x + \tfrac{b}{2}\right)^2 + c - \tfrac{b^2}{4}$.

**Watch out**
- A minus sign in front of a bracket changes the sign of **every** term inside.

## 1. Exam 1 — Expand and subtract

Which expression is equivalent to

$$
(2x - 3)(x + 5) - (x^2 - 4)
$$

**A.** $x^2 + 7x - 11$

**B.** $x^2 + 7x - 19$

**C.** $x^2 + 13x - 11$

**D.** $3x^2 + 7x - 19$

<details>
<summary><b>Working</b></summary>

Expand the product:

$$
\begin{aligned} (2x - 3)(x + 5) &= 2x^2 + 10x - 3x - 15 \\ &= 2x^2 + 7x - 15 \end{aligned}
$$

Subtract **every** term of $x^2 - 4$:

$$
\begin{aligned} 2x^2 + 7x - 15 - x^2 + 4 &= x^2 + 7x - 11 \end{aligned}
$$

$$
\boxed{x^2 + 7x - 11}
$$

**Answer: A** — $-19$ comes from $-15 - 4$: the minus was not passed to the $-4$.

</details>

## 2. Exam 2 — Match the coefficients

For all values of $x$,

$$
(ax + 4)(2x - b) = 6x^2 - x - 12,
$$

where $a$ and $b$ are constants. What is $a + b$? (Type the answer.)

<details>
<summary><b>Working</b></summary>

Expand the left side:

$$
2ax^2 + (8 - ab)x - 4b
$$

Match the $x^2$ terms and the constants:

$$
\begin{aligned} 2a &= 6 \\ a &= 3 \end{aligned}
$$

$$
\begin{aligned} -4b &= -12 \\ b &= 3 \end{aligned}
$$

Check the middle term: $8 - ab = 8 - 9$, which is $-1$. ✓

$$
\boxed{a + b = 6}
$$

</details>
