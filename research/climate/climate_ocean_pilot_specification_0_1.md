# Climate/Ocean Pilot Specification 0.1

Status: **SPECIFICATION COMPLETE — NOT AUTHORIZED FOR EXECUTION**

This document is the preregistered execution specification for the numerically qualified Climate/Ocean pilot. It uses only the frozen two-layer Phillips-QG candidate and the numerical objects from `Climate/Ocean Numerical Qualification 0.1`.

No CORE-effect operator, optimizer, optimizer angle, gap, or objective separation is constructed or inspected in this document.

## 1. Frozen scope and inherited objects

The physical and numerical inputs remain unchanged:

\[
L_x=3.0\times10^7\,\mathrm m,\qquad
L_y=1.0\times10^7\,\mathrm m,\qquad
L_D=10^6\,\mathrm m,
\]

\[
\beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},\qquad
U=8\,\mathrm{m\,s^{-1}},\qquad
r=(10\,\mathrm d)^{-1}.
\]

The qualified finite-dimensional structure is

\[
\boxed{(A_K,M_K,Q_{{\rm heat},K},B=I,R_{\rm in}=M_K)}.
\]

The signed convention is frozen as

\[
\boxed{+\equiv\text{northward/poleward eddy heat transport}},
\]

and the primary physical transport observable remains

\[
J_{\rm heat}(T)=\int_0^T x(t)^\dagger Q_{{\rm heat},K}x(t)\,dt.
\]

No absolute value, square, or positive heat-flux norm may replace this signed observable.

## 2. Frozen state ordering and Galerkin assembly

Use the already qualified basis

\[
\phi_{mn}(x,y)=
\exp\!\left(i\frac{2\pi m}{L_x}x\right)
\sin\!\left(\frac{\pi n}{L_y}y\right),
\]

with

\[
m\in\{-M_x,\ldots,-1,1,\ldots,M_x\},\qquad n=1,\ldots,N_y.
\]

It exactly enforces zonal periodicity, meridional Dirichlet streamfunction conditions and exclusion of every \(k_x=0\) mode.

The barotropic/baroclinic modal state is

\[
\boxed{x_{mn}=(\psi_{mn},\tau_{mn})^T},
\]

where

\[
\psi=\frac{\psi_1'+\psi_2'}2,\qquad
\tau=\frac{\psi_1'-\psi_2'}2.
\]

The global state is ordered lexicographically in zonal index \(m\), then meridional index \(n\), with \((\psi_{mn},\tau_{mn})\) contiguous. The finite dimension is

\[
N_K=4M_xN_y.
\]

Real physical fields satisfy the exact conjugacy condition

\[
x_{-m,n}=x_{m,n}^*.
\]

The complexified calculation retains both signs of \(m\). Consequently, exact \(\pm m\) conjugacy degeneracies are physical representation degeneracies and must be handled by the subspace rules in Section 10, never by selecting an arbitrary eigenvector.

### 2.1 Nondimensional assembly

Retain

\[
L_{\rm ref}=L_D,\qquad
U_{\rm ref}=\beta L_D^2=16\,\mathrm{m\,s^{-1}},
\]

\[
\boxed{\tau_{\rm ref}=L_D/U_{\rm ref}=62500\,\mathrm s=0.7233796296\,\mathrm d}.
\]

Streamfunction is scaled by \(U_{\rm ref}L_D\). Thus

\[
L_x^*=30,\qquad L_y^*=10,\qquad \beta^*=1,\qquad U^*=\frac12,
\]

\[
r^*=r\tau_{\rm ref}=0.072337962962963.
\]

For every retained mode define

\[
k_m^*=\frac{2\pi m}{30},\qquad
\ell_n^*=\frac{\pi n}{10},
\]

\[
a_{mn}=k_m^{*2}+\ell_n^{*2},\qquad b_{mn}=a_{mn}+1,
\]

and \(S^*=L_x^*L_y^*/2=150\).

The frozen matrices are assembled blockwise as

\[
A_{mn}=
\begin{pmatrix}
-r^*+i k_m^*/a_{mn} & -i k_m^*U^*\\[1mm]
 i k_m^*U^*(1-a_{mn})/b_{mn} & -r^*+i k_m^*/b_{mn}
\end{pmatrix},
\]

\[
M_{mn}=S^*
\begin{pmatrix}
a_{mn}&0\\
0&b_{mn}
\end{pmatrix},
\]

\[
Q_{{\rm heat},mn}=\frac{S^*}{2}
\begin{pmatrix}
0&-i k_m^*\\
 i k_m^*&0
\end{pmatrix},
\]

