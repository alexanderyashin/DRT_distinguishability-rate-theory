from __future__ import annotations

"""
ctrw_mc.py — Monte Carlo for anomalous diffusion (CTRW)

Goal:
δt_min ∼ Φ^{-1/(2+α)}
"""

import math
import numpy as np

from src.config import RNG_DEFAULT
from src.io_utils import save_json
from src.stats_utils import set_seed, linear_regression_loglog


def poisson_safe(lam: float) -> int:
    if lam <= 1e8:
        return max(1, int(np.random.poisson(lam)))
    return max(1, int(np.random.normal(lam, math.sqrt(lam))))


def run_simulation(phi_values, alpha: float, n_mc: int = 2000):
    delta_t_est = []
    p = 1.0 / (2.0 + alpha)

    for Phi in phi_values:
        delta_t0 = Phi ** (-p)
        samples = []
        for _ in range(n_mc):
            N = poisson_safe(Phi * delta_t0)
            ratio = N / (Phi * delta_t0 + 1e-30)
            samples.append(delta_t0 * ratio ** (-p))
        delta_t_est.append(np.median(samples))

    return np.array(delta_t_est)


def main():
    set_seed(RNG_DEFAULT.seed)

    alpha = 0.6
    phi_values = np.logspace(1, 4, 8)
    delta_t = run_simulation(phi_values, alpha)

    slope, intercept = linear_regression_loglog(phi_values, delta_t)

    save_json(
        "ctrw_phi_scaling.json",
        {
            "alpha": alpha,
            "phi": phi_values.tolist(),
            "delta_t": delta_t.tolist(),
            "fit_slope": slope,
            "expected_slope": -1.0 / (2.0 + alpha),
        },
    )

    print("CTRW Φ-scaling slope:", slope)


if __name__ == "__main__":
    main()
