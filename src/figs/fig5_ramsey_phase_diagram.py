"""
fig5_ramsey_phase_diagram.py — Ramsey meeting-point plot
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def main():
    data = load_json("ramsey_meeting_point.json")

    t = np.array(data["times"])
    delta_inf = np.array(data["delta_inf"])
    delta_dyn = np.array(data["delta_dyn"])
    visibility = data["visibility"]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.loglog(t, delta_inf, lw=2, label=r"Inference-limited $\delta\phi_{\inf}$")
    ax.loglog(
        t,
        delta_dyn,
        lw=2,
        label=r"Dynamical scale $\delta\phi_{\mathrm{dyn}}$",
    )

    idx = np.argmin(np.abs(np.log(delta_inf) - np.log(delta_dyn)))
    ax.scatter([t[idx]], [delta_inf[idx]], s=40, label="Meeting point")

    ax.set_xlabel(r"Interrogation time $t$")
    ax.set_ylabel(r"Phase scale")
    ax.set_title(f"Ramsey meeting-point (visibility={visibility})")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig5_ramsey_phase_diagram.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
