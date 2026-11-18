---
title: "Quantum Schedule Oracle: Grover Search for Learning-Rate Schedules in LLM Fine-Tuning"
topic: quantum-computing
example: quantum-schedule-oracle-explainer
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-11-18
author: Wei-Che Hung
---

# Quantum Schedule Oracle: Grover Search for Learning-Rate Schedules in LLM Fine-Tuning

![Quantum Schedule Oracle: Grover Search for Learning-Rate Schedules in LLM Fine-Tuning](media/quantum-schedule-oracle-explainer.gif)

## What happens

1. Three layer groups each turn their learning-rate dial. Raising $G_1$ alone or $G_2$ alone costs $-1$ ; raising both adds an interaction of $+4$ , so the pair scores $-1-1+4=+2$ .
2. Classical probes at the checkpoint measure the singles, the pairs and the triples; their sum is the score $\Phi_t(z)$ of a schedule.
3. Six groups with four rates each give $4^6=4096$ schedules on 12 search qubits, all prepared in one uniform superposition.
4. The oracle computes every score into a Fourier-basis accumulator, flips the phase of each schedule that beats the threshold (the uniform baseline scores $0$ ), and uncomputes the accumulator back to $|0\rangle$ .
5. Grover iterations amplify the marked schedules. In the eight-schedule example the one improving schedule rises from 12.5 % to 78.125 % after a single iteration.
6. One measurement gives a candidate. A classical check confirms that it beats the threshold, the threshold rises, and the schedule drives the next 200 training steps until the next checkpoint.

## Concept

### Part 1 — Quantum minimum finding and when to stop

Each of $G$ layer groups takes one of $K$ rates. The profiles fill a search register in uniform superposition:

```math
N = K^G, \qquad q_{\mathrm{srch}} = \lceil \log_2 N \rceil, \qquad |\psi_0\rangle = \frac{1}{\sqrt N}\sum_{z} |z\rangle .
```

With $M$ profiles better than the current threshold, $j$ Grover iterations find one with probability

```math
p_j(M) = \sin^2\!\big((2j+1)\theta\big), \qquad \theta = \arcsin\sqrt{M/N} .
```

BBHT draws $j$ at random and widens its range after each failure; Dürr–Høyer moves the threshold after each success. The expected total work is bounded:

```math
j \sim \mathcal U\{0,\dots,\lceil m_{\mathrm{BBHT}} \rceil - 1\}, \qquad m_{\mathrm{BBHT}} \leftarrow \min\!\big(\tfrac65\, m_{\mathrm{BBHT}},\ \sqrt N\big), \qquad \mathbb E[Q] \le \tfrac{45}{4}\sqrt N .
```

The search itself never knows that it has found the best profile. Part 1 compares fixed-budget and confidence-based stopping rules on a lookup oracle built from measured scores; the confidence rule D is the one carried into Part 2. The constant $45/4$ is derived in [Dürr–Høyer expected query bound](../durr-hoyer-expected-query-bound/content.md).

### Part 2 — The Interaction-Guided Schedule Oracle

The score of a schedule adds single-group gains, pair interactions and triple interactions:

```math
\widehat Y_t(z) = \sum_{g} Y_t(g;\eta_g) + \sum_{g \lt g'} \nu_{t,gg'} + \sum_{g \lt g' \lt g''} \nu_{t,gg'g''} .
```

Each interaction is a discrete derivative of the measured gains over the moved groups $\gamma$ :

```math
\nu_t(\gamma) = \sum_{\gamma' \subseteq \gamma} (-1)^{|\gamma|-|\gamma'|}\, Y_t(\gamma') .
```

With $\Phi_t$ the integer form of $\widehat Y_t$ and $y$ the current threshold schedule, the oracle marks every schedule that beats it:

```math
O_y\, |z\rangle = (-1)^{\mathbf 1[\Phi_t(z) > \Phi_t(y)]}\, |z\rangle .
```

### The numbers in the animation

```math
\nu_{12} = Y(\{1,2\}) - Y(\{1\}) - Y(\{2\}) = 2 - (-1) - (-1) = 4
```

```math
N = 4^6 = 4096, \qquad q_{\mathrm{srch}} = 12, \qquad \frac{1}{\sqrt{4096}} = \frac{1}{64}
```

```math
N = 8,\ M = 1: \qquad \sin\theta = \frac{1}{\sqrt 8}, \qquad p_1 = \sin^2 3\theta = \frac{25}{32} = 0.78125
```

