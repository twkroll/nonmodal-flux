# Fusion F2.5R Ion-FLR Quadrature Repair Integration Freeze 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Status:** `STABLE — F2.5R PASS INTEGRATED / REPAIRED N_mu LADDER FROZEN / F2.6 0_3 RELEASED`

## Scope

This freeze integrates only the completed

`Fusion F2.5R — Ion-FLR Magnetic-Moment Quadrature Repair / Discretization Requalification Gate 0.1`.

Canonical branch result:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

Diagnostics:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_diagnostics_0_1.json`

Reproducible pre-spectral search:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_0_1.py`

Branch verdict:

\[
\boxed{\text{F2.5R PASS — ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIRED / LADDER FROZEN — RETURN TO MASTER}.}
\]

Branch commit:

`cbfd6ca9a906df7bb34bf6270a24b6c63857f545`

Python CI #405 = `SUCCESS`.

## Integrated repaired ladder

The historical F2.5 Gauss--Laguerre magnetic-moment orders

\[
N_\mu=(8,12,16)
\]

remain an immutable audit baseline that produced the F2.6 `0_2` failure. They are superseded for subsequent F2-R numerical work only by the F2.5R repaired ladder

\[
\boxed{
N_{\mu,K0}=16,\qquad
N_{\mu,K1}=24,\qquad
N_{\mu,K2}=40.
}
\]

The representation family remains Gauss--Laguerre. No other F2.5 object is reopened.

The repaired ion-state dimensions are

\[
\boxed{
N_i(K0,K1,K2)=(18176,\ 91584,\ 357120).
}
\]

The trapped-electron dimensions and all other K0/K1/K2 orders remain unchanged.

## Structural qualification integrated

The selected orders are the first passing candidates in the predeclared deterministic sequence

\[
\{8,12,16,20,24,28,32,40,48,56,64,80,96,112,128\}.
\]

On the active frozen LGL nodes, the maximum relative manufactured local-B FLR errors are approximately

\[
2.32\times10^{-12},\qquad
3.51\times10^{-11},\qquad
5.68\times10^{-15}
\]

for K0/K1/K2. The independent 257-point-per-element Chebyshev--Lobatto geometry envelope also passes, with maximum relative errors approximately

\[
3.04\times10^{-12},\qquad
4.01\times10^{-11},\qquad
6.44\times10^{-15}.
\]

The corresponding positive-Helmholtz versus `g`-form field-block diagnostics are below the predeclared structural tolerances on all levels. Selected Gauss--Laguerre weights remain positive, and Maxwellian density/energy/heat-weight moments remain at floating-point roundoff.

The repair therefore removes the specific ion-magnetic-moment resolution defect that caused F2.6 `0_2` to fail, without changing the continuous physics, the local-B FLR convention or any physical parameter.

## Frozen upstream objects preserved

The following remain unchanged and protected:

- F2.1 reduced two-species collisionless physical model and channel definitions;
- F2.2 circular `s-alpha` geometry and kinetic conventions;
- F2.3 CBC-compatible physical point;
- F2.4 input geometry and input cost,
  \[
  B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2};
  \]
- MASTER local-B ion-FLR erratum,
  \[
  b_i(\theta)=(k_\perp\rho_{i0})^2(B_0/B(\theta))^2,
  \qquad
  \Gamma_{0i}=I_0(b_i)e^{-b_i};
  \]
- K0/K1/K2 ballooning windows, theta basis, ion Hermite orders, trapped-electron representation, bounce quadrature, quasineutrality treatment and physical channel definitions;
- absence of damping, filtering, loading, clipping, hypercollision and physical-direction deletion.

No spectrum, eigenvector, propagator, Gramian, cumulative objective, optimizer, transport effect, physical parameter scan or GENE calculation entered the repair.

## MASTER consequence

The F2.5R repair is now frozen as the controlling ion magnetic-moment quadrature specification for subsequent F2-R work.

MASTER re-releases F2.6 as a new versioned pre-spectral algebraic qualification. The prior F2.6 `0_1` HOLD and `0_2` FAIL remain immutable audit records.

Canonical next handoff:

`research/master/prompts/fusion_f2_6_rerun_after_f2_5r_quadrature_repair_0_1.md`

The rerun must use the repaired `N_mu=(16,24,40)` ladder and create new `0_3` outputs. It may not inspect spectra or finite-time quantities.

## Rollback / STOP

This integration freeze is a new protected post-paper rollback point. Historical F2.5, F2.6 `0_1`, the local-B FLR erratum, F2.6 `0_2`, and the F2.6 failure-integration freeze remain preserved audit points.

**STOP — F2.5R REPAIR FROZEN / F2.6 0_3 MAY PROCEED ONLY THROUGH THE COMMITTED HANDOFF.**
