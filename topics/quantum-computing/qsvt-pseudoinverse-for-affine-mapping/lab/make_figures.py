"""Render every figure into ../media/ with the article-slug prefix.

Filenames are already in the shape the research-note repo expects
(`media/<slug-prefix>-<thing>.png`), so publishing is a copy with no renaming.

Matplotlib must stay headless -- Tk is broken in this venv.
"""

import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from block_encoding import RectangularBlockEncoding
from classical_affine import Z, generate_targets
from qsvt_polynomial import QSPPhases, SingularValuePolynomial
from quantum_solver import QuantumPseudoInverse

MEDIA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "media")
PREFIX = "qsvt-affine-"
INK = "#1b1b1d"
ACCENT = "#2f6f9f"
WARM = "#c2603f"
MUTED = "#8a8f98"


def _save(fig, name):
    os.makedirs(MEDIA, exist_ok=True)
    path = os.path.join(MEDIA, PREFIX + name + ".png")
    fig.savefig(path, dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("wrote", os.path.relpath(path))


def fig_block_encoding(enc):
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11.5, 5), gridspec_kw={"width_ratios": [1.25, 1]})

    im = ax.imshow(enc.unitary(), cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_title("$U_A$ — Halmos dilation, $8\\times8$", fontsize=11)
    for edge in (enc.m - 0.5,):
        ax.axhline(edge, color=INK, lw=1.6)
    ax.axvline(enc.n - 0.5, color=INK, lw=1.6)
    box = dict(boxstyle="round,pad=0.28", fc="white", ec="none", alpha=0.88)
    ax.text(1.0, 2.0, "$A$", ha="center", va="center", fontsize=15, color=INK, bbox=box)
    ax.text(5.0, 1.0, "$\\sqrt{I_5-AA^{T}}$", ha="center", va="center", fontsize=10, color=INK, bbox=box)
    ax.text(1.0, 6.0, "$\\sqrt{I_3-A^{T}A}$", ha="center", va="center", fontsize=10, color=INK, bbox=box)
    ax.text(5.5, 6.0, "$-A^T$", ha="center", va="center", fontsize=13, color=INK, bbox=box)
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    ax.set_xlabel("column index (basis state)")
    ax.set_ylabel("row index (basis state)")
    fig.colorbar(im, ax=ax, fraction=0.046)

    ax2.axis("off")
    ax2.set_title("the two subspaces of one 3-qubit register", fontsize=11)
    for j in range(8):
        x = j
        in_L, in_R = j < enc.m, j < enc.n
        ax2.add_patch(plt.Rectangle((x, 1.55), 0.86, 0.5,
                                    color=ACCENT if in_L else "#e8eaed", ec=INK, lw=0.6))
        ax2.add_patch(plt.Rectangle((x, 0.85), 0.86, 0.5,
                                    color=WARM if in_R else "#e8eaed", ec=INK, lw=0.6))
        ax2.text(x + 0.43, 2.35, f"$|{j}\\rangle$", ha="center", fontsize=9)
        ax2.text(x + 0.43, 0.55, format(j, "03b"), ha="center", fontsize=7.5, color=MUTED)
    ax2.text(-0.35, 1.8, "data\n$\\mathcal{H}_L$, dim 5\nholds $|y\\rangle$",
             ha="right", va="center", fontsize=9, color=ACCENT)
    ax2.text(-0.35, 1.1, "parameter\n$\\mathcal{H}_R$, dim 3\nholds $|\\beta\\rangle$",
             ha="right", va="center", fontsize=9, color=WARM)
    ax2.text(4, 0.1, "the two overlap on $|0\\rangle,|1\\rangle,|2\\rangle$ — which is why success is\n"
                     "a question about where the output landed, not a separate flag qubit",
             ha="center", fontsize=8.5, color=MUTED)
    ax2.set_xlim(-3.4, 8.4)
    ax2.set_ylim(-0.1, 2.7)
    fig.tight_layout()
    _save(fig, "block-encoding")


def fig_polynomial(enc, poly):
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 4.6))
    x = np.linspace(-1, 1, 1200)
    s = enc.singular_values

    ax.axhline(1, color=MUTED, ls=":", lw=1)
    ax.axhline(-1, color=MUTED, ls=":", lw=1)
    ax.text(-0.97, 1.03, "hard bound $|p|\\leq1$", fontsize=8, color=MUTED)
    xr = np.linspace(0.08, 1, 600)
    ax.plot(xr, poly.C / xr, color=WARM, lw=1.6, ls="--", label="$C/\\sigma$ (target)")
    ax.plot(-xr, -poly.C / xr, color=WARM, lw=1.6, ls="--")
    ax.plot(x, poly.evaluate(x), color=ACCENT, lw=2, label=f"$p(x)$, degree {poly.degree}")
    ax.plot(s, poly.evaluate(s), "o", color=INK, ms=7, zorder=5,
            label="singular values of $A$")
    for v in s:
        ax.axvline(v, color=INK, lw=0.5, alpha=0.25)
    ax.set_ylim(-1.35, 1.35)
    ax.set_xlim(-1.02, 1.02)
    ax.set_xlabel("$x$")
    ax.set_title("the polynomial only has to be right at three points", fontsize=11)
    ax.legend(fontsize=8.5, loc="lower right")
    ax.grid(alpha=0.15)

    degs = [5, 9, 13, 19, 25]
    errs = [SingularValuePolynomial(s, scale=poly.C, degree=d, mode="interval").objective for d in degs]
    ax2.semilogy(degs, errs, "o-", color=WARM, lw=1.8, label="minimax over the whole interval")
    ax2.axhline(max(poly.singular_value_errors().max(), 1e-17), color=ACCENT, lw=1.8,
                label="exact at the three singular values")
    ax2.set_xlabel("polynomial degree")
    ax2.set_ylabel("max relative error in $C/\\sigma$")
    ax2.set_title("why interval approximation is the expensive way", fontsize=11)
    ax2.legend(fontsize=8.5)
    ax2.grid(alpha=0.2, which="both")
    fig.tight_layout()
    _save(fig, "polynomial-vs-reciprocal")


