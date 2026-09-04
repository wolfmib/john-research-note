---
title: "Graphing a Rational Function — Zeros, Intercept, Asymptotes"
topic: animations
example: rational-function-graph-zeros-intercept-asymptotes
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-04
author: Wei-Che Hung
---

# Graphing a Rational Function — Zeros, Intercept, Asymptotes

![Graphing a Rational Function — Zeros, Intercept, Asymptotes](media/rational-function-graph-zeros-intercept-asymptotes.svg)

## What happens

1. The function $f(x) = \dfrac{(x-2)(x+1)}{x-3}$ is written in factored form.
2. Setting the numerator to zero gives the zeros $x = 2$ and $x = -1$; the points $(2, 0)$ and $(-1, 0)$ are marked on the axes.
3. Evaluating $f(0) = \dfrac{(-2)(1)}{-3} = \dfrac{2}{3}$ gives the y-intercept; the third point $(0, \tfrac{2}{3})$ is marked.
4. Dividing the numerator by the denominator rewrites $f(x) = (x+2) + \dfrac{4}{x-3}$; as $x \to \pm\infty$ the remainder term vanishes, so the line $y = x + 2$ is the slant asymptote (green dashed).
5. The denominator vanishes at $x = 3$ and nothing cancels it, so $x = 3$ is a vertical asymptote (red dashed).
6. The curve is drawn through the three points: it hugs $y = x + 2$ far from the origin and blows up on either side of $x = 3$.

## Concept

$$
f(x) = \frac{(x-2)(x+1)}{x-3} = (x+2) + \frac{4}{x-3},
\qquad
\lim_{x \to \pm\infty} \bigl[ f(x) - (x+2) \bigr] = 0
$$

When the numerator degree exceeds the denominator degree by exactly one, polynomial division splits $f$ into a linear quotient and a proper remainder. The quotient $x + 2$ is the slant asymptote because the remainder $\frac{4}{x-3}$ tends to $0$; its sign says which side the curve lies on: below the line for $x < 3$, above it for $x > 3$. A zero of the numerator that does not cancel is an x-intercept; a zero of the denominator that does not cancel is a vertical asymptote (a factor that cancels leaves a hole instead, see [Removable Discontinuity](../removable-discontinuity-hole-rational-function/content.md)). The turning points $(1, 1)$ and $(5, 9)$ follow from $f'(x) = 1 - \frac{4}{(x-3)^2} = 0$.

## Summary

Three points and two asymptotes fix the graph of a rational function: the zeros of the numerator, the value $f(0)$ , the quotient of the polynomial division as the slant asymptote, and the uncancelled zero of the denominator as the vertical asymptote. For $f(x) = \frac{(x-2)(x+1)}{x-3}$ these are $(-1, 0)$ , $(2, 0)$ , $(0, \tfrac{2}{3})$ , $y = x + 2$ and $x = 3$ .

### 繁體中文

三個點與兩條漸近線就決定了有理函數的圖形：分子的零點、函數值 $f(0)$ 、多項式除法的商作為斜漸近線，以及分母未被約去的零點作為垂直漸近線。對 $f(x) = \frac{(x-2)(x+1)}{x-3}$ 而言，它們分別是 $(-1, 0)$ 、 $(2, 0)$ 、 $(0, \tfrac{2}{3})$ 、 $y = x + 2$ 與 $x = 3$ 。

### Français

Trois points et deux asymptotes fixent le graphe d'une fonction rationnelle : les zéros du numérateur, la valeur $f(0)$ , le quotient de la division polynomiale comme asymptote oblique, et le zéro non simplifié du dénominateur comme asymptote verticale. Pour $f(x) = \frac{(x-2)(x+1)}{x-3}$ ce sont $(-1, 0)$ , $(2, 0)$ , $(0, \tfrac{2}{3})$ , $y = x + 2$ et $x = 3$ .

### Deutsch

Drei Punkte und zwei Asymptoten legen den Graphen einer rationalen Funktion fest: die Nullstellen des Zählers, der Wert $f(0)$ , der Quotient der Polynomdivision als schräge Asymptote und die nicht gekürzte Nullstelle des Nenners als vertikale Asymptote. Für $f(x) = \frac{(x-2)(x+1)}{x-3}$ sind das $(-1, 0)$ , $(2, 0)$ , $(0, \tfrac{2}{3})$ , $y = x + 2$ und $x = 3$ .

### Русский

Три точки и две асимптоты задают график рациональной функции: нули числителя, значение $f(0)$ , частное от деления многочленов как наклонная асимптота и несократившийся нуль знаменателя как вертикальная асимптота. Для $f(x) = \frac{(x-2)(x+1)}{x-3}$ это $(-1, 0)$ , $(2, 0)$ , $(0, \tfrac{2}{3})$ , $y = x + 2$ и $x = 3$ .
