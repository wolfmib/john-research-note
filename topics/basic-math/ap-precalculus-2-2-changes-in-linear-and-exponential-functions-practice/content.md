---
title: "AP Precalculus 2.2 — Changes in Linear and Exponential Functions Practice"
topic: basic-math
example: ap-precalculus-2-2-changes-in-linear-and-exponential-functions-practice
course: AP Precalculus
unit: "2.2"
status: quiz
created: 2026-10-16
author: Wei-Che Hung
---

# AP Precalculus 2.2 — Changes in Linear and Exponential Functions Practice

**Quick recap:**

- Linear (constant difference):

$$
f(x)=b+mx
$$

- Linear through $(x_i,\ y_i)$:

$$
f(x)=y_i+m(x-x_i)
$$

- Exponential (constant ratio):

$$
f(x)=a\,b^{x}
$$

- Exponential through $(x_i,\ y_i)$:

$$
f(x)=y_i\,b^{(x-x_i)}
$$

- Arithmetic $a_n=a_0+dn$ becomes linear. Geometric $g_n=g_0r^n$ becomes exponential.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Table · Constant difference

$$
\begin{array}{c|cccc}
x & 0 & 1 & 2 & 3\\
\hline
y & 7 & 11 & 15 & 19
\end{array}
$$

Which function matches the table?

- **A.** $f(x)=7+4x$
- **B.** $f(x)=7\cdot4^{x}$
- **C.** $f(x)=4+7x$
- **D.** $f(x)=7(1.5)^{x}$

## 2. Table · Constant ratio

$$
\begin{array}{c|cccc}
x & 0 & 1 & 2 & 3\\
\hline
y & 2 & 6 & 18 & 54
\end{array}
$$

Which function matches the table?

- **A.** $f(x)=2+4x$
- **B.** $f(x)=3\cdot2^{x}$
- **C.** $f(x)=2\cdot3^{x}$
- **D.** $f(x)=2+3x$

## 3. Table · Halving each step

$$
\begin{array}{c|cccc}
x & 0 & 1 & 2 & 3\\
\hline
y & 80 & 40 & 20 & 10
\end{array}
$$

Which function matches the table?

- **A.** $f(x)=80-40x$
- **B.** $f(x)=80(0.5)^{x}$
- **C.** $f(x)=80\cdot2^{x}$
- **D.** $f(x)=80-20x$

## 4. Linear · Slope and a point

A linear function has slope $4$ and passes through the point $(2,\ 11)$.

Find $f(5)$.

- **A.** $20$
- **B.** $31$
- **C.** $15$
- **D.** $23$

## 5. Exponential · Ratio and a point

An exponential function passes through $(1,\ 6)$.

Its outputs triple for every increase of $1$ in $x$.

Find $f(3)$.

- **A.** $18$
- **B.** $162$
- **C.** $54$
- **D.** $12$

## 6. Sequence → function · Arithmetic

An arithmetic sequence is

$$
a_n=5+2n
$$

Which function extends it to all real inputs $x$?

- **A.** $f(x)=5\cdot2^{x}$
- **B.** $f(x)=5+2x$
- **C.** $f(x)=2+5x$
- **D.** $f(x)=2\cdot5^{x}$

## 7. Sequence → function · Allowed inputs

A geometric sequence is

$$
g_n=3\cdot2^{n}
$$

The matching exponential function is

$$
f(x)=3\cdot2^{x}
$$

Which input can $f$ use, but the sequence cannot?

- **A.** $0$
- **B.** $1$
- **C.** $4$
- **D.** $2.5$

## 8. Linear · Two points

A linear function has

$$
f(1)=5
$$

and

$$
f(4)=17
$$

Find $f(0)$.

- **A.** $1$
- **B.** $4$
- **C.** $5$
- **D.** $-7$

## 9. Exponential · Two points

An exponential function has

$$
g(0)=3
$$

and

$$
g(2)=27
$$

Its base is positive.

Find $g(1)$.

- **A.** $15$
- **B.** $13.5$
- **C.** $9$
- **D.** $12$

## 10. Context · Which change is exponential?

Which situation is modeled by an exponential function?

- **A.** A phone plan costs €20 more each year.
- **B.** A town's population grows by $5\%$ each year.
- **C.** A candle gets $3$ cm shorter each hour.
- **D.** A taxi fare adds €1.20 for each km.

---

<details>
<summary><b>Answers</b></summary>

**1. A — Equal steps in x add the same amount**

$$
\begin{aligned}
11-7 &= 4 \\
15-11 &= 4 \\
19-15 &= 4
\end{aligned}
$$

The difference is constant, so the function is linear with $b=7$ and $m=4$:

$$
\boxed{f(x)=7+4x}
$$

- Not $7\cdot4^x$: that multiplies by $4$ each step, giving $7,\ 28,\ 112$.
- Not $4+7x$: the start value is $f(0)=7$, so $7$ is $b$, not the slope.

