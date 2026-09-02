---
title: "Design Matrix Rows [x, y, 1] with reshape and hstack"
topic: animations
example: numpy-design-matrix-reshape-hstack
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-02
author: Wei-Che Hung
---

# Design Matrix Rows [x, y, 1] with reshape and hstack

![Design Matrix Rows [x, y, 1] with reshape and hstack](media/numpy-design-matrix-reshape-hstack.svg)

## What happens

1. A function receives point coordinates and reshapes them with `reshape(-1, 2)`: exactly two columns $[x, y]$, and $-1$ lets NumPy infer the row count, here $8 / 2 = 4$ rows.
2. `np.ones((P.shape[0], 1))` builds a $4 \times 1$ column of ones, one per point: the intercept term of a linear model.
3. `np.hstack` glues the two blocks side by side, so the $(4, 2)$ block and the $(4, 1)$ column become one $(4, 3)$ matrix.
4. Every row of the result has the form $[x, y, 1]$: the design matrix $Z$ of an affine fit.

## Concept

$$
Z = [\,X \mid \mathbf 1_n\,] \in \mathbb R^{n \times 3}, \qquad z_p = [x_p,\ y_p,\ 1]
$$

An affine map $p \mapsto Lp + t$ is linear in its unknowns $(L, t)$, so with one row per point the fit is the linear model $Y = Z\beta + \varepsilon$. Whether the constant column comes first, $[1, x, y]$, or last, $[x, y, 1]$, is only a column permutation: the column space of $Z$, the fitted values and the leverage $z_p^{\top}(Z^{\top}Z)^{-1}z_p$ are unchanged. Related: [a (4, 2) marker array and its centroid](../numpy-marker-array-centroid-mean-axis0/content.md).

## Summary

`reshape(-1, 2)` fixes the point columns, `np.ones` adds the intercept column, and `np.hstack` joins them into the design matrix $Z$ whose rows are $[x, y, 1]$. The column order is a convention; the model the matrix represents is the same either way.

### 繁體中文

`reshape(-1, 2)` 固定點座標的兩個欄位， `np.ones` 加上截距欄， `np.hstack` 把它們接成設計矩陣 $Z$ ，其每一列的形式為 $[x, y, 1]$ 。欄位順序只是慣例；矩陣所代表的模型兩種寫法完全相同。

### Français

`reshape(-1, 2)` fixe les colonnes des points, `np.ones` ajoute la colonne d'ordonnée à l'origine, et `np.hstack` les assemble en la matrice de conception $Z$ dont les lignes sont $[x, y, 1]$ . L'ordre des colonnes est une convention ; le modèle représenté par la matrice est le même dans les deux cas.

### Deutsch

`reshape(-1, 2)` legt die Punktspalten fest, `np.ones` fügt die Achsenabschnittsspalte hinzu, und `np.hstack` verbindet sie zur Designmatrix $Z$ , deren Zeilen die Form $[x, y, 1]$ haben. Die Spaltenreihenfolge ist eine Konvention; das Modell, das die Matrix darstellt, ist in beiden Fällen dasselbe.

### Русский

`reshape(-1, 2)` фиксирует столбцы координат точек, `np.ones` добавляет столбец свободного члена, а `np.hstack` соединяет их в матрицу плана $Z$ , строки которой имеют вид $[x, y, 1]$ . Порядок столбцов — лишь соглашение; модель, которую представляет матрица, в обоих случаях одна и та же.
