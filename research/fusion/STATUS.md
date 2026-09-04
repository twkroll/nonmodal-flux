# Fusion Branch Status

**Last updated:** 2026-09-04  
**Branch:** `main`

## Current state

The post-paper roadmap selected

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}
\]

as the next scientific program. The first-paper scientific content remains frozen and is not part of this branch.

B5.5 is complete and MASTER-integrated. The physical signed ion radial heat/thermal-energy flux for the anisotropic-ZLR four-moment R1 reduction has been derived independently from radial `E×B` transport:

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\qquad Q_{q_i,k}=Q_{q_i,k}^\dagger.
\]

For

\[
z_k=(N,U,P_\parallel,P_\perp)^T,
\qquad \Phi=\mathcal C_kN,
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

It is rank 2 and indefinite for `k_y != 0`, and the same instantaneous physical operator applies to the slab and minimal-curvature R1 generators.

The independent physical derivation satisfies the frozen energetic balance exactly:

\[
A_k^\dagger M_k+M_kA_k
=2\left(-\frac{d\ln T_{i0}}{dx}\right)\frac{Q_{q_i,k}}{p_0},
\]

or, with

\[
W_k=\frac{p_0}{2}z_k^\dagger M_kz_k,
\]

\[
\frac{dW_k}{dt}
=-\frac{d\ln T_{i0}}{dx}\,q_{i,k}.
\]

The ion particle-flux channel remains collapsed under the same frozen adiabatic-electron closure:

\[
Q_{\Gamma_i,k}=0.
\]

Canonical B5.5 result:

`research/fusion/B5_5_ion_heat_flux_observable.md`

MASTER integration freeze:

`research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`

B5.5 commit `d4d72d02cfdacb383091d24348d6f8966a49d723` passed Python CI #309.

## Active instruction

**Status:** `FUSION F1.2 ADMISSIBLE INPUT GEOMETRY / INPUT-COST GATE READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_admissible_input_geometry_input_cost_gate_0_1.md`

On a bare `GO`, first read this STATUS and then execute only that committed instruction.

## F1.2 scope

Determine, independently of all finite-time objective-separation effects, the physically admissible initial-perturbation map `B` and positive input-cost metric `R_in` for the frozen R1 state/channel.

The gate must explicitly test whether full-state initial-condition admissibility with `B=I` and free-energy cost `R_in=M_k` is physically justified; if not, derive the minimal physically motivated lower-rank geometry. Transport neutrality must not be forced for mathematical convenience.

## Forbidden until F1.2 returns

Do not compute finite-time energy/heat operators, cumulative extrema, optimizer directions, angles, performance gaps, horizon dependence or parameter scans. Do not restore FLR, kinetic electrons, six-moment GEM or GENE. Do not change `M_k` or `Q_{q_i,k}` to make an input geometry convenient. Do not open Power Grid/Photonics collaboration work or modify the frozen first paper.

## Expected return state

One of:

- `F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE`;
- `F1.2 HOLD — RETURN TO MASTER FOR INPUT-GEOMETRY DECISION`;
- `F1.2 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Governance authority

- `research/master/first_paper_scientific_content_freeze_0_1.md`
- `research/master/post_paper_scientific_roadmap_gate_0_1.md`
- `research/master/fusion_b5_5_heat_flux_observable_integration_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**