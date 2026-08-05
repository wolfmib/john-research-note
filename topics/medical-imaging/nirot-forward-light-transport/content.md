---
title: "NIROT Function 1: Forward Light-Transport Modelling"
topic: medical-imaging
project: uzh-borl-newborn-nirot
status: initial-literature-study-completed
created: 2026-08-05
author: Wei-Che Hung
---

# NIROT Function 1: Forward Light-Transport Modelling

**Initial literature synthesis completed:** 2026-08-05. The exercises below
are the next hands-on stage, not a prerequisite for using this note as evidence
of focused pre-application preparation.

## Research question

Given a pulsed near-infrared source, neonatal-head geometry, and spatially
varying tissue optical properties, how can we predict the photon fluence and
time-resolved detector measurements needed by an image-reconstruction system?

This is the first major function in the UZH/BORL PhD project. The vacancy asks
for implementation of forward models such as the diffusion equation using
finite-element or discrete-ordinate methods. A trustworthy inverse solver
cannot recover brain oxygenation if its forward physics, mesh, boundary
conditions, or instrument response are wrong.

## Physical model

Biological tissue in the near-infrared window is strongly scattering. The most
complete classical description is the radiative transfer equation (RTE), which
tracks radiance by position, direction, and time. Monte Carlo simulation
approximates this transport by sampling many photon histories and is valuable
as a reference, but it can be computationally expensive.

When scattering dominates absorption and the region is sufficiently far from
sources and boundaries, the RTE is often approximated by the time-domain
diffusion equation

\[
\frac{1}{c}\frac{\partial \Phi(\mathbf r,t)}{\partial t}
-\nabla\cdot\left[D(\mathbf r)\nabla\Phi(\mathbf r,t)\right]
+\mu_a(\mathbf r)\Phi(\mathbf r,t)
=q(\mathbf r,t),
\]

where \(\Phi\) is photon fluence rate, \(c\) is light speed in the medium,
\(\mu_a\) is the absorption coefficient, \(q\) is the source, and a common
diffusion coefficient is

\[
D(\mathbf r)=\frac{1}{3\left(\mu_a(\mathbf r)+\mu_s'(\mathbf r)\right)}.
\]

The reduced scattering coefficient \(\mu_s'=\mu_s(1-g)\) incorporates the
anisotropy factor \(g\). A Robin-type boundary condition models refractive-index
mismatch at the tissue surface. In practice, source pulse width and the
instrument-response function must also be represented or calibrated because
the SPAD records a blurred distribution of photon arrival times, not an ideal
diffusion-equation solution.

## Numerical function

Finite-element modelling converts an irregular, possibly tissue-labelled 3D
head domain into a mesh and a system of equations. For every source and
wavelength, the solver predicts boundary measurements at the detector
locations. The same forward operator is repeatedly evaluated by the inverse
algorithm, so accuracy and computational cost are coupled.

The key modelling decisions are:

- diffusion approximation versus RTE/discrete ordinates or Monte Carlo;
- realistic neonatal anatomy versus a homogeneous or layered domain;
- mesh resolution and optical-property assignment by tissue class;
- source and detector coupling, boundary conditions, and refractive mismatch;
- full time-point curves versus temporal gates or moments; and
- calibration of the laser pulse and detector instrument response.

The diffusion approximation becomes least reliable near sources and
boundaries, in low-scattering or highly absorbing regions, and at very early
photon-arrival times. These are not minor details: model discrepancy can be
misinterpreted by the inverse solver as a false absorption or scattering
change.

## Open papers to study

1. **Dehghani et al. (2009), “Near infrared optical tomography using NIRFAST:
   Algorithm for numerical model and image reconstruction.”** This is the main
   foundation. Sections on the diffusion approximation, FEM, spectral
   reconstruction, Jacobian, and inverse crime directly match the vacancy.
   [Open full text at PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC2826796/)
   ([DOI](https://doi.org/10.1002/cnm.1162)).
2. **Prakash et al. (2011), “GPU-Accelerated Finite Element Method for
   Modelling Light Transport in Diffuse Optical Tomography.”** Use this to see
   steady-state, frequency-domain, and time-domain formulations together and
   understand why forward-solver acceleration matters inside iterative
   reconstruction.
   [Open full text at PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC3195519/).
3. **Lu et al. (2019), “A new nonlocal forward model for diffuse optical
   tomography.”** This optional extension compares classical diffusion/FEM with
   a nonlocal graph-based model and makes the speed-versus-model-fidelity tradeoff
   explicit.
   [Open manuscript](https://arxiv.org/abs/1906.00882)
   ([DOI](https://doi.org/10.1364/BOE.10.006227)).

## Tonight's study exercise

- [ ] Draw the map \((\mu_a,\mu_s',\text{geometry},q)\mapsto\Phi\mapsto y\),
      where \(y\) is a detector time-of-flight histogram.
- [ ] Explain in plain language why late photons usually probe deeper tissue
      but arrive with lower signal-to-noise ratio.
- [ ] List four ways that simulated measurements may differ from the BORL
      Pioneer instrument.
- [ ] Write pseudocode for a source-by-source FEM forward solve at multiple
      wavelengths and times.
- [ ] Record when diffusion, discrete ordinates, and Monte Carlo would each be
      selected for neonatal-head modelling.

## Application-ready understanding

A defensible statement after this study is:

> I studied how time-domain NIROT forward modelling connects tissue absorption
> and reduced scattering to SPAD photon-arrival measurements, including FEM
> discretization, boundary conditions, instrument response, and the limitations
> of the diffusion approximation.

This demonstrates preparation and transferable numerical-physics experience.
It must not be presented as prior implementation of a neonatal NIROT solver.

## Concepts

Forward modelling is the physics engine of NIROT. Its purpose is not merely to
generate a plausible light field; it must predict the particular measurements
made by the real instrument accurately and quickly enough to support repeated,
quantitative inverse reconstruction.
