# MASTER Project Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Global scientific savepoints

- CORE Mathematical / Integration / Interpretation freezes: **STABLE**.
- Plasma/D10-ZF Pilot 0.2: **P2-A**, frozen.
- Neuro/CMC Pilot 0.1: **NEURO-STRONG**, frozen.
- Climate-A/Phillips-QG Pilot 0.1: **CLIM-WEAK**, frozen.
- Climate-B/Bickley-jet Pilot 0.1: **CLIM-B-FAIL — resolution robustness failure**, frozen.
- Manuscript Revision 0.4: **COMPLETE — PASS**.
- First Paper Scientific Content Freeze 0.1: **STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED**.
- Post-Paper Scientific Roadmap Gate 0.1: **COMPLETE — FUSION-F1 SELECTED**.
- Fusion B5.5 physical ion heat-flux observable: **PASS / INTEGRATED**.
- Fusion B5.5 Heat-Flux Observable Integration Freeze 0.1: **STABLE**.
- Fusion F1.2 input geometry / input cost: **PASS / INTEGRATED**.
- Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1: **STABLE — F1.3 RELEASED**.

## First-paper status

Paper 1 scientific content remains frozen. Draft 0.4 is a scientific-content baseline, not final prose. Submission preparation remains parked by user choice.

## Active post-paper program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

Planned fidelity sequence:

\[
\text{anisotropic ZLR four-moment gyrofluid}
\rightarrow
\text{FLR gyrofluid}
\rightarrow
\text{parallel/flux-tube or local gyrokinetic/GENE-compatible validation}.
\]

No finite-time Fusion objective-separation effect has yet been authorized or inspected.

## Frozen Fusion primitives after F1.2

State and electrostatic closure:

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN.
\]

Positive free-energy metric: `M_k` from B5.4.

Physical signed heat channel: `Q_{q_i,k}` from B5.5, Hermitian, rank 2 and indefinite for `k_y!=0`, with exact free-energy balance.

Admissible initial-condition geometry and input cost:

\[
\boxed{B=I_4,\qquad R_{\rm in}=M_k,\qquad \operatorname{rank}(B)=4.}
\]

`B=I_4` is a tangent-state admissibility statement, not a laboratory actuator claim. The instantaneous restricted heat channel remains non-neutral and indefinite. `Q_{Gamma_i,k}=0` remains a frozen closure restriction.

Canonical F1.2 result:

`research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

MASTER F1.2 savepoint:

`research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`

F1.2 commit `8d555475577e77e93f9646df60343a34f0503525`; Python CI #316 = `SUCCESS`.

## Immediate next gate

Fusion F1.3 — Candidate / Convention Freeze 0.1 is now the only active scientific handoff.

The intended primary candidate is the already-derived anisotropic-ZLR four-moment R1 **minimal-curvature** branch if the frozen derivation chain remains consistent. The slab branch remains an analytic/limiting control.

F1.3 must freeze exact state/normalization, Fourier and electrostatic conventions, selected generator, `M_k`, `Q_{q_i,k}`, `B`, `R_in`, gradient and curvature conventions, parallel-wavenumber convention, dissipation/closure choice, time normalization and one physical parameter point using source/model criteria only. No finite-time objective effect may be inspected.

Canonical instruction:

`research/master/prompts/fusion_candidate_convention_freeze_0_1.md`

## Planned dependency chain

1. B5.5 heat-flux observable — **COMPLETE / FROZEN**;
2. F1.2 admissible input geometry / cost — **COMPLETE / FROZEN**;
3. F1.3 candidate / convention freeze — **READY**;
4. numerical/spectral qualification;
5. targeted exact-question Fusion literature positioning;
6. pilot specification;
7. MASTER pilot freeze and one-shot execution;
8. result integration/freeze;
9. later FLR/GK fidelity progression based on physical/structural validity, not effect size.

## Other branch states

- CORE: `STABLE / PARKED`
- MODES: `PARKED / conditional Fusion companion`
- CONT: `PARKED`
- CASCADE: `PARKED`
- Neuro: frozen first result; extensions parked
- Climate: A/B frozen; no B repair or third-candidate rescue lineage
- Literature: no active task before Fusion candidate/channel freeze
- Manuscript/submission: parked
- Power Grids: `PROTECTED`
- Photonics/Waves: `PROTECTED`
- Fusion: `F1.3 CANDIDATE / CONVENTION FREEZE READY — AWAIT GO`

## Parallelism decision

No parallel science is opened. MODES remains conditional on a later high-dimensional Fusion representation problem; CONT waits for a physically frozen parameter family.

## Branch-independent / branch-dependent distinction

Branch-independent methodology remains

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}).
\]

Fusion branch-dependent semantics are frozen up through the physical heat channel and admissible input geometry. The exact candidate parameter/convention package remains the next pre-effect object.

## Protected rollback chain

All first-paper savepoints remain protected. Post-paper savepoints now include:

1. Post-Paper Scientific Roadmap Gate 0.1;
2. Fusion B5.5 Integration Freeze 0.1;
3. Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1.

## Decision record

- base through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502.

## Current next action

In `60 – FUSION – Gyrofluid/Gyrokinetic Transport`, issue bare `GO`. The branch must read `research/fusion/STATUS.md` and execute only `research/master/prompts/fusion_candidate_convention_freeze_0_1.md`.

No numerical qualification, finite-time effect inspection, FLR/GK extension or parallel branch work is authorized before F1.3 returns.
