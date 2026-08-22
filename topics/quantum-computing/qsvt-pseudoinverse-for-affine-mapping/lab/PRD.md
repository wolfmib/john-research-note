# PRD — Quantum Affine 2D Mapping via Custom Block Encoding + QSVT

Original spec as received (Codex), reformatted so the maths renders, followed by an
**Adjustments** section recording every place the implementation departs from it and why.

---

## 1. Goal

Solve a small 2D affine mapping problem $Y = ZB$ with

$$Z \in \mathbb{R}^{5\times3}, \qquad Y \in \mathbb{R}^{5\times2}, \qquad B \in \mathbb{R}^{3\times2}.$$

Rows of $Z$ are 2D source coordinates in homogeneous form, $Z_i = [x_i,\ y_i,\ 1]$, and

```math
B = \begin{bmatrix} a & d \\ b & e \\ c & f \end{bmatrix}
```

is the unknown affine transformation, so $[x_i',\ y_i'] = [x_i,\ y_i,\ 1]\,B$.

Two independent implementations are required:

1. a classical reference solution;
2. a quantum solution using a custom rectangular block encoding, QSVT-style
   singular-value transformation, and success/failure postselection.

The quantum implementation must not use $Z^TZ$ internally.

## 2. Concrete dataset

```math
Z = \begin{bmatrix} 0&0&1 \\ 1&0&1 \\ 0&1&1 \\ 1&1&1 \\ 2&-1&1 \end{bmatrix},
\qquad
B_{\mathrm{true}} = \begin{bmatrix} 1.2&-0.4 \\ 0.5&1.1 \\ 2.0&-1.0 \end{bmatrix},
\qquad
Y = ZB_{\mathrm{true}} = \begin{bmatrix} 2.0&-1.0 \\ 3.2&-1.4 \\ 2.5&0.1 \\ 3.7&-0.3 \\ 3.9&-2.9 \end{bmatrix}.
```

After generating $Y$, treat $B_{\mathrm{true}}$ as unknown.

## 3. Classical reference implementation

Ordinary least squares, $B = (Z^TZ)^{-1}Z^TY$, or preferably a numerically stable
equivalent such as `numpy.linalg.lstsq`. Print the shapes, $B$, and
$\|Y - Y_{\mathrm{pred}}\|_F$ with $Y_{\mathrm{pred}} = ZB$.

## 4. Split into two vectors

Write $Y = [y_x\ \ y_y]$ and $B = [\beta_x\ \ \beta_y]$, then solve $Z\beta_x = y_x$ and
$Z\beta_y = y_y$ independently, reusing the same block encoding of $Z$ for both columns.

## 5. Do not use the normal equations in the quantum path

The quantum path must not form $Z^TZ$ or solve $(Z^TZ)\beta = Z^Ty$. The intended
mathematics is $\beta = Z^{+}y$ via the singular-value transformation of $Z$. If
$Z = U\Sigma V^T$ then $Z^{+} = V\Sigma^{+}U^T$, and the circuit should implement an
approximation to $V\,p(\Sigma)\,U^T$ with $p(\sigma) \approx C/\sigma$. $U$ and $V$ may be
computed classically for debugging only, never used inside the circuit.

## 6. Normalize the matrix correctly

Compute $\alpha \ge \|Z\|_2$ (equality is acceptable initially) and set $A = Z/\alpha$ so
that every singular value lies in $[0,1]$. Normalize $y$ separately, as a quantum state:
$|y\rangle = y/\|y\|$. The two normalizations are different things.

## 7. Build our own `UBlock`

No ready-made block-encoding operation. For $A \in \mathbb{R}^{5\times3}$ construct

```math
U_A = \begin{bmatrix} A & \sqrt{I_5 - AA^T} \\ \sqrt{I_3 - A^TA} & -A^T \end{bmatrix},
```

an $8\times8$ unitary; $8 = 2^3$, so the dilation fits 3 qubits. Provide
`build_rectangular_block_unitary(A)` which verifies the shape, verifies $\|A\|_2 \le 1$,
computes the two PSD square roots, assembles the dilation, and prints
$\|U^\dagger U - I\|$.

## 8. Explicitly define the two subspaces

Data space $\mathcal{H}_L \simeq \mathbb{C}^5$ containing $y$; parameter space
$\mathcal{H}_R \simeq \mathbb{C}^3$ containing $\beta$. Define both projectors and
document which computational basis states each occupies.

## 9. QSVT target polynomial

$\sigma \mapsto 1/\sigma$ cannot be an amplitude transformation directly. Choose
$p(\sigma) \approx C/\sigma$ with $|p(x)| \le 1$ on the QSVT domain. Compute the singular
values for validation, determine $\sigma_{\min},\sigma_{\max}$, select a safe $C$, and
construct a bounded polynomial approximation over $[\sigma_{\min},\sigma_{\max}]$. Print
the singular values, $C$, $C/\sigma_i$ and $p(\sigma_i)$ side by side.

