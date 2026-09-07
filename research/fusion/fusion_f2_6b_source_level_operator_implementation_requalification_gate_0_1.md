# Fusion F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`  
**Status:** `F2.6B PASS — SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION FROZEN / ALGEBRA REQUALIFIED — RETURN TO MASTER`

## Executive verdict

A new versioned source-level realization of the frozen F2-R numerical model has been constructed and fully requalified pre-spectrally. This implementation is explicitly **not** claimed to be source-identical to historical F2.6 `0_3`; F2.6A established that such identity cannot be proven from canonical provenance.

The frozen generalized operator is

\[
E_K\dot x_K=F_Kx_K,\qquad A_K=E_K^{-1}F_K,
\]

with committed public interfaces `build_operator(level)`, `apply_E(op,x)`, `apply_F(op,x)` and `solve_E(op,x)`.

Canonical source:

`research/fusion/fusion_f2_6b_operator_0_1.py`

Requalification driver:

`research/fusion/fusion_f2_6b_requalification_0_1.py`

Machine-readable diagnostics:

`research/fusion/fusion_f2_6b_requalification_diagnostics_0_1.json`

Focused regression test:

`tests/test_fusion_f2_6b_operator_0_1.py`

## 1. Frozen upstream lineage

No F2.1–F2.5R object is changed. The reduced physical model, F2.2 local tokamak / `s-alpha` geometry and sign conventions, F2.3 physical point, F2.4 full input geometry, local-`B` ion-FLR convention and F2.5/F2.5R representation family remain frozen.

The ion FLR convention remains

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\qquad
b_i(\theta)=(k_\perp\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2,
\qquad
\Gamma_{0i}=I_0(b_i)e^{-b_i}.
\]

The repaired magnetic-moment ladder remains

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

## 2. Source-level implementation freeze

The state vector is ordered as ion followed by trapped electron. NumPy C-order is frozen:

\[
h_i[\theta,u,\zeta],\qquad h_e[w,E,\widehat\lambda].
\]

The dimensions are

\[
N_{\rm total}(K0,K1,K2)=(18608,\ 93204,\ 361152).
\]

Each width-`pi` element uses the exact LGL nodes/weights of the frozen polynomial degree. The global continuous derivative is assembled by mass projection of local LGL derivatives,

\[
D_\theta=M_\theta^{-1}\sum_eR_e^\dagger M_eD_eR_e,
\]

with the two global outer endpoint coefficients removed exactly as required by the compact-support freeze.

The ion physical characteristics are

\[
\dot\theta=ub/q,\qquad \dot u=-\zeta b b'/q.
\]

A raw nodal characteristic action is constructed from the committed `D_theta` and Hermite nodal derivative. The source-level structure-preserving choice is frozen as

\[
\boxed{L_{\rm adv}=\frac12\left(L_{\rm raw}-D_i^{-1}L_{\rm raw}^\dagger D_i\right).}
\]

The ion magnetic drift is added independently as the real diagonal frequency

\[
\widehat\omega_{di}=k_y\rho_{i0}\,\mathcal D(\theta)\left(u^2/b+\zeta\right),
\]

through `-i omega_di h_i`.

For trapped electrons, every retained well/pitch orbit uses the frozen regularization

\[
\sin\frac{\theta-2\pi w}{2}=\sin\frac{\theta_b}{2}\sin\chi,
\]

with the frozen interior Gauss--Legendre bounce order. The field is evaluated at every `chi` point with the local LGL polynomial of the containing spectral element. The normalized orbit quadrature defines a sparse field-to-orbit map `B_orb`; the same orbit weights define the trapped-electron magnetic-drift average. No fitted bounce frequency or independent interpolation grid is used.

The physical quadrature matrices `D_i` and `D_e` use the frozen Clebsch volume measure, local Maxwellian residual factor, generalized-Laguerre electron energy weights, pitch weights and the same regularized orbit measure.

Adjoint consistency is frozen by

\[
S_K=R_K^\dagger D_K,
\qquad
C_K\phi_K=S_Kx_K,
\qquad
P_K=C_K^{-1}S_K.
\]

The generalized time-derivative operator and exact Woodbury/Schur solve are

\[
E_K=I-R_KC_K^{-1}S_K,
\]

\[
\boxed{E_K^{-1}y=y+R_K(C_K-S_KR_K)^{-1}S_Ky.}
\]

No pseudoinverse, loading, clipping or regularization is used.

The gradient drives are implemented directly from the frozen diamagnetic frequencies. With the electron sign absorbed in `R_e=-B_orb`, both species source contributions use the physical cross-phase form

\[
-i k_y\left[G_p+G_T(E/T-5/2)\right]B_s\phi.
\]

The canonical metric is constructed as

\[
M_{g,K}=D_K-S_K^\dagger C_K^{-1}S_K,
\]

\[
\boxed{M_K=M_{g,K}+P_K^\dagger\Delta_{{\rm FLR},K}P_K,}
\]

where

\[
\Delta_{{\rm FLR},K}=\operatorname{diag}\left[m_V(\langle J_0^2\rangle_K-\Gamma_{0i})\right].
\]

The same metric is independently evaluated from the positive kinetic-plus-field Helmholtz functional.

