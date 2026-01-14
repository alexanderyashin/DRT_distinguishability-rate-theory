"""
fig6_mzi_visibility.py — Mach–Zehnder meeting-point plot

Loads:
- mzi_meeting_point.json

Shows:
- inference-limited vs geometric phase scale
- highlights operational equivalence with Ramsey case
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def main():
    data = load_json("mzi_meeting_point.json")

    t = np.array(data["times"])
    delta_inf = np.array(data["delta_inf"])
    delta_dyn = np.array(data["delta_dyn"])
    visibility = data["visibility"]

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.loglog(t, delta_inf, lw=2, label=r"Inference-limited $\delta\phi_{\inf}$")
    # Matplotlib mathtext does not know \geom; use \mathrm{geom}.
    ax.loglog(t, delta_dyn, lw=2, label=r"Geometric scale $\delta\phi_{\mathrm{geom}}$")

    idx = np.argmin(np.abs(np.log(delta_inf) - np.log(delta_dyn)))
    ax.scatter([t[idx]], [delta_inf[idx]], s=40, label="Meeting point")

    ax.set_xlabel(r"Effective interrogation time")
    ax.set_ylabel(r"Phase scale")
    ax.set_title(f"MZI meeting-point (visibility={visibility})")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig6_mzi_visibility.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
