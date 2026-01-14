"""
stats_utils.py — statistical helpers used across simulations

Focus:
- Fisher information estimators
- simple regression for scaling laws
- deterministic RNG handling
"""

from __future__ import annotations

import numpy as np
from typing import Tuple


def set_seed(seed: int) -> None:
    """Set numpy RNG seed."""
    np.random.seed(seed)


def fisher_from_loglik_grad(grad_loglik: np.ndarray) -> float:
    """
    Estimate Fisher information from gradients of log-likelihood.

    Parameters
    ----------
    grad_loglik : np.ndarray
        Array of shape (N,) containing d/dθ log p(x|θ).

    Returns
    -------
    float
        Estimated Fisher information.
    """
    grad_loglik = np.asarray(grad_loglik)
    return float(np.mean(grad_loglik ** 2))


def linear_regression_loglog(x: np.ndarray, y: np.ndarray) -> Tuple[float, float]:
    """
    Perform linear regression in log-log space:
        log y = a * log x + b

    Returns
    -------
    slope : float
        Power-law exponent.
    intercept : float
        Intercept in log space.
    """
    x = np.asarray(x)
    y = np.asarray(y)
    lx = np.log(x)
    ly = np.log(y)

    A = np.vstack([lx, np.ones_like(lx)]).T
    slope, intercept = np.linalg.lstsq(A, ly, rcond=None)[0]
    return float(slope), float(intercept)
