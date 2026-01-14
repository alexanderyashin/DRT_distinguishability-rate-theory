"""
io_utils.py — minimal I/O helpers

Purpose:
- Centralize reading/writing of results.
- Keep formats simple and explicit (json / npz).
- Avoid ad-hoc file handling in simulations and figures.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict

import numpy as np

from .config import PATHS


def ensure_dir(path: str) -> None:
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def results_path(filename: str) -> str:
    """Absolute path for a results file."""
    ensure_dir(PATHS.results_dir)
    return os.path.join(PATHS.results_dir, filename)


def figures_path(filename: str) -> str:
    """Absolute path for a figures file."""
    ensure_dir(PATHS.figures_dir)
    return os.path.join(PATHS.figures_dir, filename)


def save_json(filename: str, data: Dict[str, Any]) -> None:
    """Save a dictionary as JSON in results/."""
    path = results_path(filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def load_json(filename: str) -> Dict[str, Any]:
    """Load a JSON file from results/."""
    path = results_path(filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_npz(filename: str, **arrays: np.ndarray) -> None:
    """Save numpy arrays to NPZ in results/."""
    path = results_path(filename)
    np.savez(path, **arrays)


def load_npz(filename: str) -> Dict[str, np.ndarray]:
    """Load numpy arrays from NPZ in results/."""
    path = results_path(filename)
    with np.load(path) as data:
        return dict(data)
