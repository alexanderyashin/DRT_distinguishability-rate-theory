#!/usr/bin/env bash
# ============================================
# run_all.sh — DRT Platinum
# One-button full pipeline
# ============================================

set -euo pipefail

echo "== DRT Platinum: full pipeline =="

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/4] Environment check"
bash tools/doctor.sh

echo "[2/4] Running simulations"
bash tools/run_sims.sh

echo "[3/4] Generating figures"
make figs

echo "[4/4] Building LaTeX PDF"
bash tools/build_pdf.sh

echo "================================="
echo "DONE."
echo "Outputs:"
echo "  - Figures: figures/*.pdf"
echo "  - Paper:   paper/main.pdf"
echo "================================="
