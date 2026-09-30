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

## What happens

1. Every lesion pixel has its own recovery curve, and each curve is fitted with its own five-parameter double exponential.
2. The fitted parameters are stacked as a matrix, one row per pixel and one column per parameter. Each column is averaged over the pixels, giving the lesion mean vector $\bar{\boldsymbol{\theta}}_L$ . The same two steps on the normal-skin mask give $\bar{\boldsymbol{\theta}}_N$ .
3. The absolute difference of the two mean vectors gives one five-value vector $\Delta\boldsymbol{\theta}$ per case.
4. PCA is fitted on the $\Delta\boldsymbol{\theta}$ vectors of all training cases. PC1, PC2 and PC3 are the three leading eigenvectors, three directions in the five-parameter space.
5. A data vector is projected onto each eigenvector as row vector times column vector: five elements times five elements gives one value. PC1 gives $z_1$ , PC2 gives $z_2$ , PC3 gives $z_3$ .
6. Every training case becomes one row of three projected values, and these rows train the SVM.

## Concept

```math
f_i(t) = \theta_{i,1} + \theta_{i,2}\,e^{\theta_{i,3}t} + \theta_{i,4}\,e^{\theta_{i,5}t},
\qquad
\bar{\theta}_{L,k} = \frac{1}{n}\sum_{i \in L}\theta_{i,k},
\qquad
\Delta\boldsymbol{\theta} = \left|\bar{\boldsymbol{\theta}}_L - \bar{\boldsymbol{\theta}}_N\right| \in \mathbb{R}^5
```

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

The rows $\mathbf{w}_1^{\mathsf T}, \mathbf{w}_2^{\mathsf T}, \mathbf{w}_3^{\mathsf T}$ are the eigenvectors of the covariance of the training $\Delta\boldsymbol{\theta}$ vectors, so each $z_j$ is the length of the data along one eigenvector. PCA also subtracts the training mean before projecting; that only shifts each value by a constant. The method is general: it needs only fitted curves from two regions. It is applied here to active-thermography skin-cancer video, following SG24 (Soto & Godoy 2024, *An automatic approach to detect skin cancer utilizing active infrared thermography*), where the three values are named $PCA_{\Delta\theta 1}$ , $PCA_{\Delta\theta 2}$ , $PCA_{\Delta\theta 3}$ . PCA itself is covered in [PCA — Mr. Variance](../../machine-learning/pca-mr-variance/content.md), and the recovery-curve setting in [Thermal Dynamics of Recovery and TRC Geometry](../thermal-recovery-and-trc-geometry/content.md).

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
