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

The absorption coefficient \(\mu_a\) describes photon loss by absorption. The
scattering coefficient \(\mu_s\) describes the frequency of scattering events,
while the anisotropy factor \(g\) describes their average directionality. The
reduced scattering coefficient is

\[
\mu_s'=\mu_s(1-g).
\]

This reduced coefficient is useful because many highly forward-directed
scattering events can be represented as fewer effectively isotropic events.

## From Cross Section to Interaction Coefficient

<details open>
<summary>Cross section, interaction coefficient, and exponential attenuation</summary>

![Handwritten derivation from microscopic cross section to macroscopic interaction coefficient](media/cross-section-to-interaction-coefficient.jpg)

</details>

The microscopic cross section \(\sigma\) is an effective interaction area for
one particle. If a homogeneous medium contains \(n\) particles per unit volume,
then a thin slab of area \(A\) and thickness \(dx\) contains

\[
N=nA\,dx
\]

particles. When the effective interaction areas do not overlap appreciably,
the probability of an interaction within this infinitesimal slab is

\[
P(\text{interaction in }dx)
\approx\frac{N\sigma}{A}
=n\sigma\,dx.
\]

The macroscopic interaction coefficient is therefore

\[
\boxed{\mu=n\sigma},
\]

with units of inverse length. Thus

\[
P(\text{interaction in }dx)\approx\mu\,dx.
\]

This is a local, infinitesimal approximation. The product \(\mu L\) is not, in
general, the probability of an interaction over a finite path \(L\).

### Survival over a finite path

Divide \(L\) into \(N\) intervals of width \(\Delta x=L/N\). For each small
interval,

\[
P(\text{no interaction in }\Delta x)
\approx 1-\mu\Delta x.
\]

Assuming a homogeneous medium and independent interactions, the probability of
no interaction over the entire path is

\[
P_0(L)
=\lim_{N\to\infty}
\left(1-\frac{\mu L}{N}\right)^N
=e^{-\mu L}.
\]

Equivalently, if \(S(x)\) denotes the probability of reaching \(x\) without an
interaction, then

\[
S(x+dx)=S(x)(1-\mu\,dx)
\]

leads to

\[
\frac{dS}{dx}=-\mu S,
\qquad
S(0)=1,
\]

whose solution is

\[
\boxed{S(x)=e^{-\mu x}}.
\]

The probability of at least one interaction within \(L\) is the complement:

\[
\boxed{
P(N\geq1)=1-e^{-\mu L}=1-e^{-n\sigma L}
}.
\]

For a thin slab, \(\mu L\ll1\), the Taylor expansion

\[
e^{-\mu L}\approx1-\mu L
\]

gives

\[
P(N\geq1)\approx\mu L.
\]

The linear expression is therefore a short-distance approximation. For a
finite path, the exponential is required to keep the probability between zero
and one.

### Poisson interpretation

Under the same homogeneous, independent-interaction assumptions, the number of
interactions along \(L\) is Poisson distributed:

\[
\boxed{
P(N=k)=\frac{(\mu L)^k}{k!}e^{-\mu L}
}.
\]

Its expected value is

\[
\mathbb E[N]=\mu L,
\]

whereas the probability of at least one interaction is
\(1-e^{-\mu L}\). These quantities are different.

For example, if \(\mu=2\ \mathrm{mm}^{-1}\) and
\(L=0.5\ \mathrm{mm}\), then \(\mu L=1\), so

\[
P(N=0)=e^{-1}\approx0.368
\]

and

\[
P(N\geq1)=1-e^{-1}\approx0.632.
\]

### Extinction versus absorption survival

If

\[
\mu_t=\mu_a+\mu_s,
\]

then

\[
e^{-\mu_tL}
\]

is the probability that a photon travels a straight path \(L\) without either
absorption or scattering. It describes the uncollided, or ballistic,
component—not the probability that the photon still exists.

A scattering event changes the photon direction but does not necessarily
destroy it. For a specified total travelled path length \(L\), absorption-only
survival is

\[
e^{-\mu_aL}.
\]

In a scattering medium, however, the actual travelled path is generally longer
than the straight source-detector separation and varies from photon to photon.
This distinction is central to diffuse optical imaging.

## Radiative Transfer and Diffusion

The radiative transfer equation tracks radiance as a function of position,
direction, and time. Monte Carlo simulation approximates this process by
sampling many photon histories. It is flexible and physically detailed but can
be computationally expensive.

When scattering dominates absorption and the region is sufficiently far from
sources and boundaries, photon transport is often approximated by the
time-domain diffusion equation

\[
\frac{1}{c}\frac{\partial \Phi(\mathbf r,t)}{\partial t}
-\nabla\cdot\left[D(\mathbf r)\nabla\Phi(\mathbf r,t)\right]
+\mu_a(\mathbf r)\Phi(\mathbf r,t)
=q(\mathbf r,t),
\]

where \(\Phi\) is photon fluence rate, \(c\) is light speed in the medium,
\(q\) is the source, and

\[
D(\mathbf r)=\frac{1}{3\left(\mu_a(\mathbf r)+\mu_s'(\mathbf r)\right)}
\]

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

## Concepts

The forward model connects tissue physics to observable measurements. Its
validity depends on the transport approximation, anatomical representation,
boundary conditions, numerical discretization, and instrument calibration.