and

\[
A_K=\operatorname{blockdiag}A_{mn},\qquad
M_K=\operatorname{blockdiag}M_{mn},\qquad
Q_{{\rm heat},K}=\operatorname{blockdiag}Q_{{\rm heat},mn}.
\]

The positive square-root inverse used later is not obtained by a generic `sqrtm`; it is assembled analytically,

\[
M_{mn}^{-1/2}=\frac1{\sqrt{S^*}}
\begin{pmatrix}
a_{mn}^{-1/2}&0\\0&b_{mn}^{-1/2}
\end{pmatrix}.
\]

## 3. Frozen resolution roles

The qualified ladder is not changed:

\[
(4,4),(8,8),(12,12),(16,16),(24,24).
\]

Before any CORE-effect calculation, its roles are frozen as follows.

| role | \((M_x,N_y)\) | dimension | use |
|---|---:|---:|---|
| qualification-only smoke rung | \((4,4)\) | 64 | structural sanity only; never used to rescue or define a pilot verdict |
| coarse audit | \((8,8)\) | 256 | convergence trend and modal-support audit |
| **primary** | \(\boxed{(12,12)}\) | 576 | canonical reported pilot result |
| **confirmation** | \(\boxed{(16,16)}\) | 1024 | mandatory independent refinement check |
| **high-resolution audit** | \(\boxed{(24,24)}\) | 2304 | final nested refinement audit |

The primary choice is fixed solely as the middle qualified resolution with two finer preregistered checks and one coarser audit. It is not based on any unobserved CORE effect.

No additional rung may be introduced after execution starts.

## 4. Frozen horizon ladder

Use exactly

\[
\boxed{T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}}.
\]

The corresponding dimensional horizons are approximately

\[
T\in\{0.1808449074,\,0.3616898148,\,0.7233796296,\,1.4467592592,\,2.8935185184,\,5.7870370368\}\,\mathrm d.
\]

No horizon may be added, removed or shifted after optimizer separation is inspected.

## 5. Preregistered finite-time operators — definitions only

Execution, if later authorized by MASTER, will use the shared cross-domain definitions

\[
K_E(T)=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2},
\]

\[
G_E(T)=\lambda_{\max}(K_E(T)),
\]

and

\[
K_{\rm heat}(T)=M_K^{-1/2}H_K(T)M_K^{-1/2},
\]

with

\[
H_K(T)=\int_0^T e^{A_K^\dagger t}Q_{{\rm heat},K}e^{A_Kt}\,dt.
\]

The signed extrema to be reported are

\[
J_{\rm heat}^{+}(T)=\lambda_{\max}(K_{\rm heat}(T)),\qquad
J_{\rm heat}^{-}(T)=\lambda_{\min}(K_{\rm heat}(T)).
\]

The positive/poleward branch is primary. These formulas are preregistered here but are **not evaluated in this specification**.

## 6. Exact finite-time numerical method

The modal block structure must be used rather than forming unnecessarily dense global propagators.

### 6.1 Matrix exponential

For each \((m,n)\) and each fixed nondimensional horizon \(T^*=T/\tau_{\rm ref}\), compute

\[
E_{mn}(T)=\exp(A_{mn}T^*)
\]

with a backward-stable scaling-and-squaring Padé matrix exponential in complex double precision (`scipy.linalg.expm` or a numerically equivalent implementation). No time-stepping approximation is used for the propagator.

The global propagator, when needed for checks, is the block diagonal matrix of the modal exponentials.

### 6.2 Cumulative heat integral without time quadrature

For a modal block define

\[
H_{mn}(T)=\int_0^{T^*}e^{A_{mn}^\dagger t}Q_{{\rm heat},mn}e^{A_{mn}t}\,dt.
\]

Vectorization in column-major convention gives

\[
\frac{d}{dt}\operatorname{vec}H
=
\mathcal L_{mn}\operatorname{vec}H+q_{mn},
\]

with

\[
\mathcal L_{mn}=I_2\otimes A_{mn}^\dagger+A_{mn}^T\otimes I_2,
\qquad
q_{mn}=\operatorname{vec}(Q_{{\rm heat},mn}).
\]

Freeze the primary integral method as the augmented exponential

\[
\mathcal C_{mn}=
\begin{pmatrix}
\mathcal L_{mn}&q_{mn}\\
0_{1\times4}&0
\end{pmatrix}\in\mathbb C^{5\times5},
\]

\[
\boxed{
\operatorname{vec}H_{mn}(T)
=
\left[\exp(\mathcal C_{mn}T^*)\right]_{1:4,5}.
}
\]

