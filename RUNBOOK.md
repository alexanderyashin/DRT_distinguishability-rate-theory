# RUNBOOK — DRT Platinum

> **Purpose**  
> This document explains exactly how to run simulations, generate figures,
> build the paper, and debug common failures.  
> No hidden steps. No assumptions beyond what is written here.

---

## Minimal requirements

### System
- Linux / macOS (WSL2 ok)
- Python ≥ 3.10
- LaTeX with `latexmk` (TeX Live recommended)

### Python packages
Listed in `requirements.txt`:
- numpy
- scipy
- matplotlib
- tqdm

---

## One-command workflow (recommended)

From the repository root:

```bash
make doctor
make all
This performs, in order:

Environment sanity checks

All simulations

All figure generation

LaTeX build → paper/main.pdf

make all is equivalent to running:

make sims

make figs

make pdf

No hidden steps are executed.

Step-by-step workflow (debug mode)

Use this mode if something fails or for partial reruns.

1. Environment check
make doctor


Checks:

Python version

Required Python package imports

latexmk availability

Repository directory structure

Fix any reported issue before proceeding.

2. Run simulations
make sims


What this does:

Executes all scripts in src/sims/

Writes outputs to results/

Does not overwrite existing results unless explicitly allowed

Expected outputs:

results/*.json

results/*.npz

3. Generate figures
make figs


What this does:

Reads data from results/

Generates PDF figures in figures/

No simulations are run here

Expected outputs:

figures/fig*.pdf

4. Build the paper
make pdf


What this does:

Runs latexmk in paper/

Includes figures from figures/

Outputs paper/main.pdf

Cleaning
make clean


Removes:

LaTeX build artifacts

Temporary simulation outputs (optional; see Makefile)

Common problems & fixes
❌ latexmk: command not found

Install TeX Live (example for Debian/Ubuntu):

sudo apt install texlive-full

❌ Python package missing
pip install -r requirements.txt

❌ Figures missing in PDF

Checklist:

Ensure make figs ran successfully

Check that figures/ contains PDF files

Re-run:

make pdf

❌ Simulation takes too long

Mitigations:

Reduce grid size or number of Monte Carlo samples

See parameters at the top of each src/sims/*.py

Any such change must be documented in STATE.md.

Rules for contributors / future chats

NEVER hardcode paths; use repo-relative paths only.

NEVER write simulation outputs directly into figures/.

ALWAYS update STATE.md before stopping work.

If you change simulation parameters, document it explicitly in STATE.md.

Failure to follow these rules breaks handoff safety.

Emergency recovery

If repository state is unclear:

Read STATE.md

Run:

make doctor


Run:

make clean


Re-run steps manually (make sims, make figs, make pdf)

If the problem persists, it is reproducible — document it.

Final note

If something “almost works” but not quite, do not hack around it.
Fix the pipeline or document the limitation.

This repository is designed to survive multiple hands and multiple chats.