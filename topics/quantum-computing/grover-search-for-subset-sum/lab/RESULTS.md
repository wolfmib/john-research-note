# Results — Grover Subset-Sum

Captured console output from every run, 2026-08-09, qiskit 2.2.3 /
qiskit-aer 0.17.2 on a Mac Mini (Apple silicon). All simulations are seeded
(`seed=1234`), so these transcripts reproduce exactly.

Transcripts are verbatim except that the absolute output directory has been
shortened to `<lab>` and the interpreter path to `python3`.

| Run | Script | Duration | Outcome |
|-----|--------|----------|---------|
| Classical brute force | `classical_subset_sum.py` | < 0.1 s | `(1,0,1,0,0,1)` = 37 |
| Quantum, full lab (Aer) | `grover_subset_sum.py` | 75.8 s | `100101` = 37, P = 0.9968, checks A–E pass |
| Iteration sweep | `iteration_sweep.py` | 130.9 s | peak at r = 6, matches theory to 3.7e-13 |
| Quantum, StatevectorSampler | `grover_subset_sum.py --sampler statevector` | 610.4 s | `100101` = 37, P = 0.9970 |

---

## 1. Classical brute force

```
====================================================================
PART 1 - CLASSICAL BRUTE FORCE
====================================================================
weights = [18, 36, 34, 32, 19, 23]
target  = 75
search space = 2^6 = 64 candidates
max possible sum = 162  ->  sum register needs 8 bits

Scanning all binary combinations:
  hit: x=(1, 0, 1, 0, 0, 1)  S(x)=75  int=37  qiskit='100101'

candidates checked : 64
solutions found    : 1

CHECK A PASSED - exactly one satisfying combination.
  tuple (x0..x5)  : (1, 0, 1, 0, 0, 1)
  integer         : 37
  qiskit bitstring: 100101
  verification    : 18*1 + 36*0 + 34*1 + 32*0 + 19*0 + 23*1 = 75

Classical cost: 64 rule evaluations (worst case O(N), N=64).
Grover will need about sqrt(N) ~ 6 oracle calls for the same answer.
```

## 2. Quantum lab — full run with all validation checks (Aer)

