---
title: "PCA Parameter-Difference Features"
topic: thermal-dynamics
example: pca-parameter-difference-features
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-30
author: Wei-Che Hung
---

# PCA Parameter-Difference Features

![PCA Parameter-Difference Features](media/therma-methods-pca-parameter-difference-features.gif)

## Research question

A thermal recovery video holds one temperature curve per pixel, sampled over many frames. A classifier needs a short, fixed-length description of each case. The question is how two regions of fitted curves, a lesion and the normal skin around it, become three numbers per case.

The construction has six steps, one per scene of the animation:

```text
pixel curves -> five fitted parameters per pixel -> one mean vector per region
             -> one difference vector per case -> PCA over the training cases
             -> three projected values per case -> SVM
```

The method is general: it needs only fitted curves from two regions. It is applied here to active-thermography skin-cancer video, following SG24 (Soto & Godoy 2024), where the three values are named $PCA_{\Delta\theta 1}$ , $PCA_{\Delta\theta 2}$ , $PCA_{\Delta\theta 3}$ .

## Notation

| Symbol | Meaning |
|---|---|
| $L$ , $N$ | set of lesion pixels, set of normal-skin pixels, with $n_L$ and $n_N$ pixels |
| $T_i(t_s)$ | measured temperature of pixel $i$ at sample time $t_s$ , $s = 1, \dots, S$ |
| $f_i(t)$ | fitted model curve of pixel $i$ |
| $\boldsymbol{\theta}_i \in \mathbb{R}^5$ | the five fitted parameters of pixel $i$ ; $\theta_{i,k}$ is parameter $k$ |
| $\bar{\boldsymbol{\theta}}_L$ , $\bar{\boldsymbol{\theta}}_N$ | mean parameter vector of the lesion region, of the normal-skin region |
| $\Delta\boldsymbol{\theta} \in \mathbb{R}^5$ | absolute difference of the two mean vectors, one per case |
| $m$ | number of training cases; $r = 1, \dots, m$ indexes a case |
| $\mathbf{w}_j \in \mathbb{R}^5$ | principal direction $j$ , an eigenvector of the training covariance |
| $z_j$ | projected value of a case on $\mathbf{w}_j$ |

## Step 1 — Pixel-wise model fitting

Each pixel is treated as its own measurement. Its recovery curve is a sequence of temperatures, and the sequence is replaced by a smooth model with five free parameters, a constant plus two exponential terms:

```math
f_i(t) = \theta_{i,1} + \theta_{i,2}\,e^{\theta_{i,3}t} + \theta_{i,4}\,e^{\theta_{i,5}t}
```

The parameters have distinct roles. $\theta_{i,1}$ is a constant level. $\theta_{i,2}$ and $\theta_{i,4}$ are the amplitudes of the two exponential terms, and $\theta_{i,3}$ and $\theta_{i,5}$ are the two rates. When both rates are negative the two terms decay and the curve settles at $\theta_{i,1}$ . The fitted starting temperature is the model at $t = 0$ :

```math
f_i(0) = \theta_{i,1} + \theta_{i,2} + \theta_{i,4}
```

The five parameters are found by nonlinear least squares, the parameter set that leaves the smallest squared gap between the model and the measured samples:

```math
\boldsymbol{\theta}_i = \arg\min_{\boldsymbol{\theta}} \sum_{s=1}^{S} \bigl( T_i(t_s) - f(t_s;\boldsymbol{\theta}) \bigr)^2
```

After this step a curve of $S$ samples is described by five numbers, and every pixel carries its own vector

```math
\boldsymbol{\theta}_i = [\theta_{i,1},\ \theta_{i,2},\ \theta_{i,3},\ \theta_{i,4},\ \theta_{i,5}]
```

## Step 2 — Parameter-wise averaging

The fitted vectors of one region are stacked as a matrix, one row per pixel and one column per parameter:

```math
\boldsymbol{\Theta}_L =
\begin{bmatrix}
\theta_{1,1} & \theta_{1,2} & \theta_{1,3} & \theta_{1,4} & \theta_{1,5} \\
\theta_{2,1} & \theta_{2,2} & \theta_{2,3} & \theta_{2,4} & \theta_{2,5} \\
\vdots & \vdots & \vdots & \vdots & \vdots \\
\theta_{n_L,1} & \theta_{n_L,2} & \theta_{n_L,3} & \theta_{n_L,4} & \theta_{n_L,5}
\end{bmatrix}
\in \mathbb{R}^{n_L \times 5}
```

Each column is averaged over the pixels. The average runs down a column, so a level is averaged with levels and a rate with rates; parameters of different kinds are never mixed:

```math
\bar{\theta}_{L,k} = \frac{1}{n_L}\sum_{i \in L}\theta_{i,k},
\qquad k = 1, \dots, 5,
\qquad
\bar{\boldsymbol{\theta}}_L = [\bar{\theta}_{L,1},\ \bar{\theta}_{L,2},\ \bar{\theta}_{L,3},\ \bar{\theta}_{L,4},\ \bar{\theta}_{L,5}]
```

