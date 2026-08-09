#!/usr/bin/env python3
"""
Grover search for a 6-bit subset-sum problem  (Parts 2-8 of LabGrover.md).

    find x in {0,1}^6 such that  18x0 + 36x1 + 34x2 + 32x3 + 19x4 + 23x5 == 75

The whole point of the lab: the oracle is given the RULE (weights + target 75),
never the ANSWER (37). Grover then amplifies whatever satisfies the rule.

Pipeline
    problem rule -> reversible checker -> phase oracle -> amplification -> measure

Run:
    python3 grover_subset_sum.py                 # Aer, ~2 min
    python3 grover_subset_sum.py --sampler statevector
    python3 grover_subset_sum.py --skip-checks   # just the search
"""

import argparse
import inspect
import re
import sys
import time
from pathlib import Path

import numpy as np
from qiskit import ClassicalRegister, QuantumCircuit, transpile
from qiskit.circuit.library import WeightedAdder, grover_operator
from qiskit.quantum_info import Statevector

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classical_subset_sum import (  # noqa: E402
    N_BITS,
    TARGET,
    WEIGHTS,
    bits_to_int,
    bits_to_qiskit_string,
    brute_force,
    weighted_sum,
)

try:
    import qiskit_aer  # noqa: F401  (importing registers save_statevector on QuantumCircuit)
    from qiskit_aer import AerSimulator

    HAVE_AER = True
except ImportError:  # pragma: no cover
    HAVE_AER = False

FIGDIR = Path(__file__).resolve().parent / "figures"


def rule(msg):
    print("\n" + "=" * 72)
    print(msg)
    print("=" * 72)


# ---------------------------------------------------------------------------
# Parts 2 + 3 - registers and the reversible weighted-sum circuit
# ---------------------------------------------------------------------------

class Layout:
    """Explicit qubit-index map so state/sum/carry/control are never confused."""

    def __init__(self, adder):
        self.n_state = adder.num_state_qubits
        self.n_sum = adder.num_sum_qubits
        self.n_carry = adder.num_carry_qubits
        self.n_control = adder.num_control_qubits
        self.n_total = adder.num_qubits

        cur = 0
        self.search = list(range(cur, cur + self.n_state)); cur += self.n_state
        self.sum = list(range(cur, cur + self.n_sum)); cur += self.n_sum
        self.carry = list(range(cur, cur + self.n_carry)); cur += self.n_carry
        self.control = list(range(cur, cur + self.n_control)); cur += self.n_control
        assert cur == self.n_total, "register map does not cover the circuit"

        # everything that must come back to |0> after the oracle
        self.ancilla = self.sum + self.carry + self.control

    def report(self):
        print(f"  num_state_qubits   : {self.n_state:2d}   indices {self.search}")
        print(f"  num_sum_qubits     : {self.n_sum:2d}   indices {self.sum}")
        print(f"  num_carry_qubits   : {self.n_carry:2d}   indices {self.carry}")
        print(f"  num_control_qubits : {self.n_control:2d}   indices {self.control}")
        print(f"  num_qubits (total) : {self.n_total:2d}")
        print("  note: Qiskit 2.x splits WeightedAdder's ancillas into carry+control,")
        print(f"        so num_ancilla_qubits == {self.n_carry + self.n_control} "
              f"(carry {self.n_carry} + control {self.n_control}).")


def build_weighted_adder():
    """|x>|0>_sum  ->  |x>|S(x)>_sum, reversibly. Knows the weights, not the answer."""
    # Gotcha (qiskit 2.2.3): WeightedAdder mutates the list you hand it, turning the
    # elements into numpy.int64 in place. Pass a copy or WEIGHTS gets silently changed
    # for the rest of the process (and sum(WEIGHTS).bit_length() then blows up).
    adder = WeightedAdder(num_state_qubits=N_BITS, weights=list(WEIGHTS))
    return adder, Layout(adder)


# ---------------------------------------------------------------------------
# Part 4 - the phase oracle:  compute -> mark -> uncompute
# ---------------------------------------------------------------------------

def build_phase_marker(layout, target):
    """
    Flip the global phase iff the sum register holds `target`.

    Trick: X the sum qubits where the target bit is 0, so "sum == target"
    becomes "all sum qubits are 1", then a multi-controlled Z (here mcp(pi))
    fires only on that pattern. Undo the X gates afterwards.
    """
    target_bits = [(target >> i) & 1 for i in range(layout.n_sum)]  # little-endian
    qc = QuantumCircuit(layout.n_total, name=f"mark[S=={target}]")

    zeros = [layout.sum[i] for i, b in enumerate(target_bits) if b == 0]
    if zeros:
        qc.x(zeros)
    qc.mcp(np.pi, layout.sum[:-1], layout.sum[-1])   # all-ones -> phase flip
    if zeros:
        qc.x(zeros)
    return qc, target_bits


