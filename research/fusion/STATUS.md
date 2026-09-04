# Fusion Branch Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

The post-paper roadmap selected

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

as the active scientific program. The first-paper scientific content remains frozen and the submission track remains parked.

B5.5 is complete and MASTER-integrated: the physical signed ion radial heat/thermal-energy flux `Q_{q_i,k}` is frozen and balance-consistent. F1.2 is also complete and MASTER-integrated.

## Frozen F1.2 input geometry / cost

For the closed anisotropic-ZLR four-moment R1 tangent state

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN,
\]

the admissible initial-condition ensemble is the full retained tangent state, with

\[
\boxed{B=I_4,\qquad R_{\rm in}=M_k,\qquad \operatorname{rank}(B)=4.}
\]

`B=I_4` is a state-space initial-condition statement, not a claim of four independent laboratory actuators. The frozen positive input cost is the perturbation free-energy metric `M_k`.

The instantaneous restricted heat channel remains

\[
B^\dagger Q_{q_i,k}B=Q_{q_i,k},
\]

rank 2 and indefinite for `k_y!=0`. Transport neutrality was not imposed.

Canonical F1.2 result:

`research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

MASTER F1.2 integration freeze:

`research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`

F1.2 commit `8d555475577e77e93f9646df60343a34f0503525`; Python CI #316 = `SUCCESS`.

## Active instruction

**Status:** `FUSION F1.3 CANDIDATE / CONVENTION FREEZE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_candidate_convention_freeze_0_1.md`

On a bare `GO`, first read this STATUS and execute only that committed instruction.

## F1.3 scope

Freeze one exact reduced candidate and all source/normalization/geometry/closure/parameter conventions needed for the subsequent numerical/spectral qualification, using only pre-effect physical and structural criteria.

The intended primary candidate is the already-derived anisotropic-ZLR four-moment R1 **minimal-curvature** branch if the derivation chain remains internally consistent. The slab branch remains an analytic/limiting control.

## Forbidden until F1.3 returns

Do not compute finite-time energy/heat operators, cumulative extrema, optimizer vectors/subspaces, principal angles, performance gaps, horizon dependence or effect-guided parameter scans. Do not restore FLR, kinetic electrons, six-moment GEM or GENE. Do not open MODES/CONT/CASCADE or protected Power Grid/Photonics work. Do not modify the frozen first paper.

## Expected return state

One of:

- `F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION`;
- `F1.3 HOLD — RETURN TO MASTER FOR A SPECIFIC CONVENTION DECISION`;
- `F1.3 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`
- `research/master/fusion_f1_2_input_geometry_integration_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**