## 10. Do not hide the success/failure logic

$M = V p(\Sigma) U^T$ is not unitary, so the full state must be

$$|\Psi_{\mathrm{out}}\rangle = |S\rangle M|y\rangle + |F\rangle|\phi_F\rangle,
\qquad \|M|y\rangle\|^2 + \|\phi_F\|^2 = 1 .$$

Compute and print $P_S = \|M|y\rangle\|^2$ and $P_F = 1 - P_S$, and verify $P_S + P_F = 1$.

## 11. Show the complete normalization before postselection

Do not jump from the $\beta$ amplitudes to a success probability. Show

$$|\Psi\rangle = A_1|S,0\rangle + A_2|S,1\rangle + A_3|S,2\rangle + |\text{failure}\rangle$$

and verify $|A_1|^2 + |A_2|^2 + |A_3|^2 + P_F = 1$ before computing $P_S$.

## 12. Postselection and recovered beta state

On success, renormalize the branch to obtain
$|\beta\rangle = (\beta_0|0\rangle + \beta_1|1\rangle + \beta_2|2\rangle)/\|\beta\|$. The
expected classical vectors are $\beta_x = (1.2, 0.5, 2.0)$ and $\beta_y = (-0.4, 1.1, -1.0)$.

## 13. Measurement

Many shots, each restarting the circuit. Discard failures, record the parameter register
on success, and compare with $P_i = |\beta_i|^2/\sum_j|\beta_j|^2$. For $\beta_x$ the
theoretical ratio is $1.44 : 0.25 : 4$, normalized by $5.69$.

## 14. Signs are not recoverable from a simple histogram

A computational-basis measurement gives $|\beta_i|^2$ and loses signs. This matters for
$\beta_y$, which collapses to $0.16 : 1.21 : 1$. Add a separate phase/sign-recovery
experiment using interference. Statevector inspection is allowed as a verification tool,
but shot-based sign recovery should be discussed separately.

## 15. Qiskit implementation strategy

Fundamental tools only — `QuantumCircuit`, `UnitaryGate`, `StatePreparation`, rotation and
phase gates, controlled gates, `inverse()`, `measure()`, `Statevector`, `AerSimulator`. No
ready-made high-level QSVT regression solver. Modules roughly as:
`classical_affine.py`, `block_encoding.py`, `qsvt_polynomial.py`, `quantum_solver.py`,
`run_experiment.py`, `validation.py`, `README.md`.

## 16. Custom tooling API

`RectangularBlockEncoding` with `normalized_matrix`, `unitary`, `verify`,
`left_projector`, `right_projector`; `SingularValuePolynomial` with `coefficients`,
`evaluate`, `verify_bound`; `QuantumPseudoInverse` with `build_circuit`,
`success_probability`, `sample`. Reusable tooling, not one monolithic script.

## 17. Validation layers

A — classical affine fit matches $B_{\mathrm{true}}$.
B — $U_A^\dagger U_A \approx I$.
C — $p(\sigma_i) \approx C/\sigma_i$ for every singular value.
D — after postselection, $|\beta_{\mathrm{quantum}}\rangle$ agrees with the normalized
classical solution up to global phase, with fidelity
$F = |\langle\beta_{\mathrm{classical}}|\beta_{\mathrm{quantum}}\rangle|^2 > 0.999$.

## 18. Required diagnostic output

For each of $y_x$ and $y_y$: input $y$, $\|y\|$, $\alpha$, normalized singular values,
$C$, $p(\sigma)$, $C/\sigma$, block-unitary error, success probability, failure
probability, their sum, the postselected $\beta$ state, the classical normalized $\beta$,
the state fidelity, and the shot distribution conditioned on success.

## 19. Final reconstruction

Reconstruct $B_{\mathrm{quantum}} = [\beta_x\ \ \beta_y]$. Because quantum states lose their
absolute normalization, document how the overall coefficient scale is recovered or why
additional information is required. Compare normalized directions first, then show
$B_{\mathrm{true}}$.

## 20. Core concept the lab must demonstrate

This is not Grover search over candidate affine matrices. The transformation is

$$y \xrightarrow{\ U^T\ } \text{coefficients} \xrightarrow{\ \Sigma^{-1}\ }
\text{scaled coefficients} \xrightarrow{\ V\ } \beta,$$

with QSVT replacing the non-unitary inverse-singular-value step by $p(\sigma) \approx
C/\sigma$. The complete unitary must contain both a success and a failure subspace,
because rescaling singular components by different magnitudes changes the norm of the
desired branch. The failure component supplies the remaining norm. Postselection
renormalizes the desired branch, leaving $|\beta\rangle$.

