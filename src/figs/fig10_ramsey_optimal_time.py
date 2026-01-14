"""
fig10_ramsey_optimal_time.py — optimal interrogation time under dephasing

Depends on:
- results/ramsey_optimal_time.json
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def main():
    # load_json() already prepends results/
    data = load_json("ramsey_optimal_time.json")
    rows = data["rows"]

    gammas = np.array([r["gamma"] for r in rows], dtype=float)
    t_star = np.array([r["t_star"] for r in rows], dtype=float)
    delta_star = np.array([r["delta_star"] for r in rows], dtype=float)

    # Remove gamma=0 from loglog (undefined); plot it separately if present
    mask = gammas > 0
    gammas_pos = gammas[mask]
    t_star_pos = t_star[mask]
    delta_pos = delta_star[mask]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.loglog(gammas_pos, t_star_pos, lw=2, label=r"Optimal $t^*(\Gamma)$")
    ax.loglog(gammas_pos, delta_pos, lw=2, label=r"Optimal $\delta\phi_{\min}(\Gamma)$")

    ax.set_xlabel(r"Dephasing rate $\Gamma$")
    ax.set_ylabel("Optimal scales")
    ax.set_title("Meeting-point optimization under decoherence")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig10_ramsey_optimal_time.pdf"))
    plt.close(fig)

    print("[OK] fig10 saved:", figures_path("fig10_ramsey_optimal_time.pdf"))


if __name__ == "__main__":
    main()
