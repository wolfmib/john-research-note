---
title: "AP Precalculus 2.6: Residuals, Under or Over?"
topic: animations
example: ap-precalculus-2-6-residuals-under-or-over
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-10-16
author: Wei-Che Hung
---

# AP Precalculus 2.6: Residuals, Under or Over?

![AP Precalculus 2.6: Residuals, Under or Over?](media/ap-precalculus-2-6-residuals-under-or-over.gif)

## What happens

1. The data. An app counts its users, in thousands, for the first 6 months after launch: 5.1, 7.4, 11.4, 16.7, 25.5 and 37.9. Model P is the straight line $\hat y = 1.36 + 6.39x$ drawn dashed through the points.
2. One point at a time. For each month the value of $x$ goes into the model and gives the prediction $\hat y$. Then the actual $y$ and the prediction go into $r = y - \hat y$ and the residual comes out.
3. The gap and the verdict. A vertical stick joins the data point to the line, then drops into the residual plot. At $x = 0$ the residual is $5.1 - 1.36 = 3.74$ so the actual value is above the line and the model underestimates.
4. All six residuals of P: +3.74, −0.35, −2.74, −3.83, −1.42 and +4.59.
5. Under and over. The two points with a positive residual light up first, where the model underestimates. Then the four points with a negative residual light up, where the model overestimates. Together the six residuals make a U-shape.
6. Model Q. The exponential model $\hat y = 5(1.5)^x$ goes through the same formula. Its residuals stay between −0.2 and 0.2 and switch sign with no pattern.
7. The comparison. On one scale the residuals of P form a U and those of Q lie almost on zero. A straight line is the wrong type of model for this data, and the exponential model fits.

## Concept

The residual of a data point is the actual value minus the value the model predicts:

```math
r = y - \hat y
```

- A positive residual $r > 0$ means the actual value is above the model: the model underestimates.
- A negative residual $r < 0$ means the actual value is below the model: the model overestimates.

| $x$ | $y$ | P: $\hat y$ | P: $r$ | Q: $\hat y$ | Q: $r$ |
|---:|---:|---:|---:|---:|---:|
| 0 | 5.1 | 1.36 | +3.74 | 5.00 | +0.10 |
| 1 | 7.4 | 7.75 | −0.35 | 7.50 | −0.10 |
| 2 | 11.4 | 14.14 | −2.74 | 11.25 | +0.15 |
| 3 | 16.7 | 20.53 | −3.83 | 16.88 | −0.18 |
| 4 | 25.5 | 26.92 | −1.42 | 25.31 | +0.19 |
| 5 | 37.9 | 33.31 | +4.59 | 37.97 | −0.07 |

A model is appropriate when its residuals are small and show no pattern. The residuals of the straight line are positive at both ends and negative in the middle: the data curve upward and a line cannot bend, so a curved model type, here exponential, fits better.

Practice with three models of five points each (linear, exponential growth, exponential decay): [Math Material — Residuals: Linear, Exponential Growth and Decay](../../basic-math/math-material-residuals-linear-exponential-growth-and-decay/content.md). Questions on the same idea: [AP Precalculus 2.6 — Competing Function Model Validation](../../basic-math/ap-precalculus-2-6-competing-function-model-validation/content.md).

## Summary

A residual is the actual value minus the predicted value. For the app data the straight line P leaves the residuals +3.74, −0.35, −2.74, −3.83, −1.42 and +4.59: positive where the model underestimates and negative where it overestimates, in a U-shape that shows a line is the wrong model type, while the exponential model Q leaves small residuals with no pattern.

### 繁體中文

殘差是實際值減去模型的預測值。對這組 App 用戶資料，直線模型 P 的殘差為 +3.74、−0.35、−2.74、−3.83、−1.42 與 +4.59：殘差為正時模型低估，為負時模型高估；殘差排成 U 形，表示直線不是合適的模型類型，而指數模型 Q 的殘差很小，而且沒有規律。

### Français

Un résidu est la valeur réelle moins la valeur prédite par le modèle. Pour les données de l'application, la droite P laisse les résidus +3,74, −0,35, −2,74, −3,83, −1,42 et +4,59 : positifs là où le modèle sous-estime, négatifs là où il surestime, en forme de U, ce qui montre qu'une droite n'est pas le bon type de modèle, tandis que le modèle exponentiel Q laisse de petits résidus sans motif.

### Deutsch

Ein Residuum ist der tatsächliche Wert minus der vom Modell vorhergesagte Wert. Für die App-Daten lässt die Gerade P die Residuen +3,74, −0,35, −2,74, −3,83, −1,42 und +4,59: positiv, wo das Modell unterschätzt, negativ, wo es überschätzt, in U-Form, was zeigt, dass eine Gerade der falsche Modelltyp ist, während das Exponentialmodell Q kleine Residuen ohne Muster lässt.

### Русский

Остаток — это фактическое значение минус значение, предсказанное моделью. Для данных о пользователях приложения прямая P даёт остатки +3,74, −0,35, −2,74, −3,83, −1,42 и +4,59: положительные там, где модель занижает, и отрицательные там, где она завышает; U-образная форма показывает, что прямая — неподходящий тип модели, а у экспоненциальной модели Q остатки малы и не имеют закономерности.
