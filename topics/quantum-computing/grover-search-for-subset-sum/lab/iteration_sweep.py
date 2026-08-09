#!/usr/bin/env python3
"""
Why exactly 6 Grover iterations? (Part 6, made visible.)

Grover is a ROTATION, not a ratchet. Each iteration rotates the state by 2*theta
in the 2D plane spanned by {marked, unmarked}, so the success probability is

    P(r) = sin^2( (2r+1) * theta ),   theta = arcsin(sqrt(M/N))

which rises, peaks, and then FALLS again. Running more iterations makes the
answer worse. r = floor(pi / (4*theta)) is the integer closest below the peak.

This script measures P(r) for r = 0..12 on the real circuit and overlays theory.
Cheap trick: instead of simulating 13 separate circuits, build ONE 12-iteration
circuit and drop an Aer save_probabilities() snapshot after each iteration.

Run:
    python3 iteration_sweep.py           # ~2 min
    python3 iteration_sweep.py --max 16
"""

import argparse
import sys
import time
from pathlib import Path

import numpy as np
from qiskit import QuantumCircuit, transpile

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classical_subset_sum import bits_to_int, bits_to_qiskit_string, brute_force  # noqa: E402
from grover_subset_sum import (  # noqa: E402
    FIGDIR,
    TARGET,
    WEIGHTS,
    build_grover_operator,
    build_oracle,
    build_state_preparation,
    build_weighted_adder,
    optimal_iterations,
    success_probability,
)

try:
    from qiskit_aer import AerSimulator
except ImportError:
    sys.exit("iteration_sweep.py needs qiskit-aer: pip install qiskit-aer")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--max", type=int, default=12, help="highest iteration count to probe")
    args = ap.parse_args()

    solution = brute_force(verbose=False)[0][0]
    sol_int = bits_to_int(solution)

    adder, layout = build_weighted_adder()
    oracle, _ = build_oracle(adder, layout, TARGET)
    state_prep = build_state_preparation(layout)
    grover_op = build_grover_operator(oracle, state_prep, layout)

    n_candidates = 2 ** layout.n_state
    r_opt, theta = optimal_iterations(n_candidates, 1)

    print(f"N = {n_candidates}, M = 1, theta = {theta:.6f} rad")
    print(f"optimal r = floor(pi/(4*theta)) = {r_opt}")
    print(f"probing r = 0..{args.max} with one simulation + probability snapshots\n")

    # One circuit, snapshot after every iteration.
    qc = QuantumCircuit(layout.n_total)
    qc.compose(state_prep, inplace=True)
    qc.save_probabilities(layout.search, label="r00")
    for r in range(1, args.max + 1):
        qc.compose(grover_op, inplace=True)
        qc.save_probabilities(layout.search, label=f"r{r:02d}")

    sim = AerSimulator(method="statevector")
    t0 = time.time()
    data = sim.run(transpile(qc, sim, optimization_level=1), shots=1).result().data()
    print(f"simulated {args.max} iterations in {time.time() - t0:.1f}s\n")

    measured, theory = [], []
    print(f"  r   P(solution)   theory      note")
    print(f"  --  ------------  ----------  ----")
    for r in range(args.max + 1):
        p = float(np.asarray(data[f"r{r:02d}"])[sol_int])
        t = success_probability(r, theta)
        measured.append(p)
        theory.append(t)
        note = ""
        if r == r_opt:
            note = "<-- optimal, floor(pi/(4*theta))"
        elif r > r_opt and p < measured[r - 1]:
            note = "over-rotated: worse than before"
        print(f"  {r:2d}   {p:.6f}     {t:.6f}    {note}")

    best = int(np.argmax(measured))
    print(f"\nempirical peak at r = {best} (P = {measured[best]:.6f})")
    print(f"formula predicted r = {r_opt}  ->  {'MATCH' if best == r_opt else 'MISMATCH'}")
    print(f"max |measured - theory| = {max(abs(m - t) for m, t in zip(measured, theory)):.2e}")
    print("\nLesson: Grover rotates. Past the peak, extra iterations rotate the state")
    print("back out of the marked subspace and the answer degrades.")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("(matplotlib missing - no plot)")
        return 0

    rs = np.arange(args.max + 1)
    fine = np.linspace(0, args.max, 400)
    FIGDIR.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(fine, np.sin((2 * fine + 1) * theta) ** 2, color="#adb5bd", lw=1.2,
            label=r"theory $\sin^2((2r+1)\theta)$")
    ax.plot(rs, measured, "o-", color="#264653", lw=1.5, ms=5, label="simulated circuit")
    ax.axvline(r_opt, color="#e76f51", ls="--", lw=1.2, label=f"optimal r = {r_opt}")
    ax.axhline(1 / n_candidates, color="#8d99ae", ls=":", lw=1,
               label=f"no search: 1/{n_candidates}")
    ax.annotate(f"P = {measured[r_opt]:.4f}", xy=(r_opt, measured[r_opt]),
                xytext=(r_opt + 0.6, measured[r_opt] - 0.08),
                arrowprops=dict(arrowstyle="->", color="#e76f51"), color="#e76f51")
    ax.set_xlabel("Grover iterations r")
    ax.set_ylabel(f"P(measuring '{bits_to_qiskit_string(solution)}')")
    ax.set_title(f"Grover over-rotation - subset sum {'+'.join(map(str, WEIGHTS))} == {TARGET}")
    ax.set_ylim(0, 1.05)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(alpha=0.25)
    fig.tight_layout()
    out = FIGDIR / "iteration_sweep.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    print(f"\nplot -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
