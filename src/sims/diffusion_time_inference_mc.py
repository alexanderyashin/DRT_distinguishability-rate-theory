#!/usr/bin/env python3
"""
Clean diffusion Φ-scaling sanity simulation (NO hard-coded exponent, NO fixed-point).

Task:
- Two-window experiment: estimate distinguishability between Δt=0 and Δt>0
  using empirical mean log-likelihood ratio (i.e., KL).
- For each photon flux Φ, find Δt_min such that mean LLR >= D*.

Forward model:
- Brownian displacement between windows: ΔX ~ N(0, 2 D Δt)
- Photon counts per window: N1,N2 ~ Poisson(Φ T_obs)
- Per-photon localization noise σ_ph => mean localization noise σ_ph / sqrt(N)

Outputs:
- JSON with raw pairs (Φ, Δt_min)
- log-log slope + bootstrap CI across seeds
"""

from __future__ import annotations
import argparse
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np


@dataclass
class Params:
    D: float = 1e-12              # diffusion coefficient [m^2/s]
    sigma_ph: float = 2e-7        # per-photon localization [m]
    T_obs: float = 5e-3           # window duration [s]
    D_star: float = 1.0           # distinguishability threshold
    min_photons: int = 1          # clamp N to >=1 to avoid division by zero
    n_trials: int = 20000         # MC trials per (Φ, Δt)
    seed: int = 0


def llr_gauss_zero_mean(d: np.ndarray, v1: np.ndarray, v0: np.ndarray) -> np.ndarray:
    """
    Log-likelihood ratio log p(d|v1)/p(d|v0) for N(0,v) distributions.
    """
    # L = -0.5[ log(v1) + d^2/v1 ] - ( -0.5[ log(v0) + d^2/v0 ] )
    return -0.5 * (np.log(v1) + (d * d) / v1) + 0.5 * (np.log(v0) + (d * d) / v0)


def simulate_mean_llr(phi: float, dt: float, p: Params, rng: np.random.Generator) -> float:
    """
    One-point estimator of KL via mean LLR under H1 model.

    Procedure:
    - Sample N1,N2 ~ Poisson(phi*T_obs)
    - Clamp to >=min_photons
    - Sample diffusion displacement ΔX ~ N(0, 2D dt)
    - Sample measurement noise eps1, eps2 with Var = sigma_ph^2/N
    - Form d = ΔX + eps2 - eps1
    - Compute LLR between v1(=2Ddt+v0) and v0 for each trial
    - Return mean LLR (empirical KL)
    """
    lam = phi * p.T_obs
    N1 = rng.poisson(lam, size=p.n_trials)
    N2 = rng.poisson(lam, size=p.n_trials)
    N1 = np.maximum(N1, p.min_photons)
    N2 = np.maximum(N2, p.min_photons)

    v_loc = (p.sigma_ph ** 2) * (1.0 / N1 + 1.0 / N2)  # v0
    v_diff = 2.0 * p.D * dt
    v0 = v_loc
    v1 = v_loc + v_diff

    dX = rng.normal(loc=0.0, scale=np.sqrt(v_diff), size=p.n_trials) if dt > 0 else np.zeros(p.n_trials)
    eps1 = rng.normal(loc=0.0, scale=p.sigma_ph / np.sqrt(N1), size=p.n_trials)
    eps2 = rng.normal(loc=0.0, scale=p.sigma_ph / np.sqrt(N2), size=p.n_trials)
    d = dX + (eps2 - eps1)

    llr = llr_gauss_zero_mean(d=d, v1=v1, v0=v0)
    return float(np.mean(llr))


def find_dt_min(phi: float, p: Params, rng: np.random.Generator) -> Tuple[float, Dict[str, float]]:
    """
    Find minimal dt where mean_llr(dt;phi) >= D_star using bracket + bisection.

    No scaling assumed. Pure numeric search.
    """
    # Bracket search
    dt_lo = 0.0
    D_lo = simulate_mean_llr(phi, dt_lo, p, rng)
    if D_lo >= p.D_star:
        return dt_lo, {"D_at_dt": D_lo}

    dt_hi = 1e-6  # start with 1 microsecond
    D_hi = simulate_mean_llr(phi, dt_hi, p, rng)
    it = 0
    while D_hi < p.D_star and dt_hi < 10.0:
        dt_hi *= 2.0
        D_hi = simulate_mean_llr(phi, dt_hi, p, rng)
        it += 1
        if it > 60:
            break

    if D_hi < p.D_star:
        # Failed to reach threshold in reasonable dt range
        return float("nan"), {"D_at_dt": D_hi, "dt_hi": dt_hi}

    # Bisection
    for _ in range(30):
        dt_mid = 0.5 * (dt_lo + dt_hi)
        D_mid = simulate_mean_llr(phi, dt_mid, p, rng)
        if D_mid >= p.D_star:
            dt_hi = dt_mid
            D_hi = D_mid
        else:
            dt_lo = dt_mid
            D_lo = D_mid

    return dt_hi, {"D_at_dt": D_hi, "bracket_dt_lo": dt_lo, "bracket_dt_hi": dt_hi}


