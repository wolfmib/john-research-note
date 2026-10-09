---
title: "SAT Math 9 — Statistics and Probability"
topic: basic-math
example: sat-math-9-statistics-and-probability
course: SAT Math
status: material
created: 2026-10-09
author: Wei-Che Hung
---

# SAT Math 9 — Statistics and Probability

**SAT domain:** Problem-Solving and Data Analysis (5–7 of the 44 math questions).

**Key ideas**
- Mean and sum:
  - mean $= \dfrac{\text{sum}}{\text{count}}$
  - sum $= \text{mean} \times \text{count}$
- Median: the middle value of the sorted data (the mean of the two middle values when the count is even).
- An outlier pulls the mean towards it; the median hardly moves.
- Standard deviation measures spread: data packed close to the mean has a smaller one. No calculation is needed on the SAT, only a comparison.
- Two-way table, conditional probability:
  - $P(A \mid B) = \dfrac{\text{number in } A \text{ and } B}{\text{number in } B}$
- A random sample lets you generalise only to the population it was drawn from.
  - estimate $\pm$ margin of error gives the plausible range
  - a larger sample gives a smaller margin of error
- Line of best fit: residual $=$ actual $-$ predicted.

**Watch out**
- "Given that …" shrinks the denominator to that row or column only.

## 1. Exam 1 — Two-way table

Students were asked how they travel to school.

$$
\begin{array}{l|ccc|c} & \text{Bus} & \text{Walk} & \text{Car} & \text{Total} \\ \hline \text{Year 10} & 30 & 25 & 15 & 70 \\ \text{Year 11} & 20 & 35 & 25 & 80 \\ \hline \text{Total} & 50 & 60 & 40 & 150 \end{array}
$$

A student who walks is chosen at random. What is the probability the student is in Year 11?

**A.** $\tfrac{7}{12}$

**B.** $\tfrac{7}{30}$

**C.** $\tfrac{7}{16}$

**D.** $\tfrac{1}{2}$

<details>
<summary><b>Working</b></summary>

“A student who walks” limits the choice to the Walk column: 60 students.

Of those, 35 are in Year 11:

$$
\begin{aligned} P &= \frac{35}{60} \\ &= \frac{7}{12} \end{aligned}
$$

$$
\boxed{\tfrac{7}{12}}
$$

**Answer: A** — $\tfrac{7}{30}$ divides by all 150 students; $\tfrac{7}{16}$ divides by the Year 11 total.

</details>

## 2. Exam 2 — Remove an outlier

$$
10,\ 12,\ 15,\ 15,\ 18,\ 20,\ 50
$$

The value 50 is removed from the data. How do the mean and the median change?

**A.** The mean decreases by 5; the median does not change.

**B.** Both decrease by 5.

**C.** The mean does not change; the median decreases.

**D.** The mean decreases by 5; the median decreases by 1.5.

<details>
<summary><b>Working</b></summary>

Mean before and after:

$$
\begin{aligned} \frac{140}{7} &= 20 \\ \frac{90}{6} &= 15 \end{aligned}
$$

Median before: the 4th value, 15.

Median after (6 values): the mean of the 3rd and 4th values, $\tfrac{15 + 15}{2}$, which is 15.

The mean falls by 5; the median stays 15.

**Answer: A**

</details>
