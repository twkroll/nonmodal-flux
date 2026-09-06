# Fusion F2.6 — Discrete Generator / Helmholtz Metric / Physical Channel Reconstruction & Algebraic Balance Qualification Gate 0.1

**Date:** 2026-09-06  
**Authority:** MASTER / `research/master/prompts/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_1.md`  
**Status:** `F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`

## Executive verdict

F2.6 cannot defensibly return `PASS` on the frozen F2.1–F2.5 lineage because the required manufactured ion-FLR check exposes a specific incompatibility between two simultaneously frozen conventions:

1. the ion gyroaverage `J0i` is evaluated with the **local** cyclotron frequency
   \[
   \Omega_i(\theta)=eB(\theta)/m_i,
   \]
   as frozen in F2.2/F2.5; but
2. the polarization/free-energy factor is frozen as
   \[
   b_i^{\rm frozen}(\theta)=k_\perp^2(\theta)\rho_{i0}^2,
   \qquad
   \rho_{i0}=v_{Ti}/\Omega_i(B_0),
   \]
   with
   \[
   \Gamma_{0i}^{\rm frozen}=I_0(b_i^{\rm frozen})e^{-b_i^{\rm frozen}}.
   \]

For a Maxwellian and the locally evaluated Bessel factor, the exact identity required for the standard gyrokinetic quasineutrality/free-energy equivalence is instead

\[
\left\langle J_0^2\!\left(
\frac{k_\perp v_\perp}{\Omega_i(\theta)}
\right)\right\rangle_{F_{i0}}
=
I_0(b_i^{\rm local})e^{-b_i^{\rm local}},
\]

with

\[
\boxed{
b_i^{\rm local}(\theta)
=
\frac{k_\perp^2(\theta)v_{Ti}^2}{\Omega_i^2(\theta)}
=
(k_\perp\rho_{i0})^2
\left(\frac{B_0}{B(\theta)}\right)^2.
}
\]

Because the frozen circular geometry has `B(theta) != B0` over almost all of the ballooning line, `b_i^local` and `b_i^frozen` are not the same object. The discrepancy is order-one relative to numerical quadrature residuals and does not disappear from K0 to K2.

This is precisely the `HOLD` case defined by the F2.6 handoff: a specific implementation/convention ambiguity blocks a defensible algebraic qualification, while the broader F2-R physical/numerical architecture is not falsified.

No spectrum, eigenvalue, growth rate, pseudospectrum, propagator, Gramian, optimizer, angle, performance gap or GENE calculation was inspected.

---

## 1. Frozen inputs preserved

The following upstream freezes were preserved without retuning:

- F2.1 reduced physics: finite-ion-FLR electrostatic local-GK ions plus collisionless bounce-averaged trapped electrons, with leading adiabatic passing electrons;
- F2.2 circular large-aspect-ratio `s-alpha` ballooning geometry;
- F2.3 single CBC-compatible point: `epsilon=0.18`, `q=1.4`, `shat=0.8`, `alpha_MHD=0`, `mi/me=3672`, `Ti/Te=1`, `a/Ln=0.8`, `a/LTi=a/LTe=2.49`, `ky rho_i=+0.3`, `theta0=kx0=0`;
- F2.4: \(B=I_{\mathcal H_{F2}},\ R_{\rm in}=\mathcal M_{F2}\);
- F2.5 K0/K1/K2 state-space and quadrature ladder exactly as committed.

No resolution outside K0/K1/K2 was substituted.

---

## 2. K0/K1/K2 instantiation reached before the blocker

The frozen numerical dimensions were instantiated exactly:

| level | `N_theta` | ion DOF | trapped-e DOF |
|---|---:|---:|---:|
| K0 | 71 | 9,088 | 432 |
| K1 | 159 | 45,792 | 1,620 |
| K2 | 279 | 142,848 | 4,032 |

The factorized pre-spectral objects

