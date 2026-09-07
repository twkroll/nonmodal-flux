# MASTER Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage remains unchanged: CORE `STABLE`; Plasma `P2-A` frozen; Neuro `NEURO-STRONG` frozen; Climate-A `CLIM-WEAK` frozen; Climate-B `CLIM-B-FAIL` frozen; Manuscript Revision 0.4 `COMPLETE — PASS`; First Paper Scientific Content Freeze 0.1 `STABLE`.

Post-paper Fusion lineage now includes:

- R1 structural no-go / literature positioning: frozen;
- F2.1–F2.4 physical/balance/geometry/input freezes: `PASS / MASTER-INTEGRATED / FROZEN`;
- historical F2.5 discretization specification: `PASS / FROZEN AUDIT BASELINE`;
- F2.6 `0_1`: `HOLD — ION-FLR CONVENTION CONFLICT`, historical audit record;
- F2.6 Ion-FLR Convention Clarification / Erratum 0.1: `STABLE — LOCAL-B CONVENTION`;
- F2.6 `0_2`: `FAIL — HISTORICAL N_mu LADDER DOES NOT RESOLVE FULL-SUPPORT LOCAL-B FLR`, MASTER-integrated factual failure;
- F2.5R ion-FLR magnetic-moment quadrature repair: `PASS / MASTER-INTEGRATED / FROZEN`;
- Fusion F2.5R Ion-FLR Quadrature Repair Integration Freeze 0.1: `STABLE — F2.6 0_3 RELEASED`.

## Frozen F2-R physical structure

Primary reduced candidate remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons and collisionless balance

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 benchmark point and F2.4 input pair remain unchanged:

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),\qquad k_y\rho_{i0}=0.3,
\]

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The controlling local-B ion-FLR convention remains

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.}
\]

## F2.5R repaired numerical ladder

Historical F2.5 `N_mu=8/12/16` remains an immutable audit baseline. The controlling F2.5R ion Gauss--Laguerre magnetic-moment orders for subsequent F2-R work are

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5 objects remain unchanged. The repaired ion-state dimensions are

\[
\boxed{N_i(K0,K1,K2)=(18176,\ 91584,\ 357120).}
\]

The selected orders are the first passing values in the predeclared candidate sequence and pass active-node plus independent between-node local-B FLR manufactured criteria and positive-metric field-block tolerances. Maximum active-node relative FLR errors are approximately `2.32e-12 / 3.51e-11 / 5.68e-15`; the independent envelope gives approximately `3.04e-12 / 4.01e-11 / 6.44e-15`.

F2.5R branch commit `cbfd6ca9a906df7bb34bf6270a24b6c63857f545`; Python CI #405 = `SUCCESS`.

Canonical result:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

MASTER savepoint:

`research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`

No spectrum or finite-time quantity was inspected during the repair.

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1–F2.4 — **COMPLETE / FROZEN**;
3. historical F2.5 — **FROZEN AUDIT BASELINE**;
4. F2.6 `0_1` HOLD + local-B erratum — **COMPLETE / STABLE**;
5. F2.6 `0_2` — **FAIL / MASTER-INTEGRATED HISTORICAL RECORD**;
6. F2.5R quadrature repair — **PASS / MASTER-INTEGRATED / FROZEN**;
7. F2.6 `0_3` discrete operator/channel algebraic qualification on repaired ladder — **READY**;
8. numerical/free-energy/spectral qualification only after F2.6 PASS;
9. finite-time pilot specification only after spectral qualification.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel science is opened during F2.6 `0_3`. MODES remains conditional on a concrete representation/reduction problem after a qualified high-dimensional operator exists; CONT remains premature without an authorized physical parameter family.

## Decision record

Canonical continuation now reaches **DEC-610** in `research/master/decision_branch_log_addendum_0_13.md`.

## Rollback points

The latest protected post-paper savepoint is

\[
\boxed{\text{Fusion F2.5R Ion-FLR Quadrature Repair Integration Freeze 0.1}}.
\]

Historical F2.5, F2.6 `0_1`, the ion-FLR erratum, F2.6 `0_2` and the F2.6 failure-integration freeze remain preserved audit/rollback points.

## Active instruction

**Status:** `FUSION F2.6 0_3 DISCRETE OPERATOR / CHANNEL ALGEBRAIC QUALIFICATION READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_6_rerun_after_f2_5r_quadrature_repair_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not inspect spectra/eigenvalues/pseudospectra, construct propagators/Gramians/cumulative objectives, compute optimizers/angles/gaps, scan physical parameters, run GENE, add damping/collisions, retune F2.3/F2.4, change the repaired F2.5R ladder or any other F2.5 object, reopen R1 or open MODES/CONT/CASCADE/protected branches.

**STOP — AWAIT FUSION F2.6 0_3 `GO`.**
