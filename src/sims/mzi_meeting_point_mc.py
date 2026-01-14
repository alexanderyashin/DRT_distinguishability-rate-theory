"""
mzi_meeting_point_mc.py — meeting-point analysis for Mach–Zehnder interferometry

This is the spatial/optical analogue of the Ramsey meeting-point analysis.

Goal:
- Compare inference-limited phase resolution with
  the dynamical / geometric phase scale
- Show equivalence of meeting-point structure for Ramsey and MZI,
  reinforcing the operational (not ontological) nature of the bounds.
"""

from __future__ import annotations

import numpy as np

from src.config import RNG_DEFAULT
from src.io_utils import save_json
from src.stats_utils import set_seed
from src.fisher.mzi_fisher import mzi_fisher_max


def run_simulation(
    times,
    visibility: float,
    D_star: float = 1.0,
):
    """
    Compute inference and dynamical scales for each effective interrogation time.
    """
    delta_inf = []
    delta_dyn = []

    for t in times:
        # Accumulated Fisher
        I_t = t * mzi_fisher_max(visibility)
        delta_inf.append(np.sqrt(2.0 * D_star / I_t))

        # Geometric phase scale
        delta_dyn.append(1.0 / t)

    return np.array(delta_inf), np.array(delta_dyn)


def main():
    set_seed(RNG_DEFAULT.seed)

    times = np.logspace(-2, 1, 40)
    visibility = 0.7

    delta_inf, delta_dyn = run_simulation(times, visibility)

    save_json(
        "mzi_meeting_point.json",
        {
            "times": times.tolist(),
            "visibility": visibility,
            "delta_inf": delta_inf.tolist(),
            "delta_dyn": delta_dyn.tolist(),
        },
    )

    print("MZI meeting-point data generated.")


if __name__ == "__main__":
    main()