\[
C_{{\rm QN},K}\phi_K=S_{{\rm QN},K}x_K
\]

were instantiated with algebraic field elimination, the positive kinetic entropy-weight matrix `D_K`, frozen bounce projection, finite-ion `J0i`, and the structured `g/F0` time-derivative coupling.

Using the standard `g`-form before choosing between the conflicting polarization conventions gives

\[
E_K=I-D_K^{-1}S_K^\dagger C_{{\rm QN},K}^{-1}S_K,
\]

\[
M_K^{(g)}=D_KE_K
=
D_K-S_K^\dagger C_{{\rm QN},K}^{-1}S_K.
\]

This provisional factorization is useful only to localize the problem. It is **not** accepted as the canonical F2.6 metric because F2.5 also requires construction from the positive `delta F + polarization` Helmholtz form using the frozen `Gamma0i`; those two forms cease to be algebraically equivalent under the conflicting FLR definitions.

---

## 3. Manufactured Maxwellian FLR identity — blocking result

### 3.1 At the outboard midplane `theta=0`

Frozen geometry gives

\[
\frac{B(0)}{B_0}=\frac{1}{1+\epsilon}=0.8474576271186441,
\qquad
(k_\perp\rho_{i0})^2=0.09.
\]

Therefore

\[
b_i^{\rm local}(0)=\frac{0.09}{(0.8474576271186441)^2}=0.125316.
\]

The exact Maxwellian identity gives

\[
\langle J_0^2\rangle=\Gamma_0(0.125316)=0.8856850888548305.
\]

The frozen reference-`rho_i` polarization gives

\[
\Gamma_0(0.09)=0.9157828330545033.
\]

Thus

\[
\boxed{\Delta_{\rm FLR}(0)=-0.0300977441996727.}
\]

The relative discrepancy against the local-B value is about `3.40 %`. K0, K1 and K2 reproduce the local-B Maxwellian integral at `theta=0` to roundoff, so this is not a velocity-quadrature error.

### 3.2 At the inboard point `theta=pi`

Here

\[
\frac{B(\pi)}{B_0}=\frac{1}{1-\epsilon}=1.2195121951219512,
\]

and

\[
(k_\perp(\pi)\rho_{i0})^2=0.6584892135027468.
\]

The local-B Bessel argument corresponds to

\[
b_i^{\rm local}(\pi)=0.44276814715924695.
\]

Hence

\[
\langle J_0^2\rangle=\Gamma_0(0.44276814715924695)=0.6741214459594775,
\]

whereas the frozen reference-`rho_i` polarization is

\[
\Gamma_0(0.6584892135027468)=0.5752843264774330.
\]

Therefore

\[
\boxed{\Delta_{\rm FLR}(\pi)=+0.0988371194820445.}
\]

The discrepancy is about `14.66 %` of the source-consistent local-B value. The K0 quadrature error in `J0^2` at this point is only `2.23e-11`; K1 and K2 reproduce the local-B value to machine precision. The discrepancy therefore persists under the frozen ladder and is not a convergence failure.

---

## 4. Other pre-spectral checks completed before HOLD

These checks are reported only to show that the blocker is localized. They do **not** upgrade the gate to `PASS`.

| diagnostic | K0 | K1 | K2 |
|---|---:|---:|---:|
| QN random relative residual | `6.30e-17` | `7.51e-17` | `8.33e-17` |
| diagonal `C_QN` condition estimate | `16.17` | `21.63` | `26.75` |
| provisional Schur-Cholesky min pivot | `0.2242` | `0.1698` | `0.1366` |
| provisional `M^(g)` Hermiticity probe | `1.48e-16` | `1.57e-15` | `2.02e-15` |
| max density-moment error | `3.33e-16` | `6.66e-16` | `3.33e-16` |
| max energy-moment error | `3.62e-14` | `2.66e-15` | `8.88e-16` |
| bounce-denominator rel. error at `lambda_hat=1` | `1.70e-11` | `1.72e-11` | `1.74e-11` |
| particle ambipolarity absolute probe | `6.94e-18` | `1.04e-17` | `2.78e-17` |
| provisional `g`-form balance relative probe | `6.32e-15` | `7.29e-15` | `2.29e-13` |

