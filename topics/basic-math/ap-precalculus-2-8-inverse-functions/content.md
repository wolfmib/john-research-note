---
title: "AP Precalculus 2.8 — Inverse Functions"
topic: basic-math
example: ap-precalculus-2-8-inverse-functions
course: AP Precalculus
unit: "2.8"
status: quiz
created: 2026-10-16
author: Wei-Che Hung
---

# AP Precalculus 2.8 — Inverse Functions

**Quick recap:**

- Reverse the pair:

$$
f(a)=b \iff f^{-1}(b)=a
$$

- To find $f^{-1}$: write $y=f(x)$, swap $x$ and $y$, solve for $y$.
- The domain of $f^{-1}$ is the range of $f$.
- The graph of $f^{-1}$ is the graph of $f$ reflected over $y=x$.
- $f^{-1}(x)$ is not $\dfrac{1}{f(x)}$.

**A calculator is allowed. Show your calculation before choosing A–D.**

---

## 1. Table · Read the inverse

The function $f$ is invertible.

$$
\begin{array}{c|ccccc}
x & 2 & 4 & 6 & 7 & 9\\
\hline
f(x) & 5 & 7 & 10 & 13 & 20
\end{array}
$$

Find $f^{-1}(7)$.

- **A.** $13$
- **B.** $4$
- **C.** $\dfrac{1}{13}$
- **D.** $\dfrac{1}{7}$

## 2. Formula · Find the inverse

Let

$$
f(x)=\frac{x+4}{3}
$$

Which function is $f^{-1}(x)$?

- **A.** $f^{-1}(x)=3x+4$
- **B.** $f^{-1}(x)=\dfrac{3}{x+4}$
- **C.** $f^{-1}(x)=\dfrac{x-4}{3}$
- **D.** $f^{-1}(x)=3x-4$

## 3. Restricted domain · Square root inverse

Let

$$
f(x)=x^2+3
$$

for $x\ge0$.

Which is $f^{-1}(x)$?

- **A.** $f^{-1}(x)=\sqrt{x-3}$, for $x\ge3$
- **B.** $f^{-1}(x)=-\sqrt{x-3}$, for $x\ge3$
- **C.** $f^{-1}(x)=\sqrt{x}-3$, for $x\ge0$
- **D.** $f^{-1}(x)=\sqrt{x+3}$, for $x\ge-3$

## 4. Taxi · Distance from the fare

A taxi ride of $m$ km costs

$$
C(m)=3.5+1.2m
$$

euros.

A ride costs €15.50.

Use the inverse function to find how far the taxi drove.

- **A.** $22.1$ km
- **B.** $12.9$ km
- **C.** $10$ km
- **D.** $15.8$ km

## 5. Graph · Point on the inverse

The point $(3,-1)$ is on the graph of an invertible function $f$.

Which point must be on the graph of $f^{-1}$?

- **A.** $(3,1)$
- **B.** $(-1,3)$
- **C.** $(-3,1)$
- **D.** $(1,-3)$

---

<details>
<summary><b>Answers</b></summary>

**1. B — Find 7 in the output row**

$$
\begin{aligned}
f(4) &= 7
\end{aligned}
$$

So the inverse sends $7$ back to $4$:

$$
\begin{aligned}
f^{-1}(7) &= \boxed{4}
\end{aligned}
$$

- Not $13$: that is $f(7)$. The inverse starts from an **output** of $f$.
- Not $\dfrac{1}{13}$ or $\dfrac{1}{7}$: the $-1$ in $f^{-1}$ means inverse function, not a reciprocal.

**2. D — Swap x and y, then solve for y**

$$
\begin{aligned}
y &= \frac{x+4}{3}
\end{aligned}
$$

Swap $x$ and $y$:

$$
\begin{aligned}
x &= \frac{y+4}{3}
\end{aligned}
$$

Multiply by $3$:

$$
\begin{aligned}
3x &= y+4
\end{aligned}
$$

Subtract $4$:

$$
\begin{aligned}
y &= 3x-4
\end{aligned}
$$

So

$$
\boxed{f^{-1}(x)=3x-4}
$$

Check with $x=5$:

$$
\begin{aligned}
f(5) &= 3 \\
f^{-1}(3) &= 3(3)-4 \\
&= 5
\end{aligned}
$$

- Not $3x+4$: undo the steps in reverse order. $f$ adds $4$ then divides by $3$, so $f^{-1}$ multiplies by $3$ then **subtracts** $4$.
- Not $\dfrac{3}{x+4}$: that is the reciprocal $\dfrac{1}{f(x)}$, not the inverse.

**3. A — Swap, solve, keep the + root**

For $x\ge0$ the outputs of $f$ are $y\ge3$.

Swap $x$ and $y$:

$$
\begin{aligned}
x &= y^2+3
\end{aligned}
$$

Subtract $3$:

$$
\begin{aligned}
y^2 &= x-3
\end{aligned}
$$

The outputs of $f^{-1}$ must be $\ge0$, so take the $+$ root:

$$
\begin{aligned}
y &= \sqrt{x-3}
\end{aligned}
$$

The domain of $f^{-1}$ is the range of $f$:

$$
\boxed{f^{-1}(x)=\sqrt{x-3},\ x\ge3}
$$

Check with $x=2$:

$$
\begin{aligned}
f(2) &= 7 \\
f^{-1}(7) &= \sqrt{4} \\
&= 2
\end{aligned}
$$

- Not $-\sqrt{x-3}$: its outputs are negative, but $f$ only used inputs $x\ge0$.
- Not $\sqrt{x}-3$: subtract the $3$ **before** the square root.

**4. C — The inverse turns a fare into kilometres**

$$
\begin{aligned}
C &= 3.5+1.2m \\
C-3.5 &= 1.2m \\
m &= \frac{C-3.5}{1.2}
\end{aligned}
$$

Put in $C=15.50$:

$$
\begin{aligned}
m &= \frac{15.5-3.5}{1.2} \\
&= \frac{12}{1.2} \\
&= \boxed{10\text{ km}}
\end{aligned}
$$

- Check: $3.5+1.2(10)=15.5$
- Not $22.1$: that is $C(15.5)$, the fare for $15.5$ km. The question runs backwards.
- Not $12.9$: $15.5\div1.2$ forgets to take off the €3.50 start fee first.

**5. B — Swap the coordinates**

$$
\begin{aligned}
f(3) &= -1
\end{aligned}
$$

So

$$
\begin{aligned}
f^{-1}(-1) &= 3
\end{aligned}
$$

The point on $f^{-1}$ is

$$
\boxed{(-1,\ 3)}
$$

- Swapping $x$ and $y$ reflects the point over the line $y=x$.
- Not $(3,1)$: that reflects over the $x$-axis.
- Not $(1,-3)$: that changes both signs as well as swapping them.

An inverse function runs the function backwards: it swaps inputs and outputs, so its graph is the reflection over y = x.

</details>
