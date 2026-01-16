from __future__ import annotations

"""
diffusion_localization_mc.py — Class 0A fixed-point construction (Φ^{-1/3}) consistency check

IMPORTANT (scope / interpretation):
- This simulation is NOT an inference validation.
- It numerically implements a self-consistent fixed-point CONSTRUCTION for δt_min
  under a specified observation model, and checks numerical stability of:
    (i) the fixed-point iteration under Poisson photon statistics, and
    (ii) the log-log fitting pipeline across Φ.

Construction (encoded by design):
- Balance condition (heuristic closure, not extremization):
      2 D δt  ≈  σ_m² / √N ,   with   N ~ Poisson(Φ δt)
- This defines δt via a self-consistent loop because N depends on δt.
- The implied fixed-point scaling is δt_min ∝ Φ^{-1/3}.

This file therefore belongs to Class 0A (fixed-point constructions).
"""

import argparse
import math
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

from src.config import RNG_DEFAULT
from src.io_utils import save_json
from src.stats_utils import set_seed, linear_regression_loglog


@dataclass
class Params:
    D: float = 1.0
    sigma_m: float = 1.0
    n_mc: int = 2000
    n_iter: int = 12
    dt0: float = 1e-2
    dt_floor: float = 1e-12


def poisson_safe(lam: float, rng: np.random.Generator) -> int:
    if not np.isfinite(lam) or lam < 0.0:
        raise ValueError(f"Invalid Poisson rate lam={lam}")

    LAM_GAUSS = 1.0e8
    if lam <= LAM_GAUSS:
        return int(rng.poisson(lam))

    x = rng.normal(loc=lam, scale=math.sqrt(lam))
    return max(0, int(x))


def fixed_point_iter_delta_t(phi: float, p: Params, rng: np.random.Generator):
    dt = p.dt0
    for _ in range(p.n_iter):
        N = max(1, poisson_safe(phi * dt, rng))
        dt = max((p.sigma_m ** 2) / (2.0 * p.D * math.sqrt(float(N))), p.dt_floor)
    return dt, {"lam_last": float(phi * dt)}


def run_simulation(phi_values: np.ndarray, p: Params, rng: np.random.Generator):
    delta_t_est = []
    all_diags = []

    for phi in phi_values:
        samples = []
        diags_phi = []
        for _ in range(p.n_mc):
            dt_final, diag = fixed_point_iter_delta_t(float(phi), p, rng)
            samples.append(dt_final)
            diags_phi.append(diag)

        delta_t_est.append(float(np.median(samples)))
        all_diags.append(diags_phi)

    return np.array(delta_t_est, float), all_diags


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=RNG_DEFAULT.seed)
    ap.add_argument("--D", type=float, default=1.0)
    ap.add_argument("--sigma_m", type=float, default=1.0)
    ap.add_argument("--n_mc", type=int, default=2000)
    ap.add_argument("--n_iter", type=int, default=12)
    ap.add_argument("--phi_min", type=float, default=1e1)
    ap.add_argument("--phi_max", type=float, default=1e4)
    ap.add_argument("--n_phi", type=int, default=8)
    # IMPORTANT: filename only; save_json() will place it under results/
    ap.add_argument("--out", type=str, default="diffusion_phi_scaling.json")
    args = ap.parse_args()

    set_seed(args.seed)
    rng = np.random.default_rng(int(args.seed))

    p = Params(D=args.D, sigma_m=args.sigma_m, n_mc=args.n_mc, n_iter=args.n_iter)

    phi_values = np.logspace(np.log10(args.phi_min), np.log10(args.phi_max), args.n_phi)
    delta_t, diags = run_simulation(phi_values, p, rng)
    slope, intercept = linear_regression_loglog(phi_values, delta_t)

    payload = {
        "meta": {
            "class": "0A",
            "model": "fixed-point construction consistency check (NOT inference validation)",
            "construction": "2 D dt ≈ sigma_m^2 / sqrt(N), with N ~ Poisson(Phi * dt)",
            "params": asdict(p),
            "seed": int(args.seed),
            "phi_values": phi_values.tolist(),
            "expected_slope": -1.0 / 3.0,
            "notes": [
                "Exponent is encoded by design via the fixed-point closure.",
                "Monte Carlo reflects Poisson count fluctuations and numerical stability."
            ],
        },
        "data": {
            "phi": phi_values.tolist(),
            "delta_t_median": delta_t.tolist(),
        },
        "fit": {
            "slope": float(slope),
            "intercept": float(intercept),
        },
        "diagnostics": {
            "lam_last_samples_per_phi": [
                [d["lam_last"] for d in diags_phi] for diags_phi in diags
            ]
        },
    }

    # Ensure results/ exists because save_json likely writes there.
    Path("results").mkdir(parents=True, exist_ok=True)

    save_json(args.out, payload)

    print("Class 0A Φ-scaling fit slope:", slope)
    print("[OK] Wrote results/" + args.out)


if __name__ == "__main__":
    main()
