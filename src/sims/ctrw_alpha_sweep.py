"""
ctrw_alpha_sweep.py — validate δt_min ~ Φ^{-1/(2+α)} across alpha (baseline-consistent)

Baseline model:
  src.sims.ctrw_mc.run_simulation

Outputs:
- results/ctrw_alpha_sweep.json

Platinum:
- multi-seed per alpha (n_rep >= 20)
- mean/std
- bootstrap 95% CI for mean slope
"""

from __future__ import annotations

import numpy as np

from src.io_utils import save_json
from src.stats_utils import linear_regression_loglog, set_seed
from src.config import RNG_DEFAULT
from src.sims.ctrw_mc import run_simulation


def bootstrap_ci_mean(values: np.ndarray, n_boot: int = 2000, alpha: float = 0.05, seed: int = 777) -> tuple[float, float]:
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


def main():
    base_seed = int(getattr(RNG_DEFAULT, "seed", 12345))

    phi_values = np.logspace(1, 4, 8)
    alphas = np.linspace(0.3, 1.7, 8)

    # Compute budget (safe for Codespaces)
    n_mc = 800
    n_rep = 20

    slopes_mean = []
    slopes_std = []
    slopes_ci95 = []
    slopes_rep = []
    expected = []

    for i, a in enumerate(alphas):
        rep_slopes = []
        for r in range(n_rep):
            set_seed(base_seed + 10_000 * i + r)

            dt = run_simulation(phi_values, alpha=float(a), n_mc=int(n_mc))
            slope, _ = linear_regression_loglog(phi_values, dt)
            rep_slopes.append(float(slope))

        rep_slopes = np.array(rep_slopes, dtype=float)
        mu = float(rep_slopes.mean())
        sd = float(rep_slopes.std(ddof=1)) if rep_slopes.size > 1 else 0.0
        ci_lo, ci_hi = bootstrap_ci_mean(rep_slopes, n_boot=2000, alpha=0.05, seed=777 + i)

        slopes_rep.append(rep_slopes.tolist())
        slopes_mean.append(mu)
        slopes_std.append(sd)
        slopes_ci95.append([float(ci_lo), float(ci_hi)])
        expected.append(float(-1.0 / (2.0 + a)))

    save_json(
        "ctrw_alpha_sweep.json",
        {
            "model": "ctrw_mc.run_simulation + loglog regression",
            "phi": phi_values.tolist(),
            "alphas": alphas.tolist(),
            "n_mc": int(n_mc),
            "n_rep": int(n_rep),
            "slopes_mean": slopes_mean,
            "slopes_std": slopes_std,
            "slopes_ci95_mean": slopes_ci95,
            "slopes_rep": slopes_rep,
            "expected_slopes": expected,
        },
    )

    print("[OK] α-sweep (baseline-consistent) + multi-seed + CI written: results/ctrw_alpha_sweep.json")


if __name__ == "__main__":
    main()