The provisional channel Hermiticity probes are all at approximately `1e-16`–`2e-15`. Bounce averages of `1`, `cos(theta)` and `B(theta)` at `lambda_hat=1` agree with an independent regularized reference to approximately `1e-11` or better.

The reduced-electron ordering on the instantiated active nodes remains K0 `0.03737`, K1 `0.06224`, K2 `0.08713` for `max(k_perp rho_e)`.

---

## 5. Why the FLR conflict blocks canonical `M_K`

F2.1 uses two equivalent standard Helmholtz representations: the `g`-form and the positive `delta F` form containing `[1-Gamma0i(b_i)]|phi|^2`. Their equivalence requires

\[
\Gamma_{0i}=\langle J_{0i}^2\rangle_{F_{i0}}.
\]

With the currently frozen pair

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right),
\qquad
\Gamma_{0i}=\Gamma_0\!\left((k_\perp\rho_{i0})^2\right),
\]

that identity fails.

Consequently F2.6 has no authority to decide whether the canonical metric is the `g`-form consistent with local `J0i`, the positive form using frozen reference-`rho_i` `Gamma0i`, or a silently modified positive form with `b_i^local`. The same ambiguity propagates into the complete F2.1 balance because its left side uses the canonical `M_K`.

---

## 6. Exact MASTER decision required

MASTER must resolve exactly one object:

\[
\boxed{\text{the ion-FLR polarization parameter }b_i(\theta).}
\]

### Option A — source-consistent local-B FLR

Keep the frozen local gyroaverage

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i(\theta)}\right)
\]

and correct the polarization argument to

\[
\boxed{
b_i(\theta)=(k_\perp\rho_{i0})^2\left(\frac{B_0}{B(\theta)}\right)^2.
}
\]

Then `Gamma0i=<J0i^2>` by construction. This is the physically preferred clarification.

### Option B — reference-B0 FLR

Keep

\[
b_i=(k_\perp\rho_{i0})^2
\]

but evaluate the Bessel gyroaverage with the reference cyclotron frequency `Omega_i(B0)` rather than local `Omega_i(theta)`. That would revise the frozen F2.2/F2.5 local-gyroaverage convention and cannot be selected by F2.6 itself.

No loading, clipping, fitted `Gamma0`, damping or balance-derived correction is authorized.

---

## 7. Machine-readable diagnostics

The numerical values are stored in

`research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_1.json`.

They contain K0/K1/K2 dimensions, quadrature/moment diagnostics, quasineutrality residuals, provisional algebraic probes and the explicit `theta=0,pi` FLR mismatch. All fields marked `provisional` are noncanonical because the metric convention is unresolved.

---

## 8. Forbidden work respected

F2.6 performed no eigenvalue/eigenvector calculation, growth-rate or pseudospectral inspection, propagator, matrix exponential, Gramian, cumulative transport operator, optimizer, angle, performance gap, parameter scan, GENE execution, collision, damping, filter or regularization addition. No F2.3/F2.4/F2.5 object was retuned.

---

## 9. Verdict

The frozen discretization is not rejected as an architecture. The blockage is a single upstream FLR convention inconsistency that must be resolved before a unique `M_K` and hence a defensible complete F2.1 discrete balance can be certified.

\[
\boxed{
\text{F2.6 HOLD — SPECIFIC DISCRETE ALGEBRA/IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER}.
}
\]

**Required MASTER action:** issue an explicit FLR-convention clarification/erratum for `b_i(theta)` / `Gamma0i` relative to the already-frozen local `J0i`, then re-release F2.6. No branch-side next gate is self-authorized.

**STOP / RETURN TO MASTER.**
