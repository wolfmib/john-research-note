---
title: "Math Material — Malta Lotto Quaterno: Combinations and Expected Value"
topic: basic-math
example: math-material-malta-lotto-quaterno-combinations-and-expected-value
course: Math Material
status: material
created: 2026-10-02
author: Wei-Che Hung
---

# Math Material — Malta Lotto Quaterno: Combinations and Expected Value

Malta Lotto draws 5 numbers from 1 to 90. A Quaterno ticket costs €3 and picks 4 numbers.

| Numbers matched | Prize |
|---|---:|
| 2 of 4 | €25 |
| 3 of 4 | €475 |
| 4 of 4 | €501,750 |

## 1. Number of combinations

How many different combinations of 4 numbers can a player pick?

<details>
<summary><b>Working</b></summary>

The order of the 4 numbers does not matter, so count combinations:

$$
N=\binom{90}{4}=\frac{90!}{4!\,86!}
$$

$$
N=\frac{90\cdot89\cdot88\cdot87}{4\cdot3\cdot2\cdot1}=\boxed{2{,}555{,}190}
$$

</details>

## 2. Winning combinations

The draw is 17, 73, 40, 80 and 9. How many winning combinations match all four numbers?

<details>
<summary><b>Working</b></summary>

A ticket matches all four when its 4 numbers are 4 of the 5 drawn numbers:

$$
\binom54=\boxed{5}
$$

</details>

## 3. Tickets in each prize tier

How many tickets match exactly 2, exactly 3 and all 4 numbers?

<details>
<summary><b>Working</b></summary>

A ticket with $k$ matches takes $k$ of the 5 drawn numbers and $4-k$ of the 85 other numbers:

$$
\binom5k\binom{85}{4-k}
$$

$$
\begin{aligned}
\text{2 of 4:}\quad&\binom52\binom{85}2=10\cdot3570=35{,}700\\
\text{3 of 4:}\quad&\binom53\binom{85}1=10\cdot85=850\\
\text{4 of 4:}\quad&\binom54\binom{85}0=5\cdot1=5
\end{aligned}
$$

</details>

## 4. Expected value

What is the expected value of one ticket?

<details>
<summary><b>Working</b></summary>

Each prize tier contributes its probability times its prize, with $P_i=\dfrac{\text{tickets}_i}{N}$:

$$
E=\sum_i P_i\,W_i
$$

$$
E=\frac{35{,}700\cdot25+850\cdot475+5\cdot501{,}750}{2{,}555{,}190}
$$

$$
E=\frac{3{,}805{,}000}{2{,}555{,}190}\approx\boxed{\text{€}\,1.4891}
$$

</details>
