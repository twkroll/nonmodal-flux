# Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.3

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_6_rerun_after_f2_5r_quadrature_repair_0_1.md`  
**Controlling repair:** `research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`  
**Status:** `F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER`

## Executive verdict

The F2.5R ion magnetic-moment repair removes the only numerical defect identified in F2.6 `0_2`. On the unchanged K0/K1/K2 architecture with

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40,}
\]

the source-consistent local-\(B\) ion-FLR identity, quasineutrality reconstruction, canonical positive Helmholtz metric, conservative weak/SBP phase-space structure, independently reconstructed particle/heat channels, hydrogenic ambipolarity and the complete F2.1 discrete free-energy balance all qualify pre-spectrally.

No eigenvalue, eigenvector, growth rate, pseudospectrum, matrix exponential, propagator, Gramian, cumulative objective, optimizer, angle, performance gap, physical parameter scan or GENE result was calculated or inspected.

---

## 1. Frozen lineage preserved

No upstream physical object was changed.

The controlling reduced model remains finite-ion-FLR electrostatic local-GK ions plus collisionless bounce-averaged trapped electrons with leading adiabatic passing electrons. The F2.2 circular `s-alpha` geometry, the F2.3 CBC-compatible physical point, and the F2.4 input pair remain

\[
\boxed{B=I_{\mathcal H_{F2}},\qquad R_{\rm in}=\mathcal M_{F2}.}
\]

The controlling local-\(B\) ion-FLR convention remains

\[
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

The only supersession relative to historical F2.5 is the MASTER-integrated F2.5R `N_mu=16/24/40` ladder.

---

## 2. Factorized discrete construction

The discrete quasineutrality problem is assembled as

\[
C_K\phi_K=S_Kx_K,
\qquad
P_K=C_K^{-1}S_K,
\qquad
\phi_K=P_Kx_K.
\]

The kinetic entropy/quadrature weight is denoted \(D_K\). The field time-derivative coupling inherited directly from the frozen ion and bounce-averaged-electron equations is

\[
R_K=D_K^{-1}S_K^\dagger,
\]

so the semidiscrete system is represented without appending \(\phi_K\) to the state as

\[
E_K\dot x_K=F_Kx_K,
\qquad
E_K=I-R_KC_K^{-1}S_K.
\]

The generator is therefore applied matrix-free as

\[
\boxed{A_K=E_K^{-1}F_K}
\]

with the exact low-rank solve

\[
E_K^{-1}y
=
y+R_K(C_K-S_KR_K)^{-1}S_Ky.
\]

No dense K2 generator is stored and no generator spectrum is formed.

The `g`-form metric factorization is

\[
M_{g,K}
=
D_K-S_K^\dagger C_K^{-1}S_K.
\]

The canonical metric is constructed independently from the positive `delta F + polarization` Helmholtz functional. With the repaired finite quadrature, its exact algebraic relation to the `g` form is

\[
\boxed{
M_K
=
M_{g,K}
+
P_K^\dagger\Delta_{{\rm FLR},K}P_K,
}
\]

where

\[
\Delta_{{\rm FLR},K}
=
\operatorname{diag}
\left[
m_V
\left(
\langle J_{0i}^2\rangle_K-\Gamma_{0i}
\right)
\right].
\]

This correction is not a fitted balance term; it is the directly assembled difference between the finite ion quadrature in the positive entropy term and the analytic polarization factor.

---

## 3. Repaired local-B FLR qualification

The repaired ladder re-passes both the active LGL-node test and an independent 257-point-per-\(\pi\)-element Chebyshev--Lobatto geometry envelope.

| level | `N_mu` | active max abs | active max relative | envelope max relative | field Fro/C | field local/C |
|---|---:|---:|---:|---:|---:|---:|
| K0 | 16 | `5.209e-13` | `2.320e-12` | `3.043e-12` | `1.615e-14` | `2.604e-13` |
| K1 | 24 | `4.587e-12` | `3.508e-11` | `4.015e-11` | `1.115e-13` | `2.293e-12` |
| K2 | 40 | `6.939e-16` | `5.684e-15` | `6.440e-15` | `1.209e-16` | `3.469e-16` |

Thus the specific full-support defect that forced F2.6 `0_2` to FAIL is removed by the already-frozen F2.5R repair.

The standard Maxwellian density, energy and heat-weight moment errors are at floating-point roundoff on every level. The unchanged regularized bounce quadrature reproduces the fixed analytic tests `1`, `cos(theta)` and `B(theta)` to approximately \(10^{-14}\) or better.

---

## 4. Quasineutrality and canonical positive metric

The repaired dimensions are

\[
\boxed{
N_i=(18176,\ 91584,\ 357120),
\qquad
N_e=(432,\ 1620,\ 4032).
}
\]

For deterministic random coefficient probes, the maximum relative quasineutrality residuals are

\[
7.44\times10^{-17},\qquad
7.93\times10^{-17},\qquad
8.28\times10^{-17}
\]

for K0/K1/K2.

The normalized `g`-form Schur complements

\[
C_K^{-1/2}(C_K-S_KR_K)C_K^{-1/2}
\]

admit Cholesky factorization without shift or clipping. The minimum diagonal entries of those Cholesky factors are

\[
0.7209,\qquad 0.7249,\qquad 0.7289.
\]

The canonical positive metric is independently evaluated from the positive Helmholtz functional. The direct-positive versus factorized-metric relative discrepancies are at most

\[
2.25\times10^{-16},\qquad
3.35\times10^{-16},\qquad
4.45\times10^{-16}.
\]

Its Hermiticity probes are below \(3.0\times10^{-16}\). The minimum retained ion polarization coefficient is

\[
\min_\theta[1-\Gamma_{0i}(\theta)]
=0.1143149111>0,
\]

all phase-space quadrature weights are positive, and no loading, clipping or nullspace deletion is used. The positive functional therefore vanishes only for the zero physical perturbation, so

\[
\boxed{M_K=M_K^\dagger\succ0}
\]

on all three repaired levels.

The conforming F2.4 input geometry is inherited exactly:

\[
\boxed{B_K=I,\qquad R_{{\rm in},K}=M_K.}
\]

---

## 5. Conservative phase-space operator

The ion parallel-streaming plus mirror-force operator is assembled from the frozen physical characteristic field using the F2.5 split weak/SBP form. Magnetic drift is added with the frozen signed `+i omega_d g` convention, and the trapped-electron magnetic drift is evaluated with the same regularized bounce projection used elsewhere.

The maximum relative adjoint/skew residuals of the ion streaming/mirror block are

\[
2.41\times10^{-15},\qquad
2.88\times10^{-15},\qquad
8.86\times10^{-15}.
\]

For the complete source-free conservative ion-plus-electron phase-space operator, including magnetic drifts, the maximum residuals are

\[
2.17\times10^{-15},\qquad
5.12\times10^{-15},\qquad
4.81\times10^{-15}.
\]

No dissipation, filtering, hypercollision, viscosity or absorbing layer is present.

---

## 6. Physical transport channels

The channel operators are reconstructed independently from the frozen physical radial gyrocentre flux definitions, not from the desired free-energy balance.

After absorbing the common real `k_alpha` normalization factor, the ion particle quadratic form is assembled from

\[
\Gamma_i
=
\operatorname{Re}
\left[
-i\,
\langle
h_i,\,
J_{0i}\phi
\rangle_{D_i}
\right],
\]

and the trapped-electron particle form from

\[
\Gamma_e^{\rm tr}
=
\operatorname{Re}
\left[
-i\,
\langle
h_e,\,
\bar\phi
\rangle_{D_e}
\right].
\]

The heat forms use the same physical quadratures with

\[
E_a/T_a-\frac52.
\]

The Hermitian matrices/operators \(Q_{\Gamma,K}\), \(Q_{q_i,K}\), \(Q_{q_e,K}\) are the Hermitian representatives of these real physical quadratic forms. Bilinear Hermiticity probes are zero to displayed double precision on all three levels.

Hydrogenic ambipolarity is an exact algebraic consequence of discrete quasineutrality. Random-probe absolute residuals satisfy

\[
|\Gamma_i-\Gamma_e^{\rm tr}|
\le
8.7\times10^{-19}
\]

over the reported tests.

No heat-channel equality is imposed or observed algebraically; \(q_i\) and \(q_e^{\rm tr}\) remain distinct independently constructed physical forms.

---

## 7. Complete F2.1 discrete balance

Using the frozen equal-species gradient point in common algebraic radial units,

\[
G_n=0.8,
\qquad
G_{T,i}=G_{T,e}=2.49,
\qquad
G_{p,i}=G_{p,e}=3.29,
\]

so

\[
G_\Gamma=G_{p,i}+G_{p,e}=6.58.
\]

For each deterministic probe, `A_K` is applied as `E_K^{-1}F_K`, the left side is evaluated with the independently constructed canonical positive metric, and the right side is evaluated only from the independently reconstructed physical channels.

The maximum absolute balance residuals are

\[
7.11\times10^{-17},\qquad
7.06\times10^{-17},\qquad
5.13\times10^{-17},
\]

and the corresponding maximum relative residuals are

\[
1.92\times10^{-14},\qquad
3.15\times10^{-13},\qquad
1.61\times10^{-13}.
\]

Thus

\[
\boxed{
A_K^\dagger M_K+M_KA_K
=
2\left(
G_\Gamma Q_{\Gamma,K}
+
G_{T,i}Q_{q_i,K}
+
G_{T,e}Q_{q_e,K}
\right)
}
\]

is qualified to the reported finite-quadrature/roundoff level on K0/K1/K2.

The physical `Q` operators were constructed before this comparison and were not inferred backwards from the left-hand side.

---

## 8. Structural convergence diagnostic

A fixed smooth manufactured state with compact central ballooning support and identical physical definition on all three levels gives

\[
2W_K=
10.4716947769,\quad
10.4862883885,\quad
10.4935667328
\]

on K0/K1/K2.

The successive relative changes are approximately

\[
1.39\times10^{-3},
\qquad
6.94\times10^{-4},
\]

consistent with the repaired ladder approaching a stable discrete free-energy value. This is a structural manufactured-state diagnostic only and contains no spectral or transport-effect information.

---

## 9. Governance / forbidden-work audit

F2.6 `0_3` did not inspect any generator eigenvalue or eigenvector, spectral abscissa, growth rate, pseudospectrum, matrix exponential, propagator, Gramian, cumulative transport operator, optimizer, principal angle, performance gap or horizon dependence.

No physical parameter, wavenumber, input subspace, ballooning window or resolution outside the repaired K0/K1/K2 ladder was scanned. No GENE run, collision term, damping, filter, metric shift or physical-direction deletion was introduced.

Historical F2.6 `0_1` HOLD and `0_2` FAIL remain unchanged audit records.

---

## 10. Verdict

The F2.5R repair restores the source-consistent discrete ion-FLR structure and the complete pre-spectral F2.6 algebraic qualification now passes on every frozen repaired level.

\[
\boxed{
\text{F2.6 PASS — DISCRETE OPERATOR/CHANNEL ALGEBRA QUALIFIED — RETURN TO MASTER}.
}
\]

No branch-side next gate is self-authorized.

**STOP / RETURN TO MASTER.**
