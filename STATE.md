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
================================================================================
EXECUTION UPDATE — Executor Chat #1 (Reproducibility Pass)
================================================================================

Date: 2026-01-16
Executor: Executor Chat #1
Branch: reanchor-scaling-claims
Commit: 9d6cc36

----------------------------------------------------------------
COMMANDS EXECUTED (verbatim)
----------------------------------------------------------------
- git add -A
- git commit -m "WIP: reanchor scaling claims + paper text/sims updates (snapshot before next pass)"
- git push -u origin reanchor-scaling-claims
- make pdf
- make doctor

----------------------------------------------------------------
BUILD & ENVIRONMENT STATUS
----------------------------------------------------------------
LaTeX build:
- make pdf → SUCCESS
- Output: paper/main.pdf
- latexmk present and functional

Environment check (make doctor):
- python3 found
- Python version: 3.12
- Required python packages: AVAILABLE
- latexmk: FOUND
- directory structure: OK

----------------------------------------------------------------
UPDATED FACTUAL STATE
----------------------------------------------------------------
The following items are now COMPLETE:

- zenodo.json: PRESENT and committed
- RUNBOOK.md: PRESENT and committed
- STATE.md: updated with execution record
- LaTeX build: SUCCESSFUL
- Environment sanity check: PASSED

----------------------------------------------------------------
STATUS ASSESSMENT
----------------------------------------------------------------
Repository is now in state:

✅ READY FOR SIMULATIONS

No blockers detected at environment or build level.
No silent fixes performed.
All actions traceable to commit 9d6cc36.

----------------------------------------------------------------
NEXT ALLOWED STEP
----------------------------------------------------------------
Handoff to:
→ Executor Chat #1 (Simulation Pass)

Permitted commands (per RUNBOOK):
- make sims
- make figs

All further steps must be logged here.

================================================================================
================================================================================
EXECUTION UPDATE — Executor Chat #1 (Simulation Pass)
================================================================================

Date: 2026-01-16
Branch: reanchor-scaling-claims
Baseline commit before sims: 13ba488

----------------------------------------------------------------
COMMANDS EXECUTED (verbatim)
----------------------------------------------------------------
- make sims
- (failure diagnosis, read-only)
  - sed -n '1,220p' src/sims/phi_scaling_multiseed.py
  - python - <<'PY' ... inspect.signature(...) ... PY
  - sed -n '1,260p' src/sims/diffusion_localization_mc.py
  - ls -lah results | sed -n '1,200p'
- python -m src.sims.phi_scaling_multiseed
- make sims
- python -m src.sims.ctrw_alpha_sweep
- make sims

----------------------------------------------------------------
SIMULATION RUN #1 — FAILURE
----------------------------------------------------------------
make sims output (key lines):
[1] Diffusion localization (Φ^{-1/3})
  Class 0A Φ-scaling fit slope: -0.33011443491802445
  [OK] Wrote results/diffusion_phi_scaling.json
[2] CTRW / anomalous diffusion scalings
  Class 0B CTRW Φ-scaling slope (imposed): -0.3872003839512218
  [OK] Wrote results/ctrw_phi_scaling.json
[3] Ramsey meeting-point phase diagram
  Ramsey meeting-point data generated.
[4] Mach–Zehnder meeting-point phase diagram
  MZI meeting-point data generated.
== Simulations completed ==

[5] Multi-seed exponent robustness
  TypeError: run_simulation() got an unexpected keyword argument 'D'
  make: *** [Makefile:34: sims] Error 1

Root cause (confirmed):
- src/sims/phi_scaling_multiseed.py called diffusion_localization_mc.run_simulation with
  keyword args (D, sigma_m, n_mc), but the actual signature is:
  run_simulation(phi_values, p: Params, rng: np.random.Generator)
  and it returns (delta_t, all_diags).

----------------------------------------------------------------
FIX #1 (CODE) — phi_scaling_multiseed API alignment
----------------------------------------------------------------
File updated:
- src/sims/phi_scaling_multiseed.py

Change:
- import Params and construct p=Params(D=..., sigma_m=..., n_mc=...)
- create rng = np.random.default_rng(seed)
- call delta_t, _diags = run_simulation(phi_values, p, rng)

Single-script verification:
- python -m src.sims.phi_scaling_multiseed
  -> [OK] Multi-seed slopes + CI written: results/phi_multiseed_slopes.json

----------------------------------------------------------------
SIMULATION RUN #2 — FAILURE
----------------------------------------------------------------
make sims continued and passed steps [1]–[5], then failed at:

[6] CTRW alpha sweep
  TypeError: run_simulation() missing 1 required positional argument: 'rng'
  make: *** [Makefile:36: sims] Error 1

Root cause:
- src/sims/ctrw_alpha_sweep.py called ctrw_mc.run_simulation without rng,
  but baseline run_simulation requires an rng argument.

----------------------------------------------------------------
FIX #2 (CODE) — ctrw_alpha_sweep rng plumbing
----------------------------------------------------------------
File updated:
- src/sims/ctrw_alpha_sweep.py

Change:
- per replicate seed: set_seed(seed) + rng = np.random.default_rng(seed)
- call run_simulation(..., rng=rng)

Single-script verification:
- python -m src.sims.ctrw_alpha_sweep
  -> [OK] α-sweep ... written: results/ctrw_alpha_sweep.json

----------------------------------------------------------------
SIMULATION RUN #3 — SUCCESS (COMPLETE)
----------------------------------------------------------------
Final make sims output (key lines):
[1] Diffusion localization (Φ^{-1/3})
  Class 0A Φ-scaling fit slope: -0.33011443491802445
  [OK] Wrote results/diffusion_phi_scaling.json
[2] CTRW / anomalous diffusion scalings
  Class 0B CTRW Φ-scaling slope (imposed): -0.3872003839512218
  [OK] Wrote results/ctrw_phi_scaling.json
[3] Ramsey meeting-point phase diagram
  Ramsey meeting-point data generated.
[4] Mach–Zehnder meeting-point phase diagram
  MZI meeting-point data generated.
[5] Multi-seed exponent robustness
  [OK] Multi-seed slopes + CI written: results/phi_multiseed_slopes.json
[6] CTRW alpha sweep
  [OK] α-sweep (baseline-consistent) + multi-seed + CI written: results/ctrw_alpha_sweep.json
[7] Ramsey optimal time under dephasing
  [OK] Ramsey optimal time written: results/ramsey_optimal_time.json

Artifacts confirmed in results/ (written/overwritten during sims):
- results/diffusion_phi_scaling.json
- results/ctrw_phi_scaling.json
- results/phi_multiseed_slopes.json
- results/ctrw_alpha_sweep.json
- results/ramsey_meeting_point.json
- results/mzi_meeting_point.json
- results/ramsey_optimal_time.json

----------------------------------------------------------------
STATUS ASSESSMENT
----------------------------------------------------------------
✅ READY FOR FIGURE GENERATION
- Simulation pass now completes successfully end-to-end.
- Two runner scripts required API/rng plumbing fixes (no theory changes).

Next allowed step:
- make figs

================================================================================