The same two steps on the normal-skin pixels give the second mean vector:

```math
\bar{\theta}_{N,k} = \frac{1}{n_N}\sum_{i \in N}\theta_{i,k},
\qquad
\bar{\boldsymbol{\theta}}_N = [\bar{\theta}_{N,1},\ \dots,\ \bar{\theta}_{N,5}]
```

The result is one mean parameter vector per region. The number of pixels in a region no longer appears, so a large lesion and a small lesion are described by vectors of the same length.

## Step 3 — Regional difference

The two regions of one case are compared parameter by parameter. The absolute difference is taken element-wise:

```math
\Delta\boldsymbol{\theta} = \left|\,\bar{\boldsymbol{\theta}}_L - \bar{\boldsymbol{\theta}}_N\,\right|,
\qquad
\Delta\theta_k = \left|\,\bar{\theta}_{L,k} - \bar{\theta}_{N,k}\,\right|,
\qquad
\Delta\boldsymbol{\theta} \in \mathbb{R}^5
```

Two properties follow from the form of this equation. The comparison is made inside one case, lesion against the skin of the same subject, so a level shared by both regions cancels. The absolute value keeps the size of each difference and drops its sign, so the vector records how far the regions differ in each parameter and not which region is larger.

Each case is now one point in a five-dimensional space.

## Step 4 — PCA over the training set

The five differences of a case are not independent of each other: the parameters come from one model fitted to one kind of curve, so they tend to change together. PCA finds the directions along which the training cases vary most, and orders them.

The difference vectors of the $m$ training cases are stacked, one row per case:

```math
\mathbf{D} =
\begin{bmatrix}
\Delta\theta_{1,1} & \Delta\theta_{1,2} & \cdots & \Delta\theta_{1,5} \\
\Delta\theta_{2,1} & \Delta\theta_{2,2} & \cdots & \Delta\theta_{2,5} \\
\vdots & \vdots & \ddots & \vdots \\
\Delta\theta_{m,1} & \Delta\theta_{m,2} & \cdots & \Delta\theta_{m,5}
\end{bmatrix}
\in \mathbb{R}^{m \times 5}
```

The spread of the rows around their mean is summarised by the covariance matrix, a $5 \times 5$ table of how each pair of parameters varies together:

```math
\overline{\Delta\boldsymbol{\theta}} = \frac{1}{m}\sum_{r=1}^{m}\Delta\boldsymbol{\theta}_r,
\qquad
\mathbf{C} = \frac{1}{m-1}\sum_{r=1}^{m}
\bigl(\Delta\boldsymbol{\theta}_r - \overline{\Delta\boldsymbol{\theta}}\bigr)
\bigl(\Delta\boldsymbol{\theta}_r - \overline{\Delta\boldsymbol{\theta}}\bigr)^{\mathsf T}
```

The principal directions are the eigenvectors of this matrix, and each eigenvalue is the variance of the training cases along its direction:

```math
\mathbf{C}\,\mathbf{w}_j = \lambda_j\,\mathbf{w}_j,
\qquad
\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_5 \ge 0,
\qquad
\mathbf{w}_j^{\mathsf T}\mathbf{w}_l =
\begin{cases} 1 & j = l \\ 0 & j \ne l \end{cases}
```

PC1, PC2 and PC3 are the three leading eigenvectors $\mathbf{w}_1, \mathbf{w}_2, \mathbf{w}_3$ . Each one is a direction in the five-parameter space, a list of five weights. The share of the training variance that the three directions keep is

```math
\frac{\lambda_1 + \lambda_2 + \lambda_3}{\lambda_1 + \lambda_2 + \lambda_3 + \lambda_4 + \lambda_5}
```

The directions are learned from the training cases only. They are then fixed, and every later case is measured against the same three directions.

## Step 5 — Projection onto each eigenvector

A direction becomes a number by projection. The eigenvector is written as a row, the data vector as a column, and the product of a row of five elements with a column of five elements is one value:

```math
z_1 = \mathbf{w}_1^{\mathsf T}\,\Delta\boldsymbol{\theta}
= w_{1,1}\,\Delta\theta_1 + w_{1,2}\,\Delta\theta_2 + w_{1,3}\,\Delta\theta_3 + w_{1,4}\,\Delta\theta_4 + w_{1,5}\,\Delta\theta_5
```

The same data column is used against each eigenvector in turn, so PC1 gives $z_1$ , PC2 gives $z_2$ and PC3 gives $z_3$ . Stacking the three rows writes the three products as one matrix product:

```math
\begin{bmatrix} z_1 \\ z_2 \\ z_3 \end{bmatrix}
=
\begin{bmatrix}
w_{1,1} & w_{1,2} & w_{1,3} & w_{1,4} & w_{1,5} \\
w_{2,1} & w_{2,2} & w_{2,3} & w_{2,4} & w_{2,5} \\
w_{3,1} & w_{3,2} & w_{3,3} & w_{3,4} & w_{3,5}
\end{bmatrix}
\begin{bmatrix} \Delta\theta_1 \\ \Delta\theta_2 \\ \Delta\theta_3 \\ \Delta\theta_4 \\ \Delta\theta_5 \end{bmatrix}
```

