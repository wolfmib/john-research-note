# Reproducible Lab — Grover Search for a 6-Bit Subset-Sum Problem

Runnable code behind [the write-up](../content.md). Read the write-up for the
concepts; read this for the implementation, the validation checks, and the raw
numbers.

Classical brute force vs. quantum amplitude amplification on the **same** 64-candidate
problem, built with Qiskit 2.2.3 + Aer 0.17.2.

**The problem**

```
find (x0..x5) in {0,1}^6  such that  18x0 + 36x1 + 34x2 + 32x3 + 19x4 + 23x5 == 75
```

**The result**

```
Classical result             -> 37   (64 rule evaluations)
Quantum dominant measurement -> 100101 -> 37   (6 oracle calls, P = 0.9968)
```

The point of the lab is *not* that the quantum computer knows `37`. It knows only the
**rule** (the weights and the target 75). Grover turns that rule into a phase condition
and lets interference do the searching. `37` appears in this repo only as a
validation constant — Check E proves it never enters the circuit construction.

---

## Files

| File | What it is |
|------|-----------|
| `classical_subset_sum.py` | Brute force over all 64 binary combinations — the ground truth |
| `grover_subset_sum.py` | The main lab — registers, reversible adder, phase oracle, Grover operator, and all 5 validation checks |
| `iteration_sweep.py` | Why exactly 6 iterations, and what over-rotation looks like |
| `make_figures.py` | Renders the circuit diagrams (no simulation, ~5 s) |
| `RESULTS.md` | Captured console output of every run |
| [`../content.md`](../content.md) | The conceptual write-up this lab supports |

**Figures** (in [`../media/`](../media), shared with the write-up)

| File | What it shows |
|------|---------------|
| `grover-subset-sum-register-map.png` | How the 22 qubits split into state / sum / carry / control |
| `grover-subset-sum-phase-oracle.png` | The phase oracle: compute → mark → uncompute |
| `grover-subset-sum-grover-operator.png` | `Q = D · S_f`, with the diffusion restricted to q0–q5 |
| `grover-subset-sum-full-circuit.png` | `H⊗6` → six `Q` blocks → measure the search register |
| `grover-subset-sum-measurement-histogram.png` | Measured distribution after 6 iterations, 4096 shots |
| `grover-subset-sum-iteration-sweep.png` | P(solution) vs. iteration count, measured against theory |

## How to run

```bash
pip install qiskit qiskit-aer pylatexenc matplotlib
cd topics/quantum-computing/grover-search-for-subset-sum/lab

# classical only, instant
python3 classical_subset_sum.py

# full quantum lab + all checks, ~80s on Aer
python3 grover_subset_sum.py

# spec-mandated StatevectorSampler path (exact, but ~10 min — same answer)
python3 grover_subset_sum.py --sampler statevector --shots 2000

# why r=6, and what happens if you keep going
python3 iteration_sweep.py

# re-render the diagrams
python3 make_figures.py
```

Tested with Python 3.9, qiskit 2.2.3, qiskit-aer 0.17.2. Timings below are from a
Mac Mini (Apple silicon); Aer is multithreaded, so they will vary with core count.

`make_figures.py` writes into a local `figures/` directory. The copies displayed on
this page live in [`../media/`](../media) and are regenerated from the same script.

---

## Results

All runs 2026-08-09 on a Mac Mini (Apple silicon), qiskit 2.2.3 / qiskit-aer 0.17.2.
Full console transcripts are in [`RESULTS.md`](RESULTS.md).

| Method | Script | Purpose | Running time | Duration | Result |
|--------|--------|---------|--------------|----------|--------|
| Classical brute force | `classical_subset_sum.py` | Enumerate all 64 binary combinations, establish the ground truth the quantum run is judged against | 22:30 | < 0.1 s | 1 solution: `(1,0,1,0,0,1)` = **37**, S(x) = 75 — Check A pass |
| Quantum Grover — validation pass | `grover_subset_sum.py` | Build adder + phase oracle + Grover operator, then run checks B, C, E before trusting the search | 22:29 | 9.3 s (B) + 9.4 s (C) | Check B: ancilla leakage 5.7e-14, only state 37 phase-flipped. Check C: 0.0156 → 0.1348 (8.63×). Check E: no `37` in circuit code — **all pass** |
| Quantum Grover — final search (Aer) | `grover_subset_sum.py` | The actual answer: H⊗6, 6 Grover iterations, measure the 6 search qubits, 4096 shots | 22:29 | 55.9 s sim (75.8 s incl. checks) | `100101` → **37** with 4083/4096 counts, **P = 0.9968** vs theory 0.9966 — Check D pass, matches classical |
| Iteration sweep | `iteration_sweep.py` | Show *why* r = 6 — measure P(solution) for r = 0…12 and compare with sin²((2r+1)θ) | 22:14 | 130.9 s | Peak at r = 6 (P = 0.9966), matches theory to 3.7e-13; P collapses to 0.00007 by r = 12 |
| Quantum Grover — StatevectorSampler | `grover_subset_sum.py --sampler statevector` | Spec-mandated exact primitive path, 2000 shots — same circuit, no Aer | 22:10 | 610.4 s (10.2 min) | `100101` → **37**, **P = 0.9970** — identical answer to Aer, 10× the wall time |