This is the primary quadrature-free finite-time integral. Assemble

\[
H_K(T)=\operatorname{blockdiag}H_{mn}(T).
\]

### 6.3 Independent integral cross-check

Because every qualified \(A_{mn}\) is asymptotically stable, independently solve

\[
A_{mn}^\dagger X_{mn}+X_{mn}A_{mn}=-Q_{{\rm heat},mn}
\]

and verify

\[
H_{mn}(T)=X_{mn}-E_{mn}(T)^\dagger X_{mn}E_{mn}(T).
\]

This Lyapunov-tail identity is a check only, not a replacement chosen after seeing results.

A third direct-trajectory quadrature check is specified in Section 8.

## 7. Fixed algebraic numerical checks

All checks below are evaluated before interpreting any optimizer separation.

Define the relative Hermiticity residual

\[
\eta_H(K)=\frac{\|K-K^\dagger\|_F}{\max(1,\|K\|_F)}.
\]

Requirement:

\[
\boxed{\eta_H(K_E),\eta_H(K_{\rm heat})\le10^{-11}}.
\]

No matrix may be silently symmetrized if this gate fails. If the residual passes, the eigensolver may use \((K+K^\dagger)/2\) solely to remove floating-point antisymmetric roundoff; the applied correction norm must be recorded.

For every reported extremal eigenpair \((\lambda,w)\), require

\[
\eta_{\rm eig}
=
\frac{\|Kw-\lambda w\|_2}
{\max(1,\|K\|_2,|\lambda|)}
\le10^{-10},
\]

\[
|w^\dagger w-1|\le10^{-12},
\]

and Rayleigh reproduction

\[
\eta_R=
\frac{|w^\dagger Kw-\lambda|}{\max(1,|\lambda|)}\le10^{-11}.
\]

For the energy operator additionally require positive semidefiniteness within roundoff:

\[
\lambda_{\min}(K_E)\ge-10^{-11}\max(1,\|K_E\|_2).
\]

For the signed heat operator, no positivity condition is imposed.

## 8. Direct trajectory and integration checks

For every horizon used in a final verdict, reconstruct the physical initial state from a normalized whitened vector or optimal subspace representative by

\[
x_0=M_K^{-1/2}w.
\]

Evaluate trajectories independently as

\[
x(t)=e^{A_Kt}x_0.
\]

For heat transport, compute

\[
J_{\rm direct}=\int_0^T x(t)^\dagger Q_{{\rm heat},K}x(t)\,dt
\]

using adaptive Gauss-Kronrod quadrature with relative tolerance \(10^{-10}\) and absolute tolerance \(10^{-12}\). Require agreement with the quadratic-operator value

\[
J_{\rm op}=w^\dagger K_{\rm heat}(T)w
\]

at

\[
\boxed{
\frac{|J_{\rm direct}-J_{\rm op}|}{\max(10^{-12},|J_{\rm direct}|,|J_{\rm op}|)}\le10^{-8}.
}
\]

For the energy objective independently verify

\[
G_{\rm direct}=x(T)^\dagger M_Kx(T)
\]

against \(w^\dagger K_E(T)w\) with the same \(10^{-8}\) relative criterion, given \(x_0^\dagger M_Kx_0=1\).

The deterministic signed-flux reproduction test from Numerical Qualification 0.1 remains a prerequisite and is not redefined.

## 9. Resolution-robustness protocol

Resolution robustness is evaluated only after each individual resolution passes Section 7.

### 9.1 Objective values

For \(Y\in\{G_E,J_{\rm heat}^{+},|J_{\rm heat}^{-}|\}\), define adjacent refinement discrepancy

\[
\epsilon_Y(K_1,K_2)
=
\frac{|Y_{K_2}-Y_{K_1}|}
{\max(10^{-12},|Y_{K_2}|,|Y_{K_1}|)}.
\]

The primary/confirmation and confirmation/high-audit pairs must satisfy

\[
\boxed{\epsilon_Y\le0.02}
\]

at a horizon before that horizon can support a resolution-robust pilot claim. The \((8,8)\) coarse audit is reported as a convergence trend but is not itself a pass/fail gate. The \((4,4)\) rung is never used for the effect verdict.

### 9.2 Optimizer/subspace comparison on a common modal space

Cross-resolution vectors are never compared by padding and taking a raw angle.

For a lower/higher pair, let \(P_c\) project the higher-resolution state onto the modal subspace retained by the lower resolution. If \(W_H\) is an orthonormal basis of the higher optimal eigenspace, define the captured common-space mass

