"""
fig4_ou_gamma_bound.py — Fisher bound for OU relaxation rate γ

Uses analytic result:
    I_T(γ) ≈ T / (2γ)
    δγ_min ≳ sqrt(4 D* γ / T)

Shows:
- δγ_min vs observation time T
- confirms √(γ/T) scaling
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path
from src.fisher.ou_fisher import gamma_min_bound


def main():
    gamma = 0.5
    D_star = 1.0

    T = np.logspace(0, 3, 200)
    delta_gamma = gamma_min_bound(T, gamma, D_star=D_star)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.loglog(T, delta_gamma, lw=2, label=r"$\delta\gamma_{\min}$")
    ax.loglog(T, np.sqrt(gamma / T), "--", label=r"$\propto \sqrt{\gamma/T}$")

    ax.set_xlabel(r"Observation time $T$")
    ax.set_ylabel(r"Minimal resolvable $\delta\gamma$")
    ax.set_title("OU process: inference bound on relaxation rate")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig4_ou_gamma_bound.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