**Bottom line:** classical needs **64** rule evaluations, Grover needs **6** oracle calls,
and both land on `37`. The quantum run reaches **99.68%** confidence in the right answer
while the oracle only ever knew the weights and the target 75.

### Measured distribution — 6 iterations, 4096 shots

![Grover measurement histogram](../media/grover-subset-sum-measurement-histogram.png)

64 candidates started with equal 1.56% probability. After six Grover iterations one
of them holds **99.68%** of the measurements. Everything else is statistical dust —
the next-best outcome got 2 counts out of 4096.

---

## The mental model

Everything hangs off one chain:

```
problem rule -> reversible checker -> phase oracle -> amplification -> measurement
```

### 1. The rule becomes reversible arithmetic

A quantum circuit cannot "just evaluate" `S(x)`; it has to do so **reversibly**, on all
64 candidates in superposition at once:

```
|x> |0>_sum   ->   |x> |S(x)>_sum
```

`WeightedAdder(num_state_qubits=6, weights=[18,36,34,32,19,23])` does this. Max sum is
162, so the sum register needs 8 bits (2^7 = 128 < 162 < 256 = 2^8).

![Register map](../media/grover-subset-sum-register-map.png)

### The 22-qubit budget

| Qubits | Register | # | What it holds | Start | After the oracle | H? | Diffusion? | Measured? |
|--------|----------|---|---------------|-------|------------------|----|-----------|-----------|
| **q0–q5** | `state` | 6 | The candidate itself — one qubit per binary variable x0..x5. This is the search space. | `\|0>` | unchanged except for a phase | **yes** | **yes** | **yes** |
| **q6–q13** | `sum` | 8 | `S(x)` written in binary, little-endian: `sum[i]` = bit `i`, place value 2^i. Max sum 162 needs 8 bits. | `\|0>` | back to `\|0>` (uncomputed) | no | no | no |
| **q14–q20** | `carry` | 7 | Ripple carries while each weight is added into `sum`. Always `num_sum − 1` of them. | `\|0>` | `\|0>` | no | no | no |
| **q21** | `control` | 1 | Ancilla for the v-chain decomposition of the 3-control `mcx` gates inside the carry logic. Exists only because `num_sum > 2`. | `\|0>` | `\|0>` | no | no | no |

Only 6 of the 22 qubits carry the answer. The other 16 exist purely so the arithmetic
can be done **reversibly** — quantum gates are unitary, so `S(x)` cannot be computed
without somewhere to put the intermediate results.

Two things I verified rather than assumed:

- **`carry` and `control` are already clean at the end of the adder itself** —
  `P(all zero) = 1.000000000000` after the adder alone. They are borrowed and returned
  within the addition.
- **`sum` is the one that stays entangled with the search register.** After the adder,
  measuring `sum` would collapse the superposition of candidates. *That* is what the
  uncompute step exists to undo — not the carries.

### Detail — the search register, qubit by qubit

| Qubit | Variable | Weight it contributes |
|-------|----------|-----------------------|
| q0 | x0 | 18 |
| q1 | x1 | 36 |
| q2 | x2 | 34 |
| q3 | x3 | 32 |
| q4 | x4 | 19 |
| q5 | x5 | 23 |

The weights are **not stored in any qubit**. They are baked into which gates fire: the
adder walks the binary expansion of each weight and emits controlled additions, so
"18" lives in the circuit's shape, not in a register.

### Detail — the sum register, qubit by qubit

| Qubit | Place value | Bit of 75 | `X` applied before the phase flip? |
|-------|-------------|-----------|-----------------------------------|
| q6 | 1 | 1 | no |
| q7 | 2 | 1 | no |
| q8 | 4 | 0 | **yes** |
| q9 | 8 | 1 | no |
| q10 | 16 | 0 | **yes** |
| q11 | 32 | 0 | **yes** |
| q12 | 64 | 1 | no |
| q13 | 128 | 0 | **yes** |

