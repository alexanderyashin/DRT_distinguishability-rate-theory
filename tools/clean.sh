#!/usr/bin/env bash
# ============================================
# clean.sh — DRT Platinum
# Removes build and temporary artifacts
# ============================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "== Cleaning repository =="

# LaTeX artifacts
rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.fdb_latexmk paper/*.fls
rm -f paper/*.log paper/*.out paper/*.toc paper/*.lof paper/*.lot
rm -f paper/*.synctex.gz paper/*.run.xml

# Optional: clear results and figures (commented by default)
# rm -rf results/*
# rm -rf figures/*

echo "Done."
