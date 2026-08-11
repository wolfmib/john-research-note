---
title: "QSVT Pseudoinverse for a 2D Affine Mapping"
topic: quantum-computing
example: five-point-affine-fit
status: concept-note
created: 2026-08-11
author: Wei-Che Hung
---

# QSVT Pseudoinverse for a 2D Affine Mapping

> **Scope — this is a teaching exercise, not an application proposal.**
>
> The construction below still depends on classical linear algebra applied to the very
> matrix it sets out to invert. The normalization $\alpha=\|Z\|_2$ comes from a classical
> SVD, and assembling the block encoding requires forming $A^{T}A$ and taking a matrix
> square root. Once that much classical work has been done, the affine fit is already
> solved — a least-squares call returns $B$ immediately, and does so faster than
> constructing the circuit. No speedup is claimed here, and none exists at this scale.
>
> The value is familiarity. A concrete classical formulation — an affine map recovered by
> least squares — is carried step by step onto quantum machinery, so that block encoding,
> singular value transformation, success/failure normalization and postselected readout
> become specific operations on a specific matrix rather than abstractions. The exercise
> is practice in mapping a known classical problem onto quantum technique, and should be
> read that way rather than as a recommendation for solving affine problems.

## Research Question

Given five point correspondences related by an unknown affine transformation, can a
quantum circuit recover that transformation by applying a polynomial to the singular
values of the data matrix, rather than by solving the normal equations?

Concretely, let the source points be written in homogeneous form, $Z_i=[x_i,\ y_i,\ 1]$,
and collected into

$$
Z=\begin{bmatrix} 0&0&1 \\ 1&0&1 \\ 0&1&1 \\ 1&1&1 \\ 2&-1&1 \end{bmatrix}
\in\mathbb{R}^{5\times3},
$$

and let an unknown $B\in\mathbb{R}^{3\times2}$ act on them so that $Y=ZB$, with

$$
B_{\mathrm{true}}=\begin{bmatrix} 1.2&-0.4 \\ 0.5&1.1 \\ 2.0&-1.0 \end{bmatrix},
\qquad
Y=\begin{bmatrix} 2.0&-1.0 \\ 3.2&-1.4 \\ 2.5&0.1 \\ 3.7&-0.3 \\ 3.9&-2.9 \end{bmatrix}.
$$

After $Y$ is generated, $B_{\mathrm{true}}$ is discarded and the task is to recover it from
$Z$ and $Y$ alone.

The interest is not in the arithmetic, which is trivial classically, but in the
structure of the quantum route. Three obstacles have to be cleared, and each one is a
general feature of applying quantum linear algebra rather than an artefact of this
example: a rectangular matrix is not a unitary and cannot be applied directly; the
reciprocal $1/\sigma$ is unbounded and cannot be an amplitude transformation; and the
resulting map is not norm-preserving, so it cannot be the whole of a quantum evolution.

## Classical Reference

The affine fit is ordinary least squares. Splitting $Y$ and $B$ by column gives two
independent problems, $Z\beta_x=y_x$ and $Z\beta_y=y_y$, each solved by the
pseudoinverse:

$$
\beta = Z^{+}y, \qquad Z^{+}=V\Sigma^{-1}W^{T} \ \text{ for } \ Z=W\Sigma V^{T}.
$$

Because $Y$ was generated without noise and $Z$ has full column rank, the fit is exact:
$\|B_{\mathrm{classical}}-B_{\mathrm{true}}\|_F=8.5\times10^{-16}$. That exactness is the reason
this dataset is useful — any deviation in the quantum result is attributable to the
quantum construction, not to the statistics of the fit.

The singular values of $Z$ are $(3.0875,\ 1.9594,\ 0.7928)$, a condition number of
$\kappa=3.89$. This is a benign problem, deliberately so.

The normal-equation form $B=(Z^{T}Z)^{-1}Z^{T}Y$ gives the same answer but is
specifically what the quantum route must avoid. Forming $Z^{T}Z$ squares the condition
number, and more importantly it discards the structure — the singular values of $Z$
itself — that the quantum method operates on.

## Fitting a Rectangular Matrix Inside a Unitary

Quantum evolution is unitary. $Z$ is $5\times3$: not unitary, not even square. The
standard resolution is a **dilation** — embed the matrix in the corner of a larger
unitary and pad the remaining blocks with whatever makes the columns orthonormal.

The padding only exists if the matrix is a contraction, so $Z$ is first normalized by
$\alpha=\|Z\|_2=3.0875$, giving $A=Z/\alpha$ with every singular value in $[0,1]$. Then
the Halmos dilation

