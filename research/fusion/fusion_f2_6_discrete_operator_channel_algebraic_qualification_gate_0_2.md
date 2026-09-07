# Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.2

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_6_resume_after_ion_flr_erratum_0_1.md`  
**Controlling erratum:** `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`  
**Status:** `F2.6 FAIL — RETURN TO MASTER`

## Executive verdict

MASTER's ion-FLR erratum resolves the earlier continuous convention conflict. The source-consistent local convention is now unambiguous:

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

The representative manufactured checks at `theta=0` and `theta=pi` now pass to the expected K0/K1/K2 velocity-quadrature accuracy.

However, the required **full retained-support** check exposes a second, genuinely numerical failure of the already frozen F2.5 ladder. The local-B erratum increases the ion FLR argument in parts of the expanding ballooning windows, while the frozen magnetic-moment quadrature rises only as

\[
N_\mu=8,\ 12,\ 16
\]

on K0/K1/K2. On active LGL nodes the discrete Maxwellian moment

\[
\left\langle J_{0i}^2\right\rangle_K
\]

therefore ceases to converge uniformly to the controlling analytic

\[
\Gamma_{0i}(b_i).
\]

The maximum retained-node error is

| level | max `|<J0^2>_K-Gamma0|` | max relative error | worst `b_i` |
|---|---:|---:|---:|
| K0 | `8.3028e-05` | `3.6977e-04` | `3.4515` |
| K1 | `1.7012e-03` | `1.3010e-02` | `9.5693` |
| K2 | `2.3078e-02` | `3.0470e-01` | `27.9988` |

Thus the error **worsens** under the predeclared K0→K1→K2 ladder and reaches about `30.5 %` relative at the worst active K2 node.

This violates the F2.6 requirement that the frozen representation support the source-consistent FLR identity and the complete F2.1 discrete Helmholtz/balance structure on all three levels.

Because MASTER has already removed the convention ambiguity, and because repairing this defect would require changing the frozen F2.5 magnetic-moment resolution/integration strategy, the correct gate outcome is

\[
\boxed{\text{F2.6 FAIL — RETURN TO MASTER}.}
\]

No spectrum or finite-time object was inspected.

---

## 1. Frozen upstream objects preserved

No upstream retuning was performed.

Preserved exactly:

- F2.1 reduced collisionless two-species local-GK architecture;
- F2.2 circular `s-alpha` ballooning geometry and local gyroaverage;
- F2.3 CBC-compatible single physical point;
- F2.4
  \[
  B=I_{\mathcal H_{F2}},
  \qquad
  R_{\rm in}=\mathcal M_{F2};
  \]
- F2.5 K0/K1/K2 ballooning, ion Hermite/Laguerre, trapped-electron and bounce quadrature ladder;
- MASTER local-B ion-FLR erratum.

No hidden resolution, filtering, damping, loading, clipping or nullspace deletion was introduced.

---

## 2. Erratum verification at representative locations

With `epsilon=0.18`, `ky rho_i0=0.3`, `shat=0.8`, `alpha_MHD=0`, `kx0=0`,

\[
k_\perp\rho_{i0}
=
0.3\sqrt{1+(0.8\theta)^2}.
\]

### 2.1 Outboard midplane

At `theta=0`,

\[
b_i(0)=0.125316,
\qquad
\Gamma_0=0.8856850888548305.
\]

The frozen Laguerre quadratures give

- K0: `0.8856850888548307`;
- K1: `0.8856850888548304`;
- K2: `0.8856850888548304`.

The errors are roundoff.

### 2.2 Inboard point

At `theta=pi`,

\[
b_i(\pi)=0.44276814715924695,
\qquad
\Gamma_0=0.6741214459594775.
\]

The discrete moments are

- K0: `0.6741214459371465`, error `-2.2331e-11`;
- K1: `0.6741214459594782`, error `+6.6613e-16`;
- K2: `0.6741214459594771`, error `-4.4409e-16`.

Therefore the historical F2.6 HOLD blocker is resolved exactly as intended by MASTER.

---

## 3. Full-support FLR qualification — failing result

For the frozen ion coordinate

\[
\zeta=\mu_iB_0/T_i,
\]

the local Maxwellian perpendicular moment at fixed `theta` is discretized as

\[
\left\langle J_0^2\right\rangle_K
=
\beta
\sum_{m=1}^{N_\mu}
w_m
e^{-(\beta-1)\zeta_m}
J_0^2\!\left(
\sqrt{\frac{2\zeta_m(k_\perp\rho_{i0})^2}{\beta}}
\right),
\qquad
\beta=B/B_0,
\]

while the controlling exact value is

\[
\Gamma_0\!\left(
\frac{(k_\perp\rho_{i0})^2}{\beta^2}
\right).
\]

The full active-node search is not a parameter/resolution scan: it is the mandatory manufactured-identity check on each already frozen K-level.

### K0

Worst active node:

\[
\theta=-9.3514372393774,
\quad
B/B_0=1.21879298749796,
\quad
b_i=3.45152128554605.
\]

\[
\Gamma_0=0.2245392586383414,
\qquad
\langle J_0^2\rangle_{K0}=0.2244562305578652.
\]

Relative error:

\[
3.6977\times10^{-4}.
\]

### K1

Worst active node:

\[
\theta=-15.6657593896926,
\quad
B/B_0=1.21927386980283,
\quad
b_i=9.56927706835096.
\]

\[
\Gamma_0=0.1307612555739702,
\qquad
\langle J_0^2\rangle_{K1}=0.1290600513591330.
\]

Relative error:

\[
1.3010\times10^{-2}.
\]

### K2

Worst active node:

\[
\theta=19.7227368072874,
\quad
B/B_0=0.896354069538069,
\quad
b_i=27.9987507553276.
\]

\[
\Gamma_0=0.0757383135087993,
\qquad
\langle J_0^2\rangle_{K2}=0.0526607927467765.
\]

Relative error:

\[
\boxed{0.3047007478}.
\]

The failure is therefore not a small tolerance issue and not a monotone convergence tail. The increasingly large ballooning windows expose increasingly large ion-FLR arguments faster than the frozen `N_mu` ladder resolves the oscillatory Bessel moment.

---

## 4. Consequence for the discrete Helmholtz metric

Let `D_K` be the positive kinetic entropy matrix, `S_K` the quasineutral charge map, `C_QN,K` the electrostatic susceptibility matrix and

\[
P_{\rm QN,K}=C_{\rm QN,K}^{-1}S_K.
\]

The `g`-equation time-derivative structure yields

\[
M_K^{(g)}
=
D_K-S_K^\dagger C_{\rm QN,K}^{-1}S_K.
\]

The canonical F2.6 metric, however, must be built independently from the positive `delta F + polarization` Helmholtz functional using the controlling analytic `Gamma0(b_i)`.

At finite quadrature the two forms differ by

\[
\boxed{
M_K^{(+)}-M_K^{(g)}
=
P_{\rm QN,K}^\dagger
\Delta_{{\rm FLR},K}
P_{\rm QN,K},
}
\]

where the ion field block contains

\[
\Delta_{{\rm FLR},K}
\propto
\left\langle J_{0i}^2\right\rangle_K-\Gamma_{0i}(b_i).
\]

The normalized field-block defect grows across the frozen ladder:

| level | weighted Frobenius defect / `C_QN` | max local defect / `C_QN` |
|---|---:|---:|
| K0 | `3.9807e-06` | `4.1514e-05` |
| K1 | `1.0913e-04` | `8.5060e-04` |
| K2 | `4.0098e-03` | `1.1539e-02` |

Therefore the `g`-form symmetrizer and the independently constructed positive Helmholtz metric are not the same discrete object on the frozen ladder, and the discrepancy worsens rather than converges.

No metric shift, eigenvalue clipping, fitted `Gamma0`, quadrature-defined replacement for MASTER's analytic `Gamma0`, or physical-direction deletion is authorized.

---

## 5. Other regenerated pre-spectral checks

The failure is localized. The following checks remain satisfactory.

| diagnostic | K0 | K1 | K2 |
|---|---:|---:|---:|
| QN diagonal condition estimate | `16.1720` | `21.6335` | `26.7454` |
| QN random relative residual | `8.47e-17` | `7.75e-17` | `~1e-16` |
| max density-moment error | `3.33e-16` | `8.88e-16` | `5.55e-16` |
| max energy-moment error | `3.64e-14` | `2.66e-15` | `8.88e-16` |
| max heat-weight moment error | `3.73e-14` | `2.00e-15` | `1.55e-15` |
| regularized bounce errors (`1`, `cos theta`, `B`) | `<=3e-16` | `<=8e-16` | `<=3e-15` |
| max active-node `k_perp rho_e` | `0.03737` | `0.06224` | `0.08713` |

The physical particle/ion-heat/trapped-electron-heat forms reconstructed from the frozen radial flux integrals remain Hermitian to approximately `1e-16`–`2e-15`, and the hydrogenic particle ambipolarity probes remain at approximately `1e-17`.

These checks do not rescue the gate because the required canonical metric/balance qualification must pass on the same frozen state space.

---

## 6. Generator and balance implication

The collisionless `g`-form assembly still exhibits the previously localized roundoff-level balance probes when paired with its natural `M_K^(g)`; this is useful as a debugging check because `J0i`, the physical channels and the conservative weak/SBP assembly were not changed by the erratum.

It is **not** the required F2.6 certification.

F2.6 requires

\[
A_K^\dagger M_K^{(+)}+M_K^{(+)}A_K
=
2\left(
G_\Gamma Q_{\Gamma,K}
+G_{T,i}Q_{q_i,K}
+G_{T,e}Q_{q_e,K}
\right)
\]

with `M_K^(+)` constructed from the independent positive Helmholtz functional.

Because

\[
M_K^{(+)}\neq M_K^{(g)}
\]

by a nonconvergent full-support FLR quadrature defect, this complete canonical matrix identity cannot be certified on all three frozen levels.

The failure occurs before any spectral qualification and does not depend on an eigenvalue, growth rate, transient quantity or objective effect.

---

## 7. Why this is FAIL rather than HOLD

The previous `0_1` result was `HOLD` because two upstream FLR conventions conflicted and F2.6 had no authority to choose between them.

That ambiguity no longer exists. MASTER explicitly selected the local-B convention.

The remaining problem is numerical and concrete:

\[
\boxed{
\text{the frozen F2.5 }N_\mu=8,12,16
\text{ ladder does not resolve the required local-B ion-FLR moment on its full retained support.}
}
\]

A repair would require at least one newly authorized change such as

- a different/increased ion magnetic-moment resolution ladder;
- an analytically integrated Laguerre representation for the Bessel products;
- a different predeclared coupling between ballooning-window growth and ion velocity-space order.

All of these modify F2.5 and are explicitly forbidden inside F2.6.

The original gate therefore requires `FAIL`.

---

## 8. Machine-readable diagnostics

Canonical resumed diagnostics are stored in

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_2.json`.

A reproducible pre-spectral diagnostic script is stored in

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_0_2.py`.

The historical `0_1` HOLD files remain unchanged.

---

## 9. Forbidden work respected

No eigenvalues, eigenvectors, growth rates, spectral abscissa, pseudospectra, propagators, matrix exponentials, Gramians, cumulative objectives, optimizer directions, principal angles, performance gaps, parameter/wavenumber scans, extra resolutions, GENE runs, collisions, damping, filtering, absorbing layers, metric shifts or ad hoc regularization were used.

---

## 10. Verdict

\[
\boxed{
\text{F2.6 FAIL — RETURN TO MASTER}.
}
\]

The failure is specifically a **frozen discretization/FLR-resolution failure** after the continuous ion-FLR convention was successfully repaired.

MASTER must decide whether to reopen a versioned discretization-specification gate. F2.6 does not self-authorize such a repair.

**STOP / RETURN TO MASTER.**
