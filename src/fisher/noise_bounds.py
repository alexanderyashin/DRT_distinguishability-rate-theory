"""
noise_bounds.py — universal noise suppression bounds for Fisher information

This module implements generic upper bounds of the form:

    I_T ≤ ∫_0^T dot{I}_ideal(t) * exp(-2 Γ t) dt

which apply to a broad class of Markovian noise channels
(dephasing, amplitude damping, etc.).

These bounds formalize the statement:
noise suppresses distinguishability rates exponentially in time.
"""

from __future__ import annotations

import numpy as np
from typing import Callable


def fisher_upper_bound(
    fisher_rate_ideal: Callable[[np.ndarray], np.ndarray],
    T: float,
    gamma_noise: float,
    n_grid: int = 2000,
) -> float:
    """
    Compute an upper bound on Fisher information under noise.

    Parameters
    ----------
    fisher_rate_ideal : callable
        Function dot{I}_ideal(t), Fisher rate without noise.
    T : float
        Total observation time.
    gamma_noise : float
        Noise rate Γ ≥ 0.
    n_grid : int
        Time discretization.

    Returns
    -------
    float
        Upper bound on I_T.
    """
    if gamma_noise < 0:
        raise ValueError("gamma_noise must be non-negative")

    t = np.linspace(0.0, T, n_grid)
    rate = fisher_rate_ideal(t)

    suppression = np.exp(-2.0 * gamma_noise * t)
    integrand = rate * suppression

    return float(np.trapz(integrand, t))
