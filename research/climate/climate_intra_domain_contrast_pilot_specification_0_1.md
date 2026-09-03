# Climate Intra-Domain Contrast Pilot Specification 0.1

**Status:** `SPECIFICATION COMPLETE — NOT AUTHORIZED FOR EXECUTION`  
**Authority:** `research/master/prompts/climate_intra_domain_contrast_pilot_specification_0_1.md`  
**Scope:** pre-effect specification only. This file freezes the future Climate-B finite-time execution protocol without evaluating any finite-time objective, optimizer, angle, performance gap, horizon dependence, or verdict.

Climate-A remains permanently frozen as `CLIM-WEAK` and is not reopened, retuned, replaced, or relabeled here.

---

## 1. Frozen Climate-B model and representation

Climate-B remains exactly the numerically qualified equivalent-barotropic Bickley-jet candidate

\[
\partial_t\zeta' + U(y)\partial_x\zeta' + [\beta-U''(y)]\partial_x\psi'=-r\zeta',
\qquad \zeta'=\nabla^2\psi',
\]

\[
U(y)=U_0\operatorname{sech}^2((y-y_0)/L),
\qquad y_0=0.
\]

The dimensional point is immutable:

\[
\beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},\qquad
U_0=20\,\mathrm{m\,s^{-1}},\qquad
L=1000\,\mathrm{km},
\]

\[
r=(10\,\mathrm d)^{-1},\qquad
L_x=20000\,\mathrm{km},\qquad
L_y=10000\,\mathrm{km}.
\]

The nondimensionalization is also immutable:

\[
L_{\rm ref}=L,\qquad U_{\rm ref}=U_0,
\qquad
\boxed{\tau_{\rm ref}=L/U_0=50000\,\mathrm s=0.5787037037\,\mathrm d}.
\]

Thus

\[
L_x^*=20,\qquad L_y^*=10,\qquad \beta^*=0.8,
\qquad r^*=0.05787037037037.
\]

Use only the frozen positive-zonal-Fourier / centered-sine Galerkin representation. For

\[
k_m^*=\frac{2\pi m}{20},\qquad m=1,\ldots,M_x,
\]

and

\[
\phi_n(y^*)=\sqrt{\frac{2}{10}}
\sin\!\left[\frac{n\pi(y^*+5)}{10}\right],
\qquad n=1,\ldots,N_y,
\]

write

\[
f_m(y^*,t^*)=\sum_{n=1}^{N_y}c_{mn}(t^*)\phi_n(y^*),
\]

with real-field reconstruction

\[
\psi'^*(x^*,y^*,t^*)=
\sum_{m=1}^{M_x}\left[f_m e^{ik_m^*x^*}+f_m^*e^{-ik_m^*x^*}\right].
\]

The global complex state ordering remains

\[
\boxed{x_K=(c_1^T,c_2^T,\ldots,c_{M_x}^T)^T},
\qquad
c_m=(c_{m1},\ldots,c_{mN_y})^T.
\]

The matrices \(A_K\), \(M_K\), and \(Q_{{\rm shift},K}\) are exactly those frozen in Candidate Freeze 0.1 and qualified in Numerical Qualification 0.1. All coefficient integrals remain assembled with 512-point Gauss-Legendre quadrature with the frozen 1024-point audit. No new quadrature, basis, mask, EOF, localization, or forcing coordinate may be substituted.

The admissible-input geometry remains

\[
\boxed{B=I,\qquad R_{\rm in}=M_K}.
\]

The signed channel remains the eddy forcing of the infinitesimal jet-translation tangent

\[
g(y)=-U'(y),
\]

with

\[
q_{\rm shift}(t)=
\frac{\int g(y)[-\partial_y\overline{u'v'}]dy}{\int g(y)^2dy},
\]

and positive sign fixed as projection onto a poleward translation.

The Numerical Qualification result is inherited without repetition:

\[
\alpha(A_K)=-0.05787037037037=-0.1\,\mathrm d^{-1}<0
\]

at every frozen resolution, with all structural, parity, quadrature, sign-witness, conditioning and eigensolver gates passed.

---

## 2. Frozen resolution roles

The nested ladder and its roles remain exactly

| role | \((M_x,N_y)\) | complex dimension |
|---|---:|---:|
| structural smoke | \((8,16)\) | 128 |
| coarse audit | \((12,24)\) | 288 |
| **primary** | \(\boxed{(16,32)}\) | 512 |
| **confirmation** | \(\boxed{(20,40)}\) | 800 |
| **high-resolution audit** | \(\boxed{(24,48)}\) | 1152 |

The smoke rung is structural only. The coarse rung is a convergence trend/audit. The canonical effect result, if later authorized, is the primary rung, and every claim relevant to the verdict must survive the confirmation and high-resolution audit under the rules below.

No rung may be added, removed, or reassigned after execution begins.

---

## 3. Frozen horizon ladder

Before any Climate-B finite-time effect is inspected, freeze exactly

\[
\boxed{T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.}
\]

With \(\tau_{\rm ref}=50000\,\mathrm s\), the six dimensional horizons are

\[
\boxed{T\in\{12500,25000,50000,100000,200000,400000\}\,\mathrm s}
\]

or equivalently

\[
T\in\{0.1446759259,0.2893518519,0.5787037037,
1.1574074074,2.3148148148,4.6296296296\}\,\mathrm d.
\]

All six horizons must be reported in any later execution. No interpolation, extra horizon, shifted horizon, or post-hoc subset may be introduced to strengthen a result.

---

## 4. Frozen finite-time operators — definitions only

Because \(B=I\) and \(R_{\rm in}=M_K\), whitened initial coordinates are

\[
x(0)=M_K^{-1/2}w,\qquad \|w\|_2=1.
\]

The positive terminal perturbation-energy operator is

\[
\boxed{
K_M(T)=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2}.
}
\]

Define

\[
\boxed{G_M(T)=\lambda_{\max}(K_M(T)).}
\]

The signed cumulative jet-translation-forcing operator is

\[
P_{\rm shift}(T)=\int_0^T e^{A_K^\dagger t}Q_{{\rm shift},K}e^{A_Kt}\,dt,
\]

\[
\boxed{
K_{\rm shift}(T)=M_K^{-1/2}P_{\rm shift}(T)M_K^{-1/2}.
}
\]

Its mandatory signed extrema are

\[
\boxed{J_{\rm shift}^{+}(T)=\lambda_{\max}(K_{\rm shift}(T))},
\]

\[
\boxed{J_{\rm shift}^{-}(T)=\lambda_{\min}(K_{\rm shift}(T))}.
\]

The positive branch is the poleward-translation-forcing optimum; the negative branch is the equatorward-translation-forcing optimum. Both must be reported.

Interpretation remains restricted: \(J_{\rm shift}\) is cumulative eddy impulse/forcing of the infinitesimal translation coordinate under the frozen tangent dynamics. It is not the realized displacement of a nonlinear coupled jet and must not be described as a predicted climate-change jet shift.

No operator or eigenvalue in this section is evaluated in this specification.

---

## 5. Frozen optimizer and objective-separation diagnostics

Let \(w_M^\star\) denote a normalized terminal-energy optimum and \(w_{\rm shift}^\star\) a normalized positive shift-forcing optimum in whitened coordinates.

### 5.1 Degeneracy rule

For any Hermitian objective matrix with leading eigenvalue \(\lambda_1\), define the leading optimal cluster by

\[
|\lambda_j-\lambda_1|
\le
\delta_{\rm deg}\max(1,|\lambda_1|),
\qquad
\boxed{\delta_{\rm deg}=10^{-8}}.
\]

The span of the clustered eigenvectors is the optimal subspace. No arbitrary eigenvector from a degenerate optimum may be used to manufacture or suppress separation.

### 5.2 Same-resolution angle

For nondegenerate one-dimensional optima,

\[
\boxed{
\vartheta(T)=\arccos\left|w_M^{\star\dagger}w_{\rm shift}^\star\right|.
}
\]

If either optimum is degenerate, use the conservative smallest principal angle

\[
\boxed{
\vartheta_{\rm sub}(T)=
\arccos\sigma_{\max}(W_M^\dagger W_{\rm shift}),
}
\]

where \(W_M\) and \(W_{\rm shift}\) are orthonormal bases of the optimal subspaces.

### 5.3 Target-performance gap

For a nondegenerate energy optimum,

\[
\boxed{
\Delta_{\rm shift}(T)=
\frac{J_{\rm shift}^{+}(T)-w_M^{\star\dagger}K_{\rm shift}(T)w_M^\star}
{J_{\rm shift}^{+}(T)}.
}
\]

If the energy optimum is degenerate, use the energy-optimal direction that performs best on the shift channel,

\[
J_{{\rm shift}|M}^{\rm best}
=\lambda_{\max}(W_M^\dagger K_{\rm shift}W_M),
\]

and

\[
\boxed{
\Delta_{\rm shift}^{\rm sub}(T)=
\frac{J_{\rm shift}^{+}(T)-J_{{\rm shift}|M}^{\rm best}(T)}
{J_{\rm shift}^{+}(T)}.
}
\]

This conservative rule prevents a degenerate positive-energy subspace from appearing artificially separated because of an arbitrary basis vector.

The denominator is safely nonzero only if

\[
\boxed{
J_{\rm shift}^{+}(T)>
\max\left(10^{-12},10^4\epsilon_{\rm mach}\|K_{\rm shift}(T)\|_2\right).
}
\]

If this condition fails, \(\Delta_{\rm shift}\) is reported as undefined/uninterpretable at that horizon. No regularization or modified denominator is allowed.

---

## 6. Frozen numerical execution method

All following choices are made before effect inspection.

### 6.1 Matrix propagation

Exploit the exact zonal block structure

\[
A_K=\operatorname{blockdiag}_{m=1}^{M_x}A_m.
\]

At each frozen nondimensional horizon \(T^*=T/\tau_{\rm ref}\), compute

\[
E_m(T)=e^{A_mT^*}
\]

using a backward-stable scaling-and-squaring Padé matrix exponential in complex IEEE double precision (`scipy.linalg.expm` or a numerically equivalent implementation). No time-stepping approximation is used to define the finite-time propagator.

The inverse energy square root is assembled analytically from the diagonal positive \(M_m\); a generic matrix square-root routine is not used.

### 6.2 Primary cumulative signed-operator method: Lyapunov tail

Numerical Qualification established that every \(A_m\) is asymptotically stable. For each zonal block solve the continuous Lyapunov/Sylvester equation

\[
\boxed{
A_m^\dagger X_m+X_mA_m=-Q_{{\rm shift},m}
}
\]

in complex double precision, and form

\[
\boxed{
P_{{\rm shift},m}(T)
=X_m-E_m(T)^\dagger X_mE_m(T).
}
\]

This identity is the primary quadrature-free finite-time integral method. The global cumulative operator is assembled blockwise.

### 6.3 Independent block-exponential cross-check

Independently form for each \(m\)

\[
\mathcal V_m=
\begin{pmatrix}
-A_m^\dagger & Q_{{\rm shift},m}\\
0&A_m
\end{pmatrix}
\]

and compute

\[
\exp(\mathcal V_mT^*)=
\begin{pmatrix}
E_m(T)^{-\dagger}&Y_m(T)\\
0&E_m(T)
\end{pmatrix}.
\]

The independent cumulative block is then

\[
\boxed{
P_{{\rm shift},m}^{\rm V}(T)=E_m(T)^\dagger Y_m(T).
}
\]

Require agreement between the primary Lyapunov-tail result and this Van-Loan-type block-exponential result at

