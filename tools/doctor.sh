#!/usr/bin/env bash
# ============================================
# doctor.sh — DRT Platinum
# Environment sanity checks
# ============================================

set -euo pipefail

echo "== DRT Platinum: environment check =="

# Check python
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found"
  exit 1
fi
echo "[OK] python3 found"

# Check python version
PYVER=$(python3 - <<'EOF'
import sys
print(f"{sys.version_info.major}.{sys.version_info.minor}")
EOF
)
echo "[INFO] python version: $PYVER"

# Check required python packages
echo "[CHECK] python packages"
python3 - <<'EOF'
import importlib
pkgs = ["numpy", "scipy", "matplotlib", "tqdm"]
missing = []
for p in pkgs:
    try:
        importlib.import_module(p)
    except Exception:
        missing.append(p)
if missing:
    print("ERROR: missing python packages:", ", ".join(missing))
    raise SystemExit(1)
print("[OK] all python packages available")
EOF

# Check latexmk
if ! command -v latexmk >/dev/null 2>&1; then
  echo "ERROR: latexmk not found (install TeX Live)"
  exit 1
fi
echo "[OK] latexmk found"

# Check directory structure
echo "[CHECK] directory structure"
dirs=(src paper tools results figures)
for d in "${dirs[@]}"; do
  if [ ! -d "$d" ]; then
    echo "ERROR: missing directory: $d"
    exit 1
  fi
done
echo "[OK] directory structure looks fine"

echo "================================="
echo "Environment looks sane."
echo "================================="
