---
title: "NumPy to Geometry — A (4, 2) Marker Array and Its Centroid"
topic: animations
example: numpy-marker-array-centroid-mean-axis0
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-02
author: Wei-Che Hung
---

# NumPy to Geometry — A (4, 2) Marker Array and Its Centroid

![NumPy to Geometry — A (4, 2) Marker Array and Its Centroid](media/numpy-marker-array-centroid-mean-axis0.svg)

## What happens

1. Four marker positions are written as a NumPy array with one row per marker and two columns, so the array has shape $(4, 2)$.
2. Each row is placed in the image plane $D = [0, 640) \times [0, 480)$, with $y$ increasing downward as in image coordinates.
3. `markers.mean(axis=0)` collapses the four rows and averages each column on its own: the $x$ column gives $270$ and the $y$ column gives $255$.
4. The centroid $c_M = (270, 255)$ appears at the averaged position, joined to every marker, inside the hull that the markers span.

## Concept

$$
c_M = \frac{1}{4}\sum_{i=1}^{4} m_i, \qquad m_i = (x_i, y_i)
$$

`axis=0` means "reduce along the row index": one value survives per column, so the $(4, 2)$ array becomes a $(2,)$ vector. Averaging the columns separately is exactly the mean of the position vectors, which is why the one-line call and the formula agree. The centroid of a finite point set always lies inside the convex hull of the points, so it is a safe centre for scaling or rotating the layout. Related: [design matrix rows [x, y, 1]](../numpy-design-matrix-reshape-hstack/content.md).

## Summary

The mean over `axis=0` of a $(4, 2)$ point array is the centroid $c_M = (270, 255)$ : each coordinate column is averaged on its own, which equals the mean of the position vectors. Reading the axis argument geometrically turns a NumPy call into a statement about the point cloud.

### 繁體中文

對一個 $(4, 2)$ 的點座標陣列沿 `axis=0` 取平均，得到的就是形心 $c_M = (270, 255)$ ：每一個座標欄各自取平均，等同於位置向量的平均。把 axis 參數用幾何方式來讀，一行 NumPy 呼叫就變成對點雲的敘述。

### Français

La moyenne selon `axis=0` d'un tableau de points $(4, 2)$ est le centroïde $c_M = (270, 255)$ : chaque colonne de coordonnées est moyennée séparément, ce qui revient à la moyenne des vecteurs position. Lire l'argument axis de façon géométrique transforme un appel NumPy en un énoncé sur le nuage de points.

### Deutsch

Der Mittelwert über `axis=0` eines $(4, 2)$ Punktarrays ist der Schwerpunkt $c_M = (270, 255)$ : jede Koordinatenspalte wird für sich gemittelt, was dem Mittel der Ortsvektoren entspricht. Wer das axis-Argument geometrisch liest, macht aus einem NumPy-Aufruf eine Aussage über die Punktwolke.

### Русский

Среднее по `axis=0` массива точек $(4, 2)$ — это центроид $c_M = (270, 255)$ : каждый столбец координат усредняется отдельно, что совпадает со средним векторов положения. Геометрическое прочтение аргумента axis превращает вызов NumPy в утверждение об облаке точек.
