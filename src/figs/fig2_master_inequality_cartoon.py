"""
fig2_master_inequality_cartoon.py — Visualizing the DRT master inequality

Shows:
- Fisher ellipsoid in parameter space
- distinguishability threshold
- minimal resolvable δθ along direction u

No data dependency.
"""

import matplotlib.pyplot as plt
import numpy as np

from src.io_utils import figures_path


def main():
    fig, ax = plt.subplots(figsize=(5, 5))

    # Fisher ellipsoid (schematic)
    theta = np.linspace(0, 2 * np.pi, 400)
    a, b = 1.0, 0.6
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    ax.plot(x, y, lw=2, label="Fisher ellipsoid (local geometry)")
    ax.fill(x, y, alpha=0.1)

    # Direction u
    u = np.array([0.8, 0.2])
    u = u / np.linalg.norm(u)
    ax.arrow(0, 0, u[0], u[1], head_width=0.05, length_includes_head=True)
    ax.text(u[0] * 1.05, u[1] * 1.05, "u", fontsize=12)

    ax.set_aspect("equal", "box")
    ax.set_xlabel(r"$\theta_1$")
    ax.set_ylabel(r"$\theta_2$")
    ax.set_title("DRT master inequality (schematic)")
    ax.legend(frameon=False, loc="upper right")

    fig.tight_layout()
    fig.savefig(figures_path("fig2_master_inequality_cartoon.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
