# MASTER Decision & Branch Log — Addendum 0.2

**Date:** 2026-09-04  
**Base continuation:** `research/master/decision_branch_log_addendum_0_1.md` through DEC-486  
**Status:** `ACTIVE CANONICAL CONTINUATION`

This addendum continues the decision record without rewriting the historical base log or Addendum 0.1.

## Fusion B5.5 / F1.2 release

- **DEC-487:** `Fusion B5.5 — Physical ion radial heat-flux observable = PASS — PHYSICAL ION HEAT-FLUX OPERATOR DERIVED AND BALANCE-CONSISTENT` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-488:** For frozen R1 state `z_k=(N,U,P_parallel,P_perp)^T`, the physical signed ion heat-flux operator `Q_{q_i,k}` derived independently from radial `E×B` thermal transport, including sign, normalization, Fourier convention and anisotropic thermal combination, is now FROZEN for the R1 lineage — STABLE.
- **DEC-489:** `Q_{q_i,k}` is Hermitian, rank 2 and indefinite for `k_y!=0`; the same instantaneous physical operator applies to the slab and minimal-curvature R1 generators. Under the same frozen adiabatic-electron closure, `Q_{Gamma_i,k}=0` remains a physical restriction and may not be repaired merely to create a multichannel effect — FROZEN PHYSICAL SEMANTICS.
- **DEC-490:** The independently derived heat-flux operator reproduces the previously derived R1 free-energy injection identity exactly, equivalently `dW_k/dt=-(d ln T_i0/dx) q_{i,k}` — STABLE ENERGETIC CONSISTENCY CHECK.
- **DEC-491:** B5.5 commit `d4d72d02cfdacb383091d24348d6f8966a49d723`; Python CI #309 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-492:** `Fusion B5.5 Heat-Flux Observable Integration Freeze 0.1 = STABLE — B5.5 PHYSICAL CHANNEL FROZEN / F1.2 RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-493:** Next authorized scientific gate = `Fusion F1.2 — Admissible Input Geometry / Input-Cost Gate 0.1`; it may determine physical `B` and positive `R_in`, classify the instantaneous restricted channel `B^dagger Q B`, and test full-state versus lower-rank admissibility, but may not inspect any finite-time objective separation — SATISFIED / CLOSED.
- **DEC-494:** Canonical F1.2 handoff = `research/master/prompts/fusion_admissible_input_geometry_input_cost_gate_0_1.md`; no MODES/CONT/CASCADE or other parallel scientific branch was opened before F1.2 returned — SATISFIED / CLOSED.

## Fusion F1.2 integration / F1.3 release

- **DEC-495:** `Fusion F1.2 — Admissible Input Geometry / Input-Cost Gate 0.1 = PASS` — STABLE PRE-EFFECT SCIENTIFIC SAVEPOINT.
- **DEC-496:** The full already-closed R1 tangent state is the admissible initial-condition ensemble; the electrostatic closure reconstructs `Phi` from `N` and imposes no additional linear constraint among `(N,U,P_parallel,P_perp)` — FROZEN STATE-GEOMETRY INTERPRETATION.
- **DEC-497:** `B=I_4`, `R_in=M_k`, and `rank(B)=4` are frozen for the R1 initial-condition problem. `B=I_4` is not a claim of four independent laboratory actuators — FROZEN PHYSICAL SEMANTICS.
- **DEC-498:** `B^dagger Q_{q_i,k} B = Q_{q_i,k}` remains rank 2 and indefinite for `k_y!=0`; transport neutrality was not imposed and must not be introduced retrospectively for mathematical convenience — FROZEN INPUT-CHANNEL GEOMETRY.
- **DEC-499:** F1.2 branch commit `8d555475577e77e93f9646df60343a34f0503525`; Python CI #316 = `SUCCESS` — STABLE REPRODUCIBILITY CHECK.
- **DEC-500:** `Fusion F1.2 Input Geometry / Input-Cost Integration Freeze 0.1 = STABLE — F1.2 INPUT GEOMETRY FROZEN / CANDIDATE-CONVENTION FREEZE RELEASED` — NEW POST-PAPER ROLLBACK POINT.
- **DEC-501:** Next authorized task = `Fusion F1.3 — Candidate / Convention Freeze 0.1`. The intended primary candidate is the anisotropic-ZLR four-moment R1 minimal-curvature branch if the frozen derivation chain remains internally consistent; the slab branch remains an analytic/limiting control. Selection may not use finite-time effect size — ACTIVE SCIENTIFIC HANDOFF.
- **DEC-502:** Canonical F1.3 handoff = `research/master/prompts/fusion_candidate_convention_freeze_0_1.md`. No finite-time optimization, FLR/GK extension, MODES/CONT/CASCADE work, or protected collaboration branch is authorized before F1.3 returns — ACTIVE / FROZEN PARALLELISM RULE.
