"""
fig7_noise_suppression_bound.py — Universal noise suppression of Fisher information

Shows:
- Ideal Fisher accumulation
- Noise-suppressed upper bound
- Exponential suppression exp(-2 Γ t)

No simulation data required.
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path


def main():
    T = np.linspace(0, 10, 400)
    gamma_noise = 0.4

    # Ideal Fisher rate (constant, normalized)
    I_ideal = T

    # Noise-suppressed bound
    # NumPy 2.x: np.trapz was removed; use np.trapezoid (same intent).
    I_noise = np.trapezoid(np.exp(-2 * gamma_noise * T[:, None]), T, axis=0)
    # For plotting simplicity, show envelope
    I_noise_env = (1 - np.exp(-2 * gamma_noise * T)) / (2 * gamma_noise)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.plot(T, I_ideal, lw=2, label="Ideal Fisher accumulation")
    ax.plot(T, I_noise_env, lw=2, label="Noise-suppressed upper bound")

    ax.set_xlabel("Observation time $T$")
    ax.set_ylabel("Accumulated Fisher information")
    ax.set_title("Noise suppresses distinguishability rates")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig7_noise_suppression_bound.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