`75 = 64 + 8 + 2 + 1`, so q6, q7, q9 and q12 should read `1` and the other four should
read `0`. Flipping those four with `X` turns "equals 75" into "all eight are 1" — which
is exactly the condition a multi-controlled `P(π)` can detect. Compare this column
against the four `X` gates in the oracle diagram below: q8, q10, q11, q13.

Side note on how sparse the target is: the 64 candidates produce only **60 distinct
sums** (a few collide), and exactly one of them lands on 75 — measured
`P(sum == 75) = 1/64` exactly.

### 2. The checker becomes a phase

The oracle must produce `|x> -> (-1)^f(x)|x>` where `f(x) = [S(x) == 75]`.

75 = `0b01001011`, so in little-endian sum-register order the target bits are
`[1,1,0,1,0,0,1,0]`. Apply `X` to the sum qubits where the target bit is **0** — now
"sum equals 75" is the same as "all eight sum qubits are 1" — then one multi-controlled
`P(π)` fires only on that pattern, and undo the `X` gates.

That's the whole trick: **equality against a known constant becomes an all-ones
condition, and all-ones is what a multi-controlled gate detects.**

### 3. Compute → mark → uncompute

![Phase oracle circuit](../media/grover-subset-sum-phase-oracle.png)

Read it left to right: `S(x)` computes the weighted sum into q6–q13; the four `X` gates
sit on q8, q10, q11, q13 (the sum bits where 75 has a `0`); `P(π)` fires only when all
eight sum qubits are `1`; the `X` gates undo themselves; `adder_dg` uncomputes the sum.
The search register q0–q5 has no gate on it at all — it only picks up a phase.

The uncompute step is not optional. As shown above, the `sum` register leaves the adder
entangled with the search register; if it stayed that way, the diffusion operator would
reflect a *mixed* state and the interference that makes Grover work would be destroyed.
Check B verifies that after the full oracle, leakage out of the all-ancillas-zero
subspace is `5.7e-14`.

### 4. Amplification reflects on six qubits only

```python
grover_operator(oracle, state_preparation=state_prep, reflection_qubits=[0,1,2,3,4,5])
```

`reflection_qubits` is the load-bearing argument. The oracle circuit is 22 qubits wide,
but the diffusion must reflect about the mean of the **six search qubits only** — never
across the arithmetic ancillas.

![Grover operator](../media/grover-subset-sum-grover-operator.png)

This one picture is the whole algorithm. Left half is the oracle spanning all 22 qubits.
Right half is the diffusion — `H · X · (multi-controlled Z) · X · H` — and it touches
**only q0–q5**. The wires q6–q21 run flat through it. That is what `reflection_qubits`
buys you; get it wrong and you reflect over 4 million states instead of 64.

Stack six of those between the Hadamards and the measurement and you have the full
search circuit:

![Full search circuit](../media/grover-subset-sum-full-circuit.png)

### 5. Grover rotates, so iteration count matters

```
theta = arcsin(sqrt(M/N)) = arcsin(sqrt(1/64)) = 0.125328 rad
r     = floor(pi / (4*theta)) = floor(6.2667) = 6
P(r)  = sin^2((2r+1)*theta)  ->  P(6) = 99.66%
```

`iteration_sweep.py` measures this on the real circuit and it tracks theory to
`3.7e-13`:

| r | 0 | 1 | 3 | 5 | **6** | 7 | 9 | 12 |
|---|---|---|---|---|---|---|---|---|
| P(solution) | 0.0156 | 0.1348 | 0.5914 | 0.9635 | **0.9966** | 0.9074 | 0.4750 | 0.00007 |

![Iteration sweep](../media/grover-subset-sum-iteration-sweep.png)

More iterations is not better. Grover is a rotation in the 2D plane spanned by
{marked, unmarked}; past the peak it rotates the state back *out* of the marked
subspace. At r=12 the answer is essentially gone (P = 0.00007 — worse than not
searching at all). The simulated points sit on the analytic curve to 3.7e-13, which is
a good sanity check that the circuit really is implementing the textbook operator.

---

## Validation checks (all pass)

| Check | What it proves | Result |
|-------|----------------|--------|
| A | Classical brute force finds exactly one solution | `(1,0,1,0,0,1)` = 37 |
| B | Oracle phase-flips only the satisfying state; ancillas clean | leakage `5.7e-14`, flipped set = `[37]` |
| C | One iteration amplifies above the flat 1/64 | 0.0156 → 0.1348 (8.63×) |
| D | Six iterations dominated by `100101` | p = 0.9968 over 4096 shots |
| E | The answer is never hard-coded in the quantum construction | source scan clean |

