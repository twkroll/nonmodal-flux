# Climate Intra-Domain Contrast Pilot Freeze 0.1

**Status:** `STABLE — EXECUTION RELEASED`  
**Date:** 2026-09-03  
**Authority:** MASTER  
**Scope:** final pre-effect governance freeze for the one-shot Climate-B pilot. This document authorizes exactly one finite-time execution of the already frozen and numerically qualified Climate-B specification. It does not evaluate any Climate-B finite-time objective or result.

## 1. Executive decision

The Climate-B branch has completed, in order:

1. Climate Intra-Domain Contrast Feasibility Gate 0.1 — `PASS`;
2. Climate Intra-Domain Contrast Candidate Freeze 0.1 — `STABLE`;
3. Climate Intra-Domain Contrast Numerical Qualification 0.1 — `QUALIFIED`;
4. Climate Intra-Domain Contrast Pilot Specification 0.1 — `COMPLETE`.

The specification is internally consistent, fully pre-effect, and compatible with the project-wide anti-retuning protocol. Python CI for the specification return commit `495b53819c8b6b2cca0cb6e061898ad2efe73e1d` completed successfully.

Therefore

\[
\boxed{\text{Climate Intra-Domain Contrast Pilot Freeze 0.1 = STABLE — EXECUTION RELEASED}.}
\]

Exactly one Climate-B execution is authorized.

## 2. Frozen physical problem

Climate-B remains the equivalent-barotropic midlatitude Bickley jet

\[
\partial_t\zeta' + U(y)\partial_x\zeta' + [\beta-U''(y)]\partial_x\psi'=-r\zeta',
\qquad \zeta'=\nabla^2\psi',
\]

\[
U(y)=U_0\operatorname{sech}^2(y/L),
\]

with immutable physical point

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

The qualified representation remains positive zonal Fourier modes plus centered meridional sine Galerkin modes with exact conjugate reconstruction of real fields.

## 3. Frozen CORE objects and physical semantics

The positive metric remains barotropic perturbation kinetic energy,

\[
E'=\frac12x^\dagger M_Kx,
\qquad M_K\succ0.
\]

The signed physical channel remains the eddy forcing of the infinitesimal poleward jet-translation tangent

\[
g(y)=-U'(y),
\]

\[
q_{\rm shift}(t)
=\frac{\int g(y)[-\partial_y\overline{u'v'}]dy}{\int g(y)^2dy},
\]

with positive sign fixed as forcing toward a poleward translation.

The admissible geometry is frozen as

\[
\boxed{B=I,\qquad R_{\rm in}=M_K.}
\]

`J_shift` is cumulative eddy impulse/forcing of the infinitesimal translation coordinate under frozen tangent dynamics. It is not the realized displacement of a nonlinear coupled atmospheric jet.

## 4. Frozen stability and resolution savepoint

The complete nested resolution ladder is

\[
(8,16),\ (12,24),\ \boxed{(16,32)},\ \boxed{(20,40)},\ \boxed{(24,48)},
\]

with roles structural smoke, coarse audit, primary, confirmation, and high-resolution audit.

Numerical Qualification established at every rung

\[
\boxed{\alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0},
\]

and passed the frozen quadrature, positive-metric, Hermiticity/indefiniteness, parity, deterministic sign-witness, eigenresidual, and nested spectral-boundary gates.

No physical or numerical retuning is permitted after this savepoint.

## 5. Frozen horizon ladder

Execute exactly the six pre-effect horizons

\[
\boxed{T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}},
\]

or

\[
T\in\{12500,25000,50000,100000,200000,400000\}\,\mathrm s.
\]

All six horizons must be reported. No additional, shifted, interpolated, or selected subset of horizons may be introduced after effect inspection.

## 6. Frozen finite-time definitions

In whitened coordinates

\[
x(0)=M_K^{-1/2}w,\qquad \|w\|_2=1,
\]

define

\[
K_M(T)=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2},
\]

\[
G_M(T)=\lambda_{\max}(K_M(T)),
\]

\[
P_{\rm shift}(T)=\int_0^T e^{A_K^\dagger t}Q_{{\rm shift},K}e^{A_Kt}\,dt,
\]

\[
K_{\rm shift}(T)=M_K^{-1/2}P_{\rm shift}(T)M_K^{-1/2},
\]

\[
J_{\rm shift}^{+}(T)=\lambda_{\max}(K_{\rm shift}(T)),\qquad
J_{\rm shift}^{-}(T)=\lambda_{\min}(K_{\rm shift}(T)).
\]

