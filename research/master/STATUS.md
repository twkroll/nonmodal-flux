# MASTER Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science is active only in Fusion.

Stable first-paper lineage:

- CORE Mathematical / Integration / Interpretation freezes: `STABLE`;
- Plasma/D10-ZF: `P2-A`, `FROZEN`;
- Neuro/CMC: `NEURO-STRONG`, `FROZEN`;
- Climate-A: `CLIM-WEAK`, `FROZEN`;
- Climate-B: `CLIM-B-FAIL — resolution robustness failure`, `RESULT FROZEN`;
- Manuscript Revision 0.4: `COMPLETE — PASS`;
- Submission Readiness Gate 0.1: `PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY`;
- First Paper Scientific Content Freeze 0.1: `STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED`.

Post-paper Fusion lineage:

- Post-Paper Scientific Roadmap Gate 0.1: `COMPLETE — FUSION-F1 SELECTED`;
- B5.5 physical ion heat-flux observable: `PASS / MASTER-INTEGRATED`;
- B5.5 Heat-Flux Observable Integration Freeze 0.1: `STABLE`;
- F1.2 Admissible Input Geometry / Input-Cost Gate 0.1: `PASS / MASTER-INTEGRATED`;
- F1.2 Input Geometry / Input-Cost Integration Freeze 0.1: `STABLE — F1.3 RELEASED`.

## Fusion F1.2 result now frozen

For the closed anisotropic-ZLR four-moment R1 tangent state

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN,
\]

the admissible initial-condition geometry and cost are

\[
\boxed{B=I_4,\qquad R_{\rm in}=M_k,\qquad \operatorname{rank}(B)=4.}
\]

`B=I_4` means full closed tangent-state initial-condition admissibility; it is not an experimental actuator claim.

The instantaneous restricted heat channel is

\[
B^\dagger Q_{q_i,k}B=Q_{q_i,k},
\]

which for `k_y!=0` remains rank 2 and indefinite. Transport neutrality was not imposed.

Canonical F1.2 result:

`research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

MASTER integration freeze:

`research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`

F1.2 branch commit `8d555475577e77e93f9646df60343a34f0503525`; Python CI #316 = `SUCCESS`.

## Parallelism / parked branches

No parallel scientific branch is active.

- `MODES`: parked / conditional Fusion companion later;
- `CONT`: parked until a physical parameter family is frozen;
- `CASCADE`: parked;
- `CORE 0.2`: parked absent a concrete unresolved theorem question;
- Neuro and higher-fidelity Climate: parked;
- Power Grids and Photonics/Waves: `PROTECTED`;
- Paper-1 submission: parked.

## Selected dependency chain

1. B5.5 physical ion heat-flux derivation — **COMPLETE / FROZEN**;
2. F1.2 admissible input geometry / cost — **COMPLETE / FROZEN**;
3. F1.3 candidate / convention freeze — **READY**;
4. numerical/spectral qualification — blocked until F1.3 returns;
5. targeted exact-question Fusion literature audit;
6. pilot specification;
7. MASTER pilot freeze / one-shot execution;
8. result freeze;
9. later FLR/GK fidelity progression by physical validity, not effect size.

## Decision record

- base log through DEC-443;
- Addendum 0.1 through DEC-486;
- Addendum 0.2 through DEC-502.

## Rollback points

The protected post-paper rollback chain is now

\[
\text{Post-Paper Roadmap}
\rightarrow
\text{B5.5 Integration Freeze}
\rightarrow
\boxed{\text{F1.2 Input Geometry Integration Freeze}}.
\]

All first-paper savepoints remain separately protected.

## Active instruction

**Status:** `FUSION F1.2 INTEGRATED — F1.3 CANDIDATE / CONVENTION FREEZE READY / AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Branch status:**

`research/fusion/STATUS.md`

**Next instruction:**

`research/master/prompts/fusion_candidate_convention_freeze_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

Expected return state is one of:

- `F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION`;
- `F1.3 HOLD — RETURN TO MASTER FOR A SPECIFIC CONVENTION DECISION`;
- `F1.3 FAIL — RETURN TO MASTER`.

## STOP boundary

Do not perform finite-time Fusion optimization, horizon/parameter scans, FLR/GK extensions, numerical qualification, or parallel branch work before F1.3 returns. Do not reactivate submission work unless explicitly requested.

**STOP — AWAIT FUSION `GO`.**