def fig_circuit(solver, Y):
    qc = solver.build_circuit(Y[:, 0])
    fig = qc.draw("mpl", fold=34, scale=0.55, style={"backgroundcolor": "#ffffff"})
    fig.suptitle(
        f"QSVT pseudoinverse circuit — 5 qubits, depth {qc.depth()}, "
        f"{sum(qc.count_ops().values())} operations",
        fontsize=11, y=1.005,
    )
    _save(fig, "full-circuit")

    # one projector-controlled phase, at readable size
    from qiskit import QuantumCircuit, QuantumRegister

    sys = QuantumRegister(3, "sys")
    anc = QuantumRegister(1, "anc")
    lcu = QuantumRegister(1, "lcu")
    sub = QuantumCircuit(sys, anc, lcu)
    solver._c_pi_not(sub, sys, anc, "R")
    sub.rzz(2.0 * solver.phases[0], anc[0], lcu[0])
    solver._c_pi_not(sub, sys, anc, "R")
    fig = sub.draw("mpl", scale=0.85, style={"backgroundcolor": "#ffffff"})
    fig.suptitle(
        "one projector-controlled phase  $e^{i\\varphi(2\\Pi_R-I)}$:  mark the subspace on "
        "anc,\nrotate, unmark. RZZ ties the sign to lcu so the mirror sequence runs at once.",
        fontsize=10, y=1.02,
    )
    _save(fig, "phase-block")


def fig_success_failure(solver, Y):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    for ax, (label, col) in zip(axes, (("X", 0), ("Y", 1))):
        r = solver.solve_statevector(Y[:, col])
        amps = r["success_amplitudes"].real
        parts = list(amps**2) + [r["P_F"]]
        names = ["$|A_1|^2$", "$|A_2|^2$", "$|A_3|^2$", "$P_F$"]
        colors = [ACCENT, ACCENT, ACCENT, "#d9dde2"]
        bars = ax.bar(names, parts, color=colors, ec=INK, lw=0.7)
        for b, v in zip(bars, parts):
            ax.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.4f}", ha="center", fontsize=8.5)
        ax.set_ylim(0, 1.12)
        ax.set_title(f"{label} column:  $P_S$ = {r['P_S']:.4f},  $P_S+P_F$ = "
                     f"{r['P_S'] + r['P_F']:.6f}", fontsize=10.5)
        ax.set_ylabel("probability")
        ax.grid(axis="y", alpha=0.18)
    fig.suptitle("the failure branch carries the norm the pseudoinverse cannot keep", fontsize=11.5)
    fig.tight_layout()
    _save(fig, "success-failure")


def fig_histograms(solver, Y, shots=20000):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    labels = ["000", "001", "010"]
    for ax, (label, col) in zip(axes, (("X", 0), ("Y", 1))):
        y = Y[:, col]
        r = solver.solve_statevector(y)
        s = solver.sample(y, shots=shots)
        beta = r["beta_classical"]
        theory = beta**2 / np.sum(beta**2)
        idx = np.arange(3)
        ax.bar(idx - 0.19, s["distribution"], 0.38, color=ACCENT, ec=INK, lw=0.6,
               label=f"measured ({s['n_success']} successes)")
        ax.bar(idx + 0.19, theory, 0.38, color=WARM, ec=INK, lw=0.6,
               label="$|\\beta_i|^2/\\sum|\\beta_j|^2$")
        ax.set_xticks(idx)
        ax.set_xticklabels(labels)
        ax.set_xlabel("parameter register")
        ax.set_ylabel("probability | success")
        ax.set_title(f"{label} column   $\\beta$ = {np.array2string(beta, precision=2)}", fontsize=10.5)
        ax.legend(fontsize=8.5)
        ax.grid(axis="y", alpha=0.18)
    fig.suptitle(f"shot distribution conditioned on success, {shots} shots per column", fontsize=11.5)
    fig.tight_layout()
    _save(fig, "beta-histograms")


if __name__ == "__main__":
    enc = RectangularBlockEncoding(Z)
    poly = SingularValuePolynomial(enc.singular_values)
    solver = QuantumPseudoInverse(enc, poly, QSPPhases(poly).solve())
    Y = generate_targets()

    fig_block_encoding(enc)
    fig_polynomial(enc, poly)
    fig_circuit(solver, Y)
    fig_success_failure(solver, Y)
    fig_histograms(solver, Y)
