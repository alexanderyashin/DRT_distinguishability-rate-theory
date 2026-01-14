"""
fig3_phi_scaling.py — Φ-scaling of minimal time resolution

Loads:
- diffusion_phi_scaling.json
- ctrw_phi_scaling.json

Shows:
- δt_min vs photon flux Φ (log-log)
- comparison with predicted slopes
"""

import json
import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def main():
    data_diff = load_json("diffusion_phi_scaling.json")
    data_ctrw = load_json("ctrw_phi_scaling.json")

    phi_d = np.array(data_diff["phi"])
    dt_d = np.array(data_diff["delta_t"])

    phi_c = np.array(data_ctrw["phi"])
    dt_c = np.array(data_ctrw["delta_t"])
    alpha = data_ctrw["alpha"]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.loglog(phi_d, dt_d, "o-", label="Diffusion (MC)")
    ax.loglog(
        phi_d,
        phi_d ** (-1 / 3),
        "--",
        label=r"$\Phi^{-1/3}$ (theory)",
    )

    ax.loglog(phi_c, dt_c, "s-", label=f"CTRW α={alpha}")
    ax.loglog(
        phi_c,
        phi_c ** (-1 / (2 + alpha)),
        "--",
        label=r"$\Phi^{-1/(2+\alpha)}$ (theory)",
    )

    ax.set_xlabel(r"Photon flux $\Phi$")
    ax.set_ylabel(r"Minimal resolvable $\delta t$")
    ax.set_title("Photon-limited time resolution scaling")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig3_phi_scaling.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
