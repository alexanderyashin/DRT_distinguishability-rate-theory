# DRT Platinum — Distinguishability Rate Theory (OC Extensions K2)

This repository contains a **journal-grade, fully reproducible** research article and
simulation suite on **Distinguishability Rate Theory (DRT)**: operational /
information-theoretic limits of inference (time, distinguishability, throughput)
and the boundary between **epistemic** constraints and **ontic** nonclassicality
(Bell/Kochen–Specker; Margolus–Levitin under additional structure).

**Layer:** Ontology of Continua — Extensions, **K₂**  
**Evidence Pack:** **PLATINUM** (frozen; simulation-complete)  
**Status:** Paper extension complete; external audit pending  
**Intent:** Journal submission (foundations / information physics)

---

## What this is

- A **50+ page LaTeX paper** (in `paper/`) with a strict theorem/appendix structure.
- A **reproducible simulation + figure pipeline** (in `src/`) that generates:
  - Monte-Carlo decision-based inference (Class I),
  - self-consistent fixed-point constructions (Class 0A),
  - exponent-imposed generators for anomalous transport (Class 0B),
  - meeting-point (inference- vs dynamics-limited) regimes,
  - continuous-monitoring examples (OU),
  - noise/decoherence suppression envelopes.
- A **handoff-safe project layout** for multi-chat relay work:
  - `STATE.md` — single source of truth for status.
  - `RUNBOOK.md` — single source of truth for how to run/build.
  - `CONTEXT.md` — single source of truth for scientific intent/claims.

> **Claims hygiene:** Numerical work is used for reproducibility and regime
> illustration only. Analytic results are not inferred from simulations.

---

## One-command workflow

From the repository root:

```bash
make doctor
make all
Outputs

Figures: figures/*.pdf

Simulation artifacts: results/*

Paper PDF: paper/main.pdf

The build is deterministic given the frozen tag and recorded random seeds.

Repository map
paper/            LaTeX source
  sections/       Main text sections (≤ ~250–300 lines each)
  appendices/     Proofs and technical derivations
src/              Python code
  sims/           Monte Carlo / numerical experiments (write to results/)
  figs/           Figure generators (read from results/, write to figures/)
  fisher/         Analytic Fisher/QFI helpers and bounds
tools/            Utility scripts (doctor, run-all, clean)
results/          Generated data artifacts (produced by the pipeline)
figures/          Generated PDF figures (produced by the pipeline)


Figures are generated, not hand-authored. All figures included in the paper
are produced from the frozen Evidence Pack via scripted generators.

Scientific backbone (high level)
Core law — DRT master inequality

For an observation channel 
𝑌
𝑇
Y
T
	​

 with Fisher information matrix

𝐼
𝑇
(
𝜃
)
I
T
	​

(θ):

𝛿
𝜃
𝑇
𝐼
𝑇
(
𝜃
)
 
𝛿
𝜃
  
≥
  
2
𝐷
\*
⟺
𝛿
𝜃
min
⁡
(
𝑢
;
𝑇
)
  
≥
  
2
𝐷
\*
𝑢
𝑇
𝐼
𝑇
𝑢
.
δθ
T
I
T
	​

(θ)δθ≥2D
\*
⟺δθ
min
	​

(u;T)≥
u
T
I
T
	​

u
2D
\*
	​

	​

.

Quantum lift:

𝐼
𝑇
q
u
a
n
t
  
=
  
sup
⁡
𝑀
𝐼
𝑇
(
𝑀
)
(supremum over POVMs)
.
I
T
quant
	​

=
M
sup
	​

I
T
(M)
	​

(supremum over POVMs).
Epistemic vs ontic boundary

Epistemic: Derivable from the DRT master inequality
(local Fisher/QFI geometry + information accumulation).

Ontic: Not Fisher-reducible; requires global/algebraic/polytope structure
(Bell/KS; ML only with additional global assumptions).

Key analytic blocks included

Poisson point-process Fisher

𝐼
(
𝜃
)
=
∫
0
𝑇
(
∂
𝜃
𝜆
)
2
𝜆
 
𝑑
𝑡
.
I(θ)=∫
0
T
	​

λ
(∂
θ
	​

λ)
2
	​

dt.

OU (continuous monitoring)

𝐼
𝑇
(
𝛾
)
≈
𝑇
2
𝛾
.
I
T
	​

(γ)≈
2γ
T
	​

.

QFI under dephasing (equatorial qubit)

𝐹
𝑄
=
𝜂
2
.
F
Q
	​

=η
2
.

Noise suppression envelope

𝐼
𝑇
  
≤
  
∫
0
𝑇
𝐼
˙
i
d
e
a
l
(
𝑡
)
 
𝑒
−
2
Γ
𝑡
 
𝑑
𝑡
.
I
T
	​

≤∫
0
T
	​

I
˙
ideal
	​

(t)e
−2Γt
dt.

Fixed-point fractional scalings

𝛿
𝑡
min
⁡
∼
Φ
−
1
/
3
(diffusion localization)
,
𝛿
𝑡
min
⁡
∼
Φ
−
1
/
(
2
+
𝛼
)
(
M
S
D
∼
𝑡
𝛼
)
.
δt
min
	​

∼Φ
−1/3
(diffusion localization),δt
min
	​

∼Φ
−1/(2+α)
(MSD∼t
α
).

All scalings are classified by epistemic role (Class I / 0A / 0B) and regime of
validity in the paper.

How handoff between chats works

Open STATE.md and follow NEXT STEPS.

Run make doctor and resolve environment issues if any.

Run make sims, then make figs, then make pdf.

Update STATE.md with:

✅ done

⚠️ known issues

▶ next steps

🔁 exact commands to reproduce

License

See LICENSE.

Citation

See CITATION.cff.


---