def build_oracle(adder, layout, target):
    """
    Full phase oracle:  |x> -> (-1)^[S(x)==target] |x>,  all ancillas restored to |0>.
    """
    adder_gate = adder.to_gate(label="S(x)")
    marker, target_bits = build_phase_marker(layout, target)

    oracle = QuantumCircuit(layout.n_total, name="oracle")
    oracle.append(adder_gate, range(layout.n_total))            # 4.1 compute
    oracle.compose(marker, inplace=True)                        # 4.2 mark
    oracle.append(adder_gate.inverse(), range(layout.n_total))  # 4.3 uncompute
    return oracle, target_bits


# ---------------------------------------------------------------------------
# Parts 5 + 6 - Grover operator and iteration count
# ---------------------------------------------------------------------------

def build_state_preparation(layout):
    """H on the six search qubits ONLY. Ancillas stay |0>."""
    qc = QuantumCircuit(layout.n_total, name="H^6")
    qc.h(layout.search)
    return qc


def build_grover_operator(oracle, state_prep, layout):
    """Q = D * S_f, with the reflection restricted to the six search qubits."""
    return grover_operator(
        oracle,
        state_preparation=state_prep,
        reflection_qubits=layout.search,   # do NOT diffuse over sum/carry ancillas
    )


def optimal_iterations(n_candidates, n_marked):
    """r = floor( pi / (4 * arcsin(sqrt(M/N))) )."""
    theta = np.arcsin(np.sqrt(n_marked / n_candidates))
    return int(np.floor(np.pi / (4 * theta))), theta


def success_probability(r, theta):
    """P(marked) after r iterations = sin^2((2r+1) * theta)."""
    return float(np.sin((2 * r + 1) * theta) ** 2)


# ---------------------------------------------------------------------------
# Simulation helpers
# ---------------------------------------------------------------------------

def get_statevector(qc):
    """Exact statevector. Aer if present (fast C++), else pure-Qiskit fallback."""
    if HAVE_AER:
        sim = AerSimulator(method="statevector")
        probe = qc.copy()
        probe.save_statevector()
        return Statevector(sim.run(transpile(probe, sim, optimization_level=1)).result().get_statevector())
    return Statevector.from_instruction(qc)


def sample_counts(qc, shots, sampler):
    """Measure the six search qubits. sampler in {'aer', 'statevector'}."""
    if sampler == "statevector":
        from qiskit.primitives import StatevectorSampler

        result = StatevectorSampler(seed=1234).run([qc], shots=shots).result()[0]
        return result.data.meas.get_counts()

    if not HAVE_AER:
        raise RuntimeError("qiskit-aer not installed; use --sampler statevector")
    sim = AerSimulator()
    return sim.run(transpile(qc, sim, optimization_level=1), shots=shots, seed_simulator=1234).result().get_counts()


def build_search_circuit(state_prep, grover_op, layout, iterations):
    """H^6, then Q^r, then measure the search register only."""
    creg = ClassicalRegister(layout.n_state, "meas")
    qc = QuantumCircuit(layout.n_total)
    qc.add_register(creg)
    qc.compose(state_prep, inplace=True)
    for _ in range(iterations):
        qc.compose(grover_op, inplace=True)
    qc.measure(layout.search, creg)
    return qc


# ---------------------------------------------------------------------------
# Part 8 - validation checks
# ---------------------------------------------------------------------------

