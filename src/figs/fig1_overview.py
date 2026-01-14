"""
fig1_overview.py — Conceptual overview of DRT framework

This figure is schematic:
- operational channel
- Fisher information accumulation
- distinguishability threshold D*
- inference-limited vs dynamics-limited regimes

No data dependency.
"""

import matplotlib.pyplot as plt
import numpy as np

from src.io_utils import figures_path


def main():
    fig, ax = plt.subplots(figsize=(6, 4))

    t = np.linspace(0, 1, 200)
    ax.plot(t, t**0.5, label="Accumulated information", lw=2)
    ax.axhline(0.7, ls="--", color="k", label="Distinguishability threshold $D^*$")

    ax.annotate(
        "Inference-limited",
        xy=(0.7, 0.84),
        xytext=(0.4, 0.9),
        arrowprops=dict(arrowstyle="->"),
    )
    ax.annotate(
        "Dynamics-limited",
        xy=(0.2, 0.45),
        xytext=(0.05, 0.2),
        arrowprops=dict(arrowstyle="->"),
    )

    ax.set_xlabel("Observation time / resources")
    ax.set_ylabel("Distinguishability")
    ax.set_title("Distinguishability Rate Theory: overview")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig1_overview.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
