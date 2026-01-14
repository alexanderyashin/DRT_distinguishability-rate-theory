"""
ramsey_meeting_point_mc.py — meeting-point analysis for Ramsey interferometry

Goal:
- Compare inference-limited scale δφ_inf with dynamical scale δφ_dyn
- Identify regimes where:
    δφ_inf << δφ_dyn  (inference-limited)
    δφ_inf ~  δφ_dyn (meeting point)
    δφ_inf >> δφ_dyn (dynamics-limited)

This operationalizes the multiparameter meeting-point criterion
in a concrete quantum-optics setting.
"""

from __future__ import annotations

import numpy as np

from src.config import RNG_DEFAULT
from src.io_utils import save_json
from src.stats_utils import set_seed
from src.fisher.ramsey_fisher import ramsey_fisher_max


def run_simulation(
    times,
    visibility: float,
    D_star: float = 1.0,
):
    """
    Compute inference and dynamical scales for each interrogation time.
    """
    delta_inf = []
    delta_dyn = []

    for t in times:
        # Fisher accumulated over time t
        I_t = t * ramsey_fisher_max(visibility)
        delta_inf.append(np.sqrt(2.0 * D_star / I_t))

        # dynamical phase scale ~ 1/t
        delta_dyn.append(1.0 / t)

    return np.array(delta_inf), np.array(delta_dyn)


def main():
    set_seed(RNG_DEFAULT.seed)

    times = np.logspace(-2, 1, 40)
    visibility = 0.8

    delta_inf, delta_dyn = run_simulation(times, visibility)

    save_json(
        "ramsey_meeting_point.json",
        {
            "times": times.tolist(),
            "visibility": visibility,
            "delta_inf": delta_inf.tolist(),
            "delta_dyn": delta_dyn.tolist(),
        },
    )

    print("Ramsey meeting-point data generated.")


if __name__ == "__main__":
    main()
