# CHANGELOG — DRT Platinum

All notable changes to this project are documented in this file.

The format follows a lightweight, chronological log suitable for
multi-chat, relay-style development.

---

## [Unreleased]

### Added
- Full repository architecture for DRT Platinum.
- Formal separation of epistemic vs ontic constraints (DRT master inequality).
- Analytic backbone:
  - Poisson point process Fisher information.
  - Fixed-point fractional scalings (Φ^{-1/3}, Φ^{-1/(2+α)}).
  - Quantum Fisher information under noise.
  - Continuous monitoring (OU process).
  - Meeting-point (inference-limited vs dynamics-limited) framework.

### Planned
- Monte Carlo simulations for diffusion localization and CTRW.
- Meeting-point phase diagrams (Ramsey, MZI).
- Final LaTeX integration and Zenodo release.

---

## [0.1.0] — Initial repository generation (in progress)

### Added
- `README.md`
- `STATE.md`
- `CONTEXT.md`
- `RUNBOOK.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`

### Notes
- This version is **not** a release.
- No simulations or builds have been executed yet.
- Repository generation is ongoing.

---

## Versioning policy

- Versions < 1.0.0 are considered **pre-release**.
- A version bump requires:
  - Clean build (`make all`)
  - Updated `STATE.md`
  - Updated `CHANGELOG.md`

---

## Attribution

- Author: Alexander Yashin
- Assistant / Generator: Logion (research chat)

Further contributors will be listed as they appear.
