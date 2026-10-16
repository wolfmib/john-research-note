---
title: "Explicit vs Implicit Euler: A Falling Ball"
topic: thermal-dynamics
example: explicit-vs-implicit-euler
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-10-16
author: Wei-Che Hung
---

# Explicit vs Implicit Euler: A Falling Ball

![Explicit vs Implicit Euler: A Falling Ball](media/explicit-vs-implicit-euler.gif)

## What happens

1. A ball falls from $100\ \mathrm{m}$ with gravity $g = 9.81\ \mathrm{m/s^2}$ and air resistance $\beta = 0.1\ \mathrm{s^{-1}}$ . The exact solution of the model is the reference.
2. Explicit Euler is derived: the derivative is evaluated with the known values at step $n$ , so each step is a direct computation.
3. The explicit step is worked by hand for $n = 0 \to 1$ and $n = 1 \to 2$ with $\Delta t = 0.8\ \mathrm{s}$ : the state $t^n, v^n, y^n$ goes into the formula, the result comes out and becomes the next state, and the ball jumps to the new height next to the exact ball.
4. Explicit Euler in action: the ball jumps once per step, a table fills with every value, and the explicit ball stays above the exact height.
5. Implicit Euler is derived: the derivative is evaluated with the unknown values at step $n+1$ , so each step is an equation for the new value, solved here by hand.
6. The implicit step is worked by hand the same way. The new velocity is solved first, then it moves the ball for the whole step.
7. Implicit Euler in action: the implicit ball stays below the exact height.
8. All three curves are drawn together at $\Delta t = 0.8\ \mathrm{s}$ , then $\Delta t$ shrinks to $0.1$ , $0.05$ and $0.01\ \mathrm{s}$ and both curves move onto the exact one.
9. A table gives the height error at $t = 4\ \mathrm{s}$ for each $\Delta t$ .

## Concept

The model is a first-order system for velocity and height:

```math
\frac{dv}{dt} = -g - \beta v, \qquad \frac{dy}{dt} = v, \qquad y(0) = 100\ \mathrm{m},\ v(0) = 0
```

with the exact solution

```math
v(t) = -\frac{g}{\beta}\left(1 - e^{-\beta t}\right), \qquad
y(t) = 100 - \frac{g}{\beta}\left[t - \frac{1 - e^{-\beta t}}{\beta}\right]
```

so that $y(4) = 31.016\ \mathrm{m}$ .

**Explicit Euler** evaluates the right-hand side at the known step $n$ :

```math
v^{n+1} = v^n - \Delta t\,(g + \beta v^n), \qquad y^{n+1} = y^n + \Delta t\, v^n
```

**Implicit Euler** evaluates it at the unknown step $n+1$ and solves for the new value:

```math
v^{n+1} = \frac{v^n - g\,\Delta t}{1 + \beta\,\Delta t}, \qquad y^{n+1} = y^n + \Delta t\, v^{n+1}
```

With $\Delta t = 0.8\ \mathrm{s}$ the first two steps by hand are

| $n$ | $t^n$ (s) | explicit $v^n$ | explicit $y^n$ | implicit $v^n$ | implicit $y^n$ | exact $y(t^n)$ |
|---|---|---|---|---|---|---|
| 0 | 0.0 | 0.000 | 100.000 | 0.000 | 100.000 | 100.000 |
| 1 | 0.8 | −7.848 | 100.000 | −7.267 | 94.187 | 96.943 |
| 2 | 1.6 | −15.068 | 93.722 | −13.995 | 82.991 | 88.087 |

The ball speeds up while it falls. The explicit step applies the older, slower velocity to the whole step and moves the ball too little, so it stays above the exact height. The implicit step applies the newer, faster velocity and moves the ball too much, so it stays below. Both errors shrink with the time step:

| $\Delta t$ (s) | steps to 4 s | explicit $y(4)$ | explicit error | implicit $y(4)$ | implicit error |
|---|---|---|---|---|---|
| 0.80 | 5 | 42.0410 | 11.0250 | 20.9479 | 10.0682 |
| 0.10 | 40 | 32.3387 | 1.3227 | 29.7083 | 1.3078 |
| 0.05 | 80 | 31.6755 | 0.6595 | 30.3603 | 0.6557 |
| 0.01 | 400 | 31.1476 | 0.1316 | 30.8846 | 0.1314 |

For this scalar model the implicit step is solved by hand. For a large system such as the heat equation on a tissue block, the same idea gives a linear system at every step. That is the time stepping used in [Pennes Skin Cancer Simulator Model](../pennes-skin-cancer-simulator-model/content.md) for the equation explained in [Pennes Bioheat Equation: Four Terms, One Unit](../pennes-bioheat-equation/content.md).

## Summary

Explicit Euler uses the known state to take a step and lands above the exact height; implicit Euler solves for the new state and lands below. Both converge to the exact solution as $\Delta t$ shrinks, and the time step sets the accuracy.

### 繁體中文

顯式 Euler 用已知的狀態前進一步，落在精確高度之上；隱式 Euler 先解出新的狀態，落在精確高度之下。當 $\Delta t$ 縮小時，兩者都收斂到精確解，時間步長決定精度。

### Français

Le schéma d'Euler explicite avance avec l'état connu et reste au-dessus de la hauteur exacte ; le schéma implicite résout d'abord le nouvel état et reste en dessous. Les deux convergent vers la solution exacte quand $\Delta t$ diminue, et le pas de temps fixe la précision.

### Deutsch

Das explizite Euler-Verfahren macht den Schritt mit dem bekannten Zustand und bleibt über der exakten Höhe; das implizite Verfahren löst zuerst nach dem neuen Zustand und bleibt darunter. Beide konvergieren gegen die exakte Lösung, wenn $\Delta t$ kleiner wird, und die Schrittweite bestimmt die Genauigkeit.

### Русский

Явный метод Эйлера делает шаг по известному состоянию и остаётся выше точной высоты; неявный метод сначала решает уравнение для нового состояния и остаётся ниже. Оба сходятся к точному решению при уменьшении $\Delta t$ , и шаг по времени задаёт точность.
