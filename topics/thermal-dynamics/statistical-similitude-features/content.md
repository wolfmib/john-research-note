---
title: "Statistical Similitude Features: Projection, Correlation, Distance"
topic: thermal-dynamics
example: statistical-similitude-features
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-10-01
author: Wei-Che Hung
---

# Statistical Similitude Features: Projection, Correlation, Distance

![Statistical Similitude Features: Projection, Correlation, Distance](media/statistical-similitude-projection-correlation-distance.gif)

## What happens

1. A recovery curve sampled at $K$ time points is one vector of $K$ values. The model curve $f_m$ is the double exponential with one class's averaged fitted parameters, scaled so that $\|f_m\| = 1$ . The curve $f_n$ is one modeled curve from the lesion set or the non-lesion set of a case.
2. Projection: the two curves are multiplied sample by sample and the products are added. Because $\|f_m\| = 1$ , the result is the length of $f_n$ along $f_m$ .
3. Correlation: each sample is measured from its own curve's mean. The two deviations at the same time point are multiplied. Both below or both above the mean gives a positive product; one above and one below gives a negative product. The sum of the products is divided by the size of each curve's own deviations.
4. Distance: the gap between the two curves at each time point is squared, the squares are added, the square root is taken, and the result is divided by $K-1$ .
5. Each measure is computed for a set of at least 10 curves $f_n$ . The mean and the standard deviation over the set are the features.

## Concept

```math
\mathrm{proj}_n = \langle f_n, f_m \rangle = f_n^{\mathsf T} f_m = \sum_{k=1}^{K} f_n(t_k)\, f_m(t_k),
\qquad \|f_m\| = 1
```

```math
\rho = \frac{\mathrm{cov}(f_m, f_n)}{\sigma_{f_m}\,\sigma_{f_n}}
= \frac{\sum_k a_k\, b_k}{\sqrt{\sum_k a_k^2}\;\sqrt{\sum_k b_k^2}},
\qquad a_k = f_m(t_k) - \bar{f}_m, \quad b_k = f_n(t_k) - \bar{f}_n
```

```math
d_n = \frac{1}{K-1}\,\| f_n - f_m \| = \frac{1}{K-1}\sqrt{\sum_{k=1}^{K}\big(f_n(t_k) - f_m(t_k)\big)^2}
```

Projection grows with the size of $f_n$ . Correlation subtracts each curve's mean and divides by each curve's spread, so an offset or a positive rescaling of either curve leaves $\rho$ unchanged. Two recovery curves that are both below their means early and above them late give only positive products, and $\rho$ is close to 1.

The method follows SG24 (Soto & Godoy 2024, *An automatic approach to detect skin cancer utilizing active infrared thermography*). Two model curves (benign, malignant) are compared with two sets of curves per case (lesion, non-lesion), and each pairing gives six values: mean and standard deviation of projection, correlation and distance.

```math
2 \text{ model curves} \times 2 \text{ sets} \times 6 \text{ values} = 24 \text{ features}
```

Another feature family from the same source is covered in [PCA Parameter-Difference Features](../pca-parameter-difference-features/content.md). The three measures on plain vectors are covered in [Comparing two vectors: projection, correlation, and distance](../../statistics/comparing-two-vectors/content.md), and the mean and standard deviation over a group in [Reference-to-group vector features with mean and standard deviation](../../statistics/comparing-two-groups-of-vectors/content.md).

## Summary

Three measures compare one recovery curve with a model curve: projection is the length of the curve along the model, correlation compares the two after each curve's mean and spread are removed, and distance is the straight-line gap between them. Each measure is computed over a set of at least 10 curves, and its mean and standard deviation over the set are the features: 2 model curves, 2 sets and 6 values give 24 features.

### 繁體中文

三種量度把一條恢復曲線與一條模型曲線相比：投影是曲線沿模型方向的長度，相關係數在去除每條曲線各自的平均與離散程度後比較兩者，距離則是兩者之間的直線差距。每種量度都在至少 10 條曲線的集合上計算，其平均值與標準差就是特徵：2 條模型曲線、2 個集合、6 個數值，共 24 個特徵。

### Français

Trois mesures comparent une courbe de récupération à une courbe modèle : la projection est la longueur de la courbe le long du modèle, la corrélation compare les deux après avoir retiré la moyenne et la dispersion de chaque courbe, et la distance est l'écart en ligne droite entre elles. Chaque mesure est calculée sur un ensemble d'au moins 10 courbes, et sa moyenne et son écart-type sur l'ensemble sont les caractéristiques : 2 courbes modèles, 2 ensembles et 6 valeurs donnent 24 caractéristiques.

### Deutsch

Drei Maße vergleichen eine Erholungskurve mit einer Modellkurve: Die Projektion ist die Länge der Kurve entlang des Modells, die Korrelation vergleicht beide, nachdem Mittelwert und Streuung jeder Kurve entfernt wurden, und die Distanz ist der geradlinige Abstand zwischen ihnen. Jedes Maß wird über eine Menge von mindestens 10 Kurven berechnet, und sein Mittelwert und seine Standardabweichung über die Menge sind die Merkmale: 2 Modellkurven, 2 Mengen und 6 Werte ergeben 24 Merkmale.

### Русский

Три меры сравнивают одну кривую восстановления с модельной кривой: проекция — это длина кривой вдоль модели, корреляция сравнивает обе кривые после удаления среднего и разброса каждой из них, а расстояние — это прямой отрезок между ними. Каждая мера вычисляется по набору не менее чем из 10 кривых, а её среднее значение и стандартное отклонение по набору являются признаками: 2 модельные кривые, 2 набора и 6 значений дают 24 признака.
