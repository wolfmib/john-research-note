---
title: "Derivation of the Harmonic Sum Identity"
topic: animations
example: harmonic-sum-identity-derivation
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-08-27
author: Wei-Che Hung
---

# Derivation of the Harmonic Sum Identity

![Derivation of the Harmonic Sum Identity](media/harmonic-sum-identity-derivation.svg)

## What happens

1. The claim is stated: $\sum_{r=1}^{N} H_{r-1} = N(H_N - 1)$, a closed form for the running sum of harmonic numbers.
2. For $N = 5$ the terms $H_0, \dots, H_4$ are written out one under the other; reading the columns, the fraction $1/k$ appears $N-k$ times, so the sum is $\sum_{k=1}^{N-1} (N-k)/k$.
3. The fraction is split, $\frac{N-k}{k} = \frac{N}{k} - 1$, and the two pieces are summed separately: $N H_{N-1} - (N-1)$.
4. The recursion $H_{N-1} = H_N - \frac{1}{N}$ replaces $H_{N-1}$; the $-1$ it produces cancels the $+1$ from $-(N-1)$, leaving $N H_N - N = N(H_N - 1)$.

## Concept

$$
\sum_{r=1}^{N} H_{r-1}
= \sum_{k=1}^{N-1} \frac{N-k}{k}
= N H_{N-1} - (N-1)
= N\!\left(H_N - \tfrac{1}{N}\right) - (N-1)
= N(H_N - 1)
$$

The whole proof is a change in the order of summation: instead of adding the rows $H_{r-1}$, one adds the columns, each of which is a single fraction $1/k$ repeated $N-k$ times. The remaining steps are bookkeeping with the definition $H_{N-1} = \sum_{k=1}^{N-1} 1/k$ and the one-step recursion $H_N = H_{N-1} + 1/N$. Companion note on how $H_N$ itself grows: [Harmonic Growth and the Euler–Mascheroni Constant](../harmonic-growth-euler-mascheroni-gamma/content.md).

## Summary

Summing the first $N$ harmonic numbers gives $N(H_N - 1)$: swapping rows for columns turns the double sum into a single one, and the recursion $H_N = H_{N-1} + 1/N$ closes it. The identity shows up whenever an algorithm's cost is a running total of harmonic terms, for example expected comparisons in quicksort.

### 繁體中文

前 $N$ 個調和數之和等於 $N(H_N - 1)$ ：把逐列相加改為逐行相加，雙重求和就化為單一求和，再用遞迴式 $H_N = H_{N-1} + 1/N$ 收尾。凡是演算法的成本是調和項的累計和，例如快速排序的期望比較次數，這個恆等式就會出現。

### Français

La somme des $N$ premiers nombres harmoniques vaut $N(H_N - 1)$ : en additionnant par colonnes plutôt que par lignes, la double somme devient une somme simple, et la récurrence $H_N = H_{N-1} + 1/N$ la referme. L'identité apparaît chaque fois que le coût d'un algorithme est un cumul de termes harmoniques, par exemple le nombre attendu de comparaisons du tri rapide.

### Deutsch

Die Summe der ersten $N$ harmonischen Zahlen ist $N(H_N - 1)$ : Addiert man spaltenweise statt zeilenweise, wird aus der Doppelsumme eine einfache Summe, und die Rekursion $H_N = H_{N-1} + 1/N$ schließt sie ab. Die Identität tritt immer dann auf, wenn die Kosten eines Algorithmus eine laufende Summe harmonischer Terme sind, etwa die erwartete Zahl der Vergleiche bei Quicksort.

### Русский

Сумма первых $N$ гармонических чисел равна $N(H_N - 1)$ : суммируя по столбцам вместо строк, двойную сумму превращают в одинарную, а рекурсия $H_N = H_{N-1} + 1/N$ её замыкает. Это тождество возникает всякий раз, когда стоимость алгоритма есть накопленная сумма гармонических членов, например ожидаемое число сравнений в быстрой сортировке.
