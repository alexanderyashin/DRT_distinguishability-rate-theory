"""
config.py — central configuration (single source of truth)

Keep parameters here when they are shared between sims/figs.
Per-script parameters may still live at top of each script, but
defaults should reference this module.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Paths:
    results_dir: str = "results"
    figures_dir: str = "figures"


PATHS = Paths()


@dataclass(frozen=True)
class RNG:
    # Global default seed. Each script may derive sub-seeds deterministically.
    seed: int = 123456


RNG_DEFAULT = RNG()


@dataclass(frozen=True)
class SimulationDefaults:
    # Keep defaults modest; executor chat can increase for final runs.
    n_mc: int = 2000
    grid_size: int = 25


SIM_DEFAULTS = SimulationDefaults()
