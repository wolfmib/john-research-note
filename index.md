# Research Note Index

## Reading Queue

Suggested papers that have been collected but are not yet understood well
enough to become topics are tracked in the
[ready-to-read paper index](papers/index.md).

## Statistics

| Topic | Question | Status |
|---|---|---|
| [Confidence intervals for a process mean](topics/statistics/confidence-interval-for-process-mean/content.md) | Does a sample support the intended 100 cm process mean? | Concept note |
| [Comparing two vectors: projection, correlation, and distance](topics/statistics/comparing-two-vectors/content.md) | Does similarity mean directional alignment, centered-pattern agreement, or numerical proximity? | Concept note |
| [Reference-to-group vector features with mean and standard deviation](topics/statistics/comparing-two-groups-of-vectors/content.md) | How can projection, correlation, and distance to a reference reduce each vector group to six fixed features? | Concept note |
| [TRC vector geometry: projection, correlation, and distance](topics/statistics/trc-vector-geometry/content.md) | How do thermal recovery curves become 600-dimensional vectors, and which metric answers shape, direction, or distance? | Concept note |

## Machine Learning

The classical classification family, told as characters — one overview with the
handwritten pages, then one note per method (math + worked example + SVG figure).

| Topic | Question | Status |
|---|---|---|
| [The ML family for medical classification](topics/machine-learning/ml-family-for-medical-classification/content.md) | Which classical ML methods form the skin-cancer toolkit, and what one question does each ask? | Concept note |
| [PCA — Mr. Variance](topics/machine-learning/pca-mr-variance/content.md) | Which directions carry the variance of unlabeled lesion data? | Concept note |
| [ICA — The Source Detective](topics/machine-learning/ica-source-detective/content.md) | Can independent hidden sources be recovered from mixed measurements? | Concept note |
| [KNN — Ask Your Neighbours](topics/machine-learning/knn-ask-your-neighbours/content.md) | Can a new case be classified purely by its closest labelled neighbours? | Concept note |
| [Decision Tree — The Question Man](topics/machine-learning/decision-tree-question-man/content.md) | Which yes/no question splits the diagnosis best, and how is that measured? | Concept note |
| [Random Forest — The Tree Army](topics/machine-learning/random-forest-tree-army/content.md) | Can many deliberately different trees vote their way past one tree's overfitting? | Concept note |
| [LDA — The Class Separator](topics/machine-learning/lda-class-separator/content.md) | Which direction makes the classes look most separated — far between, tight within? | Concept note |
| [SVM — The Margin Master](topics/machine-learning/svm-margin-master/content.md) | Among all separating hyperplanes, why is the widest corridor the one to trust? | Concept note |
| [RBF-SVM — SVM Learns to Curve](topics/machine-learning/rbf-svm-curved-margin/content.md) | How does the margin philosophy survive when the boundary must bend? | Concept note |

## Thermal Dynamics

| Topic | Question | Status |
|---|---|---|
| [Thermal dynamics of recovery and TRC geometry](topics/thermal-dynamics/content.md) | How do lesion recovery, coupled thermal diffusion, and TRC-vector comparison combine into one paper-ready study framework? | Concept note |

## Medical Imaging

### Diffuse Optical Imaging

Three connected technical topics describe the measurement chain:

| Function | Topic | Core question | Status |
|---|---|---|---|
| Foundation | [From cross section to interaction coefficient](topics/medical-imaging/cross-section-to-interaction-coefficient/content.md) | How does a microscopic interaction area produce a macroscopic attenuation law? | Concept note |
| Foundation | [Reduced scattering coefficient in biomedical optics](topics/medical-imaging/reduced-scattering-coefficient/content.md) | How do scattering frequency and directional memory combine into a transport coefficient? | Concept note |
| 1 | [Photon transport in scattering tissue](topics/medical-imaging/photon-transport-in-tissue/content.md) | How do tissue optical properties produce time-resolved boundary measurements? | Concept note |
| 2 | [Inverse reconstruction in optical tomography](topics/medical-imaging/inverse-reconstruction-in-optical-tomography/content.md) | How can absorption and scattering maps be reconstructed from an ill-posed inverse problem? | Concept note |
| 3 | [Optical imaging of tissue oxygenation](topics/medical-imaging/optical-imaging-of-tissue-oxygenation/content.md) | How do multi-wavelength optical properties become quantitative oxygenation maps? | Concept note |

The functions form one measurement chain:

`pulsed near-infrared source -> photon transport -> time-resolved measurements -> inverse reconstruction -> spectral unmixing -> oxygenation map`

## Physics

No public topic added yet.

## Quantum Computing

| Topic | Question | Status |
|---|---|---|
| [Grover search for a subset-sum problem](topics/quantum-computing/grover-search-for-subset-sum/content.md) | How does a verification rule become a phase oracle that amplitude amplification can amplify? | Concept note |
| [QSVT pseudoinverse for a 2D affine mapping](topics/quantum-computing/qsvt-pseudoinverse-for-affine-mapping/content.md) | How does a rectangular least-squares fit become a polynomial applied to singular values, read out by postselection? | Concept note |

## Animations

Animated SVG concept figures (GitHub plays the SMIL animation inline).

| Topic | Question | Status |
|---|---|---|
| [Grover's iteration: the 2θ rotation](topics/animations/grover-iteration-2theta-rotation/content.md) | Why do the oracle reflection and the diffusion reflection compose into one rotation by 2θ toward the marked state? | Concept note |
| [Harmonic Growth and the Euler–Mascheroni Constant](topics/animations/harmonic-growth-euler-mascheroni-gamma/content.md) | Why does H_N − ln N settle to γ ≈ 0.5772? | Concept note |
| [Derivation of the Harmonic Sum Identity](topics/animations/harmonic-sum-identity-derivation/content.md) | Why does the running sum of harmonic numbers equal N(H_N − 1)? | Concept note |
| [Removable Discontinuity — The Hole in a Rational Function](topics/animations/removable-discontinuity-hole-rational-function/content.md) | Why does cancelling a common factor leave a hole at (4, 2) instead of an asymptote? | Concept note |
| [NumPy to Geometry — A (4, 2) Marker Array and Its Centroid](topics/animations/numpy-marker-array-centroid-mean-axis0/content.md) | What does markers.mean(axis=0) compute, geometrically, for a (4, 2) array of point coordinates? | Concept note |
| [Design Matrix Rows [x, y, 1] with reshape and hstack](topics/animations/numpy-design-matrix-reshape-hstack/content.md) | How do reshape(-1, 2), np.ones and np.hstack build the affine design matrix whose rows are [x, y, 1]? | Concept note |
| [Graphing a Rational Function — Zeros, Intercept, Asymptotes](topics/animations/rational-function-graph-zeros-intercept-asymptotes/content.md) | How do the zeros, the y-intercept, the slant asymptote from polynomial division and the vertical asymptote fix the graph of f(x) = (x−2)(x+1)/(x−3)? | Concept note |

## Field Notes

Short notes on one idea at a time, worked through in several languages with the vocabulary
alongside. See the [field note index](field-notes/index.md).
