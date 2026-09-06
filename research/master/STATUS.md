# MASTER Status

**Last updated:** 2026-09-06  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage remains unchanged: CORE `STABLE`; Plasma `P2-A` frozen; Neuro `NEURO-STRONG` frozen; Climate-A `CLIM-WEAK` frozen; Climate-B `CLIM-B-FAIL` frozen; Manuscript Revision 0.4 `COMPLETE — PASS`; First Paper Scientific Content Freeze 0.1 `STABLE`.

Post-paper Fusion lineage now includes:

- R1 structural no-go / literature positioning: frozen;
- F2.1 two-species local-GK candidate/balance specification: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.2 local magnetic-geometry family / kinetic convention freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.3 physical geometry/gradient/wavenumber single-point freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.4 kinetic admissible input geometry / input-cost freeze: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.5 structure-preserving discretization / quadrature specification: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.6 `0_1`: `HOLD — ION-FLR CONVENTION CONFLICT`, integrated as a factual pre-spectral HOLD;
- Fusion F2.6 Ion-FLR Convention Clarification / Erratum 0.1: `STABLE — LOCAL-B CONVENTION SELECTED / F2.6 RESUMPTION RELEASED`.

## Frozen F2-R architecture and balance

Primary reduced candidate:

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons. The reduced collisionless balance remains

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The R1 affine redundancy is not structurally forced in F2-R, but no finite-time F2 objective separation has been inspected.

## Frozen physical point / input geometry / numerical ladder

The F2.3 single CBC-compatible point remains unchanged and may not be retuned. In particular the reference ion normalization remains

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
\boxed{k_y\rho_{i0}=0.3}.
\]

The continuous input pair remains

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The F2.5 numerical package and predeclared K0/K1/K2 ladder remain frozen exactly as before. No basis, cutoff, quadrature or resolution has been changed after the F2.6 HOLD.

## F2.6 HOLD and MASTER FLR resolution

Historical HOLD report:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`

Historical diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_1.json`

F2.6 localized one convention conflict: the frozen local gyroaverage

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right)
\]

had been paired with a reference-`B0` polarization argument `b_i=(k_perp rho_i0)^2`. K0/K1/K2 manufactured checks showed that this does not satisfy the Maxwellian identity away from `B(theta)=B0`; the mismatch is not a quadrature/convergence error.

MASTER selects the local-B convention in

`research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`:

\[
\boxed{
\rho_i(\theta)=\rho_{i0}\frac{B_0}{B(\theta)},
\qquad
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

The local `J0i` is retained. The alternative reference-`B0` gyroaverage is rejected. This is a narrow implementation/convention erratum, not a retuning of F2.3 or a change to F2.4/F2.5.

F2.6 HOLD commit `ef5a20e728a5a6ca0dfb1cd2cd012f4003a4c0f1`; Python CI #385 = `SUCCESS`.

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1 candidate/balance — **COMPLETE / FROZEN**;
3. F2.2 geometry/conventions — **COMPLETE / FROZEN**;
4. F2.3 physical single point — **COMPLETE / FROZEN**;
5. F2.4 kinetic input geometry / input cost — **COMPLETE / FROZEN**;
6. F2.5 structure-preserving discretization / quadrature specification — **COMPLETE / FROZEN**;
7. F2.6 `0_1` pre-spectral algebraic qualification — **HOLD INTEGRATED**;
8. ion-FLR convention erratum — **COMPLETE / STABLE**;
9. F2.6 resumed algebraic qualification under corrected local-B FLR — **READY**;
10. later numerical/free-energy/spectral qualification only after F2.6 PASS;
11. only then a pre-effect finite-time pilot specification/freeze;
12. fully kinetic/GENE-compatible reference validation through separately released gates.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel scientific branch is opened while F2.6 completes the corrected discrete physical algebra. MODES remains conditional on a concrete representation/reduction problem after a qualified high-dimensional operator exists; CONT remains premature without an authorized parameter family.

## Decision record

Canonical continuation now reaches **DEC-590** in `research/master/decision_branch_log_addendum_0_11.md`.

## Rollback points

The latest protected post-paper savepoint is

\[
\boxed{\text{Fusion F2.6 Ion-FLR Convention Clarification / Erratum 0.1}}.
\]

The prior F2.5 integration freeze and the historical F2.6 HOLD record remain preserved rollback/audit points.

## Active instruction

**Status:** `FUSION F2.6 RESUMPTION AFTER ION-FLR ERRATUM READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not inspect eigenvalues/growth rates/pseudospectra, construct finite-time propagators/Gramians/cumulative objectives, compute optimizers/angles/gaps, scan parameters, run GENE, add damping/collisions, change F2.3/F2.4/F2.5 freezes, reopen R1/FLR-only rescue or open MODES/CONT/CASCADE/protected branches. Paper-1 submission remains parked unless explicitly reactivated.

**STOP — AWAIT FUSION `GO`.**
