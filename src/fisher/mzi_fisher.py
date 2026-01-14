"""
mzi_fisher.py — Fisher information for Mach–Zehnder interferometry

Model:
- Single-photon Mach–Zehnder interferometer
- Phase shift φ in one arm
- Losses encoded via effective visibility V ∈ (0, 1]

Probabilities:
    p_±(φ) = (1 ± V cos φ) / 2

This is formally identical to Ramsey interferometry, but interpreted
as a spatial / optical interferometer with losses.
"""

from __future__ import annotations

import numpy as np
from typing import Tuple


def mzi_probabilities(phi: float, visibility: float = 1.0) -> Tuple[float, float]:
    """
    Mach–Zehnder output probabilities.

    Parameters
    ----------
    phi : float
        Phase difference.
    visibility : float
        Effective visibility V ∈ (0, 1].

    Returns
    -------
    (p_plus, p_minus)
    """
    p_plus = 0.5 * (1.0 + visibility * np.cos(phi))
    p_minus = 1.0 - p_plus
    return p_plus, p_minus


def mzi_fisher(phi: float, visibility: float = 1.0) -> float:
    """
    Classical Fisher information for Mach–Zehnder interferometry.

    Parameters
    ----------
    phi : float
        Phase.
    visibility : float
        Visibility V ∈ (0, 1].

    Returns
    -------
    float
        Fisher information I(φ).
    """
    p_plus, p_minus = mzi_probabilities(phi, visibility)

    eps = 1e-15
    p_plus = np.clip(p_plus, eps, 1.0 - eps)
    p_minus = np.clip(p_minus, eps, 1.0 - eps)

    dp_dphi = -0.5 * visibility * np.sin(phi)

    fisher = (dp_dphi ** 2) * (1.0 / p_plus + 1.0 / p_minus)
    return float(fisher)


def mzi_fisher_max(visibility: float = 1.0) -> float:
    """
    Maximum Fisher information over φ.

    Achieved at φ = π/2.

    Returns
    -------
    float
        I_max = V^2.
    """
    return float(visibility ** 2)