\[
\boxed{
\frac{\|P_{{\rm shift},m}-P_{{\rm shift},m}^{\rm V}\|_F}
{\max(1,\|P_{{\rm shift},m}\|_F,\|P_{{\rm shift},m}^{\rm V}\|_F)}
\le10^{-10}
}
\]

for every block used in primary, confirmation, and high-resolution verdict calculations.

### 6.4 Algebraic finite-time gates

For either finite-time Hermitian operator \(K\), define

\[
\eta_H(K)=\frac{\|K-K^\dagger\|_F}{\max(1,\|K\|_F)}.
\]

Require

\[
\boxed{\eta_H(K_M),\eta_H(K_{\rm shift})\le10^{-11}}.
\]

No matrix may be silently symmetrized before this gate passes. After passing, \((K+K^\dagger)/2\) may be used only to remove floating-point antisymmetric roundoff, and the correction norm must be recorded.

For every reported extremal eigenpair \((\lambda,w)\), require

\[
\boxed{
\eta_{\rm eig}
=\frac{\|Kw-\lambda w\|_2}
{\max(1,\|K\|_2,|\lambda|)}\le10^{-10},
}
\]

\[
\boxed{|w^\dagger w-1|\le10^{-12}},
\]

and

\[
\boxed{
\eta_R=\frac{|w^\dagger Kw-\lambda|}{\max(1,|\lambda|)}\le10^{-11}.
}
\]

For the positive terminal-energy operator additionally require

\[
\boxed{
\lambda_{\min}(K_M)\ge-10^{-11}\max(1,\|K_M\|_2).
}
\]

No positivity requirement is imposed on the signed \(K_{\rm shift}\).

---

## 7. Direct physical-trajectory reproduction checks

For every horizon that contributes to the final verdict, and at primary, confirmation, and high-resolution audit, reconstruct

\[
x_0=M_K^{-1/2}w,
\qquad
x(t)=e^{A_Kt}x_0.
\]

### 7.1 Terminal energy

Independently evaluate terminal perturbation kinetic energy from the frozen modal coefficients,

\[
E_{\rm direct}(T)=\frac12x(T)^\dagger M_Kx(T),
\]