def loglog_slope(phi: np.ndarray, dt: np.ndarray) -> Tuple[float, float]:
    """
    Simple OLS slope of log(dt) vs log(phi).
    Returns (slope, intercept).
    """
    x = np.log(phi)
    y = np.log(dt)
    A = np.vstack([x, np.ones_like(x)]).T
    slope, intercept = np.linalg.lstsq(A, y, rcond=None)[0]
    return float(slope), float(intercept)


def bootstrap_ci(values: np.ndarray, rng: np.random.Generator, n_boot: int = 2000) -> Tuple[float, float]:
    """
    Percentile bootstrap CI (2.5%, 97.5%).
    """
    boots = []
    n = len(values)
    for _ in range(n_boot):
        sample = rng.choice(values, size=n, replace=True)
        boots.append(np.mean(sample))
    boots = np.sort(np.array(boots))
    lo = float(np.quantile(boots, 0.025))
    hi = float(np.quantile(boots, 0.975))
    return lo, hi


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=str, default="results/diffusion_time_inference_phi_scaling.json")
    ap.add_argument("--seeds", type=int, default=10)
    ap.add_argument("--seed0", type=int, default=123)
    ap.add_argument("--n_trials", type=int, default=20000)
    ap.add_argument("--D", type=float, default=1e-12)
    ap.add_argument("--sigma_ph", type=float, default=2e-7)
    ap.add_argument("--T_obs", type=float, default=5e-3)
    ap.add_argument("--D_star", type=float, default=1.0)
    ap.add_argument("--phi_min", type=float, default=5e4)
    ap.add_argument("--phi_max", type=float, default=5e7)
    ap.add_argument("--n_phi", type=int, default=12)
    args = ap.parse_args()

    p = Params(D=args.D, sigma_ph=args.sigma_ph, T_obs=args.T_obs, D_star=args.D_star,
               n_trials=args.n_trials, seed=args.seed0)

    phi_values = np.logspace(np.log10(args.phi_min), np.log10(args.phi_max), args.n_phi)

    # Multi-seed robustness: for each seed, compute dt_min(phi) curve and fit slope
    seed_slopes: List[float] = []
    seed_curves: List[Dict[str, object]] = []

    ss = np.random.SeedSequence(args.seed0)
    child_seeds = ss.spawn(args.seeds)

    for s_idx in range(args.seeds):
        rng = np.random.default_rng(child_seeds[s_idx])
        dt_mins = []
        diagnostics = []
        for phi in phi_values:
            dt_min, diag = find_dt_min(float(phi), p, rng)
            dt_mins.append(dt_min)
            diagnostics.append(diag)

        dt_mins_arr = np.array(dt_mins, float)
        ok = np.isfinite(dt_mins_arr) & (dt_mins_arr > 0)
        if np.sum(ok) < 5:
            seed_slopes.append(float("nan"))
        else:
            slope, intercept = loglog_slope(phi_values[ok], dt_mins_arr[ok])
            seed_slopes.append(slope)

        seed_curves.append({
            "seed_index": s_idx,
            "dt_min": dt_mins,
            "diagnostics": diagnostics,
            "slope": seed_slopes[-1],
        })

    slopes = np.array(seed_slopes, float)
    ok_s = np.isfinite(slopes)
    slope_mean = float(np.mean(slopes[ok_s])) if np.any(ok_s) else float("nan")
    slope_std = float(np.std(slopes[ok_s], ddof=1)) if np.sum(ok_s) > 1 else float("nan")
    rng_ci = np.random.default_rng(args.seed0 + 999)
    ci_lo, ci_hi = bootstrap_ci(slopes[ok_s], rng_ci) if np.sum(ok_s) >= 5 else (float("nan"), float("nan"))

    payload = {
        "meta": {
            "model": "two-window diffusion time inference via empirical mean LLR (KL)",
            "params": asdict(p),
            "phi_values": phi_values.tolist(),
            "seeds": args.seeds,
            "seed0": args.seed0,
        },
        "seed_curves": seed_curves,
        "summary": {
            "slope_mean": slope_mean,
            "slope_std": slope_std,
            "slope_ci95_mean_bootstrap": [ci_lo, ci_hi],
            "n_ok_seeds": int(np.sum(ok_s)),
        },
    }

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2))
    print("[OK] Wrote", out_path)
    print("Slope mean:", slope_mean, "std:", slope_std, "CI95(mean):", (ci_lo, ci_hi))


if __name__ == "__main__":
    main()
