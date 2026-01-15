# Distinguishability-Rate Theory (DRT)
## Paper Structure — Canonical Mapping (Journal-Grade)

**Title:**  
*Distinguishability as a Physical Primitive:  
Rate-Limited Inference, Temporal Resolution, and the Boundary of Quantum Ontology*

**Layer:** Ontology of Continua — Extensions, K₂  
**Evidence Pack:** PLATINUM (frozen, simulation-complete)  
**Status:** Architecture approved, paper extension in progress  
**Intent:** Journal submission (foundations / information physics)

---

## Purpose of this document

This file is the **single-source structural contract** for the paper.

It specifies:

- the logical role of each section,
- epistemic vs ontological status of claims by section,
- dependencies between analytical arguments,
- correspondence to the frozen Evidence Pack,
- where falsifiability and regime-of-validity are established.

This document is **not compiled into the PDF**.  
It exists to make the paper **auditable, extensible, and reviewer-resilient**.

---

## Global design principles

- **Inference-first:** limits are analyzed as distinguishability growth constraints.
- **Claims hygiene:** every strong claim is localizable by section and regime.
- **Boundary explicitness:** epistemic vs ontological constraints are separated formally.
- **No simulation drift:** numerical evidence is frozen and referenced, never reinterpreted.
- **Extension, not polish:** increased length comes from rigor, not exposition.

---

## Section-by-section mapping

### 00 — Extended Abstract (`sections/00_abstract.tex`)
**Role:**  
High-level operational summary for expert readers.

**Function:**  
- State the central claim: many temporal bounds are epistemic (inference-limited).
- Introduce distinguishability growth as the organizing primitive.
- Explicitly announce the epistemic–ontological boundary.
- Declare scope: what is *not* claimed.

**Claim status:**  
Epistemic framing + boundary declaration (no proofs).

---

### 01 — Introduction (`sections/01_introduction.tex`)
**Role:**  
Problem framing and motivation.

**Function:**  
- Critically review common interpretations of temporal bounds.
- Identify conflation of inference limits with ontology.
- Position the contribution relative to metrology and foundations.
- Define the scope and limits of the present work.

**Claim status:**  
Conceptual positioning; no hard bounds asserted.

---

### 02 — Operational Framework (`sections/02_operational_framework.tex`)
**Role:**  
Foundational definitions and language.

**Function:**  
- Define distinguishability operationally (decision-theoretic).
- Introduce distinguishability rate and decision thresholds.
- Formalize inference-limited vs dynamics-limited regimes.
- Establish notation used throughout the paper.

**Claim status:**  
Formal definitions (operational, epistemic).

---

### 03 — Rate-Limited Bounds (`sections/03_rate_limited_bounds.tex`)
**Role:**  
Core theoretical engine.

**Function:**  
- Derive general rate-limited bounds on inference.
- Show independence from microscopic dynamics.
- State conditions under which bounds are epistemic.
- Introduce short theorem / proposition statements.

**Claim status:**  
Epistemic bounds (provable under stated assumptions).  
**Falsifiable by:** violation via increased information rate.

---

### 04 — Classical Diffusion (`sections/04_classical_diffusion.tex`)
**Role:**  
Concrete classical realization.

**Function:**  
- Apply the framework to Brownian motion.
- Explain the origin of the $\Phi^{-1/3}$ scaling.
- Connect analytical scaling to frozen simulations.
- Identify regime of validity and breakdown.

**Claim status:**  
Epistemic scaling law (classical, non-ontological).

---

### 05 — Continuous Monitoring (`sections/05_continuous_monitoring.tex`)
**Role:**  
Bridge between classical and quantum regimes.

**Function:**  
- Treat continuous observation as an information channel.
- Show monitoring rate as the limiting factor.
- Generalize beyond i.i.d. sampling assumptions.
- Prepare the formal transition to quantum systems.

**Claim status:**  
Epistemic (channel-limited inference).

---

### 06 — Quantum Systems (`sections/06_quantum_systems.tex`)
**Role:**  
Quantum-mechanical instantiation.

**Function:**  
- Analyze Ramsey interferometry and open quantum systems.
- Use QFI to distinguish epistemic vs ontological constraints.
- Identify regimes where Fisher-reducibility fails.
- State boundary lemmas (MT-type vs ML-type limits).

**Claim status:**  
Mixed:
- Epistemic (QFI-limited inference).
- Ontological residues explicitly marked.

---

### 07 — Ontological Residues (`sections/07_ontological_residues.tex`)
**Role:**  
Conceptual resolution layer.

**Function:**  
- Precisely define the epistemic–ontological boundary.
- Identify bounds robust to unlimited inference rate.
- Clarify which structures require non-classical event algebra.
- Summarize boundary theorems informally.

**Claim status:**  
Ontological (non-Fisher-reducible constraints).

---

### 08 — Implications and Falsifiability (`sections/08_implications_falsifiability.tex`)
**Role:**  
Scientific accountability.

**Function:**  
- Propose explicit falsification strategies.
- Provide regime map (i.i.d. vs non-i.i.d., finite-$\Phi$).
- Distinguish noise, systematics, and true violations.
- Connect to experiments and metrology practice.

**Claim status:**  
Test protocols and regime diagnostics.

---

### 09 — Conclusions (`sections/09_conclusions.tex`)
**Role:**  
Synthesis and outlook.

**Function:**  
- Summarize results without repetition.
- Reiterate boundary results clearly.
- Indicate directions for future foundational work.

**Claim status:**  
No new claims.

---

## Appendices

### A — $\Phi^{-1/3}$ Scaling (`appendices/A_phi_minus_one_third.tex`)
Self-consistent derivation of the cubic-root scaling law.

### B — CTRW Derivations (`appendices/B_ctrw_derivations.tex`)
Generalization to anomalous diffusion regimes.

### C — Fisher / QFI Technicalities (`appendices/C_fisher_qfi_technicalities.tex`)
Formal definitions, inequalities, and technical lemmas.

### D — Monte Carlo Protocols (`appendices/D_monte_carlo_protocols.tex`)
Simulation methodology (documentation only; no interpretation).

### E — Reproducibility Checklist (`appendices/E_reproducibility_checklist.tex`)
One-command reproducibility and traceability guarantees.

---

## Figures

All figures are generated from the frozen Evidence Pack and included
as external PDFs via `figures/figures.tex`.

No figure content is authored manually in this repository.