**Do not hide the matrix mathematics behind library calls.**

---

# Adjustments

Everything below was checked numerically before implementation. Sections 1–4, 6, 8,
10–13, 15–18 and 20 were implemented as written.

## A1 — the singular-value transform runs in the wrong direction (§5, §9)

§9 asks the circuit to implement $V p(\Sigma) U^T$, but does not say how, and the obvious
reading is wrong. QSVT driven by $U_A$ with the projector pair $(\Pi_L, \Pi_R)$ applies
$p$ in the **forward** direction and produces $W p(\Sigma) V^T$ — the same direction as
$A$ itself. The pseudoinverse needs the adjoint direction.

**Implemented:** the alternating-phase sequence is driven by $U_A^T = U_A^\dagger$ with
the projectors swapped, since $\Pi_R U_A^T \Pi_L = A^T$. The resulting block equals
$C\alpha Z^{+}$ to $4.2\times10^{-15}$. See `sequence_factors` in `qsvt_polynomial.py`.

## A2 — the block is complex unless the real part is projected out (§9 is silent)

A QSP sequence puts a **complex** polynomial in the block. At this problem's singular
values the imaginary parts are $(-0.976, +0.871, -0.103)$ — not negligible, and different
for each singular value. Left alone they would rotate each singular component by a
different phase and scramble $\beta$.

**Implemented:** because $U_A$ is real, $V(-\Phi) = \overline{V(\Phi)}$, so a Hadamard
sandwich on one extra qubit with postselection on $|0\rangle$ yields
$\tfrac{1}{2}(V(\Phi) + \overline{V(\Phi)}) = \mathrm{Re}V(\Phi)$. Only the phase
rotations need to see that qubit — a single `RZZ(anc, lcu)` flips their sign — so $U_A$
itself is never controlled.

## A3 — five qubits, not three (§7)

§7's "3 qubits" covers the dilation only. The circuit also needs one ancilla for the
projector-controlled phase shifts (computed and uncomputed inside each phase block, so it
returns to $|0\rangle$ deterministically) and one for the real-part projection.

## A4 — interval minimax is the wrong default polynomial (§9)

§9 asks for a bounded approximation of $C/x$ over $[\sigma_{\min}, \sigma_{\max}]$. With
$\kappa = 3.89$ that needs degree $\approx 19$ to reach 1% relative error, which caps the
achievable fidelity. But $Z$ has exactly **three** singular values; what the polynomial
does anywhere else cannot affect $\beta$.

**Implemented:** an LP that pins $p(\sigma_i) = C/\sigma_i$ as hard equality constraints
while minimizing $\sup|p|$ on $[-1,1]$. Degree 9 gives an exact transform with
$\sup|p| = 0.85$. `mode="interval"` keeps the textbook version for comparison, and the
degree-vs-error sweep is printed and plotted.

## A5 — no phase-factor tooling exists (§15, §16)

Neither section mentions computing QSP phase angles, and there is no library for it here
(`pyqsp` is not installed, and §15 forbids high-level solvers regardless).

**Implemented:** `QSPPhases` — batched $2\times2$ QSP evaluation plus
`scipy.optimize.least_squares` from a zero initial guess, converging to $6.7\times10^{-16}$
at degree 9. It is a **hard gate**: the scalar fit is verified in pure numpy before any
circuit is constructed, because it is the only step that can genuinely fail.

## A6 — §19 is too pessimistic; the scale is recoverable

§19 suggests the overall coefficient scale may need extra information. It does not. Since
the polynomial is exact at every singular value, the block is exactly $C\alpha Z^{+}$, so

$$P_S = \left(\frac{C\,\alpha\,\|\beta\|}{\|y\|}\right)^2
\qquad\Longrightarrow\qquad
\|\beta\| = \frac{\sqrt{P_S}\,\|y\|}{C\,\alpha},$$

and every quantity on the right is already known. Verified exact for both columns. $B$ is
therefore **fully reconstructed**, not merely recovered up to scale. Only the global sign
of each column is unobservable, which is a statement about quantum states rather than a
limitation of the method.

## A7 — minor corrections

- §18's histogram labels `00 / 01 / 10` describe a 2-qubit register. The parameter
  register is 3 qubits: `000 / 001 / 010`.
- §5's "must not calculate $Z^TZ$" cannot be met literally — the dilation itself needs
  $\sqrt{I_3 - A^TA}$, and $\alpha = \|Z\|_2$ needs an SVD. The rule is honored in the
  sense that matters: the **algorithm** never solves the normal equations
  $(Z^TZ)\beta = Z^Ty$. Forming the dilation is construction-time preprocessing of the
  encoding; a real application would obtain $U_A$ from a data-structure oracle instead.
  This is stated plainly in `README.md` rather than glossed over.
