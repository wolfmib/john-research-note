---
title: "TRC Vector Geometry: Projection, Correlation, and Distance"
topic: statistics
example: thermal-recovery-curves
status: concept-note
created: 2026-08-12
author: Wei-Che Hung
---

# TRC Vector Geometry: Projection, Correlation, and Distance

## Introduction

A thermal recovery curve (TRC) can be treated as a vector in a high-dimensional
space. If a curve is sampled at 10 Hz for 60 seconds, then the sequence contains
600 temperature values, so each recovery trace is a point in $\mathbb{R}^{600}$.

Let

$$
T_n(t_i) \quad \text{for} \quad t_i = 0.0, 0.1, \ldots, 59.9 \text{ s}
$$

and define the vector

$$
f_n =
\begin{bmatrix}
T_n(0.0)\\
T_n(0.1)\\
\vdots\\
T_n(59.9)
\end{bmatrix}
\in \mathbb{R}^{600}.
$$

Likewise, for a second independent recovery curve,

$$
f_m =
\begin{bmatrix}
T_m(0.0)\\
T_m(0.1)\\
\vdots\\
T_m(59.9)
\end{bmatrix}
\in \mathbb{R}^{600}.
$$

This viewpoint is useful because several comparison metrics become geometric
operations on these two vectors: projection, angular similarity, centering-based
correlation, and Euclidean distance.

## Research Question

How should one compare two TRC traces of length 600?

A naive temperature comparison is often misleading, because two curves can have
very different mean levels yet nearly identical temporal shape. The key is to
separate three questions:

1. Do the two curves point in the same direction in the full 600-dimensional
   space?
2. After removing their mean baseline, do they follow the same temporal pattern?
3. How far apart are the two curves in actual temperature space?

These are answered by cosine similarity, Pearson correlation, and distance
(RMSE or Euclidean distance), respectively.

## 1. Projection and cosine similarity

If both vectors are L2-normalized,

$$
\|f_n\|_2 = 1, \qquad \|f_m\|_2 = 1,
$$

then their dot product is

$$
\langle f_n, f_m \rangle = f_n^T f_m.
$$

This is exactly the cosine similarity when the vectors are unit length:

$$
\cos\theta = \frac{f_n^T f_m}{\|f_n\|_2 \|f_m\|_2}.
$$

Geometrically, cosine similarity measures the angle between two vectors. If

$$
f_n^T f_m = 1,
$$

then the vectors point in the same direction. If

$$
f_n^T f_m = 0,
$$

they are orthogonal, and if

$$
f_n^T f_m = -1,
$$

they point in opposite directions.

The scalar projection of $f_m$ onto $f_n$ is

$$
\mathrm{proj}_{f_n}(f_m) = (f_n^T f_m) f_n,
$$

when $f_n$ is unit length. This says: how much of $f_m$ is aligned with the
orientation of $f_n$.

This metric is useful when the absolute temperature offset matters and when the
two curves are being compared as whole vectors. But it does not remove baseline
temperature differences.

## 2. Pearson correlation: shape comparison after mean removal

Pearson correlation is best understood as cosine similarity after centering the
vectors around their own mean.

Let

$$
\bar{f}_n = \frac{1}{N}\sum_{i=1}^{N} f_{n,i}, \qquad
\bar{f}_m = \frac{1}{N}\sum_{i=1}^{N} f_{m,i},
$$

with $N=600$. Define the centered vectors

$$
f_n^c = f_n - \bar{f}_n \mathbf{1},
\qquad
f_m^c = f_m - \bar{f}_m \mathbf{1}.
$$

Then Pearson correlation is

$$
\rho(f_n,f_m) =
\frac{(f_n^c)^T f_m^c}{\|f_n^c\|_2\,\|f_m^c\|_2}.
$$

This is not the same as plain cosine similarity on the original vectors. It is
cosine similarity on the mean-adjusted vectors.

### Why the mean matters

Suppose two TRC curves have the same shape but are shifted by a constant offset:

$$
f_n = [30,31,32,33]^T,
\qquad
f_m = [50,51,52,53]^T.
$$

They differ in absolute temperature, but their time pattern is identical.

Their means are

$$
\bar{f}_n = 31.5, \qquad \bar{f}_m = 51.5,
$$

so the centered versions become

$$
f_n^c = [-1.5,-0.5,0.5,1.5]^T,
\qquad
f_m^c = [-1.5,-0.5,0.5,1.5]^T.
$$

Hence

$$
\rho(f_n,f_m)=1.
$$

This is the main reason Pearson is often used to compare thermal recovery
curves: it answers the question,

> Do the curves rise and fall in the same pattern, regardless of their absolute
> baseline temperature?

This is often more informative for TRC comparison than raw dot product or cosine
similarity, because the absolute thermal level may reflect different initial
conditions, device calibration, or environmental offsets rather than the shape of
recovery itself.

## 3. What covariance is doing

The covariance between two centered curves is

$$
\mathrm{Cov}(f_n,f_m) =
\frac{1}{N}\sum_{i=1}^{N}(f_{n,i}-\bar{f}_n)(f_{m,i}-\bar{f}_m).
$$

At each time point, the sign of the product tells whether both curves are above or
below their own mean:

