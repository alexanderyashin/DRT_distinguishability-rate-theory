"""
ou_fisher.py — Fisher information for Ornstein–Uhlenbeck (OU) process

We consider the stationary OU process:
    dX_t = -γ X_t dt + sqrt(2D) dW_t

The parameter of interest is γ (relaxation rate).
For continuous monitoring over time T, the Fisher information scales as:

    I_T(γ) ≈ T / (2γ)

This module provides:
- the closed-form Fisher rate,
- helper functions for bounds used in figures.
"""

from __future__ import annotations

import numpy as np


def ou_fisher_rate(gamma: float) -> float:
    """
    Fisher information rate I_T / T for the OU process (stationary).

    Parameters
    ----------
    gamma : float
        Relaxation rate γ > 0.

    Returns
    -------
    float
        Fisher rate ≈ 1 / (2γ).
    """
    if gamma <= 0:
        raise ValueError("gamma must be positive")
    return 1.0 / (2.0 * gamma)


def ou_fisher(T: float, gamma: float) -> float:
    """
    Fisher information I_T for total observation time T.

    Parameters
    ----------
    T : float
        Observation time.
    gamma : float
        Relaxation rate γ > 0.

    Returns
    -------
    float
        Fisher information I_T ≈ T / (2γ).
    """
    return T * ou_fisher_rate(gamma)


def gamma_min_bound(T: float, gamma: float, D_star: float = 1.0) -> float:
    """
    Minimal resolvable δγ from DRT master inequality.

    δγ_min ≳ sqrt(4 D* γ / T)

    Parameters
    ----------
    T : float
        Observation time.
    gamma : float
        Relaxation rate.
    D_star : float
        Distinguishability threshold (order unity).

    Returns
    -------
    float
        Lower bound on δγ.
    """
    return np.sqrt(4.0 * D_star * gamma / T)
