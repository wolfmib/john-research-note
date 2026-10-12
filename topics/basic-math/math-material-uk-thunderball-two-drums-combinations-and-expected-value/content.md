---
title: "Math Material — UK Thunderball: Two Drums, Combinations and Expected Value"
topic: basic-math
example: math-material-uk-thunderball-two-drums-combinations-and-expected-value
course: Math Material
status: material
created: 2026-10-12
author: Wei-Che Hung
---

# Math Material — UK Thunderball: Two Drums, Combinations and Expected Value

UK Thunderball has **two drums**:

- the main drum: 5 numbers are drawn from 1 to 39
- the Thunderball drum: 1 number is drawn from 1 to 14
- a line costs £1 and picks 5 main numbers and 1 Thunderball
- every prize is a fixed amount

| Main numbers matched | Prize |
|---|---:|
| 5 + Thunderball | £500,000 |
| 5 only | £5,000 |
| 4 + Thunderball | £250 |
| 4 only | £100 |
| 3 + Thunderball | £20 |
| 3 only | £10 |
| 2 + Thunderball | £10 |
| 1 + Thunderball | £5 |
| 0 + Thunderball | £3 |

Malta Lotto Quaterno has one drum. Here the two drums are separate, so their counts **multiply**.

## 1. The main drum

How many different sets of 5 main numbers can a player pick from 1 to 39?

<details>
<summary><b>Working</b></summary>

The order of the 5 numbers does not matter, so count combinations:

$$
\binom{39}{5}=\frac{39!}{5!\,34!}
$$

$$
\begin{aligned}\binom{39}{5}&=\frac{39\cdot38\cdot37\cdot36\cdot35}{5\cdot4\cdot3\cdot2\cdot1}\\&=\frac{69{,}090{,}840}{120}\\&=\boxed{575{,}757}\end{aligned}
$$

</details>

## 2. Two drums multiply

How many different lines (5 main numbers and 1 Thunderball) are there?

<details>
<summary><b>Working</b></summary>

Any set of 5 main numbers can go with any of the 14 Thunderballs.

Two separate choices, so multiply the counts:

$$
N=\binom{39}{5}\times\binom{14}{1}
$$

$$
\begin{aligned}N&=575{,}757\times14\\&=\boxed{8{,}060{,}598}\end{aligned}
$$

So the chance of the £500,000 jackpot is 1 in 8,060,598.

</details>

## 3. All five main numbers

The draw is 2, 4, 6, 8, 17 and Thunderball 11. How many lines match all 5 main numbers?

<details>
<summary><b>Working</b></summary>

The 5 main numbers must be exactly 2, 4, 6, 8, 17:

$$
\binom55=1\ \text{way}
$$

The Thunderball can be any of the 14 numbers:

$$
1\times14=\boxed{14}
$$

Only 1 of them has Thunderball 11 (the jackpot, £500,000).

The other 13 match 5 main only (£5,000).

</details>

## 4. Lines in each prize tier

How many lines win in each prize tier?

<details>
<summary><b>Working</b></summary>

A line with $k$ main matches takes $k$ of the 5 drawn numbers and $5-k$ of the 34 others:

$$
\binom5k\binom{34}{5-k}
$$

Then the Thunderball drum:

- right Thunderball: 1 way
- wrong Thunderball: 13 ways

$$
\begin{aligned}\text{5 + TB:}\quad&\binom55\binom{34}{0}\cdot1=1\\\text{5 only:}\quad&\binom55\binom{34}{0}\cdot13=13\\\text{4 + TB:}\quad&\binom54\binom{34}{1}\cdot1=170\\\text{4 only:}\quad&\binom54\binom{34}{1}\cdot13=2{,}210\\\text{3 + TB:}\quad&\binom53\binom{34}{2}\cdot1=5{,}610\\\text{3 only:}\quad&\binom53\binom{34}{2}\cdot13=72{,}930\\\text{2 + TB:}\quad&\binom52\binom{34}{3}\cdot1=59{,}840\\\text{1 + TB:}\quad&\binom51\binom{34}{4}\cdot1=231{,}880\\\text{0 + TB:}\quad&\binom50\binom{34}{5}\cdot1=278{,}256\end{aligned}
$$

</details>

## 5. Chance of any prize

What is the chance that one line wins a prize?

<details>
<summary><b>Working</b></summary>

Add the winning lines of all nine tiers:

$$
\text{winning lines}=650{,}910
$$

$$
\begin{aligned}P(\text{prize})&=\frac{650{,}910}{8{,}060{,}598}\\&\approx\boxed{1\ \text{in}\ 12.4}\end{aligned}
$$

</details>

## 6. Expected value

What is the expected value of one £1 line?

<details>
<summary><b>Working</b></summary>

Each tier adds its number of lines times its prize:

$$
E=\frac{\sum_i \text{lines}_i\times W_i}{N}
$$

$$
\begin{aligned}1\times500{,}000&=500{,}000\\13\times5{,}000&=65{,}000\\170\times250&=42{,}500\\2{,}210\times100&=221{,}000\\5{,}610\times20&=112{,}200\\72{,}930\times10&=729{,}300\\59{,}840\times10&=598{,}400\\231{,}880\times5&=1{,}159{,}400\\278{,}256\times3&=834{,}768\\\hline\text{total}&=4{,}262{,}568\end{aligned}
$$

$$
\begin{aligned}E&=\frac{4{,}262{,}568}{8{,}060{,}598}\\&\approx\boxed{£\,0.5288}\end{aligned}
$$

About 53p of each £1 comes back on average.

Malta Quaterno gives back about €1.49 of €3, about 50%: both games return about half the price.

</details>