- $(+)(+) \Rightarrow$ positive contribution;
- $(-)(-) \Rightarrow$ positive contribution;
- $(+)(-) \Rightarrow$ negative contribution.

So covariance measures whether the curves deviate from their means in the same
way at the same times.

Pearson correlation normalizes this covariance by the standard deviations of the
two curves:

$$
\rho(f_n,f_m) =
\frac{\mathrm{Cov}(f_n,f_m)}{\sigma_n\sigma_m}.
$$

This removes scaling effects. If one curve is simply multiplied by a constant,
its covariance scales, but Pearson stays the same because the same multiplicative
factor appears in both numerator and denominator. That is why $\rho$ focuses on
pattern and direction of change rather than amplitude.

## 4. Distance and RMSE

Euclidean distance measures the actual separation between two vectors:

$$
 d(f_n,f_m) = \|f_m-f_n\|_2
 = \sqrt{\sum_{i=1}^{600}(f_{m,i}-f_{n,i})^2}.
$$

This answers the question,

> How far apart are the two actual curves in temperature space?

For a 60-second TRC sampled at 10 Hz, the natural average error per sample is the
root mean squared error (RMSE):

$$
\mathrm{RMSE}(f_n,f_m) =
\sqrt{\frac{1}{600}\sum_{i=1}^{600}(f_{m,i}-f_{n,i})^2}.
$$

This is equivalent to

$$
\mathrm{RMSE}(f_n,f_m) =
\frac{\|f_m-f_n\|_2}{\sqrt{600}}.
$$

An RMSE of $0.4^\circ\mathrm{C}$, for example, means that the typical difference
between the two curves across the 600 time points is roughly $0.4^\circ\mathrm{C}$.

## 5. Relationship between cosine and Euclidean distance

If both vectors are already L2-normalized so that $\|f_n\|_2=\|f_m\|_2=1$, then

$$
\|f_n-f_m\|_2^2
=(f_n-f_m)^T(f_n-f_m)
=f_n^T f_n + f_m^T f_m - 2f_n^T f_m.
$$

Because the norms are 1,

$$
\|f_n-f_m\|_2^2 = 2 - 2f_n^T f_m,
$$

or equivalently

$$
\|f_n-f_m\|_2 = \sqrt{2 - 2\cos\theta}.
$$

So after L2 normalization, Euclidean distance and cosine similarity contain the
same directional information up to a monotone transformation. They are not
independent measures in that setting.

This is why, for normalized curves, the practical choice is often to keep one
angle-based metric and one magnitude-based metric, rather than several features
that are mathematically redundant.

## 6. What each metric is really asking

For TRC comparison, the three metrics answer different physical questions.

### Cosine similarity

Asks whether the two full temperature trajectories point in the same direction in
$\mathbb{R}^{600}$.

### Pearson correlation

Asks whether the two curves have the same temporal pattern after removing their
means.

### RMSE / Euclidean distance

Asks how far apart the two actual curves are in temperature units.

This distinction is important for thermal recovery data. A curve may have the
same shape but a different mean level, or a similar mean level but an entirely
different dynamic recovery pattern. The right metric depends on which of these
questions is scientifically relevant.

## 7. Recommended interpretation for TRC analysis

For thermal recovery recovery analysis, a good feature set is often

$$
\mathbf{x}_{nm} =
\begin{bmatrix}
\rho(f_n,f_m)\\
\mathrm{RMSE}(f_n,f_m)\\
|\Delta T_n - \Delta T_m|\\
|\tau_n - \tau_m|
\end{bmatrix},
$$

where $\Delta T$ is the total temperature recovery change and $\tau$ is a
recovery time constant or slope-based characteristic time.

This keeps:

- a shape metric: Pearson correlation;
- a deviation metric: RMSE;
- a level metric: $\Delta T$; and
- a time-scale metric: $\tau$.

Together they describe the curve more completely than raw cosine similarity or
Euclidean distance alone.

## 8. Go / plan

A practical workflow for comparing two TRC traces is:

1. Sample and represent each curve as a vector in $\mathbb{R}^{600}$.
2. Inspect raw temperature traces and their means.
3. Compute Pearson correlation to assess waveform similarity after baseline
   removal.
4. Compute RMSE to measure average temperature difference.
5. Compare additional physical features such as initial value, final value,
   recovery slope, and characteristic time constant.
6. Use cosine similarity only when the full vector direction is scientifically
   meaningful and when absolute offset is intentionally part of the comparison.

This turns TRC comparison from a loose visual judgment into a structured
geometry problem: shape, direction, and magnitude are treated as different
concepts rather than as the same quantity.

## Summary

A TRC sampled over 60 seconds at 10 Hz is naturally represented as a vector in
$\mathbb{R}^{600}$. From that perspective:

- projection and cosine similarity describe directional agreement;
- Pearson correlation describes agreement after mean-centering;
- Euclidean distance and RMSE describe physical separation in temperature space.

The single most useful conceptual takeaway is:

$$
\boxed{\text{Pearson correlation is cosine similarity after subtracting the mean}.}
$$

This is the cleanest geometric way to understand why Pearson is useful for
comparing recovery-shape patterns while raw vector similarity is sensitive to
baseline temperature levels.

For the metric definitions independent of the TRC application, see
[Comparing Two Vectors: Projection, Correlation, and Distance](../comparing-two-vectors/content.md).
