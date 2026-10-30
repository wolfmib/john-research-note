---
title: "AP Precalculus — Logarithms Practice"
topic: basic-math
example: ap-precalculus-logarithms-practice
course: AP Precalculus
unit: "2.9–2.12"
status: quiz
created: 2026-10-30
author: Wei-Che Hung
---

# AP Precalculus — Logarithms Practice

**14 questions: 4 Easy, 6 Medium, 4 Hard.** Rules to keep in mind:

- $\log_b c = a \iff b^{a} = c$; no base written means base $10$.
- $\log_b 1 = 0$, $\log_b b = 1$; an input between $0$ and $1$ gives a negative log.
- $\log_b (mn) = \log_b m + \log_b n$, $\log_b \frac{m}{n} = \log_b m - \log_b n$, $\log_b m^{k} = k\log_b m$.
- Change of base: $\log_b c = \dfrac{\log c}{\log b}$.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## Easy

### 1. Evaluate a power of 2

Find the value of

$$
\log_2 16
$$

- **A.** $4$
- **B.** $8$
- **C.** $2$
- **D.** $32$

### 2. Base 10

No base written means base $10$. Find

$$
\log 1000
$$

- **A.** $100$
- **B.** $3$
- **C.** $10$
- **D.** $1000$

### 3. Log of 1

Find the value of

$$
\log_7 1
$$

- **A.** $7$
- **B.** $1$
- **C.** $0$
- **D.** No value

### 4. Exponential form to log form

Which equation means the same as

$$
3^4 = 81
$$

- **A.** $\log_4 81 = 3$
- **B.** $\log_3 4 = 81$
- **C.** $\log_{81} 3 = 4$
- **D.** $\log_3 81 = 4$

## Medium

### 5. A fraction exponent

Find the value of

$$
\log_9 3
$$

- **A.** $\dfrac{1}{2}$
- **B.** $3$
- **C.** $2$
- **D.** $-2$

### 6. Input below 1

Find the value of

$$
\log_2 \tfrac{1}{8}
$$

- **A.** $3$
- **B.** $\dfrac{1}{3}$
- **C.** $-3$
- **D.** $-\dfrac{1}{8}$

### 7. Estimate between two integers

Without a calculator, where is

$$
\log_3 50
$$

- **A.** Between $2$ and $3$
- **B.** Between $3$ and $4$
- **C.** Between $4$ and $5$
- **D.** Equal to $\dfrac{50}{3}$

### 8. Solve an exponential equation

Solve for $x$:

$$
5^{x} = 125
$$

- **A.** $25$
- **B.** $5$
- **C.** $625$
- **D.** $3$

### 9. Product rule

Simplify

$$
\log_6 9 + \log_6 4
$$

- **A.** $\log_6 13$
- **B.** $2$
- **C.** $36$
- **D.** $13$

### 10. Power rule and quotient rule

Simplify

$$
3\log_2 4 - \log_2 8
$$

- **A.** $3$
- **B.** $9$
- **C.** $\log_2 4$
- **D.** $1$

## Hard

### 11. Change of base

Use a calculator. To 2 decimal places,

$$
\log_5 40 \approx\ ?
$$

- **A.** $8$
- **B.** $1.60$
- **C.** $2.29$
- **D.** $0.44$

### 12. Decibels: a log scale

Loudness in decibels is

$$
L = 10\log\!\left(\frac{P}{P_0}\right)
$$

where $P$ is the sound power.

- A drill measures $100$ dB.
- A conversation measures $70$ dB.

How many times more power does the drill have?

- **A.** $3$
- **B.** $30$
- **C.** $300$
- **D.** $1000$

### 13. A fraction of two logs

Without a calculator, simplify

$$
\frac{\log 64}{\log 4}
$$

- **A.** $3$
- **B.** $16$
- **C.** $1.8$
- **D.** $\log 60$

### 14. Combine into one log

Write as a single number:

$$
2\log 5 + \log 4
$$

- **A.** $\log 14$
- **B.** $2$
- **C.** $10$
- **D.** $100$

---

<details>
<summary><b>Answers</b></summary>

**1. A — Which exponent turns 2 into 16?**

$$
\begin{aligned}
2^4 &= 16 \\
\log_2 16 &= \boxed{4}
\end{aligned}
$$

- Not $8$: that is $16\div2$. A log asks for an exponent, not a division.
- Not $32$: that is $2\times16$.

**2. B — Count the zeros**

$$
\begin{aligned}
10^3 &= 1000 \\
\log 1000 &= \boxed{3}
\end{aligned}
$$

- $\log 10 = 1$, $\log 100 = 2$, $\log 1000 = 3$: one per zero.
- Not $100$: that is $1000\div10$.

**3. C — Any base to the power 0 is 1**

$$
\begin{aligned}
7^0 &= 1 \\
\log_7 1 &= \boxed{0}
\end{aligned}
$$

- This works for every base: $\log_b 1 = 0$.
- Not "no value": the input $1$ is positive, so the log exists. Only $0$ and negatives have no log.

**4. D — Base stays the base, the exponent is the answer**

$$
b^{a} = c \iff \log_b c = a
$$

- Base $b = 3$
- Exponent $a = 4$ is the value of the log
- Result $c = 81$ is the input

$$
\boxed{\log_3 81 = 4}
$$

- Not $\log_4 81 = 3$: $4$ is the exponent, it cannot be the base.
- Not $\log_3 4 = 81$: the input of the log is the result $81$, not the exponent.

**5. A — 3 is the square root of 9**

$$
\begin{aligned}
3 &= \sqrt{9} \\
&= 9^{1/2} \\
\log_9 3 &= \boxed{\tfrac{1}{2}}
\end{aligned}
$$

- Not $2$: that is $\log_3 9$, base and input swapped.
- Not $-2$: the input $3$ is bigger than $1$, so the log is positive.

**6. C — A fraction needs a negative exponent**

$$
\begin{aligned}
\tfrac{1}{8} &= \frac{1}{2^3} \\
&= 2^{-3} \\
\log_2 \tfrac{1}{8} &= \boxed{-3}
\end{aligned}
$$

- Not $3$: $2^3 = 8$, not $\tfrac{1}{8}$. An input between $0$ and $1$ gives a negative log.
- Not $\tfrac{1}{3}$: the minus sign goes on the exponent, not under it.

**7. B — Trap 50 between two powers of 3**

$$
\begin{aligned}
3^3 &= 27 \\
3^4 &= 81
\end{aligned}
$$

$$
27 < 50 < 81
$$

So the exponent sits between $3$ and $4$:

$$
\boxed{3 < \log_3 50 < 4}
$$

- A calculator gives $\log_3 50 \approx 3.56$.
- Not $\tfrac{50}{3}$: a log is an exponent, not a division.

**8. D — Rewrite as a log, or match powers of 5**

$$
\begin{aligned}
5^{x} &= 125 \\
x &= \log_5 125 \\
&= \boxed{3}
\end{aligned}
$$

Check: $5^3 = 5\cdot5\cdot5 = 125$.

- Not $25$: that is $125\div5$.
- Not $625$: that is $5\times125$, or $5^4$.

**9. B — Logs add, inputs multiply**

$$
\log_b m + \log_b n = \log_b (mn)
$$

$$
\begin{aligned}
\log_6 9 + \log_6 4 &= \log_6 (9\cdot4) \\
&= \log_6 36 \\
&= \boxed{2}
\end{aligned}
$$

- $6^2 = 36$, so the log is $2$.
- Not $\log_6 13$: the product rule multiplies the inputs; it never adds them.
- Not $36$: that is the input of the final log, not its value.

**10. A — Evaluate each log, or use the rules**

**Way 1, evaluate each log:**

