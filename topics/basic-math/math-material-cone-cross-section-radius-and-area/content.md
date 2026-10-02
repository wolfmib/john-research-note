---
title: "Math Material — Cone Cross-Section: Radius and Area"
topic: basic-math
example: math-material-cone-cross-section-radius-and-area
course: Math Material
status: material
created: 2026-10-02
author: Wei-Che Hung
---

# Math Material — Cone Cross-Section: Radius and Area

A cone has a circular base with a fixed radius $R$. The angle between the cone's vertical axis and its sloping side is $30^\circ$.

A horizontal cut at distance $h$ below the apex makes a smaller circle with radius $x$.

![Cone with a 30° angle between the axis and the sloping side; a horizontal cut at distance h below the apex has radius x; the base has radius R](media/cone-cross-section.svg)

## 1. Radius of the smaller circle

Express the radius $x$ of the smaller circle as a function of $h$.

<details>
<summary><b>Working</b></summary>

The axis, the radius $x$ and the sloping side form a right triangle with a $30^\circ$ angle at the apex:

$$
\tan30^\circ=\frac{x}{h}
$$

$$
x(h)=h\tan30^\circ=\boxed{\frac{h}{\sqrt3}}
$$

</details>

## 2. Area of the smaller circle

Write the area of the smaller circle, $A_c(h)$, as a function of $h$.

<details>
<summary><b>Working</b></summary>

The smaller circle has radius $x(h)$:

$$
A_c=\pi x^2
$$

$$
A_c(h)=\pi\left(\frac{h}{\sqrt3}\right)^2=\boxed{\frac{\pi h^2}{3}}
$$

</details>

## 3. Domain in terms of R

Determine the domain of $A_c(h)$ in terms of the fixed base radius $R$.

<details>
<summary><b>Working</b></summary>

The smaller circle grows from a point at the apex to the base circle:

$$
0\le A_c(h)\le\pi R^2
$$

$$
0\le\frac{\pi h^2}{3}\le\pi R^2
$$

$$
0\le h^2\le3R^2
$$

Since $h\ge0$:

$$
\boxed{0\le h\le\sqrt3\,R}
$$

Check: at $h=\sqrt3\,R$, $x=\dfrac{\sqrt3\,R}{\sqrt3}=R$, the base circle.

</details>
