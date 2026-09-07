# Fusion Branch Status

**Last updated:** 2026-09-07  
**Branch:** `main`

## Current state

The active post-paper program remains

\[
\boxed{\text{FUSION-F1 — fusion heat-transport optimality ladder}}.
\]

The first-paper scientific content remains frozen and submission remains parked.

B5.5, F1.2, F1.3, F1.4, the R1 literature audit and F2.1–F2.4 remain protected historical savepoints. Historical F2.5 and F2.6 `0_1`/`0_2` remain immutable audit records. MASTER has now integrated F2.5R and frozen its repaired ion magnetic-moment quadrature ladder as the controlling downstream specification.

## Controlling physical / FLR objects

The F2-R physical model, F2.3 point and F2.4 input geometry remain frozen.

The controlling ion-FLR convention remains

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
\Gamma_{0i}=I_0(b_i)e^{-b_i}.}
\]

No physical parameter or input-space change has been made.

## Frozen F2.5R repair

Canonical branch result:

`research/fusion/fusion_f2_5r_ion_flr_quadrature_repair_gate_0_1.md`

MASTER integration freeze:

`research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`

F2.5R branch commit `cbfd6ca9a906df7bb34bf6270a24b6c63857f545`; Python CI #405 = `SUCCESS`.

The controlling repaired ion Gauss--Laguerre magnetic-moment orders are

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

All other F2.5 numerical objects remain unchanged. Historical `N_mu=8/12/16` remains only an audit baseline.

The repaired ion-state dimensions are

\[
\boxed{N_i(K0,K1,K2)=(18176,\ 91584,\ 357120).}
\]

The selected ladder is the first passing monotone ladder in the predeclared deterministic candidate sequence and passes active-node plus independent between-node local-B FLR manufactured criteria, positive-metric field-block tolerances, positive Gauss--Laguerre weights and Maxwellian moment checks.

No spectrum, eigenvector, propagator, Gramian, finite-time objective, optimizer, transport effect or GENE result was inspected.

## Active instruction

**Status:** `FUSION F2.6 0_3 DISCRETE OPERATOR / CHANNEL ALGEBRAIC QUALIFICATION READY — AWAIT GO`

**Next instruction:**

`research/master/prompts/fusion_f2_6_rerun_after_f2_5r_quadrature_repair_0_1.md`

On bare `GO`, first read this STATUS and execute only that committed instruction.

## F2.6 0_3 scope

On the unchanged K0/K1/K2 architecture with repaired `N_mu=16/24/40`, reconstruct the discrete quasineutrality, canonical positive Helmholtz metric, generator and independently defined physical particle/ion-heat/trapped-electron-heat channel operators and complete the pre-spectral algebraic qualification.

Required checks include the full-support local-B FLR identity, quasineutrality, `M_K>0`, `B_K=I`, `R_in,K=M_K`, physical-channel Hermiticity, particle ambipolarity, conservative phase-space adjoint/skew structure and the complete F2.1 discrete free-energy balance.

Create versioned `0_3` result/diagnostic files; do not overwrite historical F2.6 `0_1` or `0_2` files.

## Forbidden until F2.6 0_3 returns

Do not inspect eigenvalues, growth rates, pseudospectra or eigenvectors. Do not construct propagators, Gramians, cumulative objectives, optimizers, angles or gaps. Do not scan physical parameters or use resolutions outside the repaired K0/K1/K2 ladder, run GENE, add collisions/damping, retune F2.3/F2.4, alter the repaired F2.5R ladder or any other F2.5 object, reopen R1, or open MODES/CONT/CASCADE, Power Grid, Photonics or Paper-1 work.

## Expected return

One of:

- `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`;
- `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

**STOP / AWAIT GO.**
