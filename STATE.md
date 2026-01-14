# PROJECT STATE — DRT Platinum (OC Extensions K2)

> **Purpose of this file**  
> This is the ONLY authoritative status tracker for the project.  
> Every chat that touches this repo must update this file before stopping.

---

## CURRENT PHASE
**Phase:** Repository generation (Chat: Logion / Generator)  
**Status:** IN PROGRESS

---

## WHAT IS DONE (authoritative)
- [x] Scientific formalism (DRT, K2) fully defined and fixed in OC Extensions K2 memory.
- [x] Repository architecture defined (self-explaining, handoff-safe).
- [x] `README.md` generated.

---

## WHAT IS BEING DONE NOW
- Sequential generation of the full repository (files created one by one).
- No simulations executed yet.
- No LaTeX build attempted yet.

---

## WHAT IS NOT DONE YET
- Root project files (license, citation, runbook, etc.).
- Python simulation code.
- Figure generators.
- LaTeX paper sources.
- Any numerical execution or validation.

---

## NEXT STEPS (STRICT ORDER)
1. Finish generating all repository files.
2. Handoff to **Executor Chat #1**:
   - Run `make doctor`
   - Run simulations (`make sims`)
   - Generate figures (`make figs`)
3. Handoff to **Editor Chat #1**:
   - Integrate numerical results into text.
4. Handoff to **Reviewer Chat(s)**:
   - Polish text and structure.
5. Final build and Zenodo release.

---

## KNOWN RISKS / ASSUMPTIONS
- Python environment (numpy/scipy/matplotlib) assumed available.
- LaTeX build assumes `latexmk` is installed.
- Figures are generated as PDFs and included statically in LaTeX.

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
- Reason: Initial repository generation