$$
U_A=\begin{bmatrix} A & \sqrt{I_5-AA^{T}} \\ \sqrt{I_3-A^{T}A} & -A^{T} \end{bmatrix}
$$

is unitary. The verification is short and worth seeing, because it is the intertwining
identity $A^{T}f(AA^{T})=f(A^{T}A)A^{T}$ doing all the work. The two column blocks have
Gram matrices

$$
A^{T}A+(I_3-A^{T}A)=I_3,
\qquad
(I_5-AA^{T})+AA^{T}=I_5,
$$

and the cross term is
$A^{T}\sqrt{I_5-AA^{T}}-\sqrt{I_3-A^{T}A}\,A^{T}=0$ by the identity. Numerically,
$\|U_A^{T}U_A-I\|=3.0\times10^{-15}$.

The dimensions cooperate: $5+3=8=2^{3}$, so the entire dilation is a single three-qubit
register.

<details open>
<summary>The dilation, and the two subspaces it contains</summary>

![Left: heat map of the eight-by-eight Halmos dilation with its four blocks outlined and labelled A, square root of I5 minus A A transpose, square root of I3 minus A transpose A, and minus A transpose. Right: a diagram of the eight computational basis states of a three-qubit register, showing the five-dimensional data subspace covering states zero through four and the three-dimensional parameter subspace covering states zero through two, overlapping on the first three](media/qsvt-affine-block-encoding.png)

</details>

## Two Subspaces in One Register

Because the problem is rectangular, the input space and the output space are genuinely
different objects that happen to share a register. The data space
$\mathcal{H}_L\simeq\mathbb{C}^5$ holds $|y\rangle$ and occupies basis states
$|0\rangle$ through $|4\rangle$; the parameter space
$\mathcal{H}_R\simeq\mathbb{C}^3$ holds $|\beta\rangle$ and occupies $|0\rangle$ through
$|2\rangle$.

These two subspaces **overlap**. That is not a defect of the encoding, and it has a
consequence that shapes the whole readout: success is a question about *where in the
register the output landed*, not a value read off a separate flag qubit.

## The Pseudoinverse as a Function of Singular Values

Writing $A=W\Sigma V^{T}$, the pseudoinverse $A^{+}=V\Sigma^{-1}W^{T}$ keeps the singular
vectors untouched and replaces each singular value by its reciprocal. Quantum singular
value transformation (QSVT) is precisely the machinery for applying a polynomial to the
singular values of a block-encoded matrix without ever constructing $W$ or $V$. The
pseudoinverse therefore becomes a question about polynomials:

$$
\text{find } p \text{ with } p(\sigma)\approx C/\sigma .
$$

The direction of the transform requires care, and getting it backwards is the most
natural mistake available. QSVT driven by $U_A$ with the projector pair
$(\Pi_L,\Pi_R)$ produces $W\,p(\Sigma)\,V^{T}$ — the same direction as $A$ itself,
mapping parameters to data. The pseudoinverse needs the adjoint direction
$V\,p(\Sigma)\,W^{T}$. The fix is to drive the alternating sequence with $U_A^{T}$ and
swap the projectors, using $\Pi_R U_A^{T}\Pi_L=A^{T}$.

## Choosing the Polynomial

The reciprocal cannot be implemented as written. Any amplitude transformation is bounded
by 1 in modulus, and $1/\sigma$ diverges at the origin. The constant $C$ buys the
necessary headroom, at the cost of shrinking the output — and therefore, as will be seen,
the success probability, which scales as $C^{2}$.

The textbook construction asks for a minimax approximation of $C/x$ across the whole
interval $[\sigma_{\min},\sigma_{\max}]$. That is the honest general-purpose answer and
it is expensive: at $\kappa=3.89$, degree 19 still leaves about 1% relative error, which
caps the achievable fidelity.

For this problem there is a shortcut worth naming explicitly, because it is a
simplification rather than a general method. $Z$ has exactly **three** singular values.
Whatever $p$ does elsewhere cannot affect $\beta$. So the polynomial can be obtained from
a linear program that pins $p(\sigma_i)=C/\sigma_i$ as hard equality constraints while
minimizing $\sup|p|$ over $[-1,1]$. At degree 9 and $C=0.85\,\sigma_{\min}$ this yields an
*exact* singular value transform with $\sup|p|=0.85$, a deliberate margin below the hard
bound.

<details open>
<summary>The polynomial against the reciprocal it approximates, and the cost of the general approach</summary>