def check_b_oracle(state_prep, oracle, layout, solution):
    """
    Verify the oracle on ALL 64 candidates in one shot.

    Apply it to the uniform superposition: amplitude of |x>|0...0>_anc must be
    (1/8)*(-1)^f(x), and no amplitude may leak into non-zero ancilla states.
    """
    probe = QuantumCircuit(layout.n_total)
    probe.compose(state_prep, inplace=True)
    probe.compose(oracle, inplace=True)

    t0 = time.time()
    amps = np.asarray(get_statevector(probe))
    print(f"  statevector simulated in {time.time() - t0:.1f}s "
          f"({layout.n_total} qubits, {len(amps):,} amplitudes)")

    # Search qubits are indices 0..5, so ancilla==0 <=> basis index < 64.
    n_cand = 2 ** layout.n_state
    clean = amps[:n_cand]
    leakage = 1.0 - float(np.sum(np.abs(clean) ** 2))

    expected = np.array([
        (-1.0 if weighted_sum([(x >> i) & 1 for i in range(N_BITS)]) == TARGET else 1.0) / np.sqrt(n_cand)
        for x in range(n_cand)
    ])
    max_err = float(np.max(np.abs(clean - expected)))

    flipped = [x for x in range(n_cand) if clean[x].real < 0]
    sol_int = bits_to_int(solution)

    print(f"  ancilla leakage        : {leakage:.3e}   (must be ~0 -> ancillas clean)")
    print(f"  max amplitude error    : {max_err:.3e}")
    print(f"  states given -1 phase  : {flipped}  -> {[bits_to_qiskit_string([(x >> i) & 1 for i in range(N_BITS)]) for x in flipped]}")
    print(f"  classical solution int : {sol_int}")

    ok = abs(leakage) < 1e-9 and max_err < 1e-8 and flipped == [sol_int]
    print(f"  CHECK B {'PASSED' if ok else 'FAILED'} - exactly the satisfying state is "
          f"phase-flipped, ancillas return to |0>.")
    return ok


def check_c_one_iteration(state_prep, grover_op, layout, solution, theta):
    """After one iteration the marked state must be well above the flat 1/64."""
    qc = QuantumCircuit(layout.n_total)
    qc.compose(state_prep, inplace=True)
    qc.compose(grover_op, inplace=True)

    t0 = time.time()
    sv = get_statevector(qc)
    probs = sv.probabilities(layout.search)
    dt = time.time() - t0

    p_sol = float(probs[bits_to_int(solution)])
    p_flat = 1.0 / (2 ** layout.n_state)
    p_theory = success_probability(1, theta)

    print(f"  simulated in {dt:.1f}s")
    print(f"  P(solution) before any iteration : {p_flat:.6f}   (1/64)")
    print(f"  P(solution) after 1 iteration    : {p_sol:.6f}")
    print(f"  theory sin^2(3*theta)            : {p_theory:.6f}")
    print(f"  amplification factor             : {p_sol / p_flat:.2f}x")

    ok = p_sol > p_flat and abs(p_sol - p_theory) < 1e-6
    print(f"  CHECK C {'PASSED' if ok else 'FAILED'} - amplitude amplification is working.")
    return ok


def check_e_no_hardcoded_answer(solution):
    """
    Confirm the answer (37 / the solution bit pattern) never appears inside the
    quantum construction: oracle, marker, state preparation, diffusion.
    """
    sol_int = bits_to_int(solution)
    sol_str = bits_to_qiskit_string(solution)
    guarded = [build_weighted_adder, build_phase_marker, build_oracle,
               build_state_preparation, build_grover_operator, build_search_circuit]

    offenders = []
    for fn in guarded:
        src = inspect.getsource(fn)
        if re.search(rf"\b{sol_int}\b", src) or sol_str in src:
            offenders.append(fn.__name__)

    print(f"  scanned  : {', '.join(fn.__name__ for fn in guarded)}")
    print(f"  forbidden: integer {sol_int}, bitstring '{sol_str}'")
    print(f"  allowed  : weights {WEIGHTS}, target {TARGET}")
    ok = not offenders
    print(f"  CHECK E {'PASSED' if ok else 'FAILED'}"
          + ("" if ok else f" - answer leaked into {offenders}"))
    return ok


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

def save_drawings(adder, oracle, grover_op, circuit):
    FIGDIR.mkdir(exist_ok=True)
    items = [
        ("adder_weighted_sum.txt", adder.draw("text", fold=110)),
        ("oracle_block.txt", oracle.draw("text", fold=110)),
        ("grover_operator_block.txt", grover_op.draw("text", fold=110)),
        ("full_circuit_block.txt", circuit.draw("text", fold=110)),
    ]
    for name, art in items:
        (FIGDIR / name).write_text(str(art))
    print(f"  circuit drawings -> {FIGDIR}/")


