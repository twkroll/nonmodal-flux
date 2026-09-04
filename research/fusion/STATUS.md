# Fusion Branch Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

The post-paper roadmap selected

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

as the next scientific program. The first-paper scientific content remains frozen and is not part of this branch.

B5.5 is complete and MASTER-integrated. The physical signed ion radial heat/thermal-energy flux for the anisotropic-ZLR four-moment R1 reduction remains frozen as

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad Q_{q_i,k}=Q_{q_i,k}^\dagger,
\]

for

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN.
\]

The ion particle-flux channel remains collapsed under the same frozen adiabatic-electron closure:

\[
Q_{\Gamma_i,k}=0.
\]

## F1.2 completed result

Fusion F1.2 — Admissible Input Geometry / Input-Cost Gate 0.1 is complete.

The physically admissible state-space interpretation is the full already-closed R1 tangent state, not a claim of arbitrary laboratory actuation. The electrostatic relation

\[
\Phi=\mathcal C_kN,
\qquad \mathcal C_k>0,
\]

reconstructs the potential from `N` and imposes no additional linear relation among the four retained moment coordinates.

The selected input geometry and cost are

\[
\boxed{
B=I_4,
\qquad
R_{\rm in}=M_k,
\qquad
\operatorname{rank}(B)=4.
}
\]

Here `M_k` is the already-frozen positive perturbation free-energy metric, so

\[
R_{\rm in}=R_{\rm in}^\dagger\succ0.
\]

The instantaneous restricted physical heat channel is not forced neutral:

\[
B^\dagger Q_{q_i,k}B=Q_{q_i,k},
\]

which for `k_y!=0` remains rank 2 and indefinite with signature `(1,1,2)`.

The same `B,R_in` interpretation applies to both the slab and minimal-curvature R1 generators because they share the same state coordinates, electrostatic closure, free-energy metric and instantaneous physical heat-flux channel.

Canonical F1.2 result:

`research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

## Active instruction

**Status:** `F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE`

**Next instruction:** none in this branch.

A bare `GO` must not open a new scientific task while this status remains `RETURN TO MASTER`. MASTER must issue and commit any later handoff explicitly.

## Forbidden until MASTER returns a new committed handoff

Do not compute finite-time energy/heat operators, cumulative extrema, optimizer directions, angles, performance gaps, horizon dependence or parameter scans. Do not restore FLR, kinetic electrons, six-moment GEM or GENE. Do not reinterpret `B=I_4` as a laboratory actuator claim. Do not change `M_k` or `Q_{q_i,k}`. Do not open Power Grid/Photonics collaboration work or modify the frozen first paper.

## Expected MASTER action

If MASTER accepts the F1.2 result, the roadmap-designated next stage is the Fusion candidate/convention freeze. This branch does not self-authorize that gate.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`
- `research/master/prompts/fusion_admissible_input_geometry_input_cost_gate_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**