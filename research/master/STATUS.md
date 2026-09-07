# MASTER Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

All first-paper savepoints remain intact and the submission track remains parked by user choice. Post-paper science remains focused on Fusion.

Stable first-paper lineage remains unchanged: CORE `STABLE`; Plasma `P2-A` frozen; Neuro `NEURO-STRONG` frozen; Climate-A `CLIM-WEAK` frozen; Climate-B `CLIM-B-FAIL` frozen; Manuscript Revision 0.4 `COMPLETE — PASS`; First Paper Scientific Content Freeze 0.1 `STABLE`.

Post-paper Fusion lineage now includes:

- R1 structural no-go / literature positioning: frozen;
- F2.1 two-species local-GK candidate/balance: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.2 local magnetic geometry / kinetic conventions: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.3 physical single point: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.4 kinetic input geometry / input cost: `PASS / MASTER-INTEGRATED / FROZEN`;
- F2.5 structure-preserving discretization specification: `PASS / MASTER-INTEGRATED / HISTORICAL FROZEN LADDER`;
- F2.6 `0_1`: `HOLD — ION-FLR CONVENTION CONFLICT`, historical audit record;
- F2.6 Ion-FLR Convention Clarification / Erratum 0.1: `STABLE — LOCAL-B CONVENTION`;
- resumed F2.6 `0_2`: `FAIL — FROZEN ION MAGNETIC-MOMENT QUADRATURE DOES NOT RESOLVE LOCAL-B FLR OVER FULL SUPPORT`, MASTER-integrated factual failure;
- Fusion F2.6 Discrete-Algebra Failure Integration Freeze 0.1: `STABLE — F2.5R RELEASED`.

## Frozen F2-R physical structure

Primary reduced candidate remains

\[
\boxed{\text{finite-ion-FLR electrostatic local-GK ions}+\text{collisionless bounce-averaged trapped electrons}}
\]

with leading adiabatic passing electrons and collisionless balance

\[
\boxed{\frac{dW}{dt}=G_\Gamma\Gamma+G_{T,i}q_i+G_{T,e}q_e^{\rm tr}}.
\]

The F2.3 benchmark point and F2.4 continuous input pair remain unchanged:

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),\qquad k_y\rho_{i0}=0.3,
\]

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}}.
\]

The controlling ion-FLR convention remains the MASTER local-B erratum:

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)=(k_\perp(\theta)\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

## F2.6 resumed failure

Canonical result:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_2.md`

Diagnostics:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`

Reproducible pre-spectral check:

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`

Branch commit `78db3e41c2cce29d505f13401f6f0878cb40f854`; Python CI #398 = `SUCCESS`.

The local-B convention ambiguity is resolved: representative `theta=0` and `theta=pi` checks pass. The remaining failure is numerical. On the historical F2.5 magnetic-moment orders

\[
N_\mu=8,12,16,
\]

the full-support relative error in the manufactured identity `Gamma0i=<J0i^2>` grows approximately as

\[
3.70\times10^{-4},\quad1.30\times10^{-2},\quad3.05\times10^{-1}
\]

for K0/K1/K2. The positive-Helmholtz versus `g`-form field-block defect likewise worsens, so the canonical complete F2.1 discrete balance cannot be certified on all three historical levels.

Other pre-spectral checks remain satisfactory: quasineutrality, basic Maxwellian moments, bounce quadrature, physical-channel Hermiticity, hydrogenic particle ambipolarity and reduced-electron ordering. No spectrum or finite-time effect has been inspected.

MASTER integration freeze:

`research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`

## Current dependency chain

1. R1 structural no-go / literature positioning — **COMPLETE / FROZEN**;
2. F2.1–F2.4 physical/balance/geometry/input freezes — **COMPLETE / FROZEN**;
3. historical F2.5 discretization ladder — **FROZEN AUDIT BASELINE**;
4. F2.6 `0_1` HOLD + local-B erratum — **COMPLETE / STABLE**;
5. resumed F2.6 `0_2` — **FAIL / MASTER-INTEGRATED**;
6. F2.5R ion-FLR magnetic-moment quadrature repair / discretization requalification — **READY**;
7. only after F2.5R PASS: MASTER may re-release F2.6 as a new versioned algebraic qualification;
8. spectral qualification only after a later F2.6 PASS;
9. finite-time pilot specification only after spectral qualification.

## MASTER repair decision

Only the ion Gauss--Laguerre magnetic-moment order `N_mu` is reopened. The representation family remains Gauss--Laguerre. F2.3, F2.4, all physical channel definitions, ballooning windows/basis, ion Hermite representation, trapped-electron representation, bounce quadrature and quasineutrality treatment remain frozen.

F2.5R must choose a new monotone K0/K1/K2 `N_mu` ladder using only predeclared local-B FLR manufactured-identity and positive-metric structural criteria. No spectral/effect information may enter the repair. If the Gauss--Laguerre family is not computationally/structurally defensible, F2.5R must return `HOLD` rather than change representation family silently.

## Parallelism / parked branches

Fusion is the only active scientific branch. Literature, MODES, CONT, CASCADE, CORE 0.2, Neuro extensions and higher-fidelity Climate remain parked. Power Grids and Photonics/Waves remain `PROTECTED`. Paper-1 submission remains parked.

No parallel science is opened during F2.5R. MODES is not required for this localized quadrature-resolution defect; CONT remains premature without an authorized physical parameter family.

## Decision record

Canonical continuation now reaches **DEC-600** in `research/master/decision_branch_log_addendum_0_12.md`.

## Rollback points

The latest protected post-paper savepoint is

\[
\boxed{\text{Fusion F2.6 Discrete-Algebra Failure Integration Freeze 0.1}}.
\]

Historical F2.5, F2.6 `0_1`, the ion-FLR erratum and F2.6 `0_2` remain preserved audit/rollback points.

## Active instruction

**Status:** `FUSION F2.5R ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIR READY — AWAIT FUSION GO`

**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

**Next instruction:**

`research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

Execute only in the Fusion branch via bare `GO` under the shared handoff protocol.

## STOP boundary

Do not rerun F2.6 directly, inspect spectra/eigenvalues/pseudospectra, construct propagators/Gramians/cumulative objectives, compute optimizers/angles/gaps, scan physical parameters, run GENE, add damping/collisions, retune F2.3/F2.4, alter any F2.5 object except the explicitly released ion `N_mu` orders, reopen R1 or open MODES/CONT/CASCADE/protected branches.

**STOP — AWAIT FUSION F2.5R `GO`.**
