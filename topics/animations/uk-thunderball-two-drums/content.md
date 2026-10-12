---
title: "UK Thunderball — Two Drums and What a £1 Line Is Worth"
topic: animations
example: uk-thunderball-two-drums
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-10-12
author: Wei-Che Hung
---

# UK Thunderball — Two Drums and What a £1 Line Is Worth

![UK Thunderball — Two Drums and What a £1 Line Is Worth](media/uk-thunderball-two-drums.gif)

## What happens

1. The two drums. The main drum holds 39 balls and the Thunderball drum holds 14. A £1 line picks 5 main numbers and 1 Thunderball.
2. The draw. The numbers 2, 4, 6, 8 and 17 come out of the main drum, then Thunderball 11. A line with all six wins the fixed £500,000 jackpot.
3. A smaller prize. Against the draw 2, 4, 12, 20, 30 and Thunderball 11, the same line matches 2 main numbers and the Thunderball, which pays £10.
4. Counting the main drum. The order of the numbers does not matter, so there are $\binom{39}{5} = 575{,}757$ sets of 5 main numbers.
5. Two drums multiply. Any set of main numbers goes with any of the 14 Thunderballs, so there are $575{,}757 \times 14 = 8{,}060{,}598$ different lines. The jackpot chance is 1 in 8,060,598.
6. Every prize tier. A line with $k$ main matches takes $k$ of the 5 drawn numbers and $5 - k$ of the 34 others, then 1 way for the right Thunderball or 13 ways for a wrong one. Nine tiers pay out, 650,910 lines in total, about 1 in 12.4.
7. The expected value. All prizes over all lines add up to £4,262,568, so one line is worth $4{,}262{,}568 / 8{,}060{,}598 \approx 0.5288$ pounds on average: about 53p of each £1 comes back.

## Concept

The two drums are independent, so their counts multiply:

```math
N = \binom{39}{5} \times \binom{14}{1} = 575{,}757 \times 14 = 8{,}060{,}598
```

Inside the main drum the number of matches is hypergeometric (5 drawn numbers among 39). The Thunderball drum adds a factor 1 or 13:

```math
\text{lines}(k) = \binom{5}{k}\binom{34}{5-k} \times \begin{cases} 1 & \text{right Thunderball} \\ 13 & \text{wrong Thunderball} \end{cases}
```

| Match | Lines | Prize |
|---|---:|---:|
| 5 + Thunderball | 1 | £500,000 |
| 5 only | 13 | £5,000 |
| 4 + Thunderball | 170 | £250 |
| 4 only | 2,210 | £100 |
| 3 + Thunderball | 5,610 | £20 |
| 3 only | 72,930 | £10 |
| 2 + Thunderball | 59,840 | £10 |
| 1 + Thunderball | 231,880 | £5 |
| 0 + Thunderball | 278,256 | £3 |

```math
E = \frac{1}{N} \sum_{i} \text{lines}_i \times \text{Prize}_i = \frac{4{,}262{,}568}{8{,}060{,}598} \approx 0.5288
```

Every Thunderball prize is a fixed amount, so this expected value is exact. The expected net per line is about − £0.47, a return rate of 52.9 %. The one-drum [Malta Lotto Quaterno](../malta-lotto-quaterno-expected-value/content.md) returns 49.6 % of its €3 price.

## Summary

A £1 UK Thunderball line is one of 8,060,598 equally likely lines, because the 575,757 sets of main numbers multiply with the 14 Thunderballs. Nine fixed prize tiers cover 650,910 lines, about 1 in 12.4, and the expected value of a line is about £0.53, so the expected net is about − £0.47 and the return rate is 52.9 %.

### 繁體中文

一注 1 英鎊的英國 Thunderball 彩票，是 8,060,598 種同樣可能的組合之一：主號碼的 575,757 種選法乘以 14 個 Thunderball 號碼。九個固定獎級共涵蓋 650,910 注，約 12.4 注中 1 注，每注的期望值約為 0.53 英鎊，因此淨期望值約為 − 0.47 英鎊，回報率為 52.9 %。

### Français

Une grille UK Thunderball à 1 £ est l'une des 8 060 598 grilles équiprobables, car les 575 757 choix de numéros principaux se multiplient par les 14 Thunderballs. Les neuf rangs de gains fixes couvrent 650 910 grilles, environ 1 sur 12,4, et l'espérance d'une grille est d'environ 0,53 £ : la valeur nette espérée est d'environ − 0,47 £ et le taux de retour de 52,9 %.

### Deutsch

Eine UK-Thunderball-Reihe für 1 £ ist eine von 8.060.598 gleich wahrscheinlichen Reihen, denn die 575.757 Möglichkeiten für die Hauptzahlen multiplizieren sich mit den 14 Thunderballs. Die neun festen Gewinnklassen umfassen 650.910 Reihen, etwa 1 von 12,4, und der Erwartungswert einer Reihe beträgt etwa 0,53 £; der erwartete Nettowert liegt damit bei etwa − 0,47 £, die Rücklaufquote bei 52,9 %.

### Русский

Ставка UK Thunderball за 1 £ — одна из 8 060 598 равновероятных комбинаций: 575 757 вариантов основных чисел умножаются на 14 чисел Thunderball. Девять фиксированных призовых категорий охватывают 650 910 комбинаций, примерно 1 из 12,4, а математическое ожидание одной ставки составляет около 0,53 £, то есть ожидаемый чистый результат около − 0,47 £, а коэффициент возврата 52,9 %.
