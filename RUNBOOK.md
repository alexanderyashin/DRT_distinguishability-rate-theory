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

From repository root:

```bash
make doctor
make all
This performs:

Environment sanity checks

All simulations

All figure generation

LaTeX build → paper/main.pdf

Step-by-step workflow (debug mode)
1. Environment check
bash
Code kopieren
make doctor
Checks:

python version

required packages import

latexmk availability

directory structure

Fix any reported issue before proceeding.

2. Run simulations
bash
Code kopieren
make sims
What this does:

Executes all scripts in src/sims/

Writes outputs to results/

Does NOT overwrite existing results unless explicitly allowed

Expected outputs:

results/*.json or results/*.npz

3. Generate figures
bash
Code kopieren
make figs
What this does:

Reads data from results/

Generates PDF figures in figures/

No simulations are run here

Expected outputs:

figures/fig*.pdf

4. Build the paper
bash
Code kopieren
make pdf
What this does:

Runs latexmk in paper/

Includes figures from figures/

Outputs paper/main.pdf

Cleaning
bash
Code kopieren
make clean
Removes:

LaTeX build artifacts

Temporary simulation outputs (optional)

Common problems & fixes
❌ latexmk: command not found
Install TeX Live:

bash
Code kopieren
sudo apt install texlive-full
❌ Python package missing
bash
Code kopieren
pip install -r requirements.txt
❌ Figures missing in PDF
Ensure make figs ran successfully

Check figures/ contains PDFs

Re-run make pdf

❌ Simulation takes too long
Reduce grid size or number of Monte Carlo samples

See parameters at top of each src/sims/*.py

Rules for contributors / future chats
NEVER hardcode paths; use repo-relative paths only.

NEVER write simulation outputs directly into figures/.

ALWAYS update STATE.md before stopping work.

If you change simulation parameters, document it in STATE.md.

Emergency recovery
If repo state is unclear:

Read STATE.md

Run make doctor

Run make clean

Re-run steps manually

If still broken, the problem is reproducible — document it.

Final note
If something “almost works” but not quite, do not hack around it.
Fix the pipeline or document the limitation.

This repo is meant to survive multiple hands and multiple chats.

go
Code kopieren
