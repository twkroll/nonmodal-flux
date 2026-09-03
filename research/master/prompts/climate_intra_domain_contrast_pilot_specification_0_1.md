# MASTER Prompt — Climate Intra-Domain Contrast Pilot Specification 0.1

**Authority:** `research/master/climate_intra_domain_contrast_feasibility_gate_0_1.md`, `research/climate/climate_intra_domain_contrast_candidate_freeze_0_1.md`, and `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`.

**Target chat:** existing Climate chat (`Klimadynamik Machbarkeit prüfen`).

**Scope:** pre-effect Climate-B pilot specification only. No finite-time execution, no evaluation of energy/channel operators, no optimizer, angle, gap, parameter search, retuning, new candidate, or manuscript claim update.

## Frozen inputs that must not change

Climate-A remains permanently frozen as `CLIM-WEAK`.

Climate-B remains exactly the qualified equivalent-barotropic Bickley-jet candidate with

\[
\partial_t\zeta' + U(y)\partial_x\zeta' + [\beta-U''(y)]\partial_x\psi'=-r\zeta',
\qquad \zeta'=\nabla^2\psi',
\]

\[
U(y)=U_0\operatorname{sech}^2((y-y_0)/L),
\]

and the frozen point

\[
\beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},\quad
U_0=20\,\mathrm{m\,s^{-1}},\quad
L=1000\,\mathrm{km},\quad
r=(10\,\mathrm d)^{-1},
\]

\[
L_x=20000\,\mathrm{km},\qquad L_y=10000\,\mathrm{km},
\qquad \tau_{\rm ref}=L/U_0=50000\,\mathrm s.
\]

Keep exactly the frozen representation, state ordering, `M_K`, `Q_shift,K`, `B=I`, `R_in=M_K`, 512-point assembly rule, 1024-point assembly audit, and resolution roles:

- `(8,16)` structural smoke;
- `(12,24)` coarse audit;
- `(16,32)` primary;
- `(20,40)` confirmation;
- `(24,48)` high-resolution audit.

Numerical Qualification 0.1 is `QUALIFIED`; do not repeat it except to cite its frozen results.

## 1. Freeze the horizon ladder before effect inspection

Use the inherited shared dimensionless ladder

\[
\boxed{T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.}
\]

With `tau_ref=50000 s`, record the corresponding dimensional horizons. No horizon may later be added, removed, interpolated, shifted, or selected post hoc to strengthen a result.

## 2. Freeze the finite-time operators — definitions only

With `B=I` and `R_in=M_K`, define the positive terminal-energy operator

\[
K_M(T)=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2},
\]

and the signed cumulative jet-shift-forcing operator

\[
K_{\rm shift}(T)
=M_K^{-1/2}
\left(\int_0^T e^{A_K^\dagger t}Q_{{\rm shift},K}e^{A_Kt}\,dt\right)
M_K^{-1/2}.
\]

Define, without evaluating,

\[
G_M(T)=\lambda_{\max}(K_M(T)),
\]

\[
J_{\rm shift}^+(T)=\lambda_{\max}(K_{\rm shift}(T)),\qquad
J_{\rm shift}^-(T)=\lambda_{\min}(K_{\rm shift}(T)).
\]

The positive branch is the poleward-translation-forcing optimum. The negative branch is the equatorward-translation-forcing optimum. Preserve the interpretation restriction that `J_shift` is cumulative forcing/impulse of the infinitesimal translation coordinate under frozen tangent dynamics, not a realized nonlinear jet displacement.

## 3. Freeze comparison diagnostics

Define normalized whitened optimizer vectors/subspaces for terminal energy and positive cumulative shift forcing. Use vector angle for nondegenerate extrema and principal/subspace angles when a frozen numerical degeneracy criterion is met.

Freeze

\[
\vartheta(T)=\arccos\left|w_M^{\star\dagger}w_{\rm shift}^{\star}\right|
\]

