---
title: "1.2 Rates of Change"
topic: animations
example: ap-precalc-1-2-rates-of-change
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-04
author: Wei-Che Hung
---

# 1.2 Rates of Change

![1.2 Rates of Change](media/ap-precalc-1-2-rates-of-change.svg)

## What happens

1. The formula is stated first: the average rate of change of $f$ over $[a, b]$ is $\dfrac{f(b) - f(a)}{b - a}$, the change in output divided by the change in input.
2. Two points on the graph of $f$ are plotted, $a = 2$ with $f(a) = 3$ and $b = 6$ with $f(b) = 9$, with dashed guides back to the axes.
3. The change is drawn as two legs: the horizontal run $\Delta x = b - a$ and the vertical rise $\Delta y = f(b) - f(a)$, so the rate is $\dfrac{\Delta y}{\Delta x}$, rise over run.
4. The real numbers of the two points go in: $\Delta y = 9 - 3 = 6$, $\Delta x = 6 - 2 = 4$, and the rate is $\dfrac{6}{4} = 1.5$.
5. The secant line through $(2, 3)$ and $(6, 9)$ is drawn; its slope is the average rate of change, $1.5$.

## Concept

$$
\text{average rate of change of } f \text{ over } [a, b]
= \frac{f(b) - f(a)}{b - a}
= \frac{\Delta y}{\Delta x}
= \frac{9 - 3}{6 - 2} = \frac{6}{4} = 1.5
$$

The average rate of change compares how much the output moves with how much the input moves between two points. Geometrically it is the slope of the secant line joining $(a, f(a))$ and $(b, f(b))$: the rise $\Delta y$ over the run $\Delta x$. A positive value means $f$ ends higher than it started on the interval, even if the curve bends in between; the secant records only the net change. The idea builds on [1.1 Change in Tandem](../ap-precalc-1-1-change-in-tandem/content.md): now the related change in $y$ is measured per unit change in $x$.

## Summary

The average rate of change of $f$ over $[a, b]$ is $\frac{f(b) - f(a)}{b - a}$ , the rise $\Delta y$ divided by the run $\Delta x$ , and it equals the slope of the secant line through the two points. For $(2, 3)$ and $(6, 9)$ the rate is $\frac{6}{4} = 1.5$ : $y$ rises $1.5$ units for each unit of $x$ .

### 繁體中文

函數 $f$ 在 $[a, b]$ 上的平均變化率是 $\frac{f(b) - f(a)}{b - a}$ ，也就是縱向變化 $\Delta y$ 除以橫向變化 $\Delta x$ ，它等於通過這兩點的割線斜率。對 $(2, 3)$ 與 $(6, 9)$ 而言，變化率是 $\frac{6}{4} = 1.5$ ： $x$ 每增加一個單位， $y$ 上升 $1.5$ 個單位。

### Français

Le taux de variation moyen de $f$ sur $[a, b]$ est $\frac{f(b) - f(a)}{b - a}$ , la variation verticale $\Delta y$ divisée par la variation horizontale $\Delta x$ , et il est égal à la pente de la sécante passant par les deux points. Pour $(2, 3)$ et $(6, 9)$ le taux vaut $\frac{6}{4} = 1.5$ : $y$ monte de $1.5$ unité pour chaque unité de $x$ .

### Deutsch

Die mittlere Änderungsrate von $f$ auf $[a, b]$ ist $\frac{f(b) - f(a)}{b - a}$ , der Anstieg $\Delta y$ geteilt durch die Strecke $\Delta x$ , und sie ist gleich der Steigung der Sekante durch die beiden Punkte. Für $(2, 3)$ und $(6, 9)$ beträgt die Rate $\frac{6}{4} = 1.5$ : $y$ steigt um $1.5$ Einheiten pro Einheit von $x$ .

### Русский

Средняя скорость изменения $f$ на $[a, b]$ равна $\frac{f(b) - f(a)}{b - a}$ , то есть приращению $\Delta y$ , делённому на приращение $\Delta x$ , и совпадает с угловым коэффициентом секущей через две точки. Для $(2, 3)$ и $(6, 9)$ скорость равна $\frac{6}{4} = 1.5$ : $y$ растёт на $1.5$ единицы на каждую единицу $x$ .
