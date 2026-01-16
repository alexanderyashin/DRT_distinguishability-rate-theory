from __future__ import annotations

"""
ctrw_mc.py — Class 0B imposed-exponent generator (CTRW)

IMPORTANT (epistemic status)
----------------------------
This script does NOT derive a Φ-scaling law.
It explicitly IMPOSES a target exponent p = 1/(2+alpha) via

    delta_t0 = Phi**(-p)

and then adds Poisson sampling fluctuations around that imposed scaling.

Therefore it is suitable ONLY for:
- regression/pipeline smoke tests,
- plotting/visualization sanity checks,
- verifying that the fitter recovers an imposed slope.

It must NOT be interpreted as inference evidence that the exponent emerges
from an online decision task or from a self-consistent estimator loop.
"""

import argparse
import math
from dataclasses import dataclass
from pathlib import PurePosixPath

import numpy as np

from src.config import RNG_DEFAULT
from src.io_utils import save_json
from src.stats_utils import linear_regression_loglog


def poisson_safe(rng: np.random.Generator, lam: float) -> int:
    if not np.isfinite(lam) or lam < 0.0:
        raise ValueError(f"Invalid Poisson rate lam={lam}")
    if lam <= 1.0e8:
        return max(1, int(rng.poisson(lam)))
    # Gaussian approximation for huge rates (rare in practice here)
    return max(1, int(rng.normal(lam, math.sqrt(lam))))


def run_simulation(
    phi_values: np.ndarray,
    alpha: float,
    n_mc: int,
    rng: np.random.Generator,
) -> np.ndarray:
    """
    Imposed-exponent generator.

    We impose p = 1/(2+alpha) in the baseline scaling delta_t0(Phi),
    and then perturb it using Poisson noise in N ~ Poisson(Phi * delta_t0).

    This is intentionally NOT a self-consistent loop and NOT an inference task.
    """
    p = 1.0 / (2.0 + float(alpha))
    delta_t_est = []

    for Phi in phi_values:
        delta_t0 = float(Phi) ** (-p)  # <-- imposed exponent (Class 0B)
        samples = []
        for _ in range(int(n_mc)):
            N = poisson_safe(rng, float(Phi) * delta_t0)
            ratio = float(N) / (float(Phi) * delta_t0 + 1e-30)
            samples.append(delta_t0 * ratio ** (-p))
        delta_t_est.append(float(np.median(samples)))

    return np.asarray(delta_t_est, dtype=float)


def normalize_out_for_save_json(out: str) -> str:
    """
    src.io_utils.save_json() prefixes 'results/' internally.
    Therefore callers must pass a path RELATIVE to results/.
    If user passes 'results/xxx.json' (common habit), strip that prefix.
    """
    p = PurePosixPath(out.strip())
    if len(p.parts) >= 1 and p.parts[0] == "results":
        p = PurePosixPath(*p.parts[1:])  # drop leading 'results'
    return str(p)


@dataclass(frozen=True)
class Params:
    alpha: float
    n_mc: int
    seeds: int
    out: str


def parse_args() -> Params:
    ap = argparse.ArgumentParser(description="Class 0B CTRW imposed-exponent generator (NOT evidence).")
    ap.add_argument("--alpha", type=float, default=0.6, help="Anomalous exponent alpha in MSD ~ t^alpha.")
    ap.add_argument("--n_mc", type=int, default=2000, help="MC samples per Phi.")
    ap.add_argument("--seeds", type=int, default=1, help="Number of independent seeds to average slopes.")
    ap.add_argument(
        "--out",
        type=str,
        default="ctrw_phi_scaling.json",
        help="Output JSON path RELATIVE to results/. (If you pass 'results/...', it will be normalized.)",
    )
    a = ap.parse_args()
    return Params(alpha=a.alpha, n_mc=a.n_mc, seeds=a.seeds, out=a.out)


def main() -> None:
    p = parse_args()
    out_rel = normalize_out_for_save_json(p.out)

    phi_values = np.logspace(1, 4, 8)

    slopes = []
    intercepts = []
    all_delta_t = []

    base_seed = int(RNG_DEFAULT.seed)
    ss = np.random.SeedSequence(base_seed)
    child_seeds = ss.spawn(int(p.seeds))

    for i in range(int(p.seeds)):
        rng = np.random.default_rng(child_seeds[i])

        delta_t = run_simulation(phi_values, p.alpha, p.n_mc, rng)
        slope, intercept = linear_regression_loglog(phi_values, delta_t)

        slopes.append(float(slope))
        intercepts.append(float(intercept))
        all_delta_t.append(delta_t.tolist())

    slope_mean = float(np.mean(slopes))
    slope_std = float(np.std(slopes, ddof=1)) if len(slopes) > 1 else 0.0

    payload = {
        "class": "0B",
        "warning": (
            "Imposed-exponent generator: p=1/(2+alpha) is hard-coded via delta_t0=Phi**(-p). "
            "This output must NOT be interpreted as inference evidence or as an emergent scaling law."
        ),
        "alpha": float(p.alpha),
        "phi": phi_values.tolist(),
        "delta_t_per_seed": all_delta_t,
        "fit_slope_per_seed": slopes,
        "fit_intercept_per_seed": intercepts,
        "fit_slope_mean": slope_mean,
        "fit_slope_std": slope_std,
        "expected_slope_imposed": -1.0 / (2.0 + float(p.alpha)),
        "rng_base_seed": base_seed,
        "seeds": int(p.seeds),
        "n_mc": int(p.n_mc),
    }

    save_json(out_rel, payload)

    print(f"Class 0B CTRW Φ-scaling slope (imposed): {slope_mean}")
    print(f"[OK] Wrote results/{out_rel}")


if __name__ == "__main__":
    main()
