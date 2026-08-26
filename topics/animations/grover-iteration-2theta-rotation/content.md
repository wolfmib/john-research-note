---
title: "Grover's iteration: the 2θ rotation"
topic: animations
example: grover-iteration-2theta-rotation
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-08-26
author: Wei-Che Hung
---

# Grover's iteration: the 2θ rotation

![The state vector starts at angle theta above the bad axis, the oracle reflects it across the bad axis to minus theta, the diffusion step reflects it across the initial line, and the net result is a rotation by two theta toward the good axis](media/grover-iteration-2theta-rotation.svg)

## What happens

Only two directions matter: $|\text{bad}\rangle$ (the unmarked states, x-axis) and
$|\text{good}\rangle$ (the marked states, y-axis).

1. **Initial state.** $|\psi\rangle$ sits at a small angle $\theta$ above $|\text{bad}\rangle$.
2. **Oracle.** A sign flip on the marked component is a reflection across $|\text{bad}\rangle$: $\theta \rightarrow -\theta$.
3. **Diffusion.** Inversion about the mean is a reflection across the initial line $|\psi\rangle$: $-\theta \rightarrow 3\theta$.

Two reflections make one rotation by $2\theta$ toward $|\text{good}\rangle$.

## Concept

With $M$ marked items among $N$,

$$
\sin\theta = \sqrt{\frac{M}{N}}, \qquad
|\psi\rangle = \cos\theta\,|\text{bad}\rangle + \sin\theta\,|\text{good}\rangle .
$$

Each iteration $G = D\,O$ adds $2\theta$:

$$
G^{k}|\psi\rangle = \cos\big((2k+1)\theta\big)\,|\text{bad}\rangle + \sin\big((2k+1)\theta\big)\,|\text{good}\rangle ,
$$

so the success probability $\sin^{2}\big((2k+1)\theta\big)$ peaks at $(2k+1)\theta \approx \pi/2$, i.e.

$$
k \approx \frac{\pi}{4}\sqrt{\frac{N}{M}} .
$$

Going past $\pi/2$ lowers the probability again, which is why $k$ is fixed in advance. The
[subset-sum example](../../quantum-computing/grover-search-for-subset-sum/content.md)
uses this rule with $N=64$, $M=1$, six iterations.

## Summary

One Grover iteration is two reflections in the bad–good plane, and two reflections compose
into a single rotation by $2\theta$ toward the marked subspace. Repeating it about
$\tfrac{\pi}{4}\sqrt{N/M}$ times brings the state to $|\text{good}\rangle$ — that is the quadratic speedup.

### 繁體中文

一次 Grover 迭代就是在 bad–good 平面上的兩次鏡射，而兩次鏡射合成為一次朝向標記子空間、角度為 $2\theta$ 的旋轉。重複約 $\tfrac{\pi}{4}\sqrt{N/M}$ 次，狀態便到達 $|\text{good}\rangle$——這就是平方加速的由來。

### Français

Une itération de Grover est constituée de deux réflexions dans le plan bad–good, et deux réflexions se composent en une seule rotation de $2\theta$ vers le sous-espace marqué. En la répétant environ $\tfrac{\pi}{4}\sqrt{N/M}$ fois, l'état atteint $|\text{good}\rangle$ — c'est l'accélération quadratique.

### Deutsch

Eine Grover-Iteration besteht aus zwei Spiegelungen in der bad–good-Ebene, und zwei Spiegelungen ergeben zusammen eine einzige Drehung um $2\theta$ zum markierten Unterraum hin. Etwa $\tfrac{\pi}{4}\sqrt{N/M}$ Wiederholungen bringen den Zustand nach $|\text{good}\rangle$ — das ist die quadratische Beschleunigung.

### Русский

Одна итерация Гровера — это два отражения в плоскости bad–good, а два отражения складываются в один поворот на $2\theta$ к отмеченному подпространству. Примерно $\tfrac{\pi}{4}\sqrt{N/M}$ повторений приводят состояние в $|\text{good}\rangle$ — в этом и состоит квадратичное ускорение.
