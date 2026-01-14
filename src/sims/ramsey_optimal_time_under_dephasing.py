#!/usr/bin/env python3
"""
Ramsey optimal interrogation time t*(Γ) under dephasing.

Writes:
  results/ramsey_optimal_time.json

Model:
  Visibility V(t)=exp(-Γ t)
  Fisher (phase) for Ramsey with dephasing (standard form):
    I(t) ~ r * t^2 * V(t)^2   (up to constant factors / operating point)
  Meeting-point condition (DRT):
    δφ_min(t) = sqrt(2 D* / I(t))
  Choose t* that minimizes δφ_min (equivalently maximizes I(t)).
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)


def fisher_ramsey_dephasing(t: float, gamma: float, r: float = 1.0) -> float:
    """Simple robust Fisher proxy capturing the key trade-off."""
    if t <= 0.0:
        return 0.0
    V = math.exp(-gamma * t)
    return float(r * (t**2) * (V**2))


def delta_phi_min(I_T: float, D_star: float = 1.0) -> float:
    return float(math.sqrt(2.0 * D_star / (I_T + 1e-15)))


def optimize_t_star(gamma: float, t_grid: np.ndarray, r: float = 1.0, D_star: float = 1.0) -> dict:
    I_vals = np.array([fisher_ramsey_dephasing(float(t), gamma, r=r) for t in t_grid], dtype=float)
    idx = int(np.argmax(I_vals))
    t_star = float(t_grid[idx])
    I_star = float(I_vals[idx])
    d_star = delta_phi_min(I_star, D_star=D_star)

    return {
        "gamma": float(gamma),
        "t_star": t_star,
        "I_star": I_star,
        "delta_star": d_star,
    }


def main() -> None:
    # Parameter sweep (Γ)
    gammas = np.array([0.0, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0], dtype=float)

    # Time grid (wide enough)
    t_grid = np.linspace(1e-4, 10.0, 2000)

    r = 1.0
    D_star = 1.0

    rows = [optimize_t_star(float(g), t_grid, r=r, D_star=D_star) for g in gammas]

    out = {
        "model": "I(t)=r*t^2*exp(-2*gamma*t), meeting-point delta=sqrt(2D*/I)",
        "r": float(r),
        "D_star": float(D_star),
        "rows": rows,
    }

    out_path = RESULTS_DIR / "ramsey_optimal_time.json"
    out_path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"[OK] Ramsey optimal time written: {out_path}")


if __name__ == "__main__":
    main()
