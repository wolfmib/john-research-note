---
title: "AP Precalculus 2.5 — Exponential Function Context and Data Modeling"
topic: basic-math
example: ap-precalculus-2-5-exponential-function-context-and-data-modeling
course: AP Precalculus
unit: "2.5"
status: quiz
created: 2026-10-05
author: Wei-Che Hung
---

# AP Precalculus 2.5 — Exponential Function Context and Data Modeling

**Quick recap:**

- Increase of $r\%$ per unit:

$$
b=1+\frac{r}{100}
$$

- Decrease of $r\%$ per unit:

$$
b=1-\frac{r}{100}
$$

- Two points:

$$
b^{x_2-x_1}=\frac{y_2}{y_1}
$$

- Change the time unit:

$$
b^t=\left(b^{1/n}\right)^{nt}
$$

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Finance · Interest per month

A savings account grows by $8\%$ each year:

$$
B(t)=1500(1.08)^t
$$

Here, $t$ is in years.

Let $m$ be the number of **months**:

$$
t=\frac{m}{12}
$$

Which model gives the balance after $m$ months, with the growth factor **per month**?

- **A.** $B=1500(1.08)^{12m}$
- **B.** $B=1500(1.0067)^{m}$
- **C.** $B=1500(1.00643)^{m}$
- **D.** $B=1500(1.08)^{m}$

## 2. Finance · Find the interest rate

An investment of €5000 grows to €5832 in $2$ years.

It grows by the same percent each year.

What is the annual interest rate?

- **A.** $8\%$
- **B.** $8.32\%$
- **C.** $16.64\%$
- **D.** $1.08\%$

## 3. Medicine · Drug left in the body

A patient takes $400$ mg of a medicine.

Each hour, the body removes $20\%$ of the medicine still in the blood.

How much medicine is left after $3$ hours?

- **A.** $160$ mg
- **B.** $204.8$ mg
- **C.** $3.2$ mg
- **D.** $691.2$ mg

## 4. Medicine · Half-life per hour

A medicine has a half-life of $6$ hours:

$$
A(t)=100\left(\frac12\right)^{t/6}
$$

Here, $A$ is in mg and $t$ is in hours.

By about what percent does the amount decrease **each hour**?

- **A.** $8.3\%$
- **B.** $89.1\%$
- **C.** $50\%$
- **D.** $10.9\%$

## 5. Cooling · Coffee in a 20 °C room

A cup of coffee cools in a room at $20^\circ\text{C}$:

$$
T(t)=20+a\,b^t
$$

Here, $t$ is in minutes.

- At $t=0$, the coffee is $90^\circ\text{C}$.
- At $t=10$, the coffee is $55^\circ\text{C}$.

What is its temperature at $t=20$?

- **A.** $20^\circ\text{C}$
- **B.** $33.6^\circ\text{C}$
- **C.** $37.5^\circ\text{C}$
- **D.** $27.5^\circ\text{C}$

---

<details>
<summary><b>Answers</b></summary>

**1. C — Put t = m/12, then take the 12th root**

$$
\begin{aligned}
B &= 1500(1.08)^{m/12} \\
&= 1500\left(1.08^{1/12}\right)^{m} \\
&\approx \boxed{1500(1.00643)^{m}}
\end{aligned}
$$

- The account grows about $0.643\%$ per month.
- Not $1.0067$: that is $8\%\div12$. Monthly growth compounds, so it gives $1.0067^{12}\approx1.083$, more than $8\%$ a year.
- Not $(1.08)^{m}$: that grows $8\%$ every month, not every year.

**2. A — Two points give the growth factor**

$$
\begin{aligned}
5000\,b^2 &= 5832 \\
b^2 &= \frac{5832}{5000} \\
b^2 &= 1.1664 \\
b &= 1.08
\end{aligned}
$$

So the rate is

$$
\boxed{8\%}
$$

- Not $8.32\%$: that splits the $16.64\%$ total gain evenly over the 2 years. The second year earns interest on the first year's interest too.
- Not $1.08\%$: $1.08$ is the growth factor; the rate is $1.08-1=0.08$.

**3. B — Decrease of 20% means factor 0.8**

$$
\begin{aligned}
b &= 1-0.20 \\
b &= 0.8 \\
A(t) &= 400(0.8)^t \\
A(3) &= 400(0.8)^3 \\
&= \boxed{204.8\text{ mg}}
\end{aligned}
$$

- Not $160$ mg: that removes $80$ mg every hour (linear). The body removes $20\%$ of what is **left**, so it removes less each hour.
- Not $3.2$ mg: $400(0.2)^3$ keeps $20\%$ instead of removing it.

**4. D — Rewrite with exponent t**

$$
\begin{aligned}
\left(\frac12\right)^{t/6} &= \left(\left(\frac12\right)^{1/6}\right)^t \\
\left(\frac12\right)^{1/6} &\approx 0.891 \\
1-0.891 &= 0.109
\end{aligned}
$$

So the amount decreases by about

$$
\boxed{10.9\%}
$$

each hour.

- Not $8.3\%$: that is $50\%\div6$. Halving is repeated multiplication, not a fixed loss.
- Not $89.1\%$: $0.891$ is the part that **stays** each hour.

**5. C — Subtract the room temperature first**

$$
\begin{aligned}
T(0)-20 &= 70 \\
T(10)-20 &= 35 \\
b^{10} &= \frac{35}{70} \\
b^{10} &= \frac12
\end{aligned}
$$

The gap above room temperature halves every 10 minutes:

$$
\begin{aligned}
T(20) &= 20+70\left(\frac12\right)^2 \\
&= 20+17.5 \\
&= \boxed{37.5^\circ\text{C}}
\end{aligned}
$$

- Not $20^\circ\text{C}$: that keeps losing $35^\circ$ every 10 minutes (linear).
- Not $33.6^\circ\text{C}$: that uses the ratio $\frac{55}{90}$ of the whole temperature. Only the gap above $20^\circ\text{C}$ shrinks by a constant factor.

The base of an exponential model is the factor per unit of time: one plus the rate for growth, one minus the rate for decay.

</details>