```

========================================================================
PART 1 - CLASSICAL REFERENCE
========================================================================
brute force checked 64 candidates, found 1 solution
  x = (1, 0, 1, 0, 0, 1)   int = 37   qiskit = '100101'
  (used ONLY for validation - never fed into the quantum circuit)

========================================================================
PARTS 2+3 - SEARCH REGISTER AND REVERSIBLE WEIGHTED SUM
========================================================================
S(x) = 18*x0 + 36*x1 + 34*x2 + 32*x3 + 19*x4 + 23*x5
max S = 162 -> needs 8 sum bits (2^7=128 < 162 < 256=2^8)

  num_state_qubits   :  6   indices [0, 1, 2, 3, 4, 5]
  num_sum_qubits     :  8   indices [6, 7, 8, 9, 10, 11, 12, 13]
  num_carry_qubits   :  7   indices [14, 15, 16, 17, 18, 19, 20]
  num_control_qubits :  1   indices [21]
  num_qubits (total) : 22
  note: Qiskit 2.x splits WeightedAdder's ancillas into carry+control,
        so num_ancilla_qubits == 8 (carry 7 + control 1).

state preparation: H on qubits [0, 1, 2, 3, 4, 5] only -> uniform superposition over 64 candidates

========================================================================
PART 4 - PHASE ORACLE (compute -> mark -> uncompute)
========================================================================
target 75 in the sum register (little-endian, sum[i] = bit i):
  bits  : [1, 1, 0, 1, 0, 0, 1, 0]
  binary: 01001011  = 1 + 2 + 8 + 64 = 75
  X applied to sum qubits [8, 10, 11, 13] so 'equals target' becomes 'all ones'
oracle: 22 qubits, 7003 basic gates, depth 4809

========================================================================
PARTS 5+6 - GROVER OPERATOR AND ITERATION COUNT
========================================================================
Q = D * S_f built on 22 qubits; reflection restricted to search qubits [0, 1, 2, 3, 4, 5]

N = 64 candidates, M = 1 marked
theta = arcsin(sqrt(M/N)) = 0.125328 rad
r = floor(pi / (4*theta)) = floor(6.2667) = 6
predicted P(solution) after 6 iterations = 99.66%

========================================================================
CHECK B - ORACLE CORRECTNESS (all 64 candidates at once)
========================================================================
  statevector simulated in 9.3s (22 qubits, 4,194,304 amplitudes)
  ancilla leakage        : 5.707e-14   (must be ~0 -> ancillas clean)
  max amplitude error    : 4.026e-15
  states given -1 phase  : [37]  -> ['100101']
  classical solution int : 37
  CHECK B PASSED - exactly the satisfying state is phase-flipped, ancillas return to |0>.

========================================================================
CHECK C - ONE GROVER ITERATION
========================================================================
  simulated in 9.4s
  P(solution) before any iteration : 0.015625   (1/64)
  P(solution) after 1 iteration    : 0.134827
  theory sin^2(3*theta)            : 0.134827
  amplification factor             : 8.63x
  CHECK C PASSED - amplitude amplification is working.

========================================================================
CHECK E - NO ANSWER HARD-CODING
========================================================================
  scanned  : build_weighted_adder, build_phase_marker, build_oracle, build_state_preparation, build_grover_operator, build_search_circuit
  forbidden: integer 37, bitstring '100101'
  allowed  : weights [18, 36, 34, 32, 19, 23], target 75
  CHECK E PASSED

========================================================================
PART 7 - FULL RUN: 6 GROVER ITERATIONS, 4096 SHOTS
========================================================================
circuit: 22 qubits, 43452 gates after decomposition
sampler: aer  (qiskit-aer statevector)
simulated in 55.9s

top measurement outcomes:
  100101     4083   p=0.9968   int=37   S(x)= 75  <-- satisfies the rule
  011101        2   p=0.0005   int=29   S(x)=103
  111101        1   p=0.0002   int=61   S(x)=126
  001101        1   p=0.0002   int=13   S(x)= 84
  110110        1   p=0.0002   int=54   S(x)=112
  001010        1   p=0.0002   int=10   S(x)= 68

========================================================================
DECODE AND COMPARE
========================================================================
dominant bitstring        : '100101'  (Qiskit order = x5 x4 x3 x2 x1 x0)
decoded tuple (x0..x5)    : (1, 0, 1, 0, 0, 1)
decoded integer           : 37  (= 2^0 + 2^2 + 2^5)
rule check S(x)           : 18*1 + 36*0 + 34*1 + 32*0 + 19*0 + 23*1 = 75 (== 75)
measured probability      : 0.9968
theoretical probability   : 0.9966

CHECK D PASSED - distribution dominated by '100101'.

classical result -> 37
quantum dominant -> 100101 -> 37
MATCH: YES

========================================================================
ARTIFACTS
========================================================================
  circuit drawings -> <lab>/figures/
  histogram -> <lab>/figures/grover_counts_histogram.png

========================================================================
VALIDATION SUMMARY
========================================================================
  CHECK A  PASS  - classical brute force finds exactly one solution
  CHECK B  PASS  - oracle phase-flips only the satisfying state, ancillas clean
  CHECK C  PASS  - one Grover iteration amplifies above 1/64
  CHECK D  PASS  - 6 iterations dominated by the solution
  CHECK E  PASS  - no answer hard-coded in the quantum construction

cost comparison: classical 64 rule evaluations vs Grover 6 oracle calls (O(N) vs O(sqrt(N)))
total wall time: 75.8s

ALL CHECKS PASSED
```

## 3. Iteration sweep — why r = 6

```
N = 64, M = 1, theta = 0.125328 rad
optimal r = floor(pi/(4*theta)) = 6
probing r = 0..12 with one simulation + probability snapshots

simulated 12 iterations in 130.9s

  r   P(solution)   theory      note
  --  ------------  ----------  ----
   0   0.015625     0.015625    
   1   0.134827     0.134827    
   2   0.343895     0.343895    
   3   0.591380     0.591380    
   4   0.816377     0.816377    
   5   0.963515     0.963515    
   6   0.996586     0.996586    <-- optimal, floor(pi/(4*theta))
   7   0.907449     0.907449    over-rotated: worse than before
   8   0.718042     0.718042    over-rotated: worse than before
   9   0.474976     0.474976    over-rotated: worse than before
  10   0.238068     0.238068    over-rotated: worse than before
  11   0.065620     0.065620    over-rotated: worse than before
  12   0.000071     0.000071    over-rotated: worse than before

empirical peak at r = 6 (P = 0.996586)
formula predicted r = 6  ->  MATCH
max |measured - theory| = 3.67e-13

Lesson: Grover rotates. Past the peak, extra iterations rotate the state
back out of the marked subspace and the answer degrades.

plot -> <lab>/figures/iteration_sweep.png
```

## 4. StatevectorSampler path (spec-mandated primitive)

