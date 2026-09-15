---
title: "Binomial Theorem"
topic: animations
example: binomial-theorem
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-15
author: Wei-Che Hung
---

# Binomial Theorem

![Binomial Theorem](media/binomial-theorem.svg)

## What happens

1. The expansion is introduced as a choice problem: each factor in $(x+a)^n$ contributes either an $x$ or an $a$.
2. For $(x+a)^3$, the $k = 0$ term chooses no $a$'s, so all three factors contribute $x$ and give $x^3$.
3. The $k = 1$ term chooses one factor to contribute $a$ and the other two to contribute $x$; there are three such choices, so the term is $3x^2a$.
4. The $k = 2$ term chooses two factors to contribute $a$; again there are three choices, so the term is $3xa^2$.
5. The $k = 3$ term chooses all three factors to contribute $a$, giving $a^3$.
6. The same counting rule gives the general term: choosing $k$ of the $n$ factors to contribute $a$ gives $\binom{n}{k}x^{n-k}a^k$.

## Concept

$$
(x+a)^n
= \sum_{k=0}^{n} \binom{n}{k} x^{n-k}a^k,
\qquad
\binom{n}{k} = \frac{n!}{k!(n-k)!}
$$

The binomial theorem is a counting statement. In the product $(x+a)^n$, a term is formed by taking one piece from each of the $n$ identical factors. If exactly $k$ factors contribute $a$, then the other $n-k$ factors contribute $x$, producing $x^{n-k}a^k$. The coefficient counts how many ways to choose those $k$ factors: $\binom{n}{k}$.

For $n=3$, the coefficients are $1, 3, 3, 1$, so

$$
(x+a)^3 = x^3 + 3x^2a + 3xa^2 + a^3 .
$$

## Summary

The binomial theorem says that each term of $(x+a)^n$ comes from choosing which $k$ factors contribute $a$ and which $n-k$ factors contribute $x$. The coefficient $\binom{n}{k}$ is the number of such choices, so for $n=3$ the expansion is $x^3 + 3x^2a + 3xa^2 + a^3$.

### 繁體中文

二項式定理說，$(x+a)^n$ 的每一項都來自選擇哪 $k$ 個因子提供 $a$ ，以及哪 $n-k$ 個因子提供 $x$ 。係數 $\binom{n}{k}$ 就是這種選法的數量，所以當 $n=3$ 時，展開式是 $x^3 + 3x^2a + 3xa^2 + a^3$ 。

### Français

Le théorème binomial dit que chaque terme de $(x+a)^n$ vient du choix des $k$ facteurs qui donnent $a$ et des $n-k$ facteurs qui donnent $x$ . Le coefficient $\binom{n}{k}$ est le nombre de ces choix ; pour $n=3$ , le développement est $x^3 + 3x^2a + 3xa^2 + a^3$ .

### Deutsch

Der binomische Lehrsatz sagt, dass jeder Term von $(x+a)^n$ daraus entsteht, welche $k$ Faktoren $a$ liefern und welche $n-k$ Faktoren $x$ liefern. Der Koeffizient $\binom{n}{k}$ ist die Anzahl dieser Wahlmöglichkeiten; für $n=3$ ist die Entwicklung $x^3 + 3x^2a + 3xa^2 + a^3$ .

### Русский

Биномиальная теорема говорит, что каждый член $(x+a)^n$ получается выбором тех $k$ множителей, которые дают $a$ , и тех $n-k$ множителей, которые дают $x$ . Коэффициент $\binom{n}{k}$ равен числу таких выборов, поэтому при $n=3$ разложение равно $x^3 + 3x^2a + 3xa^2 + a^3$ .
