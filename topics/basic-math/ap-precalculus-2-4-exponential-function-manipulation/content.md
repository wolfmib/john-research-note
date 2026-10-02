---
title: "AP Precalculus 2.4 — Exponential Function Manipulation"
topic: basic-math
example: ap-precalculus-2-4-exponential-function-manipulation
course: AP Precalculus
unit: "2.4"
status: quiz
created: 2026-10-02
author: Wei-Che Hung
---

# AP Precalculus 2.4 — Exponential Function Manipulation

**Quick recap:** Use exponent rules to rewrite exponential functions into equivalent forms:

$$
b^{u+v}=b^ub^v,\qquad
b^{u-v}=\frac{b^u}{b^v},\qquad
(b^u)^v=b^{uv}
$$

**Show your calculation before choosing A–D.**

---

## 1. Simplify a shifted exponent

Rewrite the following in the form $f(x)=ab^x$:

$$
f(x)=24\cdot2^{x-3}
$$

- **A.** $f(x)=21\cdot2^x$
- **B.** $f(x)=3\cdot2^x$
- **C.** $f(x)=8\cdot2^x$
- **D.** $f(x)=192\cdot2^x$

## 2. Find the multiplication factor per unit

Rewrite the following in the form $g(x)=ab^x$:

$$
g(x)=4\cdot3^{2x+1}
$$

- **A.** $g(x)=12\cdot6^x$
- **B.** $g(x)=4\cdot9^x$
- **C.** $g(x)=12\cdot9^x$
- **D.** $g(x)=7\cdot9^x$

## 3. Rewrite a negative exponent

Which expression is equivalent to:

$$
h(x)=5\cdot2^{-x}?
$$

- **A.** $\displaystyle 5\left(\frac12\right)^x$
- **B.** $\displaystyle -5\cdot2^x$
- **C.** $\displaystyle 5(-2)^x$
- **D.** $\displaystyle \frac52\cdot2^x$

## 4. Convert a growth interval into a yearly factor

A population follows the model:

$$
P(t)=200\cdot8^{t/3}
$$

Here, $t$ is measured in years. Which equivalent model shows the **multiplication factor per year**?

- **A.** $\displaystyle P(t)=200\left(\frac83\right)^t$
- **B.** $\displaystyle P(t)=200\cdot8^t$
- **C.** $\displaystyle P(t)=200\cdot3^t$
- **D.** $\displaystyle P(t)=200\cdot2^t$

## 5. Convert daily decay into a two-day percentage

A quantity is modeled by:

$$
Q(t)=500(0.8)^t
$$

Here, $t$ is measured in days. Rewrite the model using $t/2$ in the exponent and identify the **percentage decrease every two days**.

- **A.** $Q(t)=500(0.64)^{t/2}$; decrease of $64\%$
- **B.** $Q(t)=500(0.64)^{t/2}$; decrease of $36\%$
- **C.** $Q(t)=500(0.60)^{t/2}$; decrease of $40\%$
- **D.** $Q(t)=500(0.80)^{t/2}$; decrease of $20\%$

---

<details>
<summary><b>Answers</b></summary>

**1. B — Separate the subtraction in the exponent**

$$
24\cdot2^{x-3}
=\frac{24}{2^3}\cdot2^x
=\boxed{3\cdot2^x}
$$

**2. C — Separate the sum, then simplify the power**

$$
4\cdot3^{2x+1}
=4\cdot3\cdot(3^2)^x
=\boxed{12\cdot9^x}
$$

The initial value is $12$, and the multiplication factor per unit is $9$.

**3. A — A negative exponent gives a reciprocal**

$$
5\cdot2^{-x}
=5(2^{-1})^x
=\boxed{5\left(\frac12\right)^x}
$$

A negative exponent does **not** make the output negative.

**4. D — Take the cube root of the three-year factor**

$$
200\cdot8^{t/3}
=200\left(8^{1/3}\right)^t
=\boxed{200\cdot2^t}
$$

Multiplying by $8$ over three years means multiplying by $2$ each year, since $2^3=8$.

**5. B — Square the daily factor**

$$
500(0.8)^t
=500\left((0.8)^2\right)^{t/2}
=\boxed{500(0.64)^{t/2}}
$$

Every two days, $64\%$ remains. Therefore, the decrease is:

$$
\boxed{1-0.64=0.36=36\%}
$$

</details>
