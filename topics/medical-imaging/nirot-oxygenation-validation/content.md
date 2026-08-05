---
title: "NIROT Function 3: Quantitative Oxygenation and Clinical Validation"
topic: medical-imaging
project: uzh-borl-newborn-nirot
status: initial-literature-study-completed
created: 2026-08-05
author: Wei-Che Hung
---

# NIROT Function 3: Quantitative Oxygenation and Clinical Validation

**Initial literature synthesis completed:** 2026-08-05. The exercises below
are the next hands-on stage, not a prerequisite for using this note as evidence
of focused pre-application preparation.

## Research question

How can multi-wavelength, time-resolved NIROT measurements become quantitative
3D maps of neonatal cerebral oxygenation, and what evidence is required before
those maps can be trusted in an intensive-care setting?

This is the translational function of the UZH/BORL project. The advertised goal
is not a generic optical image: it is precise, quantitative imaging of brain
oxygenation, validated first in phantoms and then with volunteer and patient
data. The intended clinical targets include hypoxia, ischemia, and hemorrhage
in preterm and term newborns.

## From optical coefficients to physiology

At wavelength \(\lambda\), tissue absorption can be represented approximately
as a mixture of chromophore contributions:

\[
\mu_a(\lambda)=
\epsilon_{\mathrm{HbO_2}}(\lambda)c_{\mathrm{HbO_2}}
+\epsilon_{\mathrm{Hb}}(\lambda)c_{\mathrm{Hb}}
+\sum_j\epsilon_j(\lambda)c_j,
\]

where \(\epsilon\) denotes an extinction coefficient and \(c\) a concentration.
With enough appropriately chosen wavelengths and a calibrated spectral model,
reconstructed absorption values can be unmixed into oxygenated hemoglobin
\(c_{\mathrm{HbO_2}}\) and deoxygenated hemoglobin \(c_{\mathrm{Hb}}\). Then

\[
\mathrm{HbT}=c_{\mathrm{HbO_2}}+c_{\mathrm{Hb}},
\qquad
\mathrm{StO_2}=\frac{c_{\mathrm{HbO_2}}}{\mathrm{HbT}}.
\]

This simple final ratio hides important dependencies: wavelength selection,
extinction spectra, water and lipid assumptions, wavelength-dependent
scattering, source coupling, calibration, partial-volume effects, superficial
tissue, head geometry, and cross-talk between absorption and scattering.

Time-domain measurement adds depth information through the temporal point-spread
function. Later-arriving photons have generally travelled longer and sampled
deeper tissue, while early photons are more influenced by superficial paths.
However, late gates contain fewer photons and are more vulnerable to noise. A
quantitative pipeline must therefore balance depth sensitivity with photon
statistics and correct for the instrument-response function.

## Evidence ladder

Validation should progress through increasingly realistic levels:

1. **Digital simulation:** known ground truth, controlled noise and model
   mismatch; useful for debugging but not proof of real-world performance.
2. **Homogeneous optical phantom:** tests localization, depth, contrast, and
   repeatability under calibrated optical properties.
3. **Anatomically realistic or dynamic phantom:** adds curved geometry, tissue
   layers, probe placement, and controlled temporal changes.
4. **Healthy volunteer or stable neonatal measurements:** evaluates fitting,
   motion, repeatability, comfort, and physiologically plausible ranges.
5. **Patient study:** tests feasibility and association with clinical events or
   reference measurements; it does not by itself establish diagnostic benefit.

At every level, report failure cases and uncertainty. For a newborn application,
probe pressure, heating, laser exposure, electrical safety, biocompatibility,
motion, acquisition time, cleaning, and workflow are part of validity—not
separate from the reconstruction science.

## Open papers to study

1. **Russomanno et al. (2022), “Resolution and penetration depth of
   reflection-mode time-domain near infrared optical tomography using a ToF
   SPAD camera.”** This BORL paper is the closest open technical match to the
   advertised system. It evaluates a 1024-pixel SPAD-camera NIROT setup using
   movable liquid-phantom inclusions, 1 s versus 100 s exposures, depths up to
   30 mm, two-target resolution, RMSE, PSNR, and Dice.
   [Open full text at PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC9774846/)
   ([DOI](https://doi.org/10.1364/BOE.470243)).
2. **Puszka et al. (2013), “Time-resolved diffuse optical tomography using
   fast-gated single-photon avalanche diodes.”** This open experiment explains
   why time gating can improve detection and localization of deep absorbing
   inclusions at short source-detector distances.
   [Open full text at PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC3756586/)
   ([DOI](https://doi.org/10.1364/BOE.4.001351)).
3. **Austin et al. (2006), “Three dimensional optical imaging of blood volume
   and oxygenation in the neonatal brain.”** This provides direct clinical
   context: acquisition and reconstruction of 3D blood-volume and oxygenation
   images from newborn infants, including unsuccessful data sets that reveal
   the gap between technical possibility and clinical robustness.
   [Open manuscript at UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/2995/)
   ([DOI](https://doi.org/10.1016/j.neuroimage.2006.02.038)).
4. **Dehaes et al. (2017), “Shedding light on the neonatal brain: probing
   cerebral hemodynamics by diffuse optical spectroscopic methods.”** Use this
   for neonatal physiology and interpretation of cerebral blood flow,
   hemoglobin concentration, oxygen saturation, and oxygen metabolism.
   [Open full text at PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC5693925/)
   ([DOI](https://doi.org/10.1038/s41598-017-15995-1)).

## Tonight's study exercise

- [ ] Explain why two or more wavelengths are needed to separate HbO2 and Hb.
- [ ] Create a table mapping each output—\(\mu_a\), \(\mu_s'\), HbO2, Hb, HbT,
      and StO2—to its unit, biological meaning, and main source of uncertainty.
- [ ] Summarize BORL's 1 s versus 100 s phantom result and explain why acquisition
      time matters clinically.
- [ ] Design a minimum phantom-validation matrix spanning target depth, size,
      contrast, wavelength, photon count, and probe placement.
- [ ] Write three acceptance criteria and three failure criteria for moving from
      phantom testing to a volunteer study.

## Three informed questions for BORL

1. Which representation of the time-of-flight data is currently most useful for
   Pioneer reconstruction: full curves, temporal gates, moments, or a hybrid?
2. What currently dominates quantitative error in oxygenation maps—forward-model
   mismatch, calibration/instrument response, probe coupling and geometry, or
   inverse regularization?
3. How will the project validate uncertainty and domain transfer when moving
   from simulations and phantoms to individual neonatal anatomies and clinical
   measurements?

## Application-ready understanding

A defensible statement after this study is:

> I understand the project as an end-to-end quantitative measurement problem:
> time-resolved multispectral acquisition, optical-property reconstruction,
> spectral unmixing, and staged validation from known phantoms to clinical data.
> My medical-image analysis and uncertainty work motivates particular interest
> in validation and failure characterization.

This states informed motivation and transferable experience without claiming
prior neonatal, NIROT, or clinical-device expertise.

## Concepts

An oxygenation image is credible only when the entire chain is validated. The
clinical quantity inherits uncertainty from photon counting, calibration,
forward modelling, inverse regularization, spectral unmixing, anatomy, and
patient motion. Quantitative validation must track those links rather than hide
them behind the final color map.
