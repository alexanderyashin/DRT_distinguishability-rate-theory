# CONTRIBUTING — DRT Platinum

This project is designed to be worked on **by multiple independent chats / contributors in sequence**.
The rules below exist to keep the repository coherent, reproducible, and reviewable.

---

## Core principles

1. **Reproducibility over cleverness**
   - Every result must be reproducible via documented commands.
   - No ad-hoc scripts, no “just run this once”.

2. **One source of truth**
   - Status → `STATE.md`
   - Intent → `CONTEXT.md`
   - How-to → `RUNBOOK.md`

3. **No silent changes**
   - If you change behavior, parameters, or assumptions, document it.

---

## Roles (typical handoff chain)

### Generator
- Creates repository structure and initial content.
- Does NOT run simulations.

### Executor (Sims)
- Runs simulations and fixes numerical issues.
- Generates figures.
- Updates `STATE.md` with exact commands and outcomes.

### Editor
- Integrates numerical results into LaTeX text.
- Improves clarity, consistency, and references.
- Does NOT change simulation logic.

### Reviewer
- Polishes language and structure.
- Checks claims vs evidence.
- Flags inconsistencies.

### Builder / Release
- Ensures clean build.
- Prepares Zenodo release.

One person/chat may take multiple roles, but the **rules still apply**.

---

## Mandatory rules (non-negotiable)

- ✅ Update `STATE.md` before you stop working.
- ✅ Record exact commands used.
- ❌ Do NOT commit generated data or figures unless explicitly instructed.
- ❌ Do NOT restructure directories without updating documentation.
- ❌ Do NOT exceed ~300 lines per LaTeX file unless unavoidable.

---

## Coding standards (Python)

- Python ≥ 3.10
- Use numpy/scipy idioms, no custom math hacks.
- Deterministic randomness:
  - Always set and document RNG seeds.
- Each simulation script:
  - Reads parameters at the top of the file.
  - Writes outputs only to `results/`.

---

## LaTeX standards

- Each section is a standalone file.
- No custom macros inside section files (use `preamble.tex`).
- Figures are included as PDFs from `figures/`.
- Every nontrivial equation must be explained in text.

---

## How to add a new simulation

1. Create a new file in `src/sims/`.
2. Ensure it writes a machine-readable output to `results/`.
3. Add a corresponding figure generator in `src/figs/`.
4. Document parameters and purpose in `STATE.md`.

---

## How to add a new section/appendix

- Check total `.tex` file count (stay ≤ 30 if possible).
- Keep file length reasonable.
- Cross-reference clearly.

---

## If you are unsure

- Prefer clarity over progress.
- Leave notes in `STATE.md`.
- Future you (or the next chat) will thank you.

---

## Attribution

This project is authored by Alexander Yashin.  
Contributors and assisting chats should be acknowledged in `CHANGELOG.md` where appropriate.
