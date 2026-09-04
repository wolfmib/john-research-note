---
title: "Random Forest, Part 1 — From One Big Tree to a Voting Forest"
topic: animations
example: random-forest-part1-one-big-tree-to-voting-forest
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-09-04
author: Wei-Che Hung
---

# Random Forest, Part 1 — From One Big Tree to a Voting Forest

![Random Forest, Part 1 — From One Big Tree to a Voting Forest](media/random-forest-part1-one-big-tree-to-voting-forest.svg)

## What happens

1. All 1000 training rows go into one big decision tree. One big tree is not good: it memorises the training rows (overfits) and changes a lot when the data changes.
2. Instead, a bootstrap sample is drawn: 1000 rows taken from the dataset with replacement. A small tree is grown on that sample.
3. A second bootstrap sample gives a second small tree, a third gives a third. Each sample, and so each tree, is a little different.
4. The process repeats until there are 100 small trees: the random forest.
5. A new input row is sent to every tree. Each tree votes yes or no; the tally is 76 yes and 24 no, so the forest answers YES.

## Concept

$$
\hat{y}(x) = \operatorname{majority}\bigl\{ h_1(x),\, h_2(x),\, \dots,\, h_{100}(x) \bigr\},
\qquad h_k \text{ grown on bootstrap sample } D_k \text{ drawn with replacement from } D
$$

This is bagging, bootstrap aggregating. A single deep tree has low bias but high variance: small changes in the data move its splits and its answers. Each tree in the forest sees a resampled copy of the data, so the trees make different mistakes, and a majority vote over many such trees cancels much of that noise. The forest keeps the low bias of deep trees and cuts the variance. Part 2 adds the second source of randomness, a random subset of features at every split, which makes the trees even less alike.

## Summary

A random forest replaces one big, overfitting decision tree with many small trees, each grown on its own bootstrap sample of the data, and lets them vote. With 100 trees voting 76 yes to 24 no the forest predicts YES; averaging many different trees lowers the variance that a single tree suffers from.

### 繁體中文

隨機森林用許多棵小樹取代一棵容易過擬合的大決策樹：每棵小樹都在自己的自助抽樣（bootstrap）資料上生長，最後由所有樹投票。100 棵樹以 76 票對 24 票投給「是」，森林就預測「是」；把許多不同的樹平均起來，可以降低單一棵樹的高變異。

### Français

Une forêt aléatoire remplace un seul grand arbre de décision, sujet au surapprentissage, par de nombreux petits arbres, chacun entraîné sur son propre échantillon bootstrap des données, puis les fait voter. Avec 100 arbres votant 76 oui contre 24 non, la forêt prédit OUI ; moyenner de nombreux arbres différents réduit la variance dont souffre un arbre unique.

### Deutsch

Ein Random Forest ersetzt einen einzelnen großen, überangepassten Entscheidungsbaum durch viele kleine Bäume, die jeweils auf einer eigenen Bootstrap-Stichprobe der Daten wachsen, und lässt sie abstimmen. Bei 100 Bäumen mit 76 Ja- gegen 24 Nein-Stimmen sagt der Wald JA voraus; die Mittelung vieler verschiedener Bäume senkt die Varianz, unter der ein einzelner Baum leidet.

### Русский

Случайный лес заменяет одно большое, переобученное дерево решений множеством маленьких деревьев, каждое из которых выращено на своей бутстрап-выборке данных, и даёт им проголосовать. При 100 деревьях, голосующих 76 «да» против 24 «нет», лес предсказывает ДА; усреднение многих разных деревьев снижает дисперсию, от которой страдает одно дерево.
