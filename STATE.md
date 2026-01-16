# PROJECT STATE — DRT Platinum (OC Extensions K2)

> **Purpose of this file**  
> This is the ONLY authoritative status tracker for the project.  
> Every chat that touches this repo must update this file before stopping.

---

## CURRENT PHASE
**Phase:** Repository generation (Chat: Logion / Generator)  
**Status:** IN PROGRESS (late generation stage)

---

## WHAT IS DONE (authoritative)

### Scientific & conceptual
- [x] Distinguishability Rate Theory (DRT) formalism fully defined and fixed
      (OC Extensions K2; epistemic vs ontological boundary explicit).
- [x] Canonical paper structure defined and frozen
      (see CONTEXT / Canonical Mapping).
- [x] Claims hygiene enforced (epistemic vs ontological separation by section).

### LaTeX manuscript (sources generated)
- [x] Main paper sections generated:
  - `00_abstract.tex`
  - `01_introduction.tex`
  - `02_operational_framework.tex`
  - `03_rate_limited_bounds.tex`
  - `04_classical_diffusion.tex`
  - `05_continuous_monitoring.tex`
  - `06_quantum_systems.tex`
  - `07_ontological_residues.tex`
  - `08_implications_falsifiability.tex`
  - `09_conclusions.tex`
- [x] Appendices generated:
  - `A_phi_minus_one_third.tex`
  - `B_ctrw_derivations.tex`
  - `C_fisher_qfi_technicalities.tex`
  - `D_monte_carlo_protocols.tex`
  - `E_reproducibility_checklist.tex`
- [x] Figures inclusion structure defined (`figures/figures.tex`, external PDFs).

### Documentation
- [x] `README.md` generated.
- [x] Canonical structure / intent document created (paper structure mapping).
- [x] `CITATION.cff` drafted (content complete, DOI placeholder present).

---

## WHAT IS BEING DONE NOW
- Completing remaining **root-level repository files**.
- Aligning metadata (citation, Zenodo, license) for release readiness.
- Ensuring internal consistency between paper, README, and metadata.

---

## WHAT IS NOT DONE YET

### Root project files
- [ ] `zenodo.json` (NOT YET PRESENT — REQUIRED before release).
- [ ] `LICENSE` file (MIT, text not yet committed).
- [ ] `RUNBOOK.md`.
- [ ] `STATE.md` final release update (this file will need another update).
- [ ] `CONTEXT.md` (if kept separate from README).

### Code & execution
- [ ] Python simulation code (`src/`).
- [ ] Figure generation code (`src/figs/`).
- [ ] Any numerical execution.
- [ ] Any LaTeX build attempt.

---

## NEXT STEPS (STRICT ORDER)

1. **Finish repository generation**
   - Add `zenodo.json`
   - Add `LICENSE`
   - Add `RUNBOOK.md`
   - Finalize `CITATION.cff` (replace DOI after Zenodo upload)

2. **Handoff to Executor Chat #1**
   - Run `make doctor`
   - Run simulations (`make sims`)
   - Generate figures (`make figs`)
   - Record exact commands and issues here

3. **Handoff to Editor Chat #1**
   - Integrate numerical outputs into figures
   - Cross-check captions vs evidence pack
   - No conceptual changes

4. **Handoff to Reviewer Chat(s)**
   - Language tightening
   - Structural sanity check
   - Zero theory changes

5. **Final build and Zenodo release**
   - `make pdf`
   - Zenodo upload
   - DOI insertion
   - Final STATE.md freeze

---

## KNOWN RISKS / ASSUMPTIONS
- Python environment (numpy/scipy/matplotlib) assumed available.
- LaTeX build assumes `latexmk` is installed.
- Figures are generated as PDFs and included statically in LaTeX.
- Zenodo metadata must match paper title EXACTLY.

---

## REPRODUCIBILITY CONTRACT
Every future chat MUST:
- Update this file.
- Record exact commands used.
- Mark any deviations from expected behavior.

Failure to update this file = broken handoff.

---

## LAST UPDATE
- By: Logion (Generator Chat)
- Reason: Repository state updated after full paper + appendices generation;
          metadata and execution layers still pending.
