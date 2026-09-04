# MASTER Project Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Global scientific savepoints

- CORE Mathematical / Integration / Interpretation freezes: **STABLE**.
- Plasma/D10-ZF Pilot 0.2: **P2-A**, strong primary domain anchor.
- Neuro/CMC Pilot 0.1: **NEURO-STRONG**, strong cross-domain demonstrator.
- Climate-A/Phillips-QG Pilot 0.1: **CLIM-WEAK**, robust weak/contrast case.
- Climate-B/Bickley-jet one-shot Pilot 0.1: **CLIM-B-FAIL — resolution robustness failure**, result frozen.
- Cross-Domain Result Integration & Freeze 0.1: **STABLE**.
- Cross-Domain Application Literature Positioning Audit 0.1: **COMPLETE**.
- Cross-Domain Manuscript Positioning & Claim Freeze 0.1: **STABLE**.
- Manuscript Structure Freeze 0.2: **STABLE**.
- Manuscript Revision 0.4: **COMPLETE — PASS**.
- Submission Readiness Gate 0.1: **PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY**.
- First Paper Scientific Content Freeze 0.1: **STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED**.
- Post-Paper Scientific Roadmap Gate 0.1: **COMPLETE — FUSION-F1 SELECTED**.
- Fusion B5.5 physical ion heat-flux observable: **PASS**.
- Fusion B5.5 Heat-Flux Observable Integration Freeze 0.1: **STABLE — PHYSICAL CHANNEL FROZEN / F1.2 RELEASED**.

## First-paper status

The scientific content of Paper 1 remains frozen. Draft 0.4 is the scientific-content baseline but not final prose. Submission preparation remains parked by user choice.

No APS portal, cover letter, author-list, OA/APC, archive DOI/release/license, or production-formatting work is active.

## Primary post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

The program asks whether finite-horizon signed ion heat-transport optimality differs meaningfully from free-energy optimality in an energy-consistent fusion hierarchy and whether any distinction survives controlled increases in physical fidelity.

Planned hierarchy:

\[
\text{anisotropic ZLR four-moment gyrofluid}
\rightarrow
\text{FLR gyrofluid}
\rightarrow
\text{parallel/flux-tube or local gyrokinetic/GENE-compatible validation}.
\]

No finite-time Fusion effect has yet been inspected or authorized.

## Fusion B5.5 integrated result

The frozen R1 state is

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad
\Phi=\mathcal C_kN.
\]

The physical ion radial thermal-energy/heat-flux channel is independently derived as

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\]

\[
Q_{q_i,k}
=p_0\mathcal V_k\mathcal C_k
\begin{pmatrix}
0&0&i/4&i/2\\
0&0&0&0\\
-i/4&0&0&0\\
-i/2&0&0&0
\end{pmatrix},
\qquad
\mathcal V_k=\frac{ck_yT_{i0}}{eB_0}.
\]

For `k_y!=0`, `Q_{q_i,k}` is Hermitian, rank 2 and indefinite. It applies to both slab and minimal-curvature R1 generators.

Its exact balance with the frozen positive free-energy metric is

\[
A_k^\dagger M_k+M_kA_k
=2\left(-\frac{d\ln T_{i0}}{dx}\right)\frac{Q_{q_i,k}}{p_0},
\]

or

\[
\frac{dW_k}{dt}= -\frac{d\ln T_{i0}}{dx}\,q_{i,k}.
\]

The ion particle-flux channel remains `Q_{Gamma_i,k}=0` in this frozen adiabatic-electron R1 closure; it is not to be repaired for effect richness.

Canonical result:

`research/fusion/B5_5_ion_heat_flux_observable.md`

MASTER savepoint:

`research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`

B5.5 commit `d4d72d02cfdacb383091d24348d6f8966a49d723`; Python CI #309 = `SUCCESS`.

## Immediate next gate

Fusion F1.2 must determine the admissible initial-perturbation geometry and input cost before any finite-time objective comparison:

\[
(B,R_{\rm in}).
\]

The gate must test whether arbitrary closed-state initial perturbations justify `B=I` with free-energy input cost `R_in=M_k`; if not, it must derive a physically motivated lower-rank `B`. It must not force transport neutrality or choose a geometry from effect size.

Canonical instruction:

`research/master/prompts/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

Branch status:

`research/fusion/STATUS.md`

## Planned dependency chain

1. B5.5 heat-flux observable derivation — **COMPLETE / FROZEN**;
2. admissible-input geometry / input-cost gate — **READY**;
3. Fusion candidate/convention freeze;
4. numerical/spectral qualification;
5. targeted Fusion literature positioning for the exact frozen question;
6. pilot specification;
7. MASTER pilot freeze and one-shot execution;
8. result integration/freeze;
9. later FLR/GK fidelity progression based on physical/structural validity, not effect size.

## Other branch states

- CORE: `STABLE / PARKED`
- MODES: `PARKED / conditional Fusion companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro: first result frozen; higher-fidelity extensions parked
- Climate: A/B frozen; no B repair or third-candidate rescue lineage
- Literature: no new task until Fusion candidate/channel freeze
- Manuscript: Paper-1 content frozen; submission parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`
- Fusion: `F1.2 INPUT GEOMETRY / INPUT COST READY — AWAIT GO`

## Parallelism decision

No immediate parallel science is opened. `MODES` may later support Fusion if high-dimensional representation/reduction robustness becomes a concrete issue. `CONT` may become natural after a physical parameter family is frozen. Neither is active now.

## Branch-independent / branch-dependent distinction

Branch-independent methodology remains

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}),
\]

with finite-time positive/signed operators, signed extrema, optimizer/subspace geometry, performance gap, physical reconstruction, robustness and anti-retuning discipline.

Fusion branch-dependent semantics are now more specific:

- `M_k`: positive perturbation free-energy metric for the R1 gyrofluid state;
- `Q_{q_i,k}`: signed radial ion thermal-energy/heat-flux observable derived from `E×B` transport;
- `Q_{Gamma_i,k}=0`: closure restriction, not a missing channel to be manufactured;
- `B,R_in`: still unresolved and therefore the next pre-effect gate.

## Protected rollback chain

All first-paper savepoints remain protected through `First Paper Scientific Content Freeze 0.1`. Post-paper savepoints now include:

1. `Post-Paper Scientific Roadmap Gate 0.1`;
2. `Fusion B5.5` branch result;
3. `Fusion B5.5 Heat-Flux Observable Integration Freeze 0.1`.

New Fusion work cannot silently revise these savepoints.

## Decision record

- base: `research/master/decision_branch_log.md` through DEC-443;
- continuation 0.1: `research/master/decision_branch_log_addendum_0_1.md` through DEC-486;
- continuation 0.2: `research/master/decision_branch_log_addendum_0_2.md` through DEC-494.

## Current next action

Use the Fusion branch/chat `60 – FUSION – Gyrofluid/Gyrokinetic Transport` and issue bare `GO` after it has read `research/fusion/STATUS.md`.

No finite-time Fusion effect inspection or parallel branch work is authorized before F1.2 returns to MASTER.
