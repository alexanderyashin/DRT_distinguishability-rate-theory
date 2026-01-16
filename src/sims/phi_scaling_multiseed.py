#!/usr/bin/env python3
"""
phi_scaling_multiseed.py — multi-seed robustness for diffusion Φ^{-1/3} scaling

This MUST match the baseline diffusion model used in:
  src.sims.diffusion_localization_mc (run_simulation)

Writes:
  results/phi_multiseed_slopes.json

Platinum:
  - multi-seed slopes (>=20)
  - mean/std
  - bootstrap 95% CI for mean slope
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from src.stats_utils import set_seed, linear_regression_loglog
from src.config import RNG_DEFAULT
from src.sims.diffusion_localization_mc import Params, run_simulation

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def bootstrap_ci_mean(
    values: np.ndarray,
    n_boot: int = 5000,
    alpha: float = 0.05,
    seed: int = 777,
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    n = int(values.size)
    if n == 0:
        return (float("nan"), float("nan"))

    means = np.empty(n_boot, dtype=float)
    for b in range(n_boot):
        samp = rng.choice(values, size=n, replace=True)
        means[b] = float(np.mean(samp))

    lo = float(np.quantile(means, alpha / 2))
    hi = float(np.quantile(means, 1 - alpha / 2))
    return lo, hi


@dataclass
class Config:
    n_seeds: int = 20
    n_mc: int = 2000  # match baseline default spirit (baseline uses 2000)
    D: float = 1.0
    sigma_m: float = 1.0
    phi_values: tuple[float, ...] = tuple(np.logspace(1, 4, 8).tolist())  # identical to baseline
    n_boot: int = 5000
    bootstrap_seed: int = 777


def main() -> None:
    cfg = Config()
    phi_values = np.array(cfg.phi_values, dtype=float)

    slopes = []
    base_seed = int(getattr(RNG_DEFAULT, "seed", 12345))

    for k in range(cfg.n_seeds):
        seed = base_seed + 10_000 + k
        set_seed(seed)
        rng = np.random.default_rng(seed)

        p = Params(
            D=float(cfg.D),
            sigma_m=float(cfg.sigma_m),
            n_mc=int(cfg.n_mc),
        )

        delta_t, _diags = run_simulation(phi_values, p, rng)
        slope, intercept = linear_regression_loglog(phi_values, delta_t)
        slopes.append(float(slope))

    slopes = np.array(slopes, dtype=float)

    slope_mean = float(slopes.mean())
    slope_std = float(slopes.std(ddof=1)) if slopes.size > 1 else 0.0
    expected = -1.0 / 3.0

    ci_lo, ci_hi = bootstrap_ci_mean(
        slopes,
        n_boot=int(cfg.n_boot),
        alpha=0.05,
        seed=int(cfg.bootstrap_seed),
    )

    out = {
        "model": "diffusion_localization_mc.run_simulation + loglog regression",
        "n_seeds": int(cfg.n_seeds),
        "n_mc": int(cfg.n_mc),
        "D": float(cfg.D),
        "sigma_m": float(cfg.sigma_m),
        "phi_values": list(map(float, phi_values)),
        "expected": float(expected),
        "slopes": list(map(float, slopes)),
        "slope_mean": slope_mean,
        "slope_std": slope_std,
        "bootstrap": {
            "n_boot": int(cfg.n_boot),
            "alpha": 0.05,
            "ci95_mean": [float(ci_lo), float(ci_hi)],
            "seed": int(cfg.bootstrap_seed),
        },
    }

    out_path = RESULTS_DIR / "phi_multiseed_slopes.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[OK] Multi-seed slopes + CI written: {out_path}")


if __name__ == "__main__":
    main()
