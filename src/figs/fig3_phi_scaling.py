"""
fig3_phi_scaling.py — Φ-scaling of minimal time resolution

Loads:
- diffusion_phi_scaling.json
- ctrw_phi_scaling.json

Shows:
- δt_min vs photon flux Φ (log-log)
- comparison with predicted slopes
"""

import numpy as np
import matplotlib.pyplot as plt

from src.io_utils import figures_path, load_json


def _extract_phi_dt_diffusion(d: dict) -> tuple[np.ndarray, np.ndarray]:
    # Legacy flat schema support
    if "phi" in d and "delta_t" in d:
        phi = np.array(d["phi"], dtype=float)
        dt = np.array(d["delta_t"], dtype=float)
        return phi, dt

    # Current nested schema from diffusion_localization_mc
    data = d.get("data", {})
    if "phi" in data and "delta_t_median" in data:
        phi = np.array(data["phi"], dtype=float)
        dt = np.array(data["delta_t_median"], dtype=float)
        return phi, dt

    # Fallback: sometimes phi may be stored in meta
    meta = d.get("meta", {})
    if "phi_values" in meta and "delta_t_median" in data:
        phi = np.array(meta["phi_values"], dtype=float)
        dt = np.array(data["delta_t_median"], dtype=float)
        return phi, dt

    raise KeyError("Could not extract diffusion phi/delta_t from JSON schema")


def _extract_phi_dt_ctrw(d: dict) -> tuple[np.ndarray, np.ndarray, float]:
    """
    Support:
    (A) Legacy flat schema:
        {"phi":[...], "delta_t":[...], "alpha":...}
    (B) Current ctrw_phi_scaling.json flat schema with per-seed series:
        {"phi":[...], "delta_t_per_seed":[[...], ...], "alpha":...}
    (C) Nested schema variants (kept for robustness):
        {"data":{"phi":[...], "delta_t_median":[...]}, "meta":{"alpha":...}}
    """
    # (A) legacy flat
    if "phi" in d and "delta_t" in d and "alpha" in d:
        phi = np.array(d["phi"], dtype=float)
        dt = np.array(d["delta_t"], dtype=float)
        alpha = float(d["alpha"])
        return phi, dt, alpha

    # (B) current ctrw_phi_scaling.json: dt per seed
    if "phi" in d and "delta_t_per_seed" in d and "alpha" in d:
        phi = np.array(d["phi"], dtype=float)
        dtps = np.array(d["delta_t_per_seed"], dtype=float)  # shape: [n_seed, n_phi]
        if dtps.ndim != 2:
            raise ValueError("delta_t_per_seed has unexpected shape")
        dt = np.median(dtps, axis=0)  # robust if future seeds > 1
        alpha = float(d["alpha"])
        return phi, dt, alpha

    # (C) nested fallback
    data = d.get("data", {})
    meta = d.get("meta", {})

    if "phi" in data:
        phi = np.array(data["phi"], dtype=float)
    elif "phi_values" in meta:
        phi = np.array(meta["phi_values"], dtype=float)
    else:
        raise KeyError("Could not extract ctrw phi from JSON schema")

    if "delta_t_median" in data:
        dt = np.array(data["delta_t_median"], dtype=float)
    elif "delta_t" in data:
        dt = np.array(data["delta_t"], dtype=float)
    else:
        raise KeyError("Could not extract ctrw delta_t from JSON schema")

    if "alpha" in meta:
        alpha = float(meta["alpha"])
    elif "alpha" in d:
        alpha = float(d["alpha"])
    else:
        raise KeyError("Could not extract ctrw alpha from JSON schema")

    return phi, dt, alpha


def main():
    data_diff = load_json("diffusion_phi_scaling.json")
    data_ctrw = load_json("ctrw_phi_scaling.json")

    phi_d, dt_d = _extract_phi_dt_diffusion(data_diff)
    phi_c, dt_c, alpha = _extract_phi_dt_ctrw(data_ctrw)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.loglog(phi_d, dt_d, "o-", label="Diffusion (MC)")
    ax.loglog(phi_d, phi_d ** (-1 / 3), "--", label=r"$\Phi^{-1/3}$ (theory)")

    ax.loglog(phi_c, dt_c, "s-", label=f"CTRW α={alpha}")
    ax.loglog(phi_c, phi_c ** (-1 / (2 + alpha)), "--", label=r"$\Phi^{-1/(2+\alpha)}$ (theory)")

    ax.set_xlabel(r"Photon flux $\Phi$")
    ax.set_ylabel(r"Minimal resolvable $\delta t$")
    ax.set_title("Photon-limited time resolution scaling")
    ax.legend(frameon=False)

    fig.tight_layout()
    fig.savefig(figures_path("fig3_phi_scaling.pdf"))
    plt.close(fig)


if __name__ == "__main__":
    main()
