---
title: "Malta Year 8 Math — Multiples & LCM"
topic: basic-math
example: malta-year-8-math-test-prep-multiples-and-lcm
course: Malta Year 8 Math
status: material
created: 2026-11-03
author: Wei-Che Hung
---

# Malta Year 8 Math — Multiples & LCM

- Multiples are the positive times-table answers.
- A common multiple appears in every list.
- The **lowest common multiple (LCM)** is the smallest positive common multiple.
- Use a ladder to find an LCM and solve repeating-event problems.

## 1. Style 1 · Lists and the ladder

**How it works**

- List multiples by adding the original number each time.
- For the ladder, choose a prime dividing at least one entry. Divide every entry it divides; carry the others unchanged.
- Continue until every entry is 1, then multiply the primes down the left.

- **Worked example:** find the LCM of **12, 18 and 30**.
- Write the first five multiples, then use a ladder.

- **Your turn:** For **8, 12 and 20**, write the first five multiples of each.
- Use the ladder method to find the LCM.

| Question | Answer |
|---:|---:|
| $\operatorname{LCM}(8,12,20)$ | ? |

<details>
<summary><b>Working</b></summary>

**1 · First five positive multiples.**

- 12: 12, 24, 36, 48, 60.
- 18: 18, 36, 54, 72, 90.
- 30: 30, 60, 90, 120, 150.

- These short lists do not yet contain a number common to all three.
- The lists continue.

**2 · Divide by primes, carrying entries unchanged when needed.**

$$
\begin{array}{r|rrr}
2 & 12 & 18 & 30 \\ 2 & 6 & 9 & 15 \\ 3 & 3 & 9 & 15 \\ 3 & 1 & 3 & 5 \\ 5 & 1 & 1 & 5 \\  & 1 & 1 & 1
\end{array}
$$

**3 · Multiply the ladder primes.**

$$
\operatorname{LCM}(12,18,30)=2\times2\times3\times3\times5
$$

$$
\operatorname{LCM}(12,18,30)=\boxed{180}
$$

**4 · Why it is the lowest.**

- 180 is divisible by 12, 18 and 30.
- The ladder includes exactly the prime factors needed to cover every number.
- Any common multiple must contain these factors, so none can be smaller.

**Practice check — after you try:**

$$
\begin{array}{r|rrr}
2 & 8 & 12 & 20 \\ 2 & 4 & 6 & 10 \\ 2 & 2 & 3 & 5 \\ 3 & 1 & 3 & 5 \\ 5 & 1 & 1 & 5 \\  & 1 & 1 & 1
\end{array}
$$

$$
\operatorname{LCM}(8,12,20)=\boxed{120}
$$

</details>

## 2. Style 2 · When do they ring together?

**How it works**

- Repeating events coincide again after the **LCM of their intervals**.
- Find the waiting time first, then add it to the starting clock time.

- **Worked example:** three bells ring every **12, 18 and 24 minutes**.
- All ring at **9:00 am**.

- Find how long until they next ring together and the clock time.
- Show a ladder.

- **Your turn:** Three bells ring every **10, 15 and 20 minutes**.
- They ring together at **10:15 am**.
- Use a ladder to find when they next ring together.

| Question | Answer |
|---:|---:|
| $\text{Minutes to wait}$ | ? |
| $\text{Next time: hour (am)}$ | ? |
| $\text{Next time: minutes}$ | ? |

<details>
<summary><b>Working</b></summary>

**1 · The waiting time must be a multiple of all three intervals.** Use the LCM.

$$
\begin{array}{r|rrr}
2 & 12 & 18 & 24 \\ 2 & 6 & 9 & 12 \\ 2 & 3 & 9 & 6 \\ 3 & 3 & 9 & 3 \\ 3 & 1 & 3 & 1 \\  & 1 & 1 & 1
\end{array}
$$

**2 · Multiply the ladder primes.**

$$
\operatorname{LCM}(12,18,24)=2\times2\times2\times3\times3
$$

$$
\text{Waiting time}=\boxed{72\text{ minutes}}
$$

**3 · Convert to hours and minutes.**

$$
72\text{ minutes}=1\text{ hour }12\text{ minutes}
$$

Starting at 9:00 am, one hour takes us to 10:00 am; another 12 minutes gives **10:12 am**.

**Practice check — after you try:**

$$
\begin{array}{r|rrr}
2 & 10 & 15 & 20 \\ 2 & 5 & 15 & 10 \\ 3 & 5 & 15 & 5 \\ 5 & 5 & 5 & 5 \\  & 1 & 1 & 1
\end{array}
$$

$$
\text{Waiting time}=\boxed{60\text{ minutes}}
$$

One hour after 10:15 am is **11:15 am**.

</details>
