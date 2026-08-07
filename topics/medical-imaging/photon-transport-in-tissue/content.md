---
title: "Photon Transport in Scattering Tissue"
topic: medical-imaging
author: Wei-Che Hung
---

# Photon Transport in Scattering Tissue

## Near-Infrared Optical Tomography

Near-infrared optical tomography uses near-infrared light introduced at the
surface of tissue and measurements of the emerging light to reconstruct
three-dimensional optical properties inside the tissue. These properties can
then provide information about blood volume and oxygenation.

Biological tissue is strongly scattering. A photon detected after travelling
through tissue generally follows a long, irregular path rather than a straight
ray. The forward problem predicts detector measurements from known geometry,
sources, and optical properties.

## Optical Properties

The absorption coefficient $\mu_a$ describes photon loss by absorption. The
scattering coefficient $\mu_s$ describes the frequency of scattering events,
while the anisotropy factor $g$ describes their average directionality. The
reduced scattering coefficient is

$$
\mu_s'=\mu_s(1-g).
$$

This reduced coefficient is useful because many highly forward-directed
scattering events can be represented as fewer effectively isotropic events.

The meaning of directional memory, transport length, and the approximation
behind $\mu_s'=\mu_s(1-g)$ are developed in
[Reduced Scattering Coefficient in Biomedical Optics](../reduced-scattering-coefficient/content.md).

The microscopic origin of an interaction coefficient and its exponential
survival law are derived separately in
[From Cross Section to Interaction Coefficient](../cross-section-to-interaction-coefficient/content.md).

## Radiative Transfer and Diffusion

The radiative transfer equation tracks radiance as a function of position,
direction, and time. Monte Carlo simulation approximates this process by
sampling many photon histories. It is flexible and physically detailed but can
be computationally expensive.

When scattering dominates absorption and the region is sufficiently far from
sources and boundaries, photon transport is often approximated by the
time-domain diffusion equation

$$
\frac{1}{c}\frac{\partial \Phi(\mathbf r,t)}{\partial t}
-\nabla\cdot\left[D(\mathbf r)\nabla\Phi(\mathbf r,t)\right]
+\mu_a(\mathbf r)\Phi(\mathbf r,t)
=q(\mathbf r,t),
$$

where $\Phi$ is photon fluence rate, $c$ is light speed in the medium,
$q$ is the source, and

$$
D(\mathbf r)=\frac{1}{3\left(\mu_a(\mathbf r)+\mu_s'(\mathbf r)\right)}
$$

is a commonly used diffusion coefficient.

The diffusion approximation is less accurate near sources and boundaries, in
low-scattering regions, and for the earliest arriving photons. Boundary
conditions must also account for refractive-index mismatch between tissue and
the surrounding medium.

## Time-Resolved Measurement

A short optical pulse broadens as photons take different paths through tissue.
The detector records a temporal point-spread function: a histogram of photon
arrival times. Early photons usually sample shallower or less scattered paths.
Later photons tend to carry greater depth sensitivity, but they are fewer and
therefore noisier.

The measured histogram is also shaped by the source pulse and detector timing.
Forward modelling must include or calibrate this instrument-response function
before simulated and measured curves can be compared quantitatively.

## Finite-Element Solution

The finite-element method represents an irregular three-dimensional tissue
volume with a mesh. Optical properties are assigned to mesh elements or nodes,
and the diffusion equation is converted into a system of algebraic equations.
For every source, wavelength, and time point, the solution predicts fluence at
the detector positions.

Important modelling choices include:

- anatomical versus homogeneous geometry;
- mesh resolution;
- tissue-specific absorption and scattering;
- source and detector representation;
- boundary conditions;
- temporal sampling; and
- treatment of the instrument response.

An inverse algorithm repeatedly evaluates this forward model. Forward accuracy
and computational speed therefore directly affect reconstruction quality.

## References

- Dehghani et al., “Near infrared optical tomography using NIRFAST: Algorithm
  for numerical model and image reconstruction.”
  [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2826796/)
  ([DOI](https://doi.org/10.1002/cnm.1162)).
- Prakash et al., “GPU-Accelerated Finite Element Method for Modelling Light
  Transport in Diffuse Optical Tomography.”
  [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC3195519/).
- Lu et al., “New nonlocal forward model for diffuse optical tomography.”
  [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC6913415/)
  ([DOI](https://doi.org/10.1364/BOE.10.006227)).
- Jacques, “Optical properties of biological tissues: a review.”
  [Review and open data](https://omlc.org/news/dec14/Jacques_PMB2013/index.html)
  ([DOI](https://doi.org/10.1088/0031-9155/58/11/R37)).

## Concepts

The forward model connects tissue physics to observable measurements. Its
validity depends on the transport approximation, anatomical representation,
boundary conditions, numerical discretization, and instrument calibration.