![Left: the degree-nine odd polynomial plotted across minus one to one, staying inside the horizontal bounds at plus and minus one, and touching the dashed reciprocal curve C over sigma exactly at three marked points. Right: a log-scale plot of maximum relative error against polynomial degree, showing minimax approximation over the whole interval falling slowly from ten percent at degree five to one percent at degree nineteen, against a flat line at machine precision for exact interpolation at the three singular values](media/qsvt-affine-polynomial-vs-reciprocal.png)

</details>

## Finding the Phase Angles

QSVT applies $p$ by interleaving the block encoding with projector-controlled phase
rotations $e^{i\varphi_k(2\Pi-I)}$. Determining the angles $\varphi_k$ that produce a
prescribed $p$ is a separate problem with its own literature.

The route taken here relies on the singular value decomposition theorem underlying QSVT:
phases that reproduce $p$ in the scalar $1\times1$ case reproduce it unchanged on the
full block encoding. The fit is therefore performed on $2\times2$ matrices — evaluate
$\langle 0|V(\Phi)|0\rangle$ across Chebyshev nodes, then least-squares the angles
against $p$ — and the result is reused verbatim in eight dimensions. From a zero initial
guess it converges to a maximum error of $6.7\times10^{-16}$.

This is the only step in the construction that can genuinely fail to converge, so in the
implementation it is a gate: the scalar fit is verified before any circuit is built.

## The Real Part Problem

A quantum signal processing sequence places a **complex** polynomial in the block; only
its real part is the $p$ that was designed. It is tempting to assume the imaginary part
is negligible. Here it is not — at the three singular values it takes the values
$(-0.976,\ +0.871,\ -0.103)$, large and different at each.

That difference is what makes it fatal rather than merely untidy. A complex $p(\sigma_i)$
rotates each singular component by its own phase, and the recombined vector is no longer
proportional to $\beta$.

Because $U_A$ is real, $V(-\Phi)=\overline{V(\Phi)}$, so a Hadamard sandwich on one
additional qubit, with postselection on $|0\rangle$, extracts

$$
\tfrac{1}{2}\left(V(\Phi)+\overline{V(\Phi)}\right)=\operatorname{Re}V(\Phi).
$$

The construction is cheaper than it first appears: only the phase angles need to know
about the extra qubit. A single $R_{ZZ}$ coupling ties their sign to it, so the block
encoding itself is never controlled.

<details open>
<summary>One projector-controlled phase rotation</summary>

![Circuit diagram of five qubits labelled sys zero, sys one, sys two, anc and lcu. Three multi-controlled X gates flip the anc qubit for the three basis states of the parameter subspace, an RZZ rotation couples anc to lcu, and the same three multi-controlled X gates uncompute the marking](media/qsvt-affine-phase-block.png)

</details>

## Success and Failure

The map the circuit implements, $M=V\,p(\Sigma)\,W^{T}$, stretches small singular values
and shrinks large ones. It is not unitary, and therefore cannot be the entirety of a
quantum evolution. The full output state is

$$
|\Psi_{\mathrm{out}}\rangle=|S\rangle M|y\rangle+|F\rangle|\phi_F\rangle,
\qquad
\|M|y\rangle\|^{2}+\|\phi_F\|^{2}=1 .
$$

The failure branch is not a leak or an implementation defect. It exists because unitarity
requires the total norm to be conserved while the desired branch is being rescaled, and
the missing norm has to live somewhere.

Writing the three success amplitudes explicitly, the identity to check before any
postselection is

$$
|A_1|^{2}+|A_2|^{2}+|A_3|^{2}+P_F=1 ,
$$

and only then is $P_S=|A_1|^{2}+|A_2|^{2}+|A_3|^{2}$ meaningful. For the $x$ column
$P_S=0.0523$ — roughly one shot in twenty is kept.

<details open>
<summary>Where the norm goes</summary>

![Two bar charts, one per output column, each showing three small bars for the squared success amplitudes and one tall bar for the failure probability, with the annotation that success plus failure equals one to six decimal places](media/qsvt-affine-success-failure.png)

</details>

Raising $C$ increases $P_S$ quadratically while pushing $\sup|p|$ toward the hard bound
of 1. The choice $C=0.85\,\sigma_{\min}$ sits deliberately short of that limit.

## Recovering the Scale

A quantum state carries no absolute magnitude, so the postselected register supplies only
the *direction* of $\beta$. The natural conclusion is that the overall scale requires
information the measurement does not provide.

That conclusion is wrong, and the reason is instructive. Because the polynomial is exact
at every singular value, the block is exactly $C\alpha Z^{+}$, so the success probability
is not an incidental quantity — it *is* the missing magnitude:

$$
P_S=\left(\frac{C\,\alpha\,\|\beta\|}{\|y\|}\right)^{2}
\qquad\Longrightarrow\qquad
\|\beta\|=\frac{\sqrt{P_S}\,\|y\|}{C\,\alpha},
$$

with $C$, $\alpha$ and $\|y\|$ all known in advance. This reproduces
$\|\beta_x\|=2.3853700$ and $\|\beta_y\|=1.5394804$ exactly, which is what converts a
recovered direction into the actual affine parameters.

## Recovering the Signs

Measuring the parameter register returns $|\beta_i|^{2}$, and the signs are lost. For
$\beta_x=(1.2,\ 0.5,\ 2.0)$ this is harmless. For $\beta_y=(-0.4,\ 1.1,\ -1.0)$ the
histogram collapses to the ratio $0.16:1.21:1$, which is equally consistent with all
three components being positive — so a histogram alone reports the wrong transformation.

Signs are phase information, and phase information requires interference. Inserting,
before measurement, the unitary that mixes one pair of basis states,

$$
G_{ij}:\ |i\rangle\mapsto\tfrac{1}{\sqrt2}(|i\rangle+|j\rangle),
\qquad
|j\rangle\mapsto\tfrac{1}{\sqrt2}(|i\rangle-|j\rangle),
$$

turns the amplitudes into $(\beta_i\pm\beta_j)/\sqrt2$, so that

$$
P(i)-P(j)=2\beta_i\beta_j .
$$

The sign of an observable difference is the sign of the product. Two pairs, $(0,1)$ and
$(0,2)$, determine every relative sign; for the $y$ column they are resolved at $z=33.9$
and $z=33.4$ from 40 000 shots. Because both indices lie inside the parameter subspace,
the mixing only redistributes amplitude within the success branch and leaves $P_S$
unchanged.

The overall sign of $\beta$ is genuinely unobservable: $|\beta\rangle$ and
$-|\beta\rangle$ are the same physical state.

## Simulation Results

<details open>
<summary>Shot distribution conditioned on success, 20 000 shots per column</summary>

![Two grouped bar charts comparing measured probabilities against theory for the three parameter basis states, one chart per output column, with measured and predicted bars visually indistinguishable](media/qsvt-affine-beta-histograms.png)

</details>

| Quantity | $x$ column | $y$ column |
|---|---|---|
| $\|y\|$ | $7.0278$ | $3.3867$ |
| Success probability $P_S$ | $0.05231$ | $0.09382$ |
| $P_S$ measured | $0.0531$ (1061 of 20 000) | $0.0972$ (1943 of 20 000) |
| State fidelity against classical $\beta$ | $1.000000000000$ | $1.000000000000$ |
| $\|\beta\|$ recovered from $P_S$ | $2.3853700$ (true $2.3853700$) | $1.5394804$ (true $1.5394804$) |
| Recovered $\beta$ | $(1.2,\ 0.5,\ 2.0)$ | $(-0.4,\ 1.1,\ -1.0)$ |

Assembling both columns:

$$
B_{\mathrm{quantum}}=\begin{bmatrix} 1.2&-0.4 \\ 0.5&1.1 \\ 2.0&-1.0 \end{bmatrix},
\qquad
\|B_{\mathrm{quantum}}-B_{\mathrm{true}}\|_F=2.9\times10^{-14}.
$$

The block itself matches the scaled classical pseudoinverse to
$\|\Pi_R\operatorname{Re}[V]\Pi_L-C\alpha Z^{+}\|=4.2\times10^{-15}$, and the Qiskit
circuit reproduces the numpy reference amplitude by amplitude to $2.5\times10^{-15}$.

## Circuit Cost

The circuit uses five qubits: three for the dilation, one ancilla for the
projector-controlled phase rotations, and one for the real-part projection. The phase
ancilla is computed and uncomputed inside each phase block and returns to $|0\rangle$
deterministically — measured residual probability $6.4\times10^{-31}$ — so it carries no
information and is not part of the postselection.

At degree 9 the sequence contains nine applications of the block encoding and nine phase
blocks, giving depth 77 and 84 operations before transpilation.

<details open>
<summary>The complete circuit</summary>

![Circuit diagram folded across three rows, showing state preparation of the target vector, a Hadamard on the lcu qubit, then nine alternating applications of the block encoding and its transpose separated by nine projector-controlled phase blocks each built from multi-controlled X gates and an RZZ coupling, closing with a second Hadamard on lcu](media/qsvt-affine-full-circuit.png)

</details>

