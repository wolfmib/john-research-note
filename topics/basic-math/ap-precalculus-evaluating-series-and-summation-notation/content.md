---
title: "AP Precalculus — Evaluating Series and Summation Notation"
topic: basic-math
example: ap-precalculus-evaluating-series-and-summation-notation
course: AP Precalculus
unit: "Series"
status: quiz
created: 2026-10-19
author: Wei-Che Hung
---

# AP Precalculus — Evaluating Series and Summation Notation

**Summation notation** (sigma notation) is shorthand for adding a list of terms:

$$
\sum_{n=1}^{k} a_n = a_1 + a_2 + \cdots + a_k
$$

- Write out every term first.
- Then add them up.

**Type your answer as a number** (decimal or fraction like 3/4).

---

## 1. Natural numbers

Evaluate

$$
\sum_{n=1}^{5} n
$$

Answer: ______

## 2. Arithmetic: constant times n

Evaluate

$$
\sum_{n=1}^{4} 3n
$$

Answer: ______

## 3. Geometric: powers of 2

Evaluate

$$
\sum_{n=0}^{4} 2^n
$$

Answer: ______

## 4. Odd numbers

Evaluate

$$
\sum_{n=1}^{5} (2n-1)
$$

Answer: ______

## 5. Sum of squares

Evaluate

$$
\sum_{k=1}^{4} k^2
$$

Answer: ______

## 6. Alternating signs

Evaluate

$$
\sum_{n=1}^{6} (-1)^{{n+1}} \\cdot n
$$

Answer: ______

## 7. Geometric: halving

Evaluate

$$
\sum_{n=0}^{3} 5 \\cdot \\left(\\tfrac{{1}}{{2}}\\right)^n
$$

Answer: ______

## 8. Telescoping fractions

Evaluate

$$
\sum_{k=1}^{3} \\dfrac{{1}}{{k(k+1)}}
$$

Answer: ______

## 9. Quadratic: n squared plus n

Evaluate

$$
\sum_{n=1}^{4} (n^2+n)
$$

Answer: ______

## 10. Geometric: multiply by 3

Evaluate

$$
\sum_{n=1}^{3} 4 \\cdot 3^{{n-1}}
$$

Answer: ______

## 11. Sum of cubes

Evaluate

$$
\sum_{n=1}^{4} n^3
$$

Answer: ______

## 12. Alternating squares

Evaluate

$$
\sum_{n=1}^{5} (-1)^n \\cdot n^2
$$

Answer: ______

## 13. Odd squares

Evaluate

$$
\sum_{k=0}^{3} (2k+1)^2
$$

Answer: ______

## 14. Factorials

Evaluate

$$
\sum_{n=1}^{3} n!
$$

Recall: $n! = n \times (n-1) \times \cdots \times 1$.

Answer: ______

## 15. Geometric: half, quarter, eighth...

Evaluate

$$
\sum_{n=1}^{4} \\dfrac{{1}}{{2^n}}
$$

Answer: ______

---

<details>
<summary><b>Answers</b></summary>

**1. $15$ — Write out the terms**

$$
\begin{aligned}
\sum_{n=1}^{5} n &= 1+2+3+4+5 \\
&= \boxed{15}
\end{aligned}
$$

**2. $30$ — Factor out the 3**

$$
\begin{aligned}
&= 3(1)+3(2)+3(3)+3(4) \\
&= 3+6+9+12 \\
&= \boxed{30}
\end{aligned}
$$

**3. $31$ — List powers of 2**

$$
\begin{aligned}
&= 2^0+2^1+2^2+2^3+2^4 \\
&= 1+2+4+8+16 \\
&= \boxed{31}
\end{aligned}
$$

**4. $25$ — List the odd numbers**

$$
\begin{aligned}
&= 1+3+5+7+9 \\
&= \boxed{25}
\end{aligned}
$$

The sum of the first $k$ odd numbers is always $k^2$.

Here $k=5$, so $5^2=25$.

**5. $30$ — Square each term**

