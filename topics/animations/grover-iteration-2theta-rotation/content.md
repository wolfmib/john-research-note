---
title: "Grover's iteration: the 2θ rotation"
topic: animations
example: grover-iteration-2theta-rotation
status: concept-note
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