for nondegenerate one-dimensional extrema, with the appropriate subspace replacement otherwise.

Freeze the target-performance gap

\[
\Delta_{\rm shift}(T)
=\frac{J_{\rm shift}^+(T)-w_M^{\star\dagger}K_{\rm shift}(T)w_M^\star}
{J_{\rm shift}^+(T)}
\]

only when `J_shift^+(T)` is safely nonzero. Specify a pre-effect near-zero denominator rule; if triggered, report `Delta_shift` as uninterpretable rather than regularizing it post hoc.

Retain the common study-specific strong criterion exactly:

\[
\boxed{\vartheta\ge20^\circ,\qquad \Delta_{\rm shift}\ge0.25}
\]

on at least two neighboring frozen horizons, together with all structural/numerical robustness gates. State explicitly that these are operational study rules, not universal physical constants.

Do not calculate whether Climate-B meets them.

## 4. Freeze numerical execution methods

Specify before execution:

- matrix propagation method for `e^{A_KT}`;
- quadrature-free or Lyapunov/Sylvester method for the cumulative signed operator, with an independent cross-check;
- Hermiticity residual tolerances for `K_M` and `K_shift`;
- extremal eigenpair residual and normalization tolerances;
- direct physical-trajectory reproduction of terminal energy and cumulative `q_shift` at every horizon used in a verdict;
- resolution-robustness criteria comparing primary `(16,32)`, confirmation `(20,40)`, and high audit `(24,48)`;
- common-space optimizer/subspace comparison across nested resolutions;
- required reporting of dominant zonal wavenumber, meridional parity content, and physical-space structures for representative optimizers, using only frozen coordinates.

Prefer numerical tolerances consistent with the already frozen Climate-A/shared cross-domain protocols unless a purely numerical reason requires a stricter choice. Do not choose a tolerance based on any inspected Climate-B effect.

## 5. Freeze verdict logic

The future execution must report all six frozen horizons and signed extrema. It may not hide weak/null outcomes.

Predefine outcome classes sufficient for MASTER integration:

- `CLIM-B-STRONG`: common strong criterion met on at least two neighboring horizons and required robustness gates pass;
- `CLIM-B-WEAK`: structurally distinct objectives may exist, but the strong performance-gap criterion is not met robustly;
- `CLIM-B-NULL`: no meaningful objective nonredundancy under the frozen diagnostics;
- `CLIM-B-FAIL`: numerical/structural execution gate fails.

These labels are operational project verdicts only. Do not evaluate them in this specification.

## 6. Anti-bias / one-shot restrictions

- no change to `U0,L,beta,r,Lx,Ly`, profile, basis, `B`, `R_in`, `Q_shift`, resolution roles, or horizon ladder after execution begins;
- no alternate jet, momentum-flux mask, EOF, localization, forcing coordinate, or channel definition;
- no third Climate candidate before the first manuscript;
- weak/null/fail is retained as a valid one-shot outcome;
- Climate-A `CLIM-WEAK` remains unchanged and is never replaced by Climate-B.

## Required output

Create and commit:

`research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md`

The file must include scope/forbidden actions, frozen model/representation, horizon ladder, finite-time operator definitions, diagnostics, numerical methods/tolerances, robustness rules, outcome logic, physical interpretation restrictions, anti-bias rules, and explicit STOP.

Update:

`research/climate/STATUS.md`

After completion set Climate status to:

`CLIMATE-B PILOT SPECIFICATION COMPLETE — RETURN TO MASTER FOR PILOT FREEZE`

and `Next instruction: RETURN TO MASTER FOR PILOT FREEZE`.

Report canonical path, full commit hash, CI status if available, then STOP.

## STOP boundary

Do not execute the pilot. Do not inspect any finite-time objective value, optimizer, angle, gap, horizon dependence, or result-classification quantity. Do not update the manuscript or open another branch.