\[
\mu_c=\frac1d\operatorname{tr}(W_H^\dagger P_cW_H),
\qquad d=\dim W_H.
\]

Require

\[
\boxed{\mu_c\ge0.95}.
\]

Orthonormalize \(P_cW_H\) and compare it with the lower optimal subspace \(W_L\) through principal angles. The optimal-subspace ranks must agree and the largest principal angle must obey

\[
\boxed{\theta_{\max}^{\rm res}\le10^\circ}.
\]

These conditions are applied separately to the energy-optimal and positive-heat-optimal subspaces for primary/confirmation and confirmation/high-audit pairs.

If a newly admitted high-wavenumber mode captures the optimum so that \(\mu_c<0.95\), if optimal-subspace rank changes, or if the principal-angle criterion fails, the corresponding horizon is **not resolution robust**. No parameter, horizon or extra resolution may then be introduced to repair the outcome.

### 9.3 Minimum robust horizon support

A branch-level physical verdict requires at least two neighboring horizons on the frozen ladder that pass both objective-value and optimizer/subspace robustness from primary through high-resolution audit. Otherwise the branch verdict is `CLIM-RESOLUTION-FAIL` regardless of same-resolution separation.

## 10. Degeneracy rule

For any Hermitian objective matrix with leading eigenvalue \(\lambda_1\), define the optimal cluster by

\[
|\lambda_j-\lambda_1|
\le
\delta_{\rm deg}\max(1,|\lambda_1|),
\qquad
\boxed{\delta_{\rm deg}=10^{-8}}.
\]

The span of all eigenvectors in this cluster is the optimal subspace. Exact \(\pm m\) conjugacy partners therefore remain together.

No arbitrary member of a degenerate optimal subspace may be used to establish optimizer separation.

### 10.1 Same-resolution objective separation under degeneracy

If both optima are nondegenerate, use the preregistered vector angle

\[
\vartheta(T)=\arccos|{w_E^\star}^\dagger w_{\rm heat}^\star|.
\]

If either optimum is degenerate, replace this by the conservative smallest principal angle between optimal subspaces,

\[
\boxed{
\vartheta_{\rm sub}(T)=
\arccos\sigma_{\max}(W_E^\dagger W_{\rm heat}).
}
\]

Thus a large angle can be claimed only when **every** admissible choice of aligned optimal directions remains separated by at least that conservative angle.

For the heat-performance gap, if the energy optimum is degenerate, use the energy-optimal vector that performs best on heat transport:

\[
J_{{\rm heat}|E}^{\rm best}
=
\lambda_{\max}(W_E^\dagger K_{\rm heat}W_E),
\]

and define

\[
\boxed{
\Delta_{\rm heat}^{\rm sub}(T)=
\frac{J_{\rm heat}^{+}(T)-J_{{\rm heat}|E}^{\rm best}(T)}
{J_{\rm heat}^{+}(T)}.
}
\]

This is conservative and reduces to the preregistered vector formula in the nondegenerate case.

The gap denominator is considered safely nonzero only if

\[
J_{\rm heat}^{+}>
\max\left(10^{-12},10^4\epsilon_{\rm mach}\|K_{\rm heat}\|_2\right).
\]

Otherwise the gap is reported as undefined at that horizon and cannot support a demonstration verdict.

## 11. Preregistered physical optimizer diagnostics

Only after execution is authorized, and only after the numerical gates above pass, reconstruct physical initial conditions

\[
x_0=M_K^{-1/2}w.
\]

For each energy- and positive-heat-optimal solution/subspace report:

1. **barotropic energy fraction**
   \[
   f_{\rm BT}=\frac{\sum_{m,n}S^*a_{mn}|\psi_{mn}|^2}
   {\sum_{m,n}S^*[a_{mn}|\psi_{mn}|^2+b_{mn}|\tau_{mn}|^2]};
   \]
2. **baroclinic energy fraction** \(f_{\rm BC}=1-f_{\rm BT}\);
3. combined conjugate-pair zonal modal weights as functions of \(|m|\);
4. meridional modal weights as functions of \(n\);
5. dominant layer structure reconstructed from
   \[
   \psi_1'=\psi+\tau,\qquad \psi_2'=\psi-\tau;
   \]
6. relative barotropic/baroclinic phase \(\arg(\tau_{mn}/\psi_{mn})\) for dominant modes, with phase omitted where either amplitude is below numerical relevance;
7. dominant signed modal contributions to the instantaneous and cumulative heat flux.

All \(+m/-m\) partner weights are combined before physical interpretation so diagnostics are invariant under the arbitrary complex representation of a real field.