Because each $\mathbf w_j$ has unit length, $z_j$ is the length of the data along that eigenvector. A large weight $w_{j,k}$ means parameter $k$ contributes strongly to value $j$ , so every $z_j$ is a weighted mix of the five parameter differences.

PCA also subtracts the training mean before projecting. That only shifts each value by a constant that is the same for every case, and leaves the distances between cases unchanged:

```math
\mathbf{w}_j^{\mathsf T}\bigl(\Delta\boldsymbol{\theta} - \overline{\Delta\boldsymbol{\theta}}\bigr)
= z_j - \mathbf{w}_j^{\mathsf T}\,\overline{\Delta\boldsymbol{\theta}}
```

## Step 6 — The values that train the SVM

Every training case is projected in the same way, and becomes one row of three values:

```math
\mathbf{Z} =
\begin{bmatrix}
z_{1,1} & z_{1,2} & z_{1,3} \\
z_{2,1} & z_{2,2} & z_{2,3} \\
\vdots & \vdots & \vdots \\
z_{m,1} & z_{m,2} & z_{m,3}
\end{bmatrix}
\in \mathbb{R}^{m \times 3}
```

The three columns are the features $PCA_{\Delta\theta 1}$ , $PCA_{\Delta\theta 2}$ and $PCA_{\Delta\theta 3}$ . Since the eigenvectors are orthogonal, the three columns are uncorrelated over the training set, and the variance of column $j$ is $\lambda_j$ . The rows, each with the label of its case, train the SVM.

A new case follows the same path with nothing refitted: its pixels are fitted, the parameters are averaged per region, the difference vector is formed, and the vector is projected onto the three stored eigenvectors.

## Relation to the source

SG24 builds its features from three kinds of input, and this feature uses the third.

| Input | Features in SG24 |
|---|---|
| The representative recovery curve of each region, taken directly or with its minimum subtracted | Euclidean distance, energy difference, rise-time difference, area difference, temperature difference at 20 s |
| A set of recovery curves compared with a class model curve | the statistical similitude features: projection, correlation and distance, each with its mean and standard deviation |
| The parameters of the double-exponential model | the PCA parameter-difference features of this note |

For this feature SG24 starts from its Eq. (1), the double-exponential model of one pixel's recovery curve. Every pixel is fitted on its own (Step 1), and the five fitted values are averaged over the lesion pixels and over the non-lesion pixels, which gives the parameter sets $\boldsymbol{\theta}_L$ and $\boldsymbol{\theta}_N$ (Step 2). The absolute difference gives five components (Step 3), and PCA on the covariance of the training differences reduces the five to three (Steps 4 to 6).

## Related notes

- [PCA — Mr. Variance](../../machine-learning/pca-mr-variance/content.md) covers PCA itself.
- [SVM — The Margin Master](../../machine-learning/svm-margin-master/content.md) covers the classifier that receives the three values.
- [Thermal Dynamics of Recovery and TRC Geometry](../thermal-recovery-and-trc-geometry/content.md) covers the recovery-curve setting.

## Reference

Soto, R. F., & Godoy, S. E. (2024). An automatic approach to detect skin cancer utilizing active infrared thermography. *Heliyon*, 10, e40608. https://doi.org/10.1016/j.heliyon.2024.e40608

## Summary

Each pixel is fitted on its own, the five fitted parameters are averaged per region, and the lesion-minus-normal difference gives five numbers per case. Three features are then built from PCA analysis followed by projection: the five numbers are mapped onto three eigenvectors, one value each.

### 繁體中文

每個像素各自擬合，五個擬合參數在每個區域內取平均，病灶與正常皮膚的差值讓每個病例得到五個數。接著由 PCA 分析加上投影建立三個特徵：把這五個數投影到三個特徵向量上，各得到一個值。

### Français

Chaque pixel est ajusté séparément, les cinq paramètres ajustés sont moyennés par région, et la différence entre lésion et peau normale donne cinq nombres par cas. Trois caractéristiques sont ensuite construites par l'analyse PCA suivie d'une projection : les cinq nombres sont projetés sur trois vecteurs propres, une valeur pour chacun.

### Deutsch

Jedes Pixel wird einzeln angepasst, die fünf angepassten Parameter werden pro Region gemittelt, und die Differenz zwischen Läsion und normaler Haut ergibt fünf Zahlen pro Fall. Drei Merkmale entstehen dann aus der PCA-Analyse mit anschließender Projektion: Die fünf Zahlen werden auf drei Eigenvektoren abgebildet, je ein Wert.

### Русский

Каждый пиксель аппроксимируется отдельно, пять подобранных параметров усредняются по области, а разность между очагом и нормальной кожей даёт пять чисел на случай. Затем три признака строятся с помощью PCA-анализа и проекции: пять чисел проецируются на три собственных вектора, по одному значению на каждый.
