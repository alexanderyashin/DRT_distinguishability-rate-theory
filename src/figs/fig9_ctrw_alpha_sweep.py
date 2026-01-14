"""
fig9_ctrw_alpha_sweep.py — exponent vs alpha (CTRW), with CI error bars

Depends on:
- results/ctrw_alpha_sweep.json
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def main():
    data = load_json("ctrw_alpha_sweep.json")

    alphas = np.array(data["alphas"], dtype=float)
    expected = np.array(data["expected_slopes"], dtype=float)

    slopes = np.array(data["slopes_mean"], dtype=float)
    ci = np.array(data["slopes_ci95_mean"], dtype=float)
    yerr = np.vstack([slopes - ci[:, 0], ci[:, 1] - slopes])

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.errorbar(alphas, slopes, yerr=yerr, fmt="o-", capsize=3, label="MC mean ± 95% CI")
    ax.plot(alphas, expected, "--", label=r"Theory: $-1/(2+\alpha)$")

    ax.set_xlabel(r"Anomalous exponent $\alpha$")
    ax.set_ylabel("Estimated Φ-exponent")
    ax.set_title("CTRW anomalous diffusion scaling validation")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig9_ctrw_alpha_sweep.pdf"))
    plt.close(fig)

    print("[OK] fig9 saved:", figures_path("fig9_ctrw_alpha_sweep.pdf"))


if __name__ == "__main__":
    main()
