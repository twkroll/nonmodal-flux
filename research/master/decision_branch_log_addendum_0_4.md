# MASTER Decision & Branch Log — Addendum 0.4

**Date:** 2026-09-05  
**Base continuation:** `research/master/decision_branch_log_addendum_0_3.md` through DEC-510  
**Status:** `ACTIVE CANONICAL CONTINUATION`

## Fusion F1.4 integration / structural redirect

- **DEC-511:** `Fusion F1.4 — Numerical / Spectral Qualification Gate 0.1 = HOLD — MARGINAL SPECTRUM — RETURN TO MASTER` — BRANCH RESULT ACCEPTED AS QUALIFICATION OUTCOME.
- **DEC-512:** All required F1.4 algebraic/physical checks pass: positive `M_k`, Hermitian rank-2 indefinite `Q_q`, `B=I_4`, `R_in=M_k`, exact/roundoff free-energy balance, source-free `M_k`-skew-adjointness, physical heat-flux reconstruction, coordinate congruence and acceptable conditioning — STABLE NUMERICAL/STRUCTURAL QUALIFICATION.
- **DEC-513:** The exact frozen spectrum consists of four distinct purely imaginary eigenvalues; the frozen R1 point is marginal, diagonalizable, neither asymptotically stable nor clearly unstable. No damping or parameter retuning is permitted — FROZEN SPECTRAL CLASSIFICATION / ANTI-RETUNING.
- **DEC-514:** F1.4 branch commit `f2562061e79c67a5ccdc6a3d809ae0f655594319`; Python CI #330 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-515:** MASTER accepts the marginal collisionless R1 point only as a qualified structural/conservative control, not as a spectrally stable finite-time demonstration candidate — REGIME ACCEPTED WITH RESTRICTION.
- **DEC-516:** Applying the already-frozen CORE balance to the frozen R1 objects gives `2(R0/L_T) K_q(T) = E_M(T) - I` because `B=I_4`, `R_in=M_k` and no dissipation term is present. Hence cumulative ion-heat and final free-energy operators are affinely equivalent and have identical optimizer eigenspaces for every horizon — STABLE BRANCH-INDEPENDENT STRUCTURAL CONSEQUENCE.
- **DEC-517:** The intended R1 free-energy-optimal versus cumulative-ion-heat-optimal objective-separation pilot is BLOCKED: running optimizer-angle/performance-gap calculations would only reproduce the exact affine balance relation. R1 is retained as a no-go / structural-collapse baseline — FROZEN PROGRAM REDIRECT.
- **DEC-518:** `Fusion F1.4 Marginal / Structural Integration Freeze 0.1 = STABLE — F1.4 MARGINAL R1 QUALIFIED AS STRUCTURAL CONTROL / R1 OBJECTIVE-SEPARATION PILOT BLOCKED / LITERATURE AUDIT RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-519:** Next authorized task = `Fusion R1 Structural Redundancy & Fidelity-Breaking Literature Audit 0.1` in the Literature branch. It must position the exact R1 structural collapse and determine which physically justified fidelity additions alter the free-energy balance by independent supply channels and/or positive dissipation, without selecting models for expected effect size — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-520:** Canonical handoff = `research/master/prompts/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`. Fusion waits while Literature executes. No finite-time Fusion objective calculation, R1 retuning, FLR/GK execution, MODES/CONT/CASCADE work, protected collaboration work or Paper-1 submission reactivation is authorized before the audit returns — ACTIVE / FROZEN PARALLELISM RULE.