## Summary

The research introduces an alternative quantum method for adaptive machine-learning training: the learning rates are selected inside training by a quantum search over all joint schedules. The paper selects one learning rate per layer group with quantum minimum finding. Part 1 decides when such a search should stop, and Part 2 builds an oracle that scores all $4096$ schedules in superposition from measured main and interaction effects and marks those that beat uniform training. The oracle was run in noise-free simulation, no measured quantum speed-up is claimed, and in closed-loop fine-tuning of a 1.5-billion-parameter model the benchmark accuracies stay within the range of five uniform-rate seeds; this first paper lays the foundation of the method.

### 繁體中文

本研究提出一種用於自適應機器學習訓練的另類量子方法：在訓練過程中，以量子搜尋在所有聯合排程中選出學習率。本論文以量子最小值搜尋為每個層組選擇一個學習率。第一部分決定這種搜尋何時應該停止；第二部分建構一個預言機（oracle），利用量測到的主效應與交互作用效應，在疊加態中為全部 $4096$ 個排程評分，並標記勝過均勻訓練的排程。此預言機以無雜訊模擬執行，未宣稱任何量測到的量子加速；在一個 15 億參數模型的閉環微調中，基準準確率落在五個均勻學習率種子的範圍之內；這第一篇論文為此方法奠定了基礎。

### Français

La recherche introduit une méthode quantique alternative pour l'entraînement adaptatif en apprentissage automatique : les taux d'apprentissage sont choisis pendant l'entraînement par une recherche quantique sur tous les calendriers conjoints. L'article choisit un taux d'apprentissage par groupe de couches à l'aide de la recherche quantique du minimum. La partie 1 décide quand une telle recherche doit s'arrêter, et la partie 2 construit un oracle qui note les $4096$ calendriers en superposition à partir des effets principaux et des interactions mesurés, puis marque ceux qui battent l'entraînement uniforme. L'oracle a été exécuté en simulation sans bruit, aucune accélération quantique mesurée n'est revendiquée, et lors de l'ajustement fin en boucle fermée d'un modèle de 1,5 milliard de paramètres, les précisions sur les benchmarks restent dans l'intervalle de cinq graines à taux uniforme ; ce premier article pose les fondations de la méthode.

### Deutsch

Die Forschung führt eine alternative Quantenmethode für adaptives Training im maschinellen Lernen ein: Die Lernraten werden während des Trainings durch eine Quantensuche über alle gemeinsamen Zeitpläne gewählt. Die Arbeit wählt mit quantenmechanischer Minimumsuche eine Lernrate pro Schichtgruppe. Teil 1 entscheidet, wann eine solche Suche anhalten soll, und Teil 2 baut ein Orakel, das alle $4096$ Zeitpläne in Superposition aus gemessenen Haupt- und Wechselwirkungseffekten bewertet und diejenigen markiert, die das gleichförmige Training übertreffen. Das Orakel lief in rauschfreier Simulation, ein gemessener Quantenvorteil wird nicht behauptet, und beim Feintuning eines Modells mit 1,5 Milliarden Parametern im geschlossenen Kreislauf bleiben die Benchmark-Genauigkeiten im Bereich von fünf Seeds mit gleichförmiger Rate; diese erste Arbeit legt das Fundament der Methode.

### Русский

Исследование предлагает альтернативный квантовый метод адаптивного обучения в машинном обучении: скорости обучения выбираются прямо во время обучения квантовым поиском по всем совместным расписаниям. В статье скорость обучения для каждой группы слоёв выбирается квантовым поиском минимума. Часть 1 определяет, когда такой поиск следует остановить, а часть 2 строит оракул, который по измеренным главным эффектам и взаимодействиям оценивает все $4096$ расписаний в суперпозиции и отмечает те, что лучше равномерного обучения. Оракул запускался в бесшумной симуляции, измеренное квантовое ускорение не заявляется, а при дообучении модели с 1,5 млрд параметров в замкнутом цикле точности на бенчмарках остаются в пределах разброса пяти запусков с равномерной скоростью; эта первая работа закладывает основу метода.

---

**Read the paper:** [arXiv:2611.21701](https://arxiv.org/abs/2611.21701) — Wei-Che Hung, *Hybrid Quantum Selection of Learning Rates in Language-Model Training: Termination Criteria and an Interaction-Guided Schedule Oracle*.