**Check B is worth understanding.** Rather than testing 64 basis states one at a time,
it applies the oracle to the uniform superposition and reads the whole statevector once.
Every amplitude at `|x>|0...0>_anc` must equal `(1/8)·(-1)^f(x)`. That validates all 64
candidates *and* ancilla cleanliness in a single 10-second simulation.

**Check E is mechanical, not a promise.** It runs `inspect.getsource()` over every
circuit-building function and greps for `37` and `100101`. If the answer ever leaks into
the oracle, the check fails.

---

## Bit ordering (the thing that trips everyone)

Qiskit prints classical bits MSB-left, so the measured string reads **x5 x4 x3 x2 x1 x0**:

```
measured '100101'
          ||||||
          |||||+- x0 = 1
          ||||+-- x1 = 0
          |||+--- x2 = 1
          ||+---- x3 = 0
          |+----- x4 = 0
          +------ x5 = 1

tuple  (x0..x5) = (1,0,1,0,0,1)
integer         = 2^0 + 2^2 + 2^5 = 37
rule check      = 18*1 + 34*1 + 23*1 = 75  ✓
```

Note the trap: the tuple `(1,0,1,0,0,1)` and the string `100101` look confusingly
alike, but one is the reverse of the other. Always decode with an explicit
`reversed()` rather than eyeballing it.

---

## Gotchas found while building this

1. **`WeightedAdder` mutates your weights list in place.** In Qiskit 2.2.3 it converts
   the elements of the list you pass into `numpy.int64` *in the caller's list*. After
   that, `sum(WEIGHTS).bit_length()` raises `AttributeError`. Pass `list(WEIGHTS)`.

2. **`num_ancilla_qubits` no longer exists.** Qiskit 2.x splits it into
   `num_carry_qubits` (7) and `num_control_qubits` (1). The lab spec's suggested
   attribute list is from an older API.

3. **`StatevectorSampler` is exact but slow at this width.** 22 qubits × 6 Grover
   iterations ≈ 43k gates; the pure-Qiskit statevector path takes ~14 minutes versus
   ~58 seconds on Aer. Both give the same answer — Aer is the default here, and
   `--sampler statevector` runs the spec's path when you want it.

4. **Use `save_probabilities`, not 13 separate simulations.** The iteration sweep drops
   an Aer probability snapshot after each iteration inside one circuit, so probing
   r = 0..12 costs one simulation instead of thirteen.

5. **Matplotlib must be forced to `Agg`.** Tk is broken in this venv; every plot here
   is written headless to `figures/`.

---

## What this lab does and does not claim

Classical search: `O(N)` rule evaluations — 64 here.
Grover: `O(sqrt(N))` oracle calls — 6 here.

That is a real query-complexity statement and it is *not* a practical speedup claim.
Each of those 6 oracle calls expands to ~7,000 basic gates, because reversible
arithmetic and multi-controlled gates are expensive. Brute-forcing 64 additions in
Python takes microseconds; the quantum simulation takes ~58 seconds.

The transferable lesson:

> Before claiming Grover helps a problem, first show that the candidate-checking rule
> can be implemented as a sufficiently efficient reversible phase oracle. The oracle,
> not the amplification, is where real applications live or die.

---

## Next steps

- **Multiple solutions** — change the target so M > 1 and watch `r = floor(pi/(4·arcsin(sqrt(M/N))))`
  shrink. Good way to see why you need to know (or estimate) M in advance.
- **Unknown M** — implement the exponential-guess schedule (Boyer–Brassard–Høyer–Tapp)
  when the number of solutions isn't known up front.
- **Real IBM hardware** — needs an IBM Quantum account and `qiskit-ibm-runtime`. Be
  warned: a 22-qubit, 43k-gate circuit is far beyond current NISQ coherence. To run on
  hardware, shrink to 3–4 variables and a smaller sum register first.
- **Compare with a smarter classical baseline** — meet-in-the-middle solves subset-sum
  in `O(2^(n/2))`, which is the same asymptotic as Grover here. Worth confronting.

## References

- [IBM Quantum — Grover's algorithm](https://quantum.cloud.ibm.com/docs/en/tutorials/grovers-algorithm)
- [`WeightedAdder`](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.WeightedAdder)
- [`grover_operator`](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator)
- [`StatevectorSampler`](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler)