The alternation between $U_A^{T}$ and $U_A$ is visible across the rows, as is the fact
that the block encoding is never controlled — only the $R_{ZZ}$ couplings touch the `lcu`
qubit. That count treats each
$8\times8$ block encoding as a single primitive, which is the appropriate accounting for
a lab whose purpose is the structure rather than the gate cost; a hardware estimate would
have to expand $U_A$ into elementary gates, and that expansion, not the QSVT layers,
would dominate.

No speedup is claimed. This is a $5\times3$ problem, the classical solve is instantaneous,
the block encoding is constructed by a classical SVD, and the simulation is a $32\times32$
matrix product. The construction is worth studying for its structure, not its cost.

Two limitations bear directly on how the result should be read. First, the block encoding
is *constructed* rather than queried — assembling the dilation requires
$\sqrt{I_3-A^{T}A}$, and $\alpha$ requires an SVD. The algorithm never solves the normal
equations $(Z^{T}Z)\beta=Z^{T}y$, which is the property that matters, but any speedup
claim would have to rest on obtaining $U_A$ from a data-structure oracle instead. Second,
the polynomial exploits knowing the spectrum in advance; exact interpolation at three
points is available only because there are three points and they are known.

## Reproducing These Results

The complete implementation is in [`lab/`](lab/README.md): the classical reference, the
hand-built block encoding, the polynomial and phase-factor solvers, the Qiskit circuit,
the sign-recovery experiment, and 22 validation checks. Captured console output for a
complete run is in [`lab/RESULTS.md`](lab/RESULTS.md), and the specification the lab was
built against, together with an audit of where the implementation departs from it, is in
[`lab/PRD.md`](lab/PRD.md).

## Reference Reading

- A. Gilyén, Y. Su, G. H. Low, and N. Wiebe, "Quantum singular value transformation and
  beyond: exponential improvements for quantum matrix arithmetics," *Proceedings of the
  51st Annual ACM Symposium on Theory of Computing* (2019), 193–204. The QSVT theorem and
  the alternating-phase construction used throughout.
  [arXiv:1806.01838](https://arxiv.org/abs/1806.01838)
- G. H. Low and I. L. Chuang, "Optimal Hamiltonian simulation by quantum signal
  processing," *Physical Review Letters* 118 (2017), 010501. The signal-processing
  formulation that QSVT generalizes.
  [arXiv:1606.02685](https://arxiv.org/abs/1606.02685)
- P. R. Halmos, "Normal dilations and extensions of operators," *Summa Brasiliensis
  Mathematicae* 2 (1950), 125–134. The rectangular unitary dilation.
- Y. Dong, X. Meng, K. B. Whaley, and L. Lin, "Efficient phase-factor evaluation in
  quantum signal processing," *Physical Review A* 103 (2021), 042419. The optimization
  approach to phase angles.
  [arXiv:2002.11649](https://arxiv.org/abs/2002.11649)
- A. M. Childs, R. Kothari, and R. D. Somma, "Quantum algorithm for systems of linear
  equations with exponentially improved dependence on precision," *SIAM Journal on
  Computing* 46 (2017), 1920–1950. Polynomial approximations of $1/x$ and the degree
  required as a function of condition number.
  [arXiv:1511.02306](https://arxiv.org/abs/1511.02306)
- J. M. Martyn, Z. M. Rossi, A. K. Tan, and I. L. Chuang, "Grand unification of quantum
  algorithms," *PRX Quantum* 2 (2021), 040203. A readable account of how QSVT subsumes
  search, simulation and linear solving.
  [arXiv:2105.02859](https://arxiv.org/abs/2105.02859)

## Concepts

Four ideas carry over to any application of quantum linear algebra.

- A matrix enters a quantum circuit through a *block encoding*, and the encoding is a
  design decision rather than a formality. Choosing the normalization $\alpha$, the
  padding blocks, and which subspaces represent input and output determines everything
  downstream, including which direction the singular value transform runs in.
- Matrix functions become polynomial approximation problems, subject to a hard bound of 1.
  The scale factor $C$ that enforces that bound is not bookkeeping: it appears directly in
  the success probability as $C^{2}$, so approximation quality and run time trade against
  each other explicitly.
- A non-unitary target implies a failure branch. Any quantum algorithm that applies a map
  which does not preserve norm must place the difference somewhere, and postselection is
  the price. Writing down the complete normalization *before* conditioning on success is
  what makes that price visible.
- Postselected amplitudes give a direction; magnitudes and phases require separate work.
  The overall scale can be reconstructed from the success probability when the transform
  is known exactly, and relative signs require an interference measurement. Reporting a
  computational-basis histogram as though it were the answer would, for the $y$ column
  here, have produced the wrong affine transformation.