For a degenerate optimal subspace, report projector/subspace-invariant modal weights and ranges over the optimal subspace rather than an arbitrary eigenvector picture.

## 12. Shared demonstration metrics and thresholds

The positive/poleward branch is primary. At each safely nonzero, numerically valid and resolution-robust horizon report the same-resolution optimizer/subspace angle and heat-performance gap.

The inherited project-level operational thresholds are frozen as

\[
\boxed{\vartheta\ge20^\circ},\qquad
\boxed{\Delta_{\rm heat}\ge0.25}.
\]

For degenerate optima, \(\vartheta\) means the conservative subspace angle and \(\Delta_{\rm heat}\) means the conservative subspace gap defined above.

A strong demonstration requires both thresholds at **at least two neighboring horizons on the fixed ladder**, and the same neighboring horizon pair must remain above threshold at primary, confirmation and high-resolution audit while satisfying Section 9.

These are project-level operational demonstration thresholds. They are **not universal climate-physics thresholds**, not significance levels, and not fitted to this model.

## 13. Frozen verdict classes

Verdicts are assigned with the following precedence. No class may be redefined after execution.

### `CLIM-NUMERICAL-FAIL`

Any mandatory Hermiticity, eigenresidual, normalization, Rayleigh-quotient, PSD, finite-time-integral cross-check or direct trajectory/integration check fails at primary, confirmation or high-resolution audit for horizons needed for interpretation.

No physical separation claim is then made.

### `CLIM-RESOLUTION-FAIL`

Per-resolution calculations are numerically valid, but fewer than two neighboring fixed horizons satisfy the complete objective-value and optimizer/subspace robustness criteria from primary through high-resolution audit.

A large separation seen only at one resolution is retained as a non-robust result and must not trigger retuning.

### `CLIM-TRANSPORT-NULL`

Numerically and resolution-valid horizons exist, but \(J_{\rm heat}^{+}\) is not safely positive/nonzero at any robust horizon according to the fixed denominator rule. The signed transport channel is therefore uninformative for this pilot realization.

### `CLIM-STRONG`

At least two neighboring fixed horizons are numerically valid and resolution robust and, at the same neighboring pair on primary, confirmation and high audit,

\[
\vartheta\ge20^\circ,\qquad \Delta_{\rm heat}\ge0.25.
\]

### `CLIM-WEAK`

The computation is numerically valid, resolution robust and has safely positive \(J_{\rm heat}^{+}\), but `CLIM-STRONG` is not met, while at least one robust horizon has a resolvable objective dependence

\[
\vartheta\ge5^\circ\quad\text{or}\quad \Delta_{\rm heat}\ge0.05.
\]

This includes one-horizon-only threshold crossings and cases where only one of the two strong thresholds is met.

### `CLIM-NULL`

The computation is numerically valid, resolution robust and has safely positive \(J_{\rm heat}^{+}\), but at every robust horizon

\[
\vartheta<5^\circ\qquad\text{and}\qquad\Delta_{\rm heat}<0.05.
\]

This records an operationally negligible Energy-vs-Heat distinction at the frozen pilot settings; it does not imply a universal equality theorem.

## 14. Anti-bias rules

After this specification is committed:

- physical parameters \(L_x,L_y,L_D,\beta,U,r\) are immutable for Pilot 0.1;
- the basis, state ordering, heat-flux sign and \(B=I,R_{\rm in}=M_K\) are immutable;
- the resolution roles and horizon ladder are immutable;
- no horizon or resolution may be selected because separation is favorable there;
- no new resolution rung may be added because an optimizer fails convergence;
- heat transport may not be converted into a positive norm;
- a resolution failure, weak result or null result must be retained as the result;
- no parameter retuning is permitted after seeing a CORE effect.

## 15. Execution authorization boundary

This specification is complete, but execution is **not self-authorized**.

In particular, this document has not computed or inspected

\[
K_E(T),\quad K_{\rm heat}(T),\quad
w_E^\star,\quad w_{\rm heat}^\star,
\]

\[
\vartheta(T),\quad\Delta_{\rm heat}(T),\quad
G_E(T),\quad J_{\rm heat}^{\pm}(T),
\]

or any related CORE-effect measure.

The branch must return to MASTER for a Pilot Freeze/Execution authorization.

\[
\boxed{\text{Climate/Ocean Pilot Specification 0.1: COMPLETE}}
\]

\[
\boxed{\text{NO CLIMATE CORE OPTIMIZATION AUTHORIZED HERE}}
\]

**STOP.**