$$
\begin{aligned}
\log_2 4 &= 2 \\
\log_2 8 &= 3 \\
3\cdot2 - 3 &= \boxed{3}
\end{aligned}
$$

**Way 2, the rules:**

$$
\begin{aligned}
3\log_2 4 &= \log_2 4^3 = \log_2 64 \\
\log_2 64 - \log_2 8 &= \log_2 \frac{64}{8} \\
&= \log_2 8 \\
&= \boxed{3}
\end{aligned}
$$

- Not $9$: $3\log_2 4$ is $3\times2 = 6$, not $3\times$ something else; then subtract $3$.
- Not $1$: $\log_2 4 - \log_2 8$ would be $-1$; the factor $3$ was dropped.

**11. C — Divide two logs of the same kind**

$$
\log_b c = \frac{\log c}{\log b} = \frac{\ln c}{\ln b}
$$

$$
\begin{aligned}
\log_5 40 &= \frac{\log 40}{\log 5} \\
&\approx \frac{1.602}{0.699} \\
&\approx \boxed{2.29}
\end{aligned}
$$

Sense check: $5^2 = 25 < 40 < 125 = 5^3$, so the answer is between $2$ and $3$.

- Not $8$: that is $40\div5$.
- Not $1.60$: that is $\log 40$ alone (base 10). Divide by $\log 5$.
- Not $0.44$: the fraction is upside down, $\frac{\log 5}{\log 40}$.

**12. D — Every 10 dB is a factor of 10**

Subtract the two readings:

$$
\begin{aligned}
L_{\text{drill}} - L_{\text{talk}} &= 10\log\frac{P_{\text{drill}}}{P_0} - 10\log\frac{P_{\text{talk}}}{P_0} \\
&= 10\log\frac{P_{\text{drill}}}{P_{\text{talk}}}
\end{aligned}
$$

That difference is $100 - 70 = 30$:

$$
\begin{aligned}
10\log\frac{P_{\text{drill}}}{P_{\text{talk}}} &= 30 \\
\log\frac{P_{\text{drill}}}{P_{\text{talk}}} &= 3 \\
\frac{P_{\text{drill}}}{P_{\text{talk}}} &= 10^3 \\
&= \boxed{1000}
\end{aligned}
$$

- $30$ dB is three steps of $10$ dB, and each step multiplies the power by $10$.
- Not $30$: that is the gap in decibels, not the factor.
- Not $3$: that is the number of steps.

**13. A — Change of base, read backwards**

$$
\frac{\log c}{\log b} = \log_b c
$$

- Top $c = 64$, bottom $b = 4$: the fraction **is** $\log_4 64$.

$$
\begin{aligned}
\frac{\log 64}{\log 4} &= \log_4 64 \\
&= \boxed{3}
\end{aligned}
$$

Check: $4^3 = 64$.

- Not $16$: the logs are not cancelled like numbers; $\frac{\log 64}{\log 4} \ne \frac{64}{4}$.
- Not $\log 60$: dividing logs does not subtract the inputs; subtracting logs does ($\log 64 - \log 4 = \log 16$).
- Not $1.8$: that is $\log 64$ alone; it still has to be divided by $\log 4 \approx 0.6$.

**14. B — Power rule first, then the product rule**

Read the rules in the **combining** direction:

$$
k\log m = \log m^{k}, \qquad \log m + \log n = \log (mn)
$$

$$
\begin{aligned}
2\log 5 + \log 4 &= \log 5^2 + \log 4 \\
&= \log 25 + \log 4 \\
&= \log (25 \cdot 4) \\
&= \log 100 \\
&= \boxed{2}
\end{aligned}
$$

- Not $\log 14$: $2\log 5$ is $\log 25$, not $\log 10$; and logs add by multiplying the inputs.
- Not $100$: that is the input of the final log. The question asks for its value, $\log 100 = 2$.

A logarithm is an exponent. Every rule on this page is a rule about exponents written backwards.

</details>
