"""
poisson_fisher.py — Fisher information for Poisson point processes

This module implements the exact Fisher information for a Poisson
point process with intensity λ(t; θ):

    I(θ) = ∫_0^T (∂_θ λ(t;θ))^2 / λ(t;θ) dt

This is a core analytic building block for:
- photon-limited regimes
- continuous monitoring
- self-consistent fixed-point scalings
"""

from __future__ import annotations

import numpy as np
from typing import Callable


def poisson_fisher(
    t: np.ndarray,
    intensity: Callable[[np.ndarray, float], np.ndarray],
    d_intensity: Callable[[np.ndarray, float], np.ndarray],
    theta: float,
) -> float:
    """
    Compute Fisher information for a Poisson point process.

    Parameters
    ----------
    t : np.ndarray
        Time grid over [0, T].
    intensity : callable
        λ(t, θ) intensity function.
    d_intensity : callable
        ∂_θ λ(t, θ).
    theta : float
        Parameter value.

    Returns
    -------
    float
        Fisher information I(θ).
    """
    lam = intensity(t, theta)
    dlam = d_intensity(t, theta)

    # Safety: avoid division by zero
    lam = np.clip(lam, 1e-15, None)

    integrand = (dlam ** 2) / lam
    return float(np.trapz(integrand, t))


def fisher_rate(
    intensity: Callable[[np.ndarray, float], np.ndarray],
    d_intensity: Callable[[np.ndarray, float], np.ndarray],
    theta: float,
    T: float,
    n_grid: int = 2000,
) -> float:
    """
    Compute average Fisher information rate I/T.

    Useful for comparing inference-limited vs dynamics-limited regimes.
    """
    t = np.linspace(0.0, T, n_grid)
    I = poisson_fisher(t, intensity, d_intensity, theta)
    return I / T
