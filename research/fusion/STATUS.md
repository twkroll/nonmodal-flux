# Fusion Branch Status

**Last updated:** 2026-09-06  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit, F2.1, F2.2, F2.3, F2.4 and F2.5 are complete and MASTER-integrated.

F2.6 `0_1` returned `HOLD` before any spectral work. MASTER has now resolved the single blocking ion-FLR convention and re-released F2.6 through a versioned resumption handoff.

## Frozen upstream lineage

The primary reduced F2-R candidate remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons, the frozen circular `s-alpha` ballooning geometry, the frozen F2.3 CBC-compatible point, and

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The F2.5 K0/K1/K2 discretization ladder remains frozen and may not be retuned.

## Historical F2.6 HOLD record

Canonical HOLD report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

Historical diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_1.json`

The HOLD localized one conflict: local ion gyroaveraging with `Omega_i(theta)` had been paired with a reference-`B0` polarization argument.

F2.6 HOLD commit `ef5a20e728a5a6ca0dfb1cd2cd012f4003a4c0f1`; Python CI #385 = `SUCCESS`.

## MASTER ion-FLR erratum

Controlling clarification:

`research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`

The reference normalization remains

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
k_y\rho_{i0}=0.3.
\]

The already-frozen local gyroaverage remains

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right).
\]

The controlling polarization/free-energy convention is now

\[
\boxed{
 b_i(\theta)
 =(k_\perp(\theta)\rho_{i0})^2
 \left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

Equivalently, `rho_i(theta)=rho_i0 B0/B(theta)`. This is a narrow convention erratum only: F2.3 parameters, F2.4 input geometry and F2.5 K0/K1/K2 architecture remain unchanged.

Historical frozen files are not overwritten; the MASTER erratum supersedes only the inconsistent varying-`B` implementation reading of `b_i` for subsequent work.

## Active instruction

**Status:** `FUSION F2.6 RESUMPTION AFTER ION-FLR ERRATUM READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.6 resumption scope

On the unchanged K0/K1/K2 ladder, rebuild all FLR-dependent discrete objects with the local-B `b_i(theta)`, re-run the manufactured FLR identity and complete the original pre-spectral algebraic qualification: quasineutrality, `M_K>0`, `B_K=I`, `R_in,K=M_K`, physical-channel Hermiticity, ambipolarity, conservative phase-space adjoint/skew structure and the complete F2.1 discrete free-energy balance.

Create versioned `0_2` result and diagnostic files; do not overwrite the historical HOLD files.

## Forbidden until F2.6 returns again

Do not inspect eigenvalues, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not scan parameters or resolutions beyond K0/K1/K2, run GENE, add collisions/damping, retune F2.3, alter F2.4/F2.5, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`
- `research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`
- `research/master/fusion_f2_5_discretization_specification_integration_freeze_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / AWAIT GO.**
