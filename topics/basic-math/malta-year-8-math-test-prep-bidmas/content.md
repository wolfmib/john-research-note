---
title: "Malta Year 8 Math — BIDMAS"
topic: basic-math
example: malta-year-8-math-test-prep-bidmas
course: Malta Year 8 Math
status: material
created: 2026-11-03
author: Wei-Che Hung
---

# Malta Year 8 Math — BIDMAS

- **B**rackets, then **I**ndices (powers).
- **D**ivision and **M**ultiplication share one priority: work left to right.
- **A**ddition and **S**ubtraction share one priority: work left to right.
- Show one new stage of working on each line.

## 1. Style 1 · Powers and mixed operations

**How it works**

- With no brackets, calculate powers first.
- Next multiply or divide, working left to right.
- Finally add or subtract, working left to right.

**Worked example:** calculate step by step.

$$
48\div6+3^2\times4-5
$$

Which operation comes first?

- **Your turn:** Calculate on paper using BIDMAS, then enter your answer.
- State which operation comes first.

$$
56\div7+4^2\times3-6
$$

| Question | Answer |
|---:|---:|
| $\text{Final answer}$ | ? |

<details>
<summary><b>Working</b></summary>

**1 · The power comes first.**

$$
3^2=9
$$

The expression becomes:

$$
48\div6+9\times4-5
$$

**2 · Divide and multiply before adding or subtracting.**

$$
48\div6=8
$$

$$
9\times4=36
$$

The expression becomes:

$$
8+36-5
$$

**3 · Add and subtract from left to right.**

$$
\begin{aligned}
8+36-5&=44-5 \\
&=\boxed{39}
\end{aligned}
$$

**Practice check — after you try:**

$$
\begin{aligned}
56\div7+4^2\times3-6&=56\div7+16\times3-6 \\
&=8+48-6 \\
&=56-6 \\
&=\boxed{50}
\end{aligned}
$$

</details>

## 2. Style 2 · Nested brackets

**How it works**

- Work from the innermost brackets outwards.
- Simplify powers before the remaining multiplication or division.
- Finish with addition and subtraction from left to right.

**Worked example:** calculate and explain why you cannot start by working everything from left to right.

$$
72\div[3\times(2+4)]+5^2-2^3
$$

- **Your turn:** Calculate on paper.
- Explain which brackets you work out first.

$$
96\div[4\times(2+4)]+6^2-3^3
$$

| Question | Answer |
|---:|---:|
| $\text{Final answer}$ | ? |

<details>
<summary><b>Working</b></summary>

**1 · Innermost brackets first.**

$$
2+4=6
$$

$$
72\div[3\times6]+5^2-2^3
$$

**2 · Finish the outer bracket.**

$$
3\times6=18
$$

$$
72\div18+5^2-2^3
$$

**3 · Simplify both powers.**

$$
5^2=25
$$

$$
2^3=8
$$

$$
72\div18+25-8
$$

**4 · Divide, then add and subtract.**

$$
\begin{aligned}
72\div18+25-8&=4+25-8 \\
&=29-8 \\
&=\boxed{21}
\end{aligned}
$$

**5 · Why not strictly left to right?**

- The whole bracket is the divisor. Dividing 72 by 3 first would ignore it.
- Left to right applies **within a shared priority**, after brackets and powers.

**Practice check — after you try:**

$$
\begin{aligned}
96\div[4\times(2+4)]+6^2-3^3&=96\div24+36-27 \\
&=4+36-27 \\
&=40-27 \\
&=\boxed{13}
\end{aligned}
$$

</details>