**2. C — Equal steps in x multiply by the same number**

$$
\begin{aligned}
\frac{6}{2} &= 3 \\
\frac{18}{6} &= 3 \\
\frac{54}{18} &= 3
\end{aligned}
$$

The ratio is constant, so the function is exponential with $a=2$ and $b=3$:

$$
\boxed{f(x)=2\cdot3^{x}}
$$

- Not $2+4x$: it fits the first two points only ($2,\ 6$), then gives $10$, not $18$.
- Not $3\cdot2^x$: the start value $f(0)$ is $2$, and the ratio is $3$.

**3. B — Each output is half of the one before**

$$
\begin{aligned}
\frac{40}{80} &= 0.5 \\
\frac{20}{40} &= 0.5 \\
\frac{10}{20} &= 0.5
\end{aligned}
$$

The ratio is constant, so

$$
\boxed{f(x)=80(0.5)^{x}}
$$

- Not $80-40x$: it fits $80,\ 40$, then gives $0$ instead of $20$. Check every point, not two.
- Not $80\cdot2^x$: the outputs get smaller, so the ratio is below $1$.

**4. D — Use the point form**

$$
\begin{aligned}
f(x) &= y_i+m(x-x_i) \\
f(x) &= 11+4(x-2)
\end{aligned}
$$

Put in $x=5$:

$$
\begin{aligned}
f(5) &= 11+4(5-2) \\
&= 11+12 \\
&= \boxed{23}
\end{aligned}
$$

- From $x=2$ to $x=5$ is $3$ steps, and each step adds $4$.
- Not $31$: $11+4\cdot5$ forgets to subtract $x_i=2$.
- Not $15$: that adds only one step of $4$.

**5. C — Use the point form with ratio 3**

$$
\begin{aligned}
f(x) &= y_i\,b^{(x-x_i)} \\
f(x) &= 6\cdot3^{(x-1)}
\end{aligned}
$$

Put in $x=3$:

$$
\begin{aligned}
f(3) &= 6\cdot3^{2} \\
&= 6\cdot9 \\
&= \boxed{54}
\end{aligned}
$$

- From $x=1$ to $x=3$ is $2$ steps: $6\to18\to54$.
- Not $162$: $6\cdot3^3$ uses $x=3$ instead of $x-1=2$.
- Not $12$: $6+3\cdot2$ adds, but exponential change multiplies.

**6. B — Match the parts: a₀ → b, d → m, n → x**

Arithmetic matches linear:

$$
\begin{aligned}
a_n &= a_0+dn \\
f(x) &= b+mx
\end{aligned}
$$

With $a_0=5$ and $d=2$:

$$
\boxed{f(x)=5+2x}
$$

- Not $5\cdot2^x$: that is geometric (multiply by $2$). This sequence **adds** $2$.
- Not $2+5x$: the start value $5$ and the step $2$ are swapped.

**7. D — A sequence uses whole numbers only**

- The sequence has a 0th, 1st, 2nd … term: $n$ is a whole number.
- The function accepts every real $x$.

So the input is

$$
\boxed{2.5}
$$

$$
\begin{aligned}
f(2.5) &= 3\cdot2^{2.5} \\
&\approx 16.97
\end{aligned}
$$

- Not $0$, $1$ or $4$: both the sequence and the function can use these.

**8. A — Slope first, then step back to x = 0**

$$
\begin{aligned}
m &= \frac{17-5}{4-1} \\
&= \frac{12}{3} \\
&= 4
\end{aligned}
$$

One step back from $x=1$ takes away $4$:

$$
\begin{aligned}
f(0) &= 5-4 \\
&= \boxed{1}
\end{aligned}
$$

- Not $4$: that is the slope $m$, not a value of $f$.
- Not $-7$: $5-12$ steps back the whole change $12$. One step of $x$ changes $f$ by $4$ only.

**9. C — Two steps multiply by b twice**

$$
\begin{aligned}
3\,b^2 &= 27 \\
b^2 &= 9 \\
b &= 3
\end{aligned}
$$

$$
\begin{aligned}
g(1) &= 3\cdot3 \\
&= \boxed{9}
\end{aligned}
$$

- Check: $3\to9\to27$, multiplying by $3$ each step.
- Not $15$: $\frac{3+27}{2}$ is the middle of a **linear** function. Exponential change multiplies, so the middle value is $9$.

**10. B — Equal steps multiply by the same factor**

- A $5\%$ increase multiplies the population by the same factor each year:

$$
\begin{aligned}
b &= 1+0.05 \\
&= 1.05
\end{aligned}
$$

$$
\boxed{\text{the population, } P(t)=P_0(1.05)^t}
$$

- The other three **add** (or take away) the same amount each step, so they are linear.

Linear functions add the same amount over equal steps; exponential functions multiply by the same factor.

</details>
