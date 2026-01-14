#!/usr/bin/env bash
# ============================================
# run_sims.sh — DRT Platinum
# Runs all numerical experiments
# ============================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "== Running simulations =="

mkdir -p results

echo "[1] Diffusion localization (Φ^{-1/3})"
python -m src.sims.diffusion_localization_mc

echo "[2] CTRW / anomalous diffusion scalings"
python -m src.sims.ctrw_mc

echo "[3] Ramsey meeting-point phase diagram"
python -m src.sims.ramsey_meeting_point_mc

echo "[4] Mach–Zehnder meeting-point phase diagram"
python -m src.sims.mzi_meeting_point_mc

echo "== Simulations completed =="
echo "Results written to results/"