Same circuit, same answer, ~10× the wall time. Checks B/C/E were skipped here
because they had already passed on the Aer run — this run exists to prove the
`StatevectorSampler` path works, not to re-validate the oracle.

```

========================================================================
PART 1 - CLASSICAL REFERENCE
========================================================================
brute force checked 64 candidates, found 1 solution
  x = (1, 0, 1, 0, 0, 1)   int = 37   qiskit = '100101'
  (used ONLY for validation - never fed into the quantum circuit)

========================================================================
PARTS 2+3 - SEARCH REGISTER AND REVERSIBLE WEIGHTED SUM
========================================================================
S(x) = 18*x0 + 36*x1 + 34*x2 + 32*x3 + 19*x4 + 23*x5
max S = 162 -> needs 8 sum bits (2^7=128 < 162 < 256=2^8)

  num_state_qubits   :  6   indices [0, 1, 2, 3, 4, 5]
  num_sum_qubits     :  8   indices [6, 7, 8, 9, 10, 11, 12, 13]
  num_carry_qubits   :  7   indices [14, 15, 16, 17, 18, 19, 20]
  num_control_qubits :  1   indices [21]
  num_qubits (total) : 22
  note: Qiskit 2.x splits WeightedAdder's ancillas into carry+control,
        so num_ancilla_qubits == 8 (carry 7 + control 1).

state preparation: H on qubits [0, 1, 2, 3, 4, 5] only -> uniform superposition over 64 candidates

========================================================================
PART 4 - PHASE ORACLE (compute -> mark -> uncompute)
========================================================================
target 75 in the sum register (little-endian, sum[i] = bit i):
  bits  : [1, 1, 0, 1, 0, 0, 1, 0]
  binary: 01001011  = 1 + 2 + 8 + 64 = 75
  X applied to sum qubits [8, 10, 11, 13] so 'equals target' becomes 'all ones'
oracle: 22 qubits, 7003 basic gates, depth 4809

========================================================================
PARTS 5+6 - GROVER OPERATOR AND ITERATION COUNT
========================================================================
Q = D * S_f built on 22 qubits; reflection restricted to search qubits [0, 1, 2, 3, 4, 5]

N = 64 candidates, M = 1 marked
theta = arcsin(sqrt(M/N)) = 0.125328 rad
r = floor(pi / (4*theta)) = floor(6.2667) = 6
predicted P(solution) after 6 iterations = 99.66%

========================================================================
PART 7 - FULL RUN: 6 GROVER ITERATIONS, 2000 SHOTS
========================================================================
circuit: 22 qubits, 43452 gates after decomposition
sampler: statevector  (StatevectorSampler is exact but slow - expect ~15 min)
simulated in 609.2s

top measurement outcomes:
  100101     1994   p=0.9970   int=37   S(x)= 75  <-- satisfies the rule
  000000        1   p=0.0005   int= 0   S(x)=  0
  110000        1   p=0.0005   int=48   S(x)= 42
  100011        1   p=0.0005   int=35   S(x)= 77
  010100        1   p=0.0005   int=20   S(x)= 53
  010011        1   p=0.0005   int=19   S(x)= 73

========================================================================
DECODE AND COMPARE
========================================================================
dominant bitstring        : '100101'  (Qiskit order = x5 x4 x3 x2 x1 x0)
decoded tuple (x0..x5)    : (1, 0, 1, 0, 0, 1)
decoded integer           : 37  (= 2^0 + 2^2 + 2^5)
rule check S(x)           : 18*1 + 36*0 + 34*1 + 32*0 + 19*0 + 23*1 = 75 (== 75)
measured probability      : 0.9970
theoretical probability   : 0.9966

CHECK D PASSED - distribution dominated by '100101'.

classical result -> 37
quantum dominant -> 100101 -> 37
MATCH: YES

========================================================================
ARTIFACTS
========================================================================
  circuit drawings -> <lab>/figures/
  histogram -> <lab>/figures/grover_counts_histogram.png

========================================================================
VALIDATION SUMMARY
========================================================================
  CHECK A  PASS  - classical brute force finds exactly one solution
  CHECK B  SKIP  - oracle phase-flips only the satisfying state, ancillas clean
  CHECK C  SKIP  - one Grover iteration amplifies above 1/64
  CHECK D  PASS  - 6 iterations dominated by the solution
  CHECK E  SKIP  - no answer hard-coded in the quantum construction

cost comparison: classical 64 rule evaluations vs Grover 6 oracle calls (O(N) vs O(sqrt(N)))
total wall time: 610.4s

ALL CHECKS PASSED
```
