# MASTER Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

All first-paper scientific and manuscript savepoints remain intact:

- CORE Mathematical / Integration / Interpretation freezes: `STABLE`;
- Plasma/D10-ZF: `P2-A`, `FROZEN`;
- Neuro/CMC: `NEURO-STRONG`, `FROZEN`;
- Climate-A/Phillips-QG: `CLIM-WEAK`, `FROZEN`;
- Climate-B/Bickley jet: `CLIM-B-FAIL — resolution robustness failure`, `RESULT FROZEN`;
- Cross-Domain Result / Literature / Claim freezes: `STABLE/COMPLETE`;
- Manuscript Structure Freeze 0.2: `STABLE`;
- Manuscript Revision 0.4: `COMPLETE — PASS`;
- Submission Readiness Gate 0.1: `PASS WITH AUTHOR/METADATA ITEMS — SCIENTIFIC PACKAGE READY`;
- First Paper Scientific Content Freeze 0.1: `STABLE — SCIENTIFIC CONTENT BASELINE FROZEN / SUBMISSION TRACK PARKED`;
- Post-Paper Scientific Roadmap Gate 0.1: `COMPLETE — FUSION-F1 SELECTED`;
- Fusion B5.5 physical ion heat-flux observable: `PASS`;
- Fusion B5.5 Heat-Flux Observable Integration Freeze 0.1: `STABLE — PHYSICAL CHANNEL FROZEN / F1.2 RELEASED`.

## Paper-1 publication status

Primary journal target remains `Physical Review E — Regular Article`, with Chaos and Physical Review Research as backups.

The submission track remains **PARKED by explicit user choice**. Draft 0.4 is the scientific-content baseline, not final prose. No portal, cover-letter, author-list, OA/APC, DOI/release/license or production-formatting task is active.

## Post-paper primary scientific program

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The intended hierarchy remains

\[
\text{anisotropic ZLR four-moment gyrofluid}
\rightarrow
\text{FLR gyrofluid}
\rightarrow
\text{parallel/flux-tube or local gyrokinetic/GENE-compatible validation}.
\]

No finite-time objective-separation effect has yet been authorized.

## B5.5 result now integrated

The R1 physical ion radial heat/thermal-energy channel is now independently frozen as

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad
Q_{q_i,k}=Q_{q_i,k}^\dagger,
\]

with frozen state

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad
\Phi=\mathcal C_kN,
\]

and

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

For `k_y!=0`, the operator is rank 2 and indefinite. The same physical instantaneous channel applies to slab and minimal-curvature R1 generators.

The physical derivation satisfies the earlier free-energy balance exactly:

\[
A_k^\dagger M_k+M_kA_k
=2\left(-\frac{d\ln T_{i0}}{dx}\right)\frac{Q_{q_i,k}}{p_0},
\]

or

\[
\frac{dW_k}{dt}
=-\frac{d\ln T_{i0}}{dx}\,q_{i,k}.
\]

The ion particle-flux channel remains collapsed under the same frozen adiabatic-electron closure:

\[
Q_{\Gamma_i,k}=0.
\]

This restriction is physical for the R1 closure and may not be changed simply to obtain a richer objective geometry.

Canonical branch result:

`research/fusion/B5_5_ion_heat_flux_observable.md`

MASTER integration freeze:

`research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`

B5.5 commit `d4d72d02cfdacb383091d24348d6f8966a49d723` passed Python CI #309.

## Parallelism / parked branches

No immediate parallel scientific branch is active.

- `MODES`: preferred conditional companion only if a later qualified Fusion operator makes reduction/representation robustness concrete;
- `CONT`: parked until a physical parameter family is frozen;
- `CASCADE`: parked;
- `CORE 0.2`: parked absent a concrete new structural hypothesis;
- delayed/higher-fidelity Neuro: parked;
- higher-fidelity Climate: parked; Climate-B repair/third-candidate rescue remains forbidden;
- Power Grids: `PROTECTED` collaboration branch;
- Photonics/Waves: `PROTECTED` collaboration branch;
- Manuscript/submission: parked.

## Selected dependency chain

1. B5.5 physical ion heat-flux observable derivation — **COMPLETE / FROZEN**;
2. admissible-input geometry / input-cost gate — **READY**;
3. Fusion candidate/convention freeze;
4. numerical/spectral qualification with no finite-time effect inspection;
5. targeted exact-question Fusion literature-positioning audit after candidate/channel freeze;
6. pilot specification;
7. MASTER pilot freeze / one-shot execution release;
8. execution and result freeze;
9. later FLR and gyrokinetic fidelity progression based on physical/structural validity, not effect size.

## Decision record

- base: `research/master/decision_branch_log.md` through DEC-443;
- continuation 0.1: `research/master/decision_branch_log_addendum_0_1.md` through DEC-486;
- continuation 0.2: `research/master/decision_branch_log_addendum_0_2.md` through DEC-494.

## Rollback points

The protected chain includes the complete first-paper lineage through `First Paper Scientific Content Freeze 0.1`, the post-paper roadmap savepoint, and now

\[
\boxed{\text{Fusion B5.5 Heat-Flux Observable Integration Freeze 0.1}}.
\]

New Fusion work may reuse this frozen physical channel but may not silently rewrite it or Paper 1.

## Active instruction

**Status:** `FUSION B5.5 INTEGRATED — F1.2 INPUT GEOMETRY / INPUT COST READY / AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Branch status:**

`research/fusion/STATUS.md`

**Next instruction:**

`research/master/prompts/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

Expected return state is one of:

- `F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE`;
- `F1.2 HOLD — RETURN TO MASTER FOR INPUT-GEOMETRY DECISION`;
- `F1.2 FAIL — RETURN TO MASTER`.

## STOP boundary

Do not perform finite-time Fusion optimization, parameter/horizon scans, FLR/GK extensions, or parallel branch work before F1.2 returns. Do not reactivate submission work unless explicitly requested by the user.

**STOP — AWAIT FUSION `GO`.**