Both signed extrema are mandatory.

Optimizer/subspace comparison, degeneracy handling, principal-angle rules, `Delta_shift`, and the safely-nonzero denominator rule are exactly those in `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md` and may not be altered during execution.

## 7. Frozen numerical execution protocol

Execution must use exactly the pre-specified methods and tolerances:

- blockwise scaling-and-squaring Padé matrix exponentials;
- analytic inverse energy square root;
- Lyapunov-tail cumulative signed operator as primary method;
- independent block-exponential/Van-Loan cross-check;
- Hermiticity gates before any roundoff symmetrization;
- PSD gate for `K_M`;
- eigenpair, normalization, and Rayleigh-residual gates;
- direct physical terminal-energy reproduction;
- direct reconstructed Reynolds-stress / jet-translation-forcing time-history integration;
- primary/confirmation/high-audit objective-value convergence `<=2%`;
- common-space optimizer/subspace captured mass `mu_c>=0.95`;
- maximum cross-resolution principal angle `<=10 deg`;
- no added resolution rung after execution begins.

A horizon may support a physical verdict only if all mandatory numerical and robustness gates in the specification pass.

## 8. Frozen operational verdict logic

The strong demonstration thresholds remain

\[
\boxed{\vartheta\ge20^\circ},\qquad
\boxed{\Delta_{\rm shift}\ge0.25}
\]

at the same pair of at least two neighboring frozen horizons, robustly at primary, confirmation, and high-resolution audit, with a reproducible physical/modal interpretation.

The weak/null thresholds remain

\[
\vartheta\ge5^\circ\quad\text{or}\quad\Delta_{\rm shift}\ge0.05
\]

for resolvable objective dependence when the strong criterion is not met.

Execution must assign exactly one outcome using the precedence and definitions frozen in the Pilot Specification:

- `CLIM-B-FAIL`;
- `CLIM-B-NULL`;
- `CLIM-B-STRONG`;
- `CLIM-B-WEAK`.

These are project-level operational classes, not universal atmospheric-physics constants.

## 9. Mandatory reporting

The execution result must report, for every frozen horizon and required resolution role:

- `G_M(T)`;
- `J_shift^+(T)` and `J_shift^-(T)`;
- safely interpretable angle/subspace-angle diagnostics;
- `Delta_shift` or explicit undefined status under the denominator rule;
- degeneracy ranks;
- algebraic and independent-integral cross-check residuals;
- direct physical-trajectory reproduction residuals;
- objective-value and optimizer/subspace resolution-robustness diagnostics;
- physical optimizer diagnostics: zonal wavenumber content, meridional parity, physical streamfunction/velocity structure, Reynolds stress, momentum-flux convergence, translation projection, and representative `q_shift(t)` histories;
- exactly one final one-shot verdict.

All effect values must be retained whether strong, weak, null, or failure.

## 10. Anti-bias / no-retuning rules

Once execution starts, do not change:

- physical parameters, jet profile, domain, damping, or translation tangent;
- `M_K`, `Q_shift,K`, `B`, or `R_in`;
- basis, quadrature, state ordering, or resolution roles;
- horizon ladder;
- propagation/integration method or tolerances;
- degeneracy, denominator, robustness, or verdict criteria.

Do not inspect a partial result and then modify any frozen choice.

Climate-A remains permanently `CLIM-WEAK` regardless of Climate-B outcome.

Climate-B is the only additional Climate attempt authorized before the first manuscript. After this execution there is no third Climate search.

## 11. Manuscript dependency and rollback

`Manuscript Structure Freeze 0.2` remains on HOLD during Climate-B execution and is the mandatory return point after the Climate-B result is integrated/frozen.

Protected rollback points remain:

1. Plasma `P2-A` result freeze;
2. Neuro `NEURO-STRONG` result freeze;
3. Climate-A `CLIM-WEAK` result freeze;
4. Cross-Domain Result Integration & Freeze 0.1;
5. Manuscript Claim Freeze / Draft 0.2;
6. Climate-B Candidate Freeze 0.1;
7. Climate-B Numerical Qualification 0.1;
8. Climate-B Pilot Specification 0.1;
9. this Pilot Freeze 0.1.

No earlier savepoint may be rewritten by the Climate-B outcome.

## 12. Execution release

The next and only authorized Climate action is `Climate Intra-Domain Contrast Pilot Execution 0.1` under the committed MASTER execution prompt.

\[
\boxed{\text{STABLE — EXECUTION RELEASED}}
\]

**STOP.**