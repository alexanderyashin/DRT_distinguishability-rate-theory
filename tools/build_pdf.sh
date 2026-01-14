#!/usr/bin/env bash
# ============================================
# build_pdf.sh — DRT Platinum
# Builds LaTeX paper using latexmk
# ============================================

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PAPER_DIR="$ROOT_DIR/paper"

cd "$PAPER_DIR"

echo "== Building LaTeX paper =="

command -v latexmk >/dev/null 2>&1 || {
  echo "ERROR: latexmk not found. Install TeX Live."
  exit 1
}

latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

echo "================================="
echo "LaTeX build successful"
echo "Output: paper/main.pdf"
echo "================================="
