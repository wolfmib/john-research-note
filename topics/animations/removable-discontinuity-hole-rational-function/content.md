---
title: "Removable Discontinuity — The Hole in a Rational Function"
topic: animations
example: removable-discontinuity-hole-rational-function
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-08-28
author: Wei-Che Hung
---

# Removable Discontinuity — The Hole in a Rational Function

![Removable Discontinuity — The Hole in a Rational Function](media/removable-discontinuity-hole-rational-function.svg)

## What happens

1. The rational function $f(x) = \dfrac{(x-4)(x+2)}{(x-4)(x-1)}$ is written in factored form; the goal is to find where it has a hole and where it has a vertical asymptote.
2. The common factor $(x-4)$ is struck out: $f(x) = \dfrac{x+2}{x-1}$ with the restriction $x \neq 4$, because the original expression is undefined there.
3. The denominator $x-1$ vanishes at $x = 1$ and nothing cancels it, so $x = 1$ is a vertical asymptote; equal degrees give the horizontal asymptote $y = 1$.
4. The limit $\lim_{x\to 4} \dfrac{x+2}{x-1} = \dfrac{6}{3} = 2$ gives the height of the hole; the curve is drawn with an open circle at $(4, 2)$.

## Concept

$$
f(x) = \frac{(x-4)(x+2)}{(x-4)(x-1)}
= \frac{x+2}{x-1}, \quad x \neq 4,
\qquad
\lim_{x \to 4} f(x) = \frac{4+2}{4-1} = 2
$$

A zero of the denominator produces one of two things. If the factor also divides the numerator, it cancels and the limit exists; the graph is the simplified curve with a single point missing — a **removable discontinuity**, or hole, here at $(4, 2)$. If the factor does not cancel, as with $x - 1$, the function grows without bound on both sides and the line $x = 1$ is a vertical asymptote. Cancelling does not enlarge the domain: $f(4)$ stays undefined, only $\lim_{x \to 4} f(x)$ is defined.

## Summary

A common factor of numerator and denominator cancels algebraically but leaves a hole in the graph at the value it removes; a factor that survives in the denominator is a vertical asymptote. The limit of the simplified function gives the height of the hole, here $(4, 2)$ for $f(x) = \frac{(x-4)(x+2)}{(x-4)(x-1)}$ .

### 繁體中文

分子與分母的公因式在代數上可以約掉，但會在圖形上留下一個洞，位置就在被約去的那個 $x$ 值；留在分母裡的因式則是垂直漸近線。化簡後函數的極限給出洞的高度，此處 $f(x) = \frac{(x-4)(x+2)}{(x-4)(x-1)}$ 的洞在 $(4, 2)$ 。

### Français

Un facteur commun au numérateur et au dénominateur se simplifie algébriquement mais laisse un trou dans le graphe à la valeur qu'il supprime ; un facteur qui subsiste au dénominateur est une asymptote verticale. La limite de la fonction simplifiée donne la hauteur du trou, ici $(4, 2)$ pour $f(x) = \frac{(x-4)(x+2)}{(x-4)(x-1)}$ .

### Deutsch

Ein gemeinsamer Faktor von Zähler und Nenner kürzt sich algebraisch, hinterlässt aber im Graphen ein Loch an der Stelle, die er entfernt; ein Faktor, der im Nenner bleibt, ist eine vertikale Asymptote. Der Grenzwert der gekürzten Funktion liefert die Höhe des Lochs, hier $(4, 2)$ für $f(x) = \frac{(x-4)(x+2)}{(x-4)(x-1)}$ .

### Русский

Общий множитель числителя и знаменателя сокращается алгебраически, но оставляет на графике дыру в той точке, которую он убирает; множитель, остающийся в знаменателе, даёт вертикальную асимптоту. Предел упрощённой функции задаёт высоту дыры, здесь $(4, 2)$ для $f(x) = \frac{(x-4)(x+2)}{(x-4)(x-1)}$ .
