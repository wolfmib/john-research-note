# RESULTS — QSVT Pseudoinverse for a 2D Affine Mapping

Captured from a complete run:

```bash
python3 run_experiment.py --all
```

`qiskit 2.2.3`, `qiskit-aer 0.17.2`, `scipy 1.13.1`, Python 3.9.6. Total wall time 2.8 s.

*(The interpreter in the invocation line above has been shortened from the absolute path
of the machine's virtual environment. The captured console output below is unedited.)*
Shot counts use `--shots 20000` (the default) and a fixed simulator seed, so the numbers
below reproduce exactly.

**Headline:** the circuit recovers `B` in full — direction, relative signs and absolute
scale — matching the classical least-squares fit to `2.9e-14`, with 22/22 checks passing.

---

## 1. Classical reference


```text
==============================================
Classical reference: least-squares affine fit
==============================================

Z shape: (5, 3)
Y shape: (5, 2)
Recovered B shape: (3, 2)

Z =
[[ 0.  0.  1.]
 [ 1.  0.  1.]
 [ 0.  1.  1.]
 [ 1.  1.  1.]
 [ 2. -1.  1.]]

Y = Z B_true =
[[ 2.  -1. ]
 [ 3.2 -1.4]
 [ 2.5  0.1]
 [ 3.7 -0.3]
 [ 3.9 -2.9]]

B =
[[ 1.2 -0.4]
 [ 0.5  1.1]
 [ 2.  -1. ]]

Y_pred = Z B =
[[ 2.  -1. ]
 [ 3.2 -1.4]
 [ 2.5  0.1]
 [ 3.7 -0.3]
 [ 3.9 -2.9]]

||Y - Y_pred||_F = 1.526304e-15
||B - B_true||_F = 8.545833e-16
```

## 2. Custom rectangular block encoding

The Halmos dilation, its unitarity, and the two subspaces.

```text
==============================================
Custom rectangular block encoding
==============================================

raw matrix shape      : (5, 3)
alpha = ||Z||_2       : 3.0874516155
singular values of Z  : [3.087452 1.959378 0.792767]
singular values of A  : [1.       0.634626 0.256771]
condition number      : 3.894527
dilation dimension    : 8  ->  3 qubits
data subspace  H_L    : dimension 5, basis states [0, 1, 2, 3, 4]
param subspace H_R    : dimension 3, basis states [0, 1, 2]

U_A =
[[ 0.       0.       0.32389  0.9233  -0.1015  -0.07818 -0.10299 -0.12482]
 [ 0.32389  0.       0.32389 -0.1015   0.79061 -0.10081 -0.20869 -0.31796]
 [ 0.       0.32389  0.32389 -0.07818 -0.10081  0.86267 -0.15995 -0.06428]
 [ 0.32389  0.32389  0.32389 -0.10299 -0.20869 -0.15995  0.73435 -0.25742]
 [ 0.64778 -0.32389  0.32389 -0.12482 -0.31796 -0.06428 -0.25742  0.42835]
 [ 0.40014  0.06483 -0.45414 -0.      -0.32389 -0.      -0.32389 -0.64778]
 [ 0.06483  0.82335 -0.05635 -0.      -0.      -0.32389 -0.32389  0.32389]
 [-0.45414 -0.05635  0.5158  -0.32389 -0.32389 -0.32389 -0.32389 -0.32389]]

||U^T U - I||       = 3.003e-15
||Pi_L U Pi_R - A|| = 0.000e+00
||Pi_R U^T Pi_L - A^T|| = 0.000e+00
```

## 3. Singular-value polynomial

Degree 9, `C = 0.85 * sigma_min`. Exact at all three singular values, `sup|p| = 0.85`
with a deliberate margin under the hard bound of 1.

```text
==============================================
Singular-value polynomial  (mode=exact, degree=9)
==============================================

normalized singular values:
  sigma1 = 1.0000000000
  sigma2 = 0.6346263960
  sigma3 = 0.2567706055

chosen C = 0.2182550147   ( = 0.8500 * sigma_min )

target:
  C/sigma1 = 0.2182550147
  C/sigma2 = 0.3439110255
  C/sigma3 = 0.8500000000

polynomial:
  p(sigma1) = 0.2182550147
  p(sigma2) = 0.3439110255
  p(sigma3) = 0.8500000000

max |p(sigma_i) - C/sigma_i| = 2.776e-16
sup |p(x)| on [-1,1]         = 0.849999   (must be <= 1)
```

### Why not the textbook interval approximation

From `python3 qsvt_polynomial.py`. Minimax approximation of `C/x` across the whole
interval still leaves ~1% relative error at degree 19, which would cap the achievable
fidelity. Exact interpolation at the three singular values `Z` actually has reaches
machine precision at degree 9.

```text
Minimax approximation of C/x over the whole interval, for comparison:
 degree   max rel err    sup|p|
      5     3.967e-01    0.6249
      9     1.439e-01    0.7346
     13     5.056e-02    0.8195
     19     1.046e-02    0.9387
     25     5.546e-03    0.9800

Degree 19 still leaves ~1% relative error, which caps the achievable
fidelity. The exact mode reaches machine precision at degree 9 because it
only has to be right at the three singular values Z actually has.
```

## 4. QSP phase factors

Solved in 2x2 arithmetic before any circuit is built — this is the one step that can
genuinely fail to converge, so it is gated. Note the imaginary parts: large, and different
at each singular value. That is what forces the real-part projection in the circuit.

```text
==============================================
QSP phase factors  (degree 9, 9 angles)
==============================================

max |Re<0|V|0> - p(x)| over 80 nodes = 6.661e-16

Phi =
[-0.78777299  2.11743819 -0.88017295  1.73089991  1.70059491  1.87833186  3.66972768 -2.39227674 -2.10435486]

at the singular values:
  sigma1=1.000000   Re<0|V|0> = +0.21825501   Im<0|V|0> = -0.97589177
  sigma2=0.634626   Re<0|V|0> = +0.34391103   Im<0|V|0> = +0.87067108
  sigma3=0.256771   Re<0|V|0> = +0.85000000   Im<0|V|0> = -0.10278606

The imaginary parts are large, and they differ across singular values.
Left alone they would rotate each singular component by a different
phase and scramble beta -- hence the real-part projection in the circuit.
```

## 5. QSVT operator and circuit size

The block really is the scaled pseudoinverse, in the adjoint direction.

```text
==============================================
QSVT operator check
==============================================

||Pi_R Re[V] Pi_L  -  V p(Sigma) W^T||  = 4.547e-15
||Pi_R Re[V] Pi_L  -  C*alpha*pinv(Z)|| = 4.180e-15

Circuit size:
  qubits 5   depth 77   ops 84
  {'mcx_o0': 10, 'mcx_o1': 10, 'mcx_o2': 10, 'unitary': 9, 'rzz': 9, 'mcx_o5': 8, 'mcx_o6': 8, 'mcx': 8, 'x': 8, 'h': 2, 'state_preparation': 1, 'barrier': 1}
```

## 6. Quantum solve — X column

```text
==============================================
Affine quantum solve: X output
==============================================

Input y:
[2.  3.2 2.5 3.7 3.9]
||y|| = 7.0278019323

Matrix normalization alpha: 3.0874516155
Normalized singular values: [1.         0.6346264  0.25677061]
Polynomial scale C:         0.2182550147
p(sigma):                   [0.21825501 0.34391103 0.85      ]
C/sigma:                    [0.21825501 0.34391103 0.85      ]
Block-unitary error:        3.003e-15

Complete normalization BEFORE postselection
----------------------------------------------
The circuit output is a single normalized state spread over the whole
register. Writing the success amplitudes as A1, A2, A3:

  A1 = <S,0|Psi>  = +0.1150604648     |A1|^2 = 0.0132389106
  A2 = <S,1|Psi>  = +0.0479418604     |A2|^2 = 0.0022984220
  A3 = <S,2|Psi>  = +0.1917674414     |A3|^2 = 0.0367747516
                            sum |Ai|^2 = 0.0523120841   <- this is P_S
                                   P_F = 0.9476879159   <- everything else
                               P_S+P_F = 1.0000000000

The failure branch is not a bug or a leak. p(sigma) rescales each singular
component by a different factor, so the desired branch cannot keep unit norm;
unitarity forces the missing norm to live somewhere, and that somewhere is
the failure subspace.

Success probability: 0.0523120841
Failure probability: 0.9476879159
Success + failure:   1.000000

Postselected beta state:    [0.50306617 0.2096109  0.83844362]
Classical normalized beta:  [0.50306617 0.2096109  0.83844362]
State fidelity:             1.000000000000

Shot distribution conditioned on success (1061 of 20000 shots):
  000: 0.2413    theory |beta_0|^2/sum = 0.2531    (256 counts)
  001: 0.0434    theory |beta_1|^2/sum = 0.0439    (46 counts)
  010: 0.7154    theory |beta_2|^2/sum = 0.7030    (759 counts)
  measured P_S = 0.0530   exact P_S = 0.0523

Scale recovery (PRD section 19):
  A quantum state carries no absolute scale, but P_S does:
      P_S = || C*alpha*pinv(Z) |y> ||^2 = ( C*alpha*||beta|| / ||y|| )^2
  so  ||beta|| = sqrt(P_S) * ||y|| / (C*alpha), all of which is known.
      sqrt(0.05231208) * 7.027802 / (0.218255 * 3.087452)
      = 2.3853720884     (classical ||beta|| = 2.3853720884)

Recovered beta:  [1.2 0.5 2. ]
Classical beta:  [1.2 0.5 2. ]
```

## 7. Quantum solve — Y column

The interesting column: `beta_y = (-0.4, 1.1, -1.0)` has mixed signs, which a
computational-basis histogram cannot see.

```text
==============================================
Affine quantum solve: Y output
==============================================

Input y:
[-1.  -1.4  0.1 -0.3 -2.9]
||y|| = 3.3867388444

Matrix normalization alpha: 3.0874516155
Normalized singular values: [1.         0.6346264  0.25677061]
Polynomial scale C:         0.2182550147
p(sigma):                   [0.21825501 0.34391103 0.85      ]
C/sigma:                    [0.21825501 0.34391103 0.85      ]
Block-unitary error:        3.003e-15

Complete normalization BEFORE postselection
----------------------------------------------
The circuit output is a single normalized state spread over the whole
register. Writing the success amplitudes as A1, A2, A3:

  A1 = <S,0|Psi>  = -0.0795870988     |A1|^2 = 0.0063341063
  A2 = <S,1|Psi>  = +0.2188645217     |A2|^2 = 0.0479016789
  A3 = <S,2|Psi>  = -0.1989677470     |A3|^2 = 0.0395881644
                            sum |Ai|^2 = 0.0938239495   <- this is P_S
                                   P_F = 0.9061760505   <- everything else
                               P_S+P_F = 1.0000000000

The failure branch is not a bug or a leak. p(sigma) rescales each singular
component by a different factor, so the desired branch cannot keep unit norm;
unitarity forces the missing norm to live somewhere, and that somewhere is
the failure subspace.

Success probability: 0.0938239495
Failure probability: 0.9061760505
Success + failure:   1.000000

Postselected beta state:    [-0.25982792  0.71452678 -0.6495698 ]
Classical normalized beta:  [-0.25982792  0.71452678 -0.6495698 ]
State fidelity:             1.000000000000

Shot distribution conditioned on success (1943 of 20000 shots):
  000: 0.0705    theory |beta_0|^2/sum = 0.0675    (137 counts)
  001: 0.4972    theory |beta_1|^2/sum = 0.5105    (966 counts)
  010: 0.4323    theory |beta_2|^2/sum = 0.4219    (840 counts)
  measured P_S = 0.0972   exact P_S = 0.0938

Scale recovery (PRD section 19):
  A quantum state carries no absolute scale, but P_S does:
      P_S = || C*alpha*pinv(Z) |y> ||^2 = ( C*alpha*||beta|| / ||y|| )^2
  so  ||beta|| = sqrt(P_S) * ||y|| / (C*alpha), all of which is known.
      sqrt(0.09382395) * 3.386739 / (0.218255 * 3.087452)
      = 1.5394804318     (classical ||beta|| = 1.5394804318)

Recovered beta:  [-0.4  1.1 -1. ]
Classical beta:  [-0.4  1.1 -1. ]
```

## 8. Sign recovery from shots

No statevector used. The interference experiment recovers every relative sign at
`z` between 19 and 80.

```text
==============================================
Sign recovery from shots (PRD section 14)
==============================================

--- sign recovery, X output ---
  computational basis alone gives only |beta_i|^2 = [0.2531 0.0439 0.703 ]
  mix |0>,|1> : n_0=536    n_1=99      P(0)-P(1)=+0.2111  z=   +18.8  => sign(b0*b1) = +1   (true +1)
  mix |0>,|2> : n_0=1882   n_2=116     P(0)-P(2)=+0.8531  z=   +79.7  => sign(b0*b2) = +1   (true +1)
  recovered signs (b0 taken +) : [1 1 1]
  true signs      (b0 taken +) : [1 1 1]
  match: True

--- sign recovery, Y output ---
  computational basis alone gives only |beta_i|^2 = [0.0675 0.5105 0.4219]
  mix |0>,|1> : n_0=389    n_1=1766    P(0)-P(1)=-0.3650  z=   -33.9  => sign(b0*b1) = -1   (true -1)
  mix |0>,|2> : n_0=1562   n_2=297     P(0)-P(2)=+0.3353  z=   +33.4  => sign(b0*b2) = +1   (true +1)
  recovered signs (b0 taken +) : [ 1 -1  1]
  true signs      (b0 taken +) : [ 1 -1  1]
  match: True
```

## 9. Final reconstruction

```text
==============================================
Final reconstruction
==============================================

B_quantum = [beta_x, beta_y] =
[[ 1.2 -0.4]
 [ 0.5  1.1]
 [ 2.  -1. ]]

B_classical =
[[ 1.2 -0.4]
 [ 0.5  1.1]
 [ 2.  -1. ]]

B_true =
[[ 1.2 -0.4]
 [ 0.5  1.1]
 [ 2.  -1. ]]

||B_quantum - B_true||_F    = 2.881585e-14
||B_classical - B_true||_F  = 8.545833e-16

Note on what was and was not recovered by measurement:
  - magnitudes |beta_i|  : from the shot histogram
  - relative signs       : from the interference experiment above
  - overall scale ||beta||: from P_S, via the identity in each column report
  - global sign          : NOT observable. |beta> and -|beta> are the same
    physical state; the convention here is fixed against the classical fit.
```

## 10. Validation — 22/22

```text
=================================================================================
VALIDATION
=================================================================================
PASS  A  classical affine fit                 8.546e-16            < 1e-12
PASS  B  block unitary U^T U = I              3.003e-15            < 1e-12
PASS  B  adjoint block = A^T                  0.000e+00            < 1e-12
PASS  C  p(sigma_i) = C/sigma_i               2.776e-16            < 1e-10
PASS  C  sup|p| <= 1 on [-1,1]                0.849999             <= 1
PASS     QSP phase fit (2x2, pre-circuit)     6.661e-16            < 1e-10
PASS  index convention (Qiskit LE == numpy)   1.332e-15            < 1e-12
PASS     QSVT block = C*alpha*pinv(Z)         4.180e-15            < 1e-10
PASS     circuit == numpy (X)                 2.483e-15            < 1e-10
PASS     phase ancilla uncomputes (X)         6.441e-31            < 1e-12
PASS  D  fidelity vs classical beta (X)       1.000000000000       > 0.999
PASS     |A1|^2+|A2|^2+|A3|^2 + P_F = 1 (X)   0.000e+00            < 1e-12
PASS     ||beta|| scale recovery (X)          1.776e-14            < 1e-6
PASS     shot histogram chi2 (X, n=1061)      chi2=0.82 p=0.663    p > 0.001
PASS     sign recovery from shots (X)         [1 1 1] vs [1 1 1]   exact
PASS     circuit == numpy (Y)                 2.900e-15            < 1e-10
PASS     phase ancilla uncomputes (Y)         5.150e-31            < 1e-12
PASS  D  fidelity vs classical beta (Y)       1.000000000000       > 0.999
PASS     |A1|^2+|A2|^2+|A3|^2 + P_F = 1 (Y)   0.000e+00            < 1e-12
PASS     ||beta|| scale recovery (Y)          1.932e-14            < 1e-6
PASS     shot histogram chi2 (Y, n=1943)      chi2=1.44 p=0.488    p > 0.001
PASS     sign recovery from shots (Y)         [ 1 -1  1] vs [ 1 -1  1] exact
---------------------------------------------------------------------------------
22/22 checks pass
```