def save_histogram(counts, solution, iterations, shots):
    try:
        import matplotlib
        matplotlib.use("Agg")  # headless: Tk is broken on this Mac Mini
        import matplotlib.pyplot as plt
    except ImportError:
        print("  (matplotlib not available - skipping histogram)")
        return

    FIGDIR.mkdir(exist_ok=True)
    top = sorted(counts.items(), key=lambda kv: -kv[1])[:12]
    labels = [k for k, _ in top]
    values = [v for _, v in top]
    target_label = bits_to_qiskit_string(solution)
    colors = ["#2a9d8f" if lb == target_label else "#adb5bd" for lb in labels]

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.bar(labels, values, color=colors)
    ax.set_xlabel("measured search register (x5 x4 x3 x2 x1 x0)")
    ax.set_ylabel(f"counts / {shots} shots")
    ax.set_title(f"Grover, {iterations} iterations - subset sum "
                 f"{'+'.join(map(str, WEIGHTS))} == {TARGET}")
    ax.tick_params(axis="x", rotation=45)
    for lb, v in zip(labels, values):
        ax.text(lb, v, f"{v / shots:.3f}", ha="center", va="bottom", fontsize=8)
    fig.tight_layout()
    out = FIGDIR / "grover_counts_histogram.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"  histogram -> {out}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sampler", choices=["aer", "statevector"], default="aer",
                    help="'aer' = qiskit-aer (fast). 'statevector' = qiskit StatevectorSampler (exact, slow).")
    ap.add_argument("--shots", type=int, default=4096)
    ap.add_argument("--iterations", type=int, default=None,
                    help="override the computed optimal iteration count")
    ap.add_argument("--skip-checks", action="store_true")
    args = ap.parse_args()

    t_start = time.time()

    # ---- classical ground truth -------------------------------------------
    rule("PART 1 - CLASSICAL REFERENCE")
    solutions, checked = brute_force(verbose=False)
    solution = solutions[0]
    print(f"brute force checked {checked} candidates, found {len(solutions)} solution")
    print(f"  x = {solution}   int = {bits_to_int(solution)}   "
          f"qiskit = '{bits_to_qiskit_string(solution)}'")
    print("  (used ONLY for validation - never fed into the quantum circuit)")

    # ---- parts 2 + 3 -------------------------------------------------------
    rule("PARTS 2+3 - SEARCH REGISTER AND REVERSIBLE WEIGHTED SUM")
    adder, layout = build_weighted_adder()
    print(f"S(x) = " + " + ".join(f"{w}*x{i}" for i, w in enumerate(WEIGHTS)))
    print(f"max S = {sum(WEIGHTS)} -> needs {sum(WEIGHTS).bit_length()} sum bits "
          f"(2^7={2**7} < {sum(WEIGHTS)} < {2**8}=2^8)\n")
    layout.report()

    state_prep = build_state_preparation(layout)
    print(f"\nstate preparation: H on qubits {layout.search} only "
          f"-> uniform superposition over {2 ** layout.n_state} candidates")

    # ---- part 4 ------------------------------------------------------------
    rule("PART 4 - PHASE ORACLE (compute -> mark -> uncompute)")
    oracle, target_bits = build_oracle(adder, layout, TARGET)
    print(f"target {TARGET} in the sum register (little-endian, sum[i] = bit i):")
    print(f"  bits  : {target_bits}")
    print(f"  binary: {TARGET:08b}  = " + " + ".join(
        str(1 << i) for i, b in enumerate(target_bits) if b) + f" = {TARGET}")
    print(f"  X applied to sum qubits {[layout.sum[i] for i, b in enumerate(target_bits) if b == 0]} "
          "so 'equals target' becomes 'all ones'")
    decomposed = oracle.decompose(reps=4)
    print(f"oracle: {oracle.num_qubits} qubits, {decomposed.size()} basic gates, "
          f"depth {decomposed.depth()}")

    # ---- parts 5 + 6 -------------------------------------------------------
    rule("PARTS 5+6 - GROVER OPERATOR AND ITERATION COUNT")
    grover_op = build_grover_operator(oracle, state_prep, layout)
    print(f"Q = D * S_f built on {grover_op.num_qubits} qubits; "
          f"reflection restricted to search qubits {layout.search}")

    n_candidates = 2 ** layout.n_state
    n_marked = len(solutions)
    r_opt, theta = optimal_iterations(n_candidates, n_marked)
    iterations = args.iterations if args.iterations is not None else r_opt
    print(f"\nN = {n_candidates} candidates, M = {n_marked} marked")
    print(f"theta = arcsin(sqrt(M/N)) = {theta:.6f} rad")
    print(f"r = floor(pi / (4*theta)) = floor({np.pi / (4 * theta):.4f}) = {r_opt}")
    print(f"predicted P(solution) after {r_opt} iterations = "
          f"{success_probability(r_opt, theta) * 100:.2f}%")
    if iterations != r_opt:
        print(f"  (overridden by --iterations {iterations})")

    # ---- part 8 checks B, C, E --------------------------------------------
    results = {"A": True}
    if not args.skip_checks:
        rule("CHECK B - ORACLE CORRECTNESS (all 64 candidates at once)")
        results["B"] = check_b_oracle(state_prep, oracle, layout, solution)

        rule("CHECK C - ONE GROVER ITERATION")
        results["C"] = check_c_one_iteration(state_prep, grover_op, layout, solution, theta)

        rule("CHECK E - NO ANSWER HARD-CODING")
        results["E"] = check_e_no_hardcoded_answer(solution)

    # ---- part 7 ------------------------------------------------------------
    rule(f"PART 7 - FULL RUN: {iterations} GROVER ITERATIONS, {args.shots} SHOTS")
    circuit = build_search_circuit(state_prep, grover_op, layout, iterations)
    print(f"circuit: {circuit.num_qubits} qubits, {circuit.decompose(reps=5).size()} gates after decomposition")
    print(f"sampler: {args.sampler}"
          + ("  (StatevectorSampler is exact but slow - expect ~15 min)"
             if args.sampler == "statevector" else "  (qiskit-aer statevector)"))

    t0 = time.time()
    counts = sample_counts(circuit, args.shots, args.sampler)
    print(f"simulated in {time.time() - t0:.1f}s")

    ranked = sorted(counts.items(), key=lambda kv: -kv[1])
    print("\ntop measurement outcomes:")
    for bitstr, cnt in ranked[:6]:
        bits = tuple(int(b) for b in reversed(bitstr))
        marker = "  <-- satisfies the rule" if weighted_sum(bits) == TARGET else ""
        print(f"  {bitstr}   {cnt:6d}   p={cnt / args.shots:.4f}   "
              f"int={int(bitstr, 2):2d}   S(x)={weighted_sum(bits):3d}{marker}")

    # ---- decode + compare --------------------------------------------------
    rule("DECODE AND COMPARE")
    top_str, top_cnt = ranked[0]
    top_bits = tuple(int(b) for b in reversed(top_str))   # qiskit prints x5..x0
    p_top = top_cnt / args.shots

    print(f"dominant bitstring        : '{top_str}'  (Qiskit order = x5 x4 x3 x2 x1 x0)")
    print(f"decoded tuple (x0..x5)    : {top_bits}")
    print(f"decoded integer           : {int(top_str, 2)}  "
          f"(= " + " + ".join(f"2^{i}" for i, b in enumerate(top_bits) if b) + ")")
    print(f"rule check S(x)           : " + " + ".join(
        f"{w}*{x}" for w, x in zip(WEIGHTS, top_bits)) + f" = {weighted_sum(top_bits)} "
        f"({'== ' if weighted_sum(top_bits) == TARGET else '!= '}{TARGET})")
    print(f"measured probability      : {p_top:.4f}")
    print(f"theoretical probability   : {success_probability(iterations, theta):.4f}")

    results["D"] = (top_bits == solution and p_top > 0.9)
    print(f"\nCHECK D {'PASSED' if results['D'] else 'FAILED'} - distribution dominated by "
          f"'{bits_to_qiskit_string(solution)}'.")

    print(f"\nclassical result -> {bits_to_int(solution)}")
    print(f"quantum dominant -> {top_str} -> {int(top_str, 2)}")
    print(f"MATCH: {'YES' if top_bits == solution else 'NO'}")

    # ---- artifacts ---------------------------------------------------------
    rule("ARTIFACTS")
    save_drawings(adder, oracle, grover_op, circuit)
    save_histogram(counts, solution, iterations, args.shots)

    # ---- summary -----------------------------------------------------------
    rule("VALIDATION SUMMARY")
    labels = {"A": "classical brute force finds exactly one solution",
              "B": "oracle phase-flips only the satisfying state, ancillas clean",
              "C": "one Grover iteration amplifies above 1/64",
              "D": f"{iterations} iterations dominated by the solution",
              "E": "no answer hard-coded in the quantum construction"}
    for key in "ABCDE":
        if key in results:
            print(f"  CHECK {key}  {'PASS' if results[key] else 'FAIL'}  - {labels[key]}")
        else:
            print(f"  CHECK {key}  SKIP  - {labels[key]}")

    print(f"\ncost comparison: classical {checked} rule evaluations vs "
          f"Grover {iterations} oracle calls (O(N) vs O(sqrt(N)))")
    print(f"total wall time: {time.time() - t_start:.1f}s")

    ok = all(results.values())
    print("\n" + ("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
