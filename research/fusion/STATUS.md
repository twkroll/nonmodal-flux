# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. F2.5 remains the historical discretization specification; F2.5R now supplies one narrow superseding repair for its ion magnetic-moment quadrature order.

F2.6 `0_1` historically returned HOLD on an ion-FLR convention conflict. MASTER resolved that conflict through the local-B ion-FLR erratum. F2.6 `0_2` then returned FAIL before any spectral work because the historical F2.5 `N_mu=8/12/16` ladder did not resolve the corrected full-support local-B FLR identity.

MASTER released F2.5R to repair only that numerical object.

## Controlling physical / FLR objects

The F2-R physical model, F2.3 point and F2.4 input geometry remain frozen.

The controlling ion-FLR convention is

\[
\rho_{i0}=v_{Ti}/\Omega_i(B_0),
\qquad
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\]

\[
\boxed{
b_i(\theta)
=(k_\perp(\theta)\rho_{i0})^2
\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
}
\]

No physical parameter or input-space change has been made.

## F2.5R completed repair

Canonical result:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_diagnostics_0_1.json`

Reproducible pre-spectral search:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_0_1.py`

**Status:** `F2.5R PASS — ION-FLR MAGNETIC-MOMENT QUADRATURE REPAIRED / LADDER FROZEN — RETURN TO MASTER`

The deterministic predeclared candidate sequence was

\[
N_\mu\in\{8,12,16,20,24,28,32,40,48,56,64,80,96,112,128\}.
\]

Using the active frozen LGL nodes plus an independent 257-point Chebyshev--Lobatto geometry envelope per `pi` element, the smallest passing monotone ladder is

\[
\boxed{
N_{\mu,K0}=16,\qquad
N_{\mu,K1}=24,\qquad
N_{\mu,K2}=40.
}
\]

The selected full-support active-node FLR errors are:

| level | max abs | max relative | field Fro/C | field local/C |
|---|---:|---:|---:|---:|
| K0 | `5.209e-13` | `2.320e-12` | `1.615e-14` | `2.604e-13` |
| K1 | `4.587e-12` | `3.508e-11` | `1.115e-13` | `2.293e-12` |
| K2 | `6.939e-16` | `5.684e-15` | `1.209e-16` | `3.469e-16` |

The independent between-node envelope also passes at all levels, with maximum relative errors approximately

\[
3.04\times10^{-12},\qquad
4.01\times10^{-11},\qquad
6.44\times10^{-15}.
\]

All selected Gauss--Laguerre weights remain positive and Maxwellian density/energy/heat-weight moments remain at floating-point roundoff.

The repaired ion-state dimensions are

\[
\boxed{
N_i(K0,K1,K2)=(18176,\ 91584,\ 357120).
}
\]

All other F2.5 objects remain unchanged. Historical F2.5 and F2.6 files remain immutable audit records.

No spectrum, eigenvector, propagator, Gramian, finite-time objective, optimizer, transport effect or GENE result was inspected.

## Active instruction

**Next instruction:** none in this branch.

A bare `GO` must not rerun F2.6, open spectral qualification, or begin finite-time work until MASTER integrates F2.5R and commits an explicit new handoff.

## Forbidden while RETURN TO MASTER remains

Do not inspect eigenvalues, growth rates, pseudospectra, eigenvectors, propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not change F2.3/F2.4 or any F2.5 object other than the now-frozen F2.5R `N_mu` repair. Do not run GENE, add collisions/damping, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Governance authority

- `research/master/fusion_f2_6_discrete_algebra_failure_integration_freeze_0_1.md`
- `research/master/prompts/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`
- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`

**STOP / RETURN TO MASTER.**
