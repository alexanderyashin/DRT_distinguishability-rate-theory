#!/usr/bin/env python3
"""
fig8_phi_slope_hist.py — histogram of Φ-scaling slopes across seeds

Depends on:
- results/phi_multiseed_slopes.json
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def main():
    # IMPORTANT: load_json() already prepends results/ internally.
    data = load_json("phi_multiseed_slopes.json")

    slopes = np.array(data["slopes"], dtype=float)
    expected = float(data.get("expected", -1.0 / 3.0))
    mu = float(np.mean(slopes))
    sd = float(np.std(slopes, ddof=1)) if len(slopes) > 1 else 0.0

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(slopes, bins=min(20, max(5, len(slopes) // 2)))
    ax.axvline(expected, lw=2, label=f"expected {expected:.4f}")
    ax.axvline(mu, lw=2, label=f"mean {mu:.4f}")

    ax.set_xlabel("Fitted log-log slope")
    ax.set_ylabel("Count")
    ax.set_title(f"Φ^{-1/3} robustness (n={len(slopes)}), std={sd:.4f}")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig8_phi_slope_hist.pdf"))
    plt.close(fig)

    print("[OK] fig8 saved:", figures_path("fig8_phi_slope_hist.pdf"))


if __name__ == "__main__":
    main()
