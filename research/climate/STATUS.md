# Climate/Ocean Branch Status

## Current state

- **Feasibility Gate 0.1:** passed. Leading candidate: damped two-layer baroclinic Phillips QG model with established QG perturbation energy and signed meridional eddy heat transport.
- **Pilot Candidate Freeze 0.1:** promoted and frozen.
- **Numerical Qualification 0.1:** **QUALIFIED**.
- **Cross-Domain Integration Gate 0.1:** **PASSED**.
- **Pilot Specification 0.1:** **COMPLETE**.

## Frozen pilot objects

The Climate/Ocean pilot uses

\[
(A_K,M_K,Q_{{\rm heat},K},B=I,R_{\rm in}=M_K)
\]

on the balanced two-layer QG eddy state space with zonal periodicity, meridional Dirichlet streamfunction conditions, and all \(k_x=0\) modes excluded.

The primary signed transport observable remains the cumulative meridional eddy heat transport

\[
J_{\rm heat}(T)=\int_0^T x^\dagger Q_{{\rm heat},K}x\,dt,
\]

with positive sign fixed as northward/poleward transport.

## Numerical qualification freeze

Canonical qualification document:

`research/climate/climate_ocean_numerical_qualification_0_1.md`

Frozen nondimensionalization:

\[
L_{\rm ref}=L_D=1000\ {\rm km},\qquad
U_{\rm ref}=\beta L_D^2=16\ {\rm m\,s^{-1}},
\]

\[
\tau_{\rm ref}=L_D/U_{\rm ref}=62500\ {\rm s}=0.7233796296\ {\rm d}.
\]

Frozen qualified resolution ladder:

\[
(M_x,N_y)=(4,4),(8,8),(12,12),(16,16),(24,24).
\]

Qualification results remain:

- \(M_K=M_K^\dagger\succ0\): PASS.
- \(Q_{{\rm heat},K}=Q_{{\rm heat},K}^\dagger\): PASS.
- \(Q_{{\rm heat},K}\) indefinite and signed: PASS.
- Direct heat-flux reproduction by \(x^\dagger Q_{{\rm heat},K}x\): PASS.
- Spectral stability at every fixed resolution:
  \[
  \alpha(A_K)=-0.072337962962963=-0.1\ {\rm d}^{-1}<0.
  \]
- Common-mode spectral convergence on the nested ladder: machine precision, \(\delta_{\rm spec}<10^{-14}\).
- No physical parameter retuning performed.

## Pilot Specification 0.1 freeze

Canonical specification document:

`research/climate/climate_ocean_pilot_specification_0_1.md`

Resolution roles are now frozen before any CORE-effect calculation:

- qualification-only smoke: \((4,4)\);
- coarse audit: \((8,8)\);
- **primary:** \((12,12)\);
- **confirmation:** \((16,16)\);
- **high-resolution audit:** \((24,24)\).

The inherited fixed horizon ladder is

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

The finite-time numerical method is preregistered as blockwise scaling-and-squaring Padé matrix exponentials and a blockwise augmented \(5\times5\) matrix exponential for the cumulative heat integral, with an independent stable Lyapunov-tail identity and direct trajectory/quadrature checks.

The specification also freezes:

- Hermiticity, eigenresidual, normalization, Rayleigh-quotient and direct integration tolerances;
- objective-value convergence and common-modal-subspace optimizer robustness criteria;
- exact degeneracy handling through optimal eigenspaces/projectors and principal angles;
- physical optimizer diagnostics using barotropic/baroclinic energy fractions, modal weights, layer structure and relative phases;
- project-level demonstration thresholds
  \[
  \vartheta\ge20^\circ,\qquad \Delta_{\rm heat}\ge0.25
  \]
  at at least two neighboring fixed horizons;
- verdict classes `CLIM-STRONG`, `CLIM-WEAK`, `CLIM-NULL`, `CLIM-TRANSPORT-NULL`, `CLIM-RESOLUTION-FAIL`, and `CLIM-NUMERICAL-FAIL`.

The \(20^\circ\) and \(0.25\) thresholds are project-level operational thresholds, not universal climate-physics thresholds.

## Explicitly not yet computed

The branch has still not constructed, computed or inspected

\[
K_E(T),\quad K_{\rm heat}(T),\quad
w_E^\star,\quad w_{\rm heat}^\star,
\]

nor optimizer angles, gaps, objective separation, transient gain, transport extrema or any other CORE-effect measure.

## Next instruction

`RETURN TO MASTER FOR PILOT FREEZE`

The Climate/Ocean branch must not self-authorize execution. A later MASTER instruction is required before any CORE optimization or effect operator is constructed.

## Branch gate

\[
\boxed{\text{PILOT SPECIFICATION COMPLETE; RETURN TO MASTER}}
\]

\[
\boxed{\text{NO CLIMATE CORE OPTIMIZATION AUTHORIZED}}
\]

## Canonical documents

- `research/climate/climate_ocean_numerical_qualification_0_1.md`
- `research/climate/climate_ocean_pilot_specification_0_1.md`
- `research/master/cross_domain_integration_gate_0_1.md`
- `research/master/prompts/climate_ocean_pilot_specification_0_1.md`
- `research/master/prompt_handoff_protocol_0_1.md`
