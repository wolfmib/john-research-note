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
- A **common-factor ladder** shows the HCF on the left and helps find the LCM.
- Use the LCM to solve repeating-event problems.

## 1. Style 1 · Lists and the ladder

**How it works**

- List multiples by adding the original number each time.
- Choose a prime that divides **both** entries, then divide both.
- Stop when no factor greater than 1 divides both bottom entries.
- **HCF:** multiply the common factors on the left.
- **LCM:** multiply the left factors **and both bottom entries**.

- **Worked example:** find the HCF and LCM of **18 and 24**.
- Write the first five multiples, then use a ladder.

- **Your turn:** For **16 and 24**, write the first five multiples of each.
- Use the common-factor ladder to find both HCF and LCM.

| Question | Answer |
|---:|---:|
| $\operatorname{HCF}(16,24)$ | ? |
| $\operatorname{LCM}(16,24)$ | ? |

<details>
<summary><b>Working</b></summary>

**1 · First five positive multiples.**

- 18: 18, 36, 54, 72, 90.
- 24: 24, 48, 72, 96, 120.

The first common multiple is **72**.

**2 · Divide both numbers by common primes.**

$$
\begin{array}{r|rr}
2 & 18 & 24 \\ 3 & 9 & 12 \\  & 3 & 4
\end{array}
$$

- Stop at 3 and 4: neither 2 nor 3 divides both.
- Keep these bottom entries.

**3 · HCF: the left side only.**

$$
\operatorname{HCF}(18,24)=2\times3
$$

$$
\operatorname{HCF}(18,24)=\boxed{6}
$$

**4 · LCM: the left side and the bottom.**

$$
\operatorname{LCM}(18,24)=2\times3\times3\times4
$$

$$
\operatorname{LCM}(18,24)=\boxed{72}
$$

The common factors are counted once; the bottom entries supply what each number still needs.

**Practice check — after you try:**

- Divide only by a prime that divides **every** number in the row.
- Stop when no prime divides them all.

$$
\begin{array}{r|rr}
2 & 16 & 24 \\ 2 & 8 & 12 \\ 2 & 4 & 6 \\  & 2 & 3
\end{array}
$$

**HCF: multiply the common factors on the left.**

$$
\operatorname{HCF}=2\times2\times2
$$

$$
\operatorname{HCF}=\boxed{8}
$$

**LCM: left factors × bottom entries.** No two bottom entries share a factor greater than 1.

$$
\operatorname{LCM}=2\times2\times2\times2\times3
$$

$$
\operatorname{LCM}=\boxed{48}
$$

</details>

## 2. Style 2 · When do they ring together?

**How it works**

- Repeating events coincide again after the **LCM of their intervals**.
- Divide by primes common to **all three** numbers; the left product is their HCF.
- In this example, no two bottom entries share a factor, so left factors × bottom entries gives the LCM.
- Find the waiting time first, then add it to the starting clock time.

- **Worked example:** three bells ring every **12, 18 and 30 minutes**.
- All ring at **9:00 am**.

- Find how long until they next ring together and the clock time.
- Show a ladder.

- **Your turn:** Three bells ring every **4, 6 and 10 minutes**.
- They ring together at **10:15 am**.
- Use a common-factor ladder to find when they next ring together.

| Question | Answer |
|---:|---:|
| $\text{Minutes to wait}$ | ? |
| $\text{Next time: hour (am)}$ | ? |
| $\text{Next time: minutes}$ | ? |

<details>
<summary><b>Working</b></summary>

**1 · Divide by primes common to all three.**

$$
\begin{array}{r|rrr}
2 & 12 & 18 & 30 \\ 3 & 6 & 9 & 15 \\  & 2 & 3 & 5
\end{array}
$$

The left factors are 2 and 3; the bottom entries are 2, 3 and 5.

$$
\operatorname{HCF}(12,18,30)=2\times3
$$

$$
\operatorname{HCF}(12,18,30)=\boxed{6}
$$

**2 · Multiply the left factors and the bottom entries.**

No two of 2, 3 and 5 share a factor greater than 1.

$$
\operatorname{LCM}(12,18,30)=2\times3\times2\times3\times5
$$

$$
\text{Waiting time}=\boxed{180\text{ minutes}}
$$

**3 · Convert to hours and minutes.**

$$
180\text{ minutes}=3\text{ hours}
$$

Three hours after 9:00 am is **12:00 noon**.

**4 · A check for three numbers.**

- The left product is always the HCF.
- Multiply all bottom entries only if **no two share a factor greater than 1**.
- If bottom entries still share factors, find their LCM first, then multiply by the left product.

**Practice check — after you try:**

- Divide only by a prime that divides **every** number in the row.
- Stop when no prime divides them all.

$$
\begin{array}{r|rrr}
2 & 4 & 6 & 10 \\  & 2 & 3 & 5
\end{array}
$$

**HCF: multiply the common factors on the left.**

$$
\operatorname{HCF}=2
$$

$$
\operatorname{HCF}=\boxed{2}
$$

**LCM: left factors × bottom entries.** No two bottom entries share a factor greater than 1.

$$
\operatorname{LCM}=2\times2\times3\times5
$$

$$
\operatorname{LCM}=\boxed{60}
$$

One hour after 10:15 am is **11:15 am**.

</details>
