---
title: "AP Precalculus 2.14 — Logarithmic Function Context and Data Modeling"
topic: basic-math
example: ap-precalculus-2-14-logarithmic-function-context-and-data-modeling
course: AP Precalculus
unit: "2.14"
status: quiz
created: 2026-11-17
author: Wei-Che Hung
---

# AP Precalculus 2.14 — Logarithmic Function Context and Data Modeling

**Quick recap:**

$$
y=a+b\log x
$$

$$
L=10\log\frac{I}{I_0}
$$

$$
M=\log\frac{A}{A_0}
$$

- A log model: each $\times10$ in $x$ adds $b$ to $y$.
- $\log1=0$ and $\log10=1$, so the points $x=1$ and $x=10$ give $a$ and $b$ fast.
- Decibels: every $10$ dB is $\times10$ in intensity.
- Richter: every $1$ in magnitude is $\times10$ in amplitude.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Which table fits a log model?

Which table is best modelled by a logarithmic function

$$
y=a+b\log x\,?
$$

- **A.** $x$: $0$, $1$, $2$, $3$ → $y$: $2$, $5$, $8$, $11$
- **B.** $x$: $1$, $10$, $100$, $1000$ → $y$: $2$, $5$, $8$, $11$
- **C.** $x$: $0$, $1$, $2$, $3$ → $y$: $2$, $6$, $18$, $54$
- **D.** $x$: $1$, $2$, $3$, $4$ → $y$: $1$, $4$, $9$, $16$

## 2. A log model from two points

A model $y=a+b\log x$ passes through the points $(1,3)$ and $(10,7)$. Which is the model?

- **A.** $y=3+4\ln x$
- **B.** $y=4+3\log x$
- **C.** $y=7+3\log x$
- **D.** $y=3+4\log x$

## 3. Decibels

Sound level in decibels:

$$
L=10\log\frac{I}{I_0}
$$

- A busy street is $70$ dB.
- A loud concert is $90$ dB.

How many times greater is the intensity $I$ of the concert?

- **A.** $100$ times
- **B.** $20$ times
- **C.** $1000$ times
- **D.** about $1.3$ times

## 4. The Richter scale

Earthquake magnitude:

$$
M=\log\frac{A}{A_0}
$$

Here $A$ is the wave amplitude. One earthquake has magnitude $7.5$ and another has magnitude $4.5$. How many times greater is the amplitude of the stronger one?

- **A.** $3$ times
- **B.** $30$ times
- **C.** $1000$ times
- **D.** about $1.7$ times

## 5. Predict from a regression model

A logarithmic regression gives the distance $d$ (km) a new cyclist can ride after $t$ weeks of training:

$$
d=2.1+4.3\ln t
$$

Predict the distance after $20$ weeks.

- **A.** about $7.7$ km
- **B.** about $15.0$ km
- **C.** about $19.2$ km
- **D.** about $88.1$ km

---

<details>
<summary><b>Answers</b></summary>

**1. B — Inputs multiply by 10, outputs add the same amount**

- In a log model, **multiplying** $x$ by the same factor **adds** the same amount to $y$.
- Table B: each $\times10$ in $x$ adds $3$ to $y$.

$$
\begin{aligned}
y &= 2+3\log x \\
y(1000) &= 2+3\log1000 \\
&= 2+3(3) \\
&= 11
\end{aligned}
$$

$$
\boxed{\text{Table B}}
$$

- Not A: $x$ goes up by $1$ and $y$ adds $3$. That is linear.
- Not C: $x$ goes up by $1$ and $y$ is multiplied by $3$. That is exponential.
- Not D: $y=x^{2}$. That is quadratic.

**2. D — Use x = 1 first: log 1 = 0**

- At $x=1$, $\log1=0$, so the point $(1,3)$ gives $a$ at once.
- At $x=10$, $\log10=1$, so the point $(10,7)$ gives $b$.

$$
\begin{aligned}
3 &= a+b\log1 \\
a &= 3 \\
7 &= 3+b\log10 \\
b &= 4
\end{aligned}
$$

$$
\boxed{y=3+4\log x}
$$

- Not $3+4\ln x$: $\ln10\approx2.30$, so $x=10$ gives about $12.2$, not $7$.
- Not $4+3\log x$: at $x=1$ it gives $4$, not $3$.

**3. A — Every 10 dB is a factor of 10**

- $+10$ dB multiplies the intensity by $10$.
- $90-70=20$ dB is two steps of $10$ dB.

$$
\begin{aligned}
\frac{I_{\rm concert}}{I_{\rm street}} &= 10^{(90-70)/10} \\
&= 10^{2} \\
&= 100
\end{aligned}
$$

$$
\boxed{100\text{ times}}
$$

- Not $20$: $20$ dB is the difference in level, not the ratio of intensities.
- Not $1000$: that would be $30$ dB.
- Not $1.3$: $90\div70$ treats the scale as linear.

**4. C — Each magnitude step is a factor of 10**

- $+1$ in magnitude multiplies the amplitude by $10$.
- $7.5-4.5=3$ steps.

$$
\begin{aligned}
\frac{A_{7.5}}{A_{4.5}} &= 10^{7.5-4.5} \\
&= 10^{3} \\
&= 1000
\end{aligned}
$$

$$
\boxed{1000\text{ times}}
$$

- Not $3$: that is the difference in magnitude, not the ratio.
- Not $30$: the steps multiply ($10\times10\times10$), they do not add $10$ each.
- Not $1.7$: $7.5\div4.5$ treats the scale as linear.

**5. B — Substitute t = 20, using ln**

$$
\begin{aligned}
d &= 2.1+4.3\ln20 \\
&\approx 2.1+4.3(2.996) \\
&\approx 2.1+12.88 \\
&\approx 15.0
\end{aligned}
$$

$$
\boxed{d\approx15.0\text{ km}}
$$

- Not $7.7$: the model uses $\ln$, not $\log$ base $10$.
- Not $19.2$: only the $4.3$ multiplies $\ln t$; the $2.1$ is added.
- Not $88.1$: $\ln t$ was replaced by $t$.

On a log scale, equal steps mean equal factors: add to the level, multiply the quantity.

</details>
