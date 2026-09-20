---
title: "Malta Lotto Quaterno — What a €3 Ticket Is Worth"
topic: animations
example: malta-lotto-quaterno-expected-value
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-20
author: Wei-Che Hung
---

# Malta Lotto Quaterno — What a €3 Ticket Is Worth

![A 3-euro Quaterno ticket misses the draw; the combination space, the hypergeometric prize tiers and probability times prize give an expected payout of 1.49 euro and an expected net of minus 1.51 euro](media/malta-lotto-quaterno-expected-value.svg)

## What happens

1. The ticket and the draw. A €3 Quaterno ticket holds 4 numbers, here 11, 16, 24 and 66. The draw of 19 Sept 2026 takes 5 numbers from 1 to 90: 17, 73, 40, 80 and 9. Nothing matches, and the question becomes what the ticket was worth before the draw.
2. The combination space. A ticket is any 4 of the 90 numbers, so there are $C(90, 4) = 2{,}555{,}190$ possible tickets.
3. The jackpot combinations. Leaving out one of the 5 drawn numbers at a time gives $C(5, 4) = 5$ tickets that match all four, so the jackpot probability is $5 / 2{,}555{,}190$ , about 1 in 511,038.
4. Every prize tier. A ticket with $k$ matches takes $k$ of the 5 drawn numbers and $4 - k$ of the 85 others. That gives 35,700 tickets with two matches (€25), 850 with three (€475) and 5 with four (€501,750); the probability of any prize is about 1.43 %.
5. The expected value. Each tier contributes its probability times its prize: €0.3493, €0.1580 and €0.9818, together €1.4891. Subtracting the €3 ticket cost leaves − €1.5109 per ticket, a return rate of 49.64 %.
6. The long run. €3.00 goes in, €1.49 comes back on average, and the expected profit is − €1.51. Probability does not predict the next draw; it explains the long run.

## Concept

The number of matches follows the hypergeometric distribution: 5 winning numbers among 90, and 4 numbers on the ticket.

```math
P(k) = \frac{C(5, k) \cdot C(85, 4 - k)}{C(90, 4)}, \qquad C(90, 4) = \frac{90!}{4! \times 86!} = 2{,}555{,}190
```

The expected payout is the sum over the prize tiers of probability times prize:

```math
E[X] = \sum_{k} P(k) \times \mathrm{Prize}(k) = \frac{35{,}700}{2{,}555{,}190} \times 25 + \frac{850}{2{,}555{,}190} \times 475 + \frac{5}{2{,}555{,}190} \times 501{,}750 \approx 1.4891
```

```math
E[\text{net}] = E[X] - 3 \approx -1.5109, \qquad \frac{E[X]}{3} \approx 49.64 \%
```

Two thirds of the expected payout sits in the jackpot tier, an event with probability $5 / 2{,}555{,}190$ . The expected value is therefore a statement about the average over a very large number of tickets, not about what a single ticket is likely to return: 98.57 % of tickets return nothing.

## Summary

A €3 Malta Lotto Quaterno ticket has an expected payout of about €1.49, so its expected net value is − €1.51 and the return rate is 49.64 %. The matches follow a hypergeometric distribution, the probability of any prize is about 1.43 %, and two thirds of the expected payout comes from a jackpot with a chance of 1 in 511,038. Winning is random; the expected value is mathematics.

### 繁體中文

一張 3 歐元的馬耳他 Quaterno 樂透，期望回報約為 1.49 歐元，因此淨期望值為 − 1.51 歐元，回報率為 49.64 %。中獎號碼數服從超幾何分佈，贏得任何獎金的機率約為 1.43 %，而期望回報中有三分之二來自機率僅 511,038 分之 1 的頭獎。中獎靠運氣，期望值則是數學。

### Français

Un billet Quaterno du Malta Lotto à 3 € a un gain espéré d'environ 1,49 €, de sorte que sa valeur nette espérée est de − 1,51 € et le taux de retour de 49,64 %. Le nombre de numéros gagnants suit une loi hypergéométrique, la probabilité d'obtenir un lot quelconque est d'environ 1,43 %, et les deux tiers du gain espéré proviennent d'un gros lot dont la chance est de 1 sur 511 038. Gagner relève du hasard ; l'espérance relève des mathématiques.

### Deutsch

Ein Quaterno-Schein des Malta Lotto für 3 € hat eine erwartete Auszahlung von etwa 1,49 €, sodass der erwartete Nettowert − 1,51 € und die Rücklaufquote 49,64 % beträgt. Die Anzahl der Treffer folgt einer hypergeometrischen Verteilung, die Wahrscheinlichkeit für irgendeinen Gewinn liegt bei etwa 1,43 %, und zwei Drittel der erwarteten Auszahlung stammen aus einem Hauptgewinn mit einer Chance von 1 zu 511.038. Gewinnen ist Zufall; der Erwartungswert ist Mathematik.

### Русский

Билет Quaterno мальтийской лотереи за 3 € имеет ожидаемую выплату около 1,49 €, поэтому его ожидаемая чистая стоимость равна − 1,51 €, а коэффициент возврата составляет 49,64 %. Число совпадений подчиняется гипергеометрическому распределению, вероятность любого выигрыша составляет около 1,43 %, а две трети ожидаемой выплаты приходятся на джекпот с шансом 1 к 511 038. Выигрыш случаен; математическое ожидание — это математика.
