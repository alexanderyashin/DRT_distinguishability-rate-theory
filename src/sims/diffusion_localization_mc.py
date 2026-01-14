from __future__ import annotations

"""
diffusion_localization_mc.py — Monte Carlo for Φ^{-1/3} scaling

Model:
- 1D Brownian motion: X_t ~ N(0, 2 D t)
- Localization via Poisson photon detections
- Each photon gives position with Gaussian PSF noise σ_m
- Time resolution inferred from change in width

Goal:
- Empirically confirm δt_min ∝ Φ^{-1/3}
"""

import math
import numpy as np

from src.config import RNG_DEFAULT
from src.io_utils import save_json
from src.stats_utils import set_seed, linear_regression_loglog


def poisson_safe(lam: float) -> int:
    if not np.isfinite(lam) or lam < 0.0:
        raise ValueError(f"Invalid Poisson rate lam={lam}")

    LAM_GAUSS = 1.0e8
    if lam <= LAM_GAUSS:
        return int(np.random.poisson(lam))

    x = np.random.normal(loc=lam, scale=math.sqrt(lam))
    return max(0, int(x))


def run_simulation(
    phi_values,
    D=1.0,
    sigma_m=1.0,
    n_mc=2000,
):
    """
    Stable fixed-point Monte Carlo for diffusion localization.

    Balance condition:
        2 D δt  ≈  σ_m² / √N ,   N ~ Poisson(Φ δt)
    """
    delta_t_est = []

    for Phi in phi_values:
        samples = []
        for _ in range(n_mc):
            delta_t = 1e-2
            for _ in range(10):
                N = max(1, poisson_safe(Phi * delta_t))
                delta_t = max(
                    sigma_m**2 / (2.0 * D * math.sqrt(float(N))),
                    1e-12,
                )
            samples.append(delta_t)
        delta_t_est.append(np.median(samples))

    return np.array(delta_t_est)


def main():
    set_seed(RNG_DEFAULT.seed)

    phi_values = np.logspace(1, 4, 8)
    delta_t = run_simulation(phi_values)

    slope, intercept = linear_regression_loglog(phi_values, delta_t)

    save_json(
        "diffusion_phi_scaling.json",
        {
            "phi": phi_values.tolist(),
            "delta_t": delta_t.tolist(),
            "fit_slope": slope,
            "fit_intercept": intercept,
            "expected_slope": -1.0 / 3.0,
        },
    )

    print("Φ-scaling fit slope:", slope)


if __name__ == "__main__":
    main()