and, for the representative physical-space reconstruction, verify the same kinetic energy by direct spatial evaluation of \(|\nabla\psi'|^2/2\) using the frozen Fourier representation and 1024-point Gauss-Legendre meridional quadrature.

Compare the normalized operator value against the corresponding direct gain with relative discrepancy no larger than

\[
\boxed{10^{-8}}.
\]

### 7.2 Cumulative signed shift forcing

Independently reconstruct the real perturbation, compute the zonal-mean Reynolds stress

\[
\overline{u'v'}(y,t),
\]

then evaluate the physical channel directly from

\[
q_{\rm shift}(t)=
\frac{\int g'(y)\overline{u'v'}(y,t)\,dy}{\int g(y)^2dy}
\]

using 1024-point Gauss-Legendre meridional quadrature. Integrate this scalar time history using adaptive Gauss-Kronrod quadrature with relative tolerance \(10^{-10}\) and absolute tolerance \(10^{-12}\).

Require

\[
\boxed{
\frac{|J_{\rm direct}-w^\dagger K_{\rm shift}(T)w|}
{\max(10^{-12},|J_{\rm direct}|,|w^\dagger K_{\rm shift}(T)w|)}
\le10^{-8}.
}
\]

The deterministic \(m=1,c_{11}=1,c_{12}=\pm i\) instantaneous sign witness from Numerical Qualification remains a prerequisite and is not redefined.

---

## 8. Frozen resolution-robustness protocol

Resolution robustness is assessed only after the per-resolution algebraic gates pass.

### 8.1 Objective values

For

\[
Y\in\{G_M,J_{\rm shift}^{+},|J_{\rm shift}^{-}|\},
\]

define

\[
\epsilon_Y(K_1,K_2)=
\frac{|Y_{K_2}-Y_{K_1}|}
{\max(10^{-12},|Y_{K_2}|,|Y_{K_1}|)}.
\]

Require

\[
\boxed{\epsilon_Y\le0.02}
\]

for the primary/confirmation pair and the confirmation/high-audit pair at a horizon before that horizon may support a robust physical verdict. The coarse audit is reported as a convergence trend but is not a pass/fail gate; the smoke rung never defines the effect verdict.

### 8.2 Common-space optimizer/subspace robustness

Cross-resolution raw vectors of unequal dimension are never compared by padding.

All resolutions use nested frozen \((m,n)\) coordinates and the same retained-coordinate energy normalization. For a lower/higher pair, let \(P_c\) retain only higher-resolution whitened coordinates also present at the lower resolution. If \(W_H\) spans the higher-resolution optimal eigenspace of rank \(d\), define captured common-space mass

\[
\boxed{
\mu_c=\frac1d\operatorname{tr}(W_H^\dagger P_cW_H).
}
\]

Require

\[
\boxed{\mu_c\ge0.95}.
\]

Orthonormalize the projected higher-resolution subspace and compare with the lower-resolution optimal subspace by principal angles. Require equal optimal-subspace ranks and

\[
\boxed{\theta_{\max}^{\rm res}\le10^\circ}.
\]

Apply these checks separately to terminal-energy and positive-shift-forcing optima for primary/confirmation and confirmation/high-audit.

A horizon is not resolution robust if newly admitted small scales capture more than 5% of an optimal subspace, if optimal rank changes, or if the largest common-space principal angle exceeds \(10^\circ\). Such failure is retained; no new rung or retuning is allowed.

### 8.3 Minimum robust support

A non-failure branch verdict requires at least two neighboring horizons on the frozen ladder that pass all objective-value and optimizer/subspace robustness checks from primary through high-resolution audit. If fewer than two neighboring horizons meet this requirement, the future verdict is `CLIM-B-FAIL` with reason `resolution robustness`.

---

## 9. Frozen physical optimizer diagnostics

Only after later execution authorization and successful numerical gates, report for terminal-energy and positive-shift-forcing optima/subspaces:

1. zonal modal energy/whitened weight versus \(m\), including dominant \(m\) and its physical wavelength \(L_x/m\);
2. meridional modal weight versus \(n\);
3. even-about-jet-center versus odd-about-jet-center parity fractions, using odd \(n\) for even parity and even \(n\) for odd parity;
4. physical-space streamfunction \(\psi'(x,y)\) and velocity structure \((u',v')\) for representative nondegenerate optima;
5. zonal-mean Reynolds stress \(\overline{u'v'}(y)\), momentum-flux convergence \(-\partial_y\overline{u'v'}\), and projection onto \(g=-U'\);
6. dominant signed modal/parity-pair contributions to instantaneous and cumulative shift forcing;
7. the time history of the signed \(q_{\rm shift}(t)\) for representative verdict-relevant trajectories.

For degenerate optimal subspaces, report projector/subspace-invariant modal and parity weights and physically meaningful ranges rather than choosing an arbitrary eigenvector picture.

A large angle alone is not sufficient for `CLIM-B-STRONG`; the optimizer difference must have a reproducible physical/modal interpretation.

---

## 10. Frozen study thresholds

At every numerically valid, safely nonzero, resolution-robust horizon report the same-resolution angle/subspace angle and shift-performance gap.

The inherited operational strong thresholds are

\[
\boxed{\vartheta\ge20^\circ},
\qquad
\boxed{\Delta_{\rm shift}\ge0.25}.
\]

A strong result requires **both** thresholds at at least two neighboring frozen horizons, with the same neighboring pair meeting them at primary, confirmation, and high-resolution audit while all Section 8 gates pass.

These are project-level operational demonstration thresholds. They are not universal atmospheric-physics constants, not significance levels, and were not fitted to Climate-B.

For operational weak/null separation, inherit the already preregistered Climate-A resolution thresholds:

\[
\boxed{\vartheta\ge5^\circ\quad\text{or}\quad\Delta_{\rm shift}\ge0.05}
\]

at at least one robust horizon constitutes resolvable objective dependence if `CLIM-B-STRONG` is not met.

---

## 11. Frozen one-shot verdict logic

Assign exactly one of the four MASTER-requested Climate-B outcome classes, in the following precedence.

### `CLIM-B-FAIL`

Use this class if any mandatory structural/numerical execution gate fails at primary, confirmation, or high-resolution audit for horizons needed for interpretation, including Hermiticity, PSD, eigenpair, Lyapunov/block-exponential integral agreement, direct physical-trajectory reproduction, or the minimum two-neighbor resolution-robustness requirement.

No physical objective-separation claim is made after such a failure.

### `CLIM-B-NULL`

Use this class if execution is numerically valid and resolution robust but either:

1. no robust horizon has safely positive/nonzero \(J_{\rm shift}^{+}\) under the fixed denominator rule; or
2. every robust safely interpretable horizon satisfies
   \[
   \vartheta<5^\circ,
   \qquad
   \Delta_{\rm shift}<0.05.
   \]

This is an operational null for the frozen Climate-B channel and does not imply a universal equality theorem.

### `CLIM-B-STRONG`

Use this class only if all numerical/physical-interpretability gates pass and the same pair of at least two neighboring frozen horizons satisfies, robustly from primary through high audit,

\[
\vartheta\ge20^\circ,
\qquad
\Delta_{\rm shift}\ge0.25,
\]

with a reproducible modal/parity/physical-space interpretation of the optimizer difference.

### `CLIM-B-WEAK`

Use this class when execution is numerically valid, sufficiently resolution robust, and has a safely positive signed branch, but `CLIM-B-STRONG` is not met while at least one robust horizon has resolvable objective dependence,

\[
\vartheta\ge5^\circ
\quad\text{or}\quad
\Delta_{\rm shift}\ge0.05.
\]

This includes one-horizon strong-threshold crossings, angle-only separation, and cases where the energy optimum remains a relatively good proxy for the shift-forcing optimum despite structural differences.

No verdict is evaluated in this specification.

---

## 12. Anti-bias and one-shot restrictions

After this specification is committed, the following are immutable for Climate-B:

- \(U_0,L,\beta,r,L_x,L_y\), Bickley profile and centered jet;
- translation tangent \(g=-U'\) and signed orientation;
- basis family, state ordering, 512-point assembly and 1024-point audit;
- \(M_K,Q_{{\rm shift},K},B=I,R_{\rm in}=M_K\);
- resolution ladder and roles;
- six-horizon ladder;
- finite-time numerical methods and tolerances;
- degeneracy, denominator, robustness and verdict rules.

No alternative jet, momentum-flux mask, EOF, localization, forcing coordinate, channel definition, resolution rung, or horizon may be introduced after execution begins.

A weak, null, or failed Climate-B result is retained as the one-shot result. No third Climate candidate is authorized before the first manuscript.

Climate-A remains `CLIM-WEAK` regardless of Climate-B's eventual result.

---

## 13. Explicit execution boundary

This specification has **not** constructed, evaluated, or inspected

\[
K_M(T),\quad K_{\rm shift}(T),\quad G_M(T),\quad J_{\rm shift}^{\pm}(T),
\]

nor any optimizer, optimal subspace, angle, performance gap, horizon dependence, or Climate-B verdict.

Execution is not self-authorized. The branch must return to MASTER for a separate Pilot Freeze / execution release.

\[
\boxed{\text{CLIMATE-B PILOT SPECIFICATION 0.1: COMPLETE}}
\]

\[
\boxed{\text{NO CLIMATE-B FINITE-TIME EXECUTION AUTHORIZED HERE}}
\]

**STOP.**