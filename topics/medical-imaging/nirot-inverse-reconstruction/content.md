---
title: "NIROT Function 2: Regularized and Learned Inverse Reconstruction"
topic: medical-imaging
project: uzh-borl-newborn-nirot
status: initial-literature-study-completed
created: 2026-08-05
author: Wei-Che Hung
---

# NIROT Function 2: Regularized and Learned Inverse Reconstruction

**Initial literature synthesis completed:** 2026-08-05. The exercises below
are the next hands-on stage, not a prerequisite for using this note as evidence
of focused pre-application preparation.

## Research question

How can noisy, incomplete time-resolved boundary measurements be converted into
stable 3D maps of absorption and reduced scattering without allowing noise,
model error, or learned priors to create clinically misleading structure?

This is the central computational function in the UZH/BORL PhD description. It
explicitly includes iterative solvers, optimization, regularization, and
machine-learning reconstruction in Python, MATLAB, PyTorch, or TensorFlow.

## Why the inverse problem is difficult

Let \(x\) contain the unknown voxel- or node-level optical properties and let
\(F(x)\) be the nonlinear forward model. The data model is

\[
y=F(x)+\varepsilon+\delta,
\]

where \(\varepsilon\) is measurement noise and \(\delta\) represents modelling
error. Diffuse scattering smooths spatial information before photons reach the
boundary, while the number and placement of sources and detectors limit what is
observed. Many different internal distributions can therefore explain nearly
the same data.

A common model-based reconstruction minimizes

\[
\hat{x}=\arg\min_x
\frac{1}{2}\left\|W\left(y-F(x)\right)\right\|_2^2
+\lambda R(x),
\]

where \(W\) weights measurements by their noise, \(R(x)\) expresses prior
structure, and \(\lambda\) controls the data-fit/regularization tradeoff. After
linearization around \(x_k\), the Jacobian

\[
J_k=\frac{\partial F}{\partial x}\bigg|_{x_k}
\]

relates a small property update to a measurement change. Gauss-Newton or related
iterations solve a regularized update and repeatedly call the forward model.

## Three reconstruction families

### Conventional model-based iteration

Tikhonov, smoothness, total-variation, sparsity, anatomical, positivity, or
Bayesian priors stabilize the solution. These approaches expose the data
fidelity and physics but may be slow and sensitive to regularization choices,
initialization, calibration, and mesh/model error.

### Fully learned inversion

A network learns a direct map from measurements or an initial reconstruction to
an image. Inference can be fast, but performance depends on whether training
simulations reproduce the actual neonatal anatomy, noise, optical properties,
probe coupling, and instrument response. A realistic-looking output is not
evidence of quantitative correctness.

### Model-based learned iteration

Physics-based data-consistency steps are interleaved with learned components,
such as learned updates or learned regularizers. This is a promising bridge for
the BORL project: it can accelerate reconstruction and learn image structure
while retaining an explicit relationship to measured data. It still requires
out-of-distribution testing, calibration, and uncertainty evaluation.

## Open papers to study

1. **Dehghani et al. (2009), “Near infrared optical tomography using NIRFAST.”**
   Study the least-squares reconstruction, Jacobian construction, spectral
   inversion, regularization, stopping criteria, and use of different meshes to
   avoid an inverse crime.
   [Open full text at PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2826796/).
2. **Mozumder et al. (2022), “A model-based iterative learning approach for
   diffuse optical tomography.”** This is the best bridge between the vacancy's
   numerical-inverse and PyTorch/ML requirements. It interleaves model-based and
   learned components, tests simulated and experimental data, and discusses
   compensation for coarse-discretization error.
   [Open accepted manuscript](https://oulurepo.oulu.fi/bitstream/handle/10024/31026/nbnfi-fe2021122262966.pdf?sequence=1&isAllowed=y)
   ([preprint](https://arxiv.org/abs/2104.09579),
   [DOI](https://doi.org/10.1109/TMI.2021.3136461)).
3. **Yoo et al. (2020), “Deep Learning Diffuse Optical Tomography.”** Read as a
   contrasting learned inversion. Concentrate on how the physics motivates the
   network, what data train it, and whether simulation-to-experiment transfer is
   sufficient for neonatal use.
   [Open preprint](https://arxiv.org/abs/1712.00912)
   ([DOI](https://doi.org/10.1109/TMI.2019.2936522)).

## Validation rules for a clinical reconstruction

Never judge an algorithm only by a clean example image. Compare methods on:

- data residuals and held-out measurements;
- localization and depth error;
- absorption/scattering contrast recovery and cross-talk;
- spatial resolution and ability to separate two inclusions;
- sensitivity to photon counts, background properties, and geometry errors;
- calibration and instrument-response mismatch;
- performance on unseen anatomies and acquisition conditions;
- computation time and memory; and
- uncertainty calibration and failure detection.

The training and test simulations must not share an unrealistically identical
forward model. That would be an inverse crime or a closely related form of data
leakage and would overstate clinical performance.

## Tonight's study exercise

- [ ] Derive the linearized regularized least-squares update for a toy problem:

      \[
      \Delta x=(J^T W^T WJ+\lambda L^TL)^{-1}
      J^T W^T W\left(y-F(x_k)\right).
      \]
- [ ] Explain the role of \(J\), \(L\), and \(\lambda\) without mathematical
      jargon.
- [ ] Make a comparison table for conventional, fully learned, and hybrid
      reconstruction: speed, interpretability, domain-shift risk, and
      validation burden.
- [ ] Propose one train/validation/test split that separates phantom geometry
      and optical-property conditions.
- [ ] Specify three failure flags that should stop a neonatal image from being
      interpreted clinically.

## Application-ready understanding

A defensible statement after this study is:

> I am especially interested in hybrid reconstruction that combines a
> diffusion-model data-consistency step with learned regularization, evaluated
> against conventional iterative baselines under realistic geometry,
> calibration, and noise mismatch.

This is a research interest grounded in paper study, not a claim that BORL has
already chosen this design or that it is automatically safer than a conventional
solver.

## Concepts

The inverse algorithm must balance three things: agreement with measured data,
physical credibility, and prior information. Machine learning is most useful
when it improves that balance measurably and its failure domain is tested—not
when it merely produces sharper-looking images.
