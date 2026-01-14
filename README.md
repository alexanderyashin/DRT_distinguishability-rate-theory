# DRT Platinum — Distinguishability Rate Theory (OC Extensions K2)

This repository contains a journal-grade, reproducible research article and simulation suite on **Distinguishability Rate Theory (DRT)**: operational / information-theoretic limits of inference (time, distinguishability, throughput) and the boundary between **epistemic** constraints and **ontic** nonclassicality (Bell/KS, ML).

## What this is
- A **50+ page** LaTeX paper (in `paper/`) with a strict theorem/appendix structure.
- A **reproducible simulation + figure pipeline** (in `src/`) that generates:
  - Monte Carlo confirmations of fixed-point fractional scalings (e.g. Φ^{-1/3}, Φ^{-1/(2+α)}),
  - meeting-point (inference-limited vs dynamics-limited) phase diagrams,
  - continuous-monitoring examples (OU), and noise-suppression bounds.
- A “handoff-safe” project layout designed for **multi-chat relay work**:
  - `STATE.md` is the single source of truth for status.
  - `RUNBOOK.md` is the single source of truth for how to run/build.
  - `CONTEXT.md` is the single source of truth for scientific intent/claims.

## One-command workflow
From the repo root:

```bash
make doctor
make all
Outputs:

Figures: figures/*.pdf

Simulation artifacts: results/*

Paper PDF: paper/main.pdf

Repo map
paper/ — LaTeX source

sections/ — main text sections (≤ ~250–300 lines each)

appendices/ — proof/derivation appendices

src/ — python code

src/sims/ — Monte Carlo / numerical experiments (write to results/)

src/figs/ — figure generators (read from results/, write to figures/)

src/fisher/ — analytic Fisher/QFI helpers and bounds

tools/ — dumb scripts (run-all, doctor, clean)

results/ — generated data (tracked only via README, not committed)

figures/ — generated PDFs (tracked only via README, not committed)

Scientific backbone (high-level)
Core law (DRT master inequality):

For observation channel 
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
⊤
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
⇔
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
⊤
𝐼
𝑇
𝑢
δθ 
⊤
 I 
T
​
 (θ)δθ≥2D 
\*
​
 ⇔δθ 
min
​
 (u;T)≥ 
u 
⊤
 I 
T
​
 u
2D 
\*
​
 
​
 
​
 
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
𝑀
I 
T
quant
​
 =sup 
M
​
 I 
T
M
​
  (sup over POVMs).

Epistemic vs ontic boundary:

Epistemic: derivable from DRT master inequality (local Fisher/QFI geometry + information accumulation).

Ontic: not Fisher-reducible; requires global/algebraic/polytope structure (Bell/KS; ML via orthogonality + lower-bounded spectrum).

Key analytic blocks included:

Poisson point process Fisher: 
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
/
𝜆
 
𝑑
𝑡
I(θ)=∫ 
0
T
​
 (∂ 
θ
​
 λ) 
2
 /λdt.

OU (continuous monitoring): 
𝐼
𝑇
(
𝛾
)
≈
𝑇
/
(
2
𝛾
)
I 
T
​
 (γ)≈T/(2γ).

QFI under dephasing: 
𝐹
𝑄
=
𝜂
2
F 
Q
​
 =η 
2
  (equatorial qubit).

Noise suppression bound: 
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

Fixed-point fractional scalings: 
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
δt 
min
​
 ∼Φ 
−1/3
  (diffusion localization) and 
Φ
−
1
/
(
2
+
𝛼
)
Φ 
−1/(2+α)
  (MSD ~ t^α).

How handoff between chats works
Open STATE.md and follow “NEXT STEPS”.

Run make doctor and fix environment issues if any.

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