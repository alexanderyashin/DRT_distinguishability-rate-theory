"""
ramsey_fisher.py — Fisher / QFI for Ramsey interferometry

Model:
- Two-level system
- Phase φ = ω t encoded unitarily
- Optional dephasing with visibility V = exp(-γ t)

Probabilities:
    p_± = (1 ± V cos φ) / 2
"""

from __future__ import annotations

import numpy as np
from typing import Tuple


def ramsey_probabilities(phi: float, visibility: float = 1.0) -> Tuple[float, float]:
    """
    Ramsey outcome probabilities.

    Parameters
    ----------
    phi : float
        Phase.
    visibility : float
        Visibility V ∈ (0, 1].

    Returns
    -------
    (p_plus, p_minus)
    """
    p_plus = 0.5 * (1.0 + visibility * np.cos(phi))
    p_minus = 1.0 - p_plus
    return p_plus, p_minus


def ramsey_fisher(phi: float, visibility: float = 1.0) -> float:
    """
    Classical Fisher information for Ramsey interferometry.

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
    p_plus, p_minus = ramsey_probabilities(phi, visibility)

    # Avoid numerical issues near boundaries
    eps = 1e-15
    p_plus = np.clip(p_plus, eps, 1.0 - eps)
    p_minus = np.clip(p_minus, eps, 1.0 - eps)

    dp_dphi = -0.5 * visibility * np.sin(phi)

    fisher = (dp_dphi ** 2) * (1.0 / p_plus + 1.0 / p_minus)
    return float(fisher)


def ramsey_fisher_max(visibility: float = 1.0) -> float:
    """
    Maximum Fisher information over φ.

    Achieved at φ = π/2.

    Returns
    -------
    float
        I_max = V^2.
    """
    return float(visibility ** 2)