## 3. Independent physical channels

Particle and heat channels are built before the balance comparison from the frozen radial cross phases:

\[
\Gamma_i={\rm Re}\left[-ik_y\langle h_i,J_{0i}\phi\rangle_{D_i}\right],
\]

\[
\Gamma_e^{tr}={\rm Re}\left[-ik_y\langle h_e,\bar\phi\rangle_{D_e}\right].
\]

Heat channels multiply the same physical integrands by `E/T-5/2`. Their matrix-free Hermitian representatives are the Hermitian parts of these direct bilinear maps and are not inferred from the free-energy identity.

## 4. Requalification results

The active-node local-`B` FLR maximum relative errors are

\[
2.32\times10^{-12},\quad3.51\times10^{-11},\quad5.39\times10^{-15},
\]

and the independent 257-point-per-element envelope maxima are

\[
3.04\times10^{-12},\quad4.02\times10^{-11},\quad6.44\times10^{-15}.
\]

All phase-space weights are strictly positive. Ion Maxwellian density/energy/heat-weight moment errors are at floating-point roundoff. The fixed `lambda_hat=1` bounce checks against a 512-point reference give at worst approximately `8.49e-12` for `cos(theta)` and `1.35e-12` for `B/B0`.

Maximum QN relative residuals are

\[
7.30\times10^{-17},\quad9.06\times10^{-17},\quad9.26\times10^{-17},
\]

and `solve_E(apply_E(x))-x` residuals are

\[
4.02\times10^{-17},\quad3.07\times10^{-17},\quad2.48\times10^{-17}.
\]

The diagonal `C_K` condition estimates are `16.17, 21.63, 26.75`; the normalized `E`-Schur condition estimates are `2.77, 2.91, 2.95`. All field-space Cholesky factorizations succeed without shifts.

Metric Hermiticity residuals are at most

\[
3.59\times10^{-16},\quad3.11\times10^{-15},\quad1.94\times10^{-15},
\]

and direct-positive versus factorized metric discrepancies are at most `2.22e-16, 1.66e-16, 1.13e-16`. Thus

\[
\boxed{M_K=M_K^\dagger\succ0},\qquad B_K=I,\qquad R_{{\rm in},K}=M_K.
\]

Streaming/mirror skew residuals are at most

\[
1.62\times10^{-15},\quad6.44\times10^{-15},\quad1.56\times10^{-15},
\]

and complete source-free conservative residuals are at most

\[
7.36\times10^{-16},\quad1.08\times10^{-15},\quad1.44\times10^{-15}.
\]

Maximum physical-channel Hermiticity residuals are

\[
1.97\times10^{-15},\quad1.22\times10^{-15},\quad8.73\times10^{-15}.
\]

Direct physical channel values and their Hermitian representatives agree to absolute errors below `1.1e-21`. Hydrogenic particle ambipolarity absolute residuals are at most

\[
3.71\times10^{-22},\quad2.38\times10^{-22},\quad1.99\times10^{-23}.
\]

With

\[
G_\Gamma=6.58,\qquad G_{T,i}=G_{T,e}=2.49,
\]

the independently constructed channels satisfy

\[
A_K^\dagger M_K+M_KA_K=2\left(G_\Gamma Q_{\Gamma,K}+G_{T,i}Q_{q_i,K}+G_{T,e}Q_{q_e,K}\right)
\]

with maximum relative residuals

\[
\boxed{1.29\times10^{-13},\qquad5.64\times10^{-13},\qquad5.87\times10^{-13}.}
\]

A fixed smooth manufactured state gives

\[
2W_K=8.5835647932,\quad8.5972174967,\quad8.6039815033,
\]

with successive relative changes `1.5906e-3` and `7.8677e-4`.

The diagnostics JSON stores deterministic seeds, tolerances, level metadata, all structural residuals and SHA-256 regression hashes for level-defining arrays (`theta`, `D_i`, `D_e`, `J0`, sparse orbit-map CSR arrays, and the field Schur block). The committed operator source itself is identified by Git blob `ab2ecd18a53ddf8a3a4b4c4826a876054de15dd9`.

## 5. Historical comparison and governance

F2.6B does not force exact numerical equality with historical F2.6 `0_3`. The new source-level realization reproduces the same qualified physical/algebraic behavior and the complete balance remains at approximately `1e-13` relative scale. No material discrepancy requiring an upstream change was found.

Historical F2.6 `0_3`, F2.6A and earlier failure records remain immutable audit savepoints. F2.6B is the new provenance-clean executable realization, but no later gate is self-authorized.

F2.6B computed or inspected no eigenvalue, eigenvector, Ritz value, spectral abscissa, growth rate or pseudospectrum. It constructed no matrix exponential, propagator, Gramian, cumulative objective, optimizer, principal angle, performance gap or horizon curve. No parameter/wavenumber/input-space scan, GENE run, collision, damping, filtering, hypercollision, artificial viscosity or absorbing layer was used.

## Verdict

\[
\boxed{\text{F2.6B PASS — SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION FROZEN / ALGEBRA REQUALIFIED — RETURN TO MASTER}.}
\]

**STOP / RETURN TO MASTER.**