$$
\begin{aligned}
&= 1^2+2^2+3^2+4^2 \\
&= 1+4+9+16 \\
&= \boxed{30}
\end{aligned}
$$

**6. $-3$ — Signs alternate + - + - ...**

$$
\begin{aligned}
&= (+1)+(-2)+(+3)+(-4)+(+5)+(-6) \\
&= (1-2)+(3-4)+(5-6) \\
&= (-1)+(-1)+(-1) \\
&= \boxed{-3}
\end{aligned}
$$

**7. $9.375$ — Each term is half the previous**

$$
\begin{aligned}
&= 5+2.5+1.25+0.625 \\
&= \boxed{9.375}
\end{aligned}
$$

**8. $\frac{3}{4}$ — Partial fractions cancel**

Each term splits:

$$
\begin{aligned}
\frac{1}{k(k+1)} &= \frac{1}{k}-\frac{1}{k+1}
\end{aligned}
$$

So the sum telescopes:

$$
\begin{aligned}
&= \left(\frac{1}{1}-\frac{1}{2}\right)+\left(\frac{1}{2}-\frac{1}{3}\right)+\left(\frac{1}{3}-\frac{1}{4}\right) \\
&= 1-\frac{1}{4} \\
&= \boxed{\frac{3}{4}}
\end{aligned}
$$

**9. $40$ — Evaluate each term**

$$
\begin{aligned}
n=1: &\ 1+1=2 \\
n=2: &\ 4+2=6 \\
n=3: &\ 9+3=12 \\
n=4: &\ 16+4=20
\end{aligned}
$$

$$
\begin{aligned}
&= 2+6+12+20 \\
&= \boxed{40}
\end{aligned}
$$

**10. $52$ — List the terms**

$$
\begin{aligned}
n=1: &\ 4 \cdot 3^0 = 4 \\
n=2: &\ 4 \cdot 3^1 = 12 \\
n=3: &\ 4 \cdot 3^2 = 36
\end{aligned}
$$

$$
\begin{aligned}
&= 4+12+36 \\
&= \boxed{52}
\end{aligned}
$$

**11. $100$ — Cube each term**

$$
\begin{aligned}
&= 1^3+2^3+3^3+4^3 \\
&= 1+8+27+64 \\
&= \boxed{100}
\end{aligned}
$$

The sum of the first $k$ cubes equals $\left(\frac{k(k+1)}{2}\right)^2$.

Here $k=4$: $\left(\frac{4 \cdot 5}{2}\right)^2 = 10^2 = 100$.

**12. $-15$ — Signs: -, +, -, +, -**

$$
\begin{aligned}
&= -1+4-9+16-25 \\
&= (4+16)-(1+9+25) \\
&= 20-35 \\
&= \boxed{-15}
\end{aligned}
$$

**13. $84$ — The odd numbers 1, 3, 5, 7 squared**

$$
\begin{aligned}
k=0: &\ 1^2=1 \\
k=1: &\ 3^2=9 \\
k=2: &\ 5^2=25 \\
k=3: &\ 7^2=49
\end{aligned}
$$

$$
\begin{aligned}
&= 1+9+25+49 \\
&= \boxed{84}
\end{aligned}
$$

**14. $9$ — 1! = 1, 2! = 2, 3! = 6**

$$
\begin{aligned}
1! &= 1 \\
2! &= 2 \\
3! &= 6
\end{aligned}
$$

$$
\begin{aligned}
&= 1+2+6 \\
&= \boxed{9}
\end{aligned}
$$

**15. $\frac{15}{16}$ — List powers of 1/2**

$$
\begin{aligned}
&= \frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\frac{1}{16}
\end{aligned}
$$

Common denominator 16:

$$
\begin{aligned}
&= \frac{8+4+2+1}{16} \\
&= \boxed{\frac{15}{16}}
\end{aligned}
$$

As a decimal: $0.9375$.

To evaluate a sum, substitute each value of the index, list the terms, and add.

</details>
