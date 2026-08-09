#!/usr/bin/env python3
"""
Render the diagrams embedded in README.md.

Produces, into figures/:
    register_map.png     - how the 22 qubits are split into state/sum/carry/control
    oracle_circuit.png   - the phase oracle at block level: compute -> mark -> uncompute
    grover_operator.png  - Q = D * S_f, showing oracle and diffusion blocks
    full_circuit.png     - H^6, six Q blocks, measure the search register

The histogram and the iteration sweep are produced by grover_subset_sum.py and
iteration_sweep.py respectively.

Run:
    python3 make_figures.py     # ~5s, no simulation
"""

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # headless: Tk is broken in this venv
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

from qiskit import ClassicalRegister, QuantumCircuit  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grover_subset_sum import (  # noqa: E402
    FIGDIR,
    TARGET,
    WEIGHTS,
    build_grover_operator,
    build_oracle,
    build_state_preparation,
    build_weighted_adder,
)


def draw_register_map(layout):
    """Structure diagram: which qubit index does what."""
    blocks = [
        ("state / search\nx0..x5", layout.search, "#2a9d8f",
         "H applied here\nreflection acts here"),
        (f"sum\nS(x), {layout.n_sum} bits", layout.sum, "#e9c46a",
         f"holds {' + '.join(str(w) for w in WEIGHTS)}\ncompared against {TARGET}"),
        ("carry\nripple scratch", layout.carry, "#f4a261", "adder-internal"),
        ("control\nscratch", layout.control, "#e76f51", "adder-internal"),
    ]

    fig, ax = plt.subplots(figsize=(11, 3.6))
    for label, idx, color, note in blocks:
        x0, width = idx[0], len(idx)
        ax.add_patch(Rectangle((x0, 0.35), width, 0.5, facecolor=color,
                               edgecolor="white", lw=2))
        if width >= 3:
            ax.text(x0 + width / 2, 0.60, label, ha="center", va="center",
                    fontsize=10, weight="bold", color="#1d3557")
            ax.text(x0 + width / 2, 0.22, note, ha="center", va="top",
                    fontsize=7.5, color="#495057")
        else:
            # too narrow to hold text - label it underneath instead
            ax.text(x0 + width / 2, 0.22, label.replace("\n", " ") + f"\n{note}",
                    ha="center", va="top", fontsize=7.5, color="#495057")
        ax.text(x0 + width / 2, 0.93, f"q{idx[0]}–q{idx[-1]}", ha="center",
                va="bottom", fontsize=8, color="#495057")

    ax.plot([0, layout.n_total], [0.35, 0.35], color="#dee2e6", lw=0.8, zorder=0)
    ax.set_xlim(-0.4, layout.n_total + 0.4)
    ax.set_ylim(-0.05, 1.15)
    ax.set_xticks(range(0, layout.n_total + 1, 2))
    ax.set_yticks([])
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.set_xlabel("qubit index")
    ax.set_title(f"Register map — {layout.n_total} qubits total "
                 f"(only the 6 search qubits are measured)", fontsize=11)
    fig.tight_layout()
    out = FIGDIR / "register_map.png"
    fig.savefig(out, dpi=150)
    plt.close(fig)
    return out


def save_circuit(circuit, name, title, fold=-1, scale=0.75):
    fig = circuit.draw("mpl", fold=fold, scale=scale, style={"name": "clifford"})
    # y > 1 puts the title above the drawer's own bbox; bbox_inches="tight" then
    # crops to title + circuit with no dead band in between.
    fig.suptitle(title, fontsize=11, y=1.02)
    out = FIGDIR / name
    fig.savefig(out, dpi=140, bbox_inches="tight")
    plt.close(fig)
    trim_whitespace(out)
    return out


def trim_whitespace(path, pad=14, max_gap=28):
    """
    The mpl circuit drawer bottom-anchors its content, leaving a dead white band
    between the title and the circuit. bbox_inches='tight' only crops the OUTER
    margin, so also collapse any interior run of all-white rows down to max_gap.
    """
    import numpy as np
    from PIL import Image

    img = np.asarray(Image.open(path).convert("RGB"))
    white_row = (img >= 250).all(axis=(1, 2))

    keep = np.ones(len(white_row), dtype=bool)
    start = None
    for i, is_white in enumerate(np.append(white_row, False)):
        if is_white and start is None:
            start = i
        elif not is_white and start is not None:
            if i - start > max_gap:                 # collapse the run
                keep[start + max_gap // 2:i - max_gap // 2] = False
            start = None
    img = img[keep]

    # now crop the outer margin down to `pad`
    content = ~(img >= 250).all(axis=2)
    rows, cols = np.where(content)
    if not len(rows):
        return
    img = img[max(0, rows.min() - pad):rows.max() + pad,
              max(0, cols.min() - pad):cols.max() + pad]
    Image.fromarray(img).save(path)


def main():
    FIGDIR.mkdir(exist_ok=True)
    adder, layout = build_weighted_adder()
    oracle, _ = build_oracle(adder, layout, TARGET)
    state_prep = build_state_preparation(layout)
    grover_op = build_grover_operator(oracle, state_prep, layout)

    written = [draw_register_map(layout)]

    written.append(save_circuit(
        oracle, "oracle_circuit.png",
        f"Phase oracle: compute S(x) → mark S(x)=={TARGET} → uncompute"))

    # Top level only. Decomposing turns this into 22k unreadable gates; undecomposed
    # it shows exactly the point: oracle across all 22 qubits, diffusion on q0-q5 only.
    written.append(save_circuit(
        grover_op, "grover_operator.png",
        "Grover operator Q = D · S_f  (diffusion touches only q0–q5)"))

    # Structure view: Q as six labelled boxes instead of 43k inlined gates.
    q_gate = grover_op.to_gate(label="Q")
    creg = ClassicalRegister(layout.n_state, "meas")
    display = QuantumCircuit(layout.n_total)
    display.add_register(creg)
    display.compose(state_prep, inplace=True)
    for _ in range(6):
        display.append(q_gate, range(layout.n_total))
    display.measure(layout.search, creg)
    written.append(save_circuit(
        display, "full_circuit.png",
        "Full search circuit: H⊗6 on the search register, six Grover iterations, measure"))

    for path in written:
        print(f"  wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
