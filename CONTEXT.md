# CONTEXT — Distinguishability Rate Theory (DRT Platinum)

## Purpose of this document
This file explains **what problem this project solves**, **what it does and does not claim**, and **how to interpret results**.  
A new contributor or chat must read this file before touching code or text.

---

## Scientific question

**Central question:**
> Which parts of quantum-mechanical limits are consequences of *epistemic / operational constraints on inference*, and which require *ontological nonclassicality*?

This project addresses this question using a unified, information-theoretic framework centered on **distinguishability**.

---

## Core idea

The primitive object is **distinguishability**, not time, energy, or discreteness.

Given an observation channel \(Y_T\) over duration \(T\), the local distinguishability of nearby parameters \(\theta\) is governed by Fisher geometry:
\[
D(\theta,\theta+\delta\theta;T)
\;=\;
\frac12\,\delta\theta^\top I_T(\theta)\,\delta\theta
\quad(\text{local regime})
\]

From this follows the **DRT master inequality**:
\[
\delta\theta^\top I_T(\theta)\,\delta\theta \ge 2D_\*
\]

Everything in this repository is a consequence, specialization, or boundary test of this inequality.

---

## Epistemic vs ontic boundary

### Epistemic (DRT-derivable)
Constraints that arise from:
- local distinguishability geometry (Fisher / QFI),
- accumulation rate of information,
- finite throughput, noise, or coarse-graining.

Examples:
- CRLB and multi-parameter Fisher bounds,
- Mandelstam–Tamm quantum speed limit,
- operational minimal time resolution,
- fractional scalings (e.g. Φ^{-1/3}) from self-consistent inference.

### Ontic (not Fisher-reducible)
Constraints that require global or algebraic structure:
- Bell nonlocality (polytope violation),
- Kochen–Specker contextuality,
- Margolus–Levitin bound (orthogonality + lower-bounded spectrum).

The paper proves that epistemic effects **cannot generate ontic phenomena** (No-Free-Epistemic-Lunch).

---

## What this project DOES claim

- A large class of “quantum-looking” limits are inference limits.
- Distinguishability rate, not discreteness, sets minimal operational scales.
- Classical and quantum systems share the same inferential backbone.
- Ontological nonclassicality has a sharp, provable boundary.

---

## What this project does NOT claim

- It does NOT claim that time or space is discrete.
- It does NOT reduce all of quantum mechanics to epistemics.
- It does NOT modify quantum dynamics.
- It does NOT rely on metaphysical assumptions.

All claims are operational and falsifiable.

---

## Relation to previous work

- Extends the author’s previous Zenodo work on minimal temporal distinguishability in diffusion.
- Generalizes to:
  - Poisson point processes,
  - continuous monitoring,
  - quantum Fisher information,
  - noisy quantum channels.
- Integrated as **OC Extensions K2** (epistemic layer of time/distinguishability).

---

## Role of simulations

Simulations are used to:
- confirm analytic scalings,
- visualize meeting-point regimes,
- provide phase diagrams where closed-form expressions are unavailable.

Simulations are **supporting**, not defining, the theory.

---

## Reading order (for humans)

1. `paper/sections/01_introduction.tex`
2. `paper/sections/03_master_inequality.tex`
3. `paper/sections/05_fixed_point_scalings.tex`
4. `paper/sections/06_quantum_block.tex`
5. `paper/sections/07_ontic_boundary.tex`
6. Appendices as needed.

---

## If something seems unclear

Check in order:
1. This file.
2. `STATE.md`
3. `RUNBOOK.md`

If still unclear, the problem is in the repo, not in you.
Fix the repo.
