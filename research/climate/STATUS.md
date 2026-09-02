# Climate/Ocean Branch Status

## Current state

- **Feasibility Gate 0.1:** passed. Leading candidate: damped two-layer baroclinic Phillips QG model with established QG perturbation energy and signed meridional eddy heat transport.
- **Pilot Candidate Freeze 0.1:** promoted and frozen.
- **Numerical Qualification 0.1:** **QUALIFIED**.

## Frozen pilot objects

The Climate/Ocean pilot uses

\[
(A,M,Q_{\rm heat},B=I,R_{\rm in}=M)
\]

on the balanced two-layer QG eddy state space with zonal periodicity, meridional Dirichlet streamfunction conditions, and all \(k_x=0\) modes excluded.

The primary signed transport observable remains the cumulative meridional eddy heat transport

\[
J_{\rm heat}(T)=\int_0^T x^\dagger Q_{\rm heat}x\,dt.
\]

No CORE optimization has yet been authorized for this branch.

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

Frozen resolution ladder:

\[
(M_x,N_y)=
(4,4),(8,8),(12,12),(16,16),(24,24).
\]

Qualification results:

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

## Explicitly not yet computed

The branch has not computed or inspected

\[
K_E(T),\quad K_{\rm heat}(T),\quad
w_E^\star,\quad w_{\rm heat}^\star,
\]

nor optimizer angles, gaps, objective separation, or any other CORE-effect measure.

## Branch gate

\[
\boxed{\text{NUMERICALLY QUALIFIED; AWAIT NEXT EXPLICIT FREEZE/EXECUTION STEP}}
\]
