# Climate Intra-Domain Contrast Numerical Qualification 0.1

**Status:** `QUALIFIED`  
**Authority:** `research/master/prompts/climate_intra_domain_contrast_numerical_qualification_0_1.md`  
**Scope:** structural and spectral numerical qualification only. No finite-time CORE operator, horizon selection, optimizer, angle, gap, parameter search, retuning, new channel, or reinterpretation of Climate-A is performed here.

Climate-A remains frozen as `CLIM-WEAK`.

---

## 1. Frozen Climate-B candidate

The qualified candidate is exactly the one-shot equivalent-barotropic Bickley jet

\[
U(y)=U_0\operatorname{sech}^2((y-y_0)/L),
\]

with the unchanged dimensional point

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

The frozen nondimensionalization is

\[
L_{\rm ref}=L,\qquad U_{\rm ref}=U_0,
\qquad \tau_{\rm ref}=L/U_0=50000\,\mathrm s=0.5787037037\,\mathrm d,
\]

with

\[
L_x^*=20,\quad L_y^*=10,\quad \beta^*=0.8,
\quad r^*=0.05787037037037.
\]

The signed channel remains the eddy-induced forcing of the infinitesimal poleward jet-translation coordinate

\[
g(y)=-U'(y),
\]

\[
q_{\rm shift}(t)=
\frac{\int g(y)[-\partial_y\overline{u'v'}]dy}{\int g(y)^2dy},
\]

with positive sign fixed as forcing in the poleward translation direction.

The admissible initial-condition geometry remains

\[
B=I,\qquad R_{\rm in}=M_K.
\]

No physical or numerical object above was changed during qualification.

---

## 2. Frozen representation and assembly

Use positive zonal Fourier modes

\[
k_m^*=\frac{2\pi m}{20},\qquad m=1,\ldots,M_x,
\]

with exact conjugate reconstruction of real fields and the centered orthonormal Dirichlet sine basis

\[
\phi_n(y^*)=\sqrt{\frac{2}{10}}
\sin\left[\frac{n\pi(y^*+5)}{10}\right],
\qquad n=1,\ldots,N_y.
\]

The state is

\[
x_K=(c_1^T,c_2^T,\ldots,c_{M_x}^T)^T,
\qquad c_m=(c_{m1},\ldots,c_{mN_y})^T.
\]

For each positive zonal mode,

\[
D_m=-\operatorname{diag}(\kappa_{m1}^2,\ldots,\kappa_{mN_y}^2),
\qquad
\kappa_{mn}^2=k_m^{*2}+(n\pi/10)^2,
\]

and the frozen 512-point Gauss-Legendre coefficient matrices are

\[
(U_N)_{pn}=\int_{-5}^{5}\phi_pU^*\phi_n\,dy^*,
\]

\[
(C_N)_{pn}=\int_{-5}^{5}\phi_p(\beta^*-U^{*\prime\prime})\phi_n\,dy^*,
\]

\[
(R_N)_{pn}=\int_{-5}^{5}g^{*\prime}\phi_p\phi_n'\,dy^*.
\]

The numerical objects are exactly

\[
A_m=-r^*I-i k_m^*D_m^{-1}(U_ND_m+C_N),
\]

\[
M_m=2L_x^*\operatorname{diag}(\kappa_{m1}^2,\ldots,\kappa_{mN_y}^2),
\]

\[
Q_{{\rm shift},m}=\frac{i k_m^*}{G_g^*}(R_N-R_N^T),
\]

with

\[
G_g^*=8\left(\frac{\tanh^3 5}{3}-\frac{\tanh^5 5}{5}\right)
=1.0666666007257188.
\]

Global matrices are block diagonal in positive zonal wavenumber.

---

## 3. Frozen resolution ladder

No rung was added, removed, or reassigned:

| role | \(M_x\) | \(N_y\) | complex dim. | real dim. |
|---|---:|---:|---:|---:|
| structural smoke | 8 | 16 | 128 | 256 |
| coarse audit | 12 | 24 | 288 | 576 |
| **primary** | **16** | **32** | **512** | **1024** |
| **confirmation** | **20** | **40** | **800** | **1600** |
| **high-resolution audit** | **24** | **48** | **1152** | **2304** |

---

## 4. 512-versus-1024 quadrature audit

The preregistered requirement is

\[
\frac{\|X_{1024}-X_{512}\|_F}{\max(1,\|X_{1024}\|_F)}\le10^{-12},
\qquad X\in\{U_N,C_N,R_N\}.
\]

| role | \(M_x,N_y\) | \(U_N\) rel. | \(C_N\) rel. | \(R_N\) rel. |
|---|---|---:|---:|---:|
| structural smoke | 8,16 | 1.00e-14 | 1.14e-14 | 1.03e-14 |
| coarse audit | 12,24 | 1.00e-14 | 1.16e-14 | 1.01e-14 |
| primary | 16,32 | 9.99e-15 | 1.60e-14 | 1.01e-14 |
| confirmation | 20,40 | 1.00e-14 | 2.17e-14 | 1.03e-14 |
| high-resolution audit | 24,48 | 1.01e-14 | 2.91e-14 | 1.03e-14 |

The worst observed audit defect is

\[
\boxed{2.92\times10^{-14}<10^{-12}}.
\]

**Quadrature audit: PASS.**

---

## 5. Positive metric and signed channel checks

At every frozen rung,

\[
M_K=M_K^\dagger\succ0
\]

analytically and numerically. The minimum eigenvalue is identical on the nested ladder,

\[
\boxed{\lambda_{\min}(M_K)=7.895683520871486>0}.
\]

The assembled signed-channel matrix obeys

\[
Q_{{\rm shift},K}=Q_{{\rm shift},K}^\dagger
\]

to machine representation and is nontrivial and indefinite at every rung.

| role | \(\lambda_{\min}(Q_{\rm shift})\) | \(\lambda_{\max}(Q_{\rm shift})\) |
|---|---:|---:|
| structural smoke | -13.70098629 | +13.70098629 |
| coarse audit | -41.75379781 | +41.75379781 |
| primary | -87.92576690 | +87.92576690 |
| confirmation | -153.28570721 | +153.28570721 |
| high-resolution audit | -238.49980644 | +238.49980644 |

Hence the channel remains genuinely signed; no absolute value, square, or positive norm has been substituted.

**Metric/channel structure: PASS.**

---

## 6. Exact parity-selection audit

Odd \(n\) basis functions are even about the jet center and even \(n\) basis functions are odd. Because \(U^*\) and \(\beta^*-U^{*\prime\prime}\) are even, \(A_K\) may couple only equal parity. Because differentiation reverses parity, \(Q_{{\rm shift},K}\) may couple only opposite parity.

Normalized parity-forbidden Frobenius residuals are:

| role | \(U_N\) forbidden | \(C_N\) forbidden | \(A_K\) forbidden | \(Q_{\rm shift}\) forbidden |
|---|---:|---:|---:|---:|
| structural smoke | 8.51e-16 | 8.55e-16 | 9.98e-16 | 9.94e-16 |
| coarse audit | 1.38e-15 | 1.42e-15 | 2.24e-15 | 1.75e-15 |
| primary | 1.32e-15 | 1.37e-15 | 3.45e-15 | 1.54e-15 |
| confirmation | 1.26e-15 | 1.38e-15 | 2.81e-14 | 1.23e-15 |
| high-resolution audit | 3.11e-15 | 3.10e-15 | 5.21e-14 | 4.40e-15 |

All are ordinary quadrature/roundoff residuals and far below the requested double-precision scientific tolerance.

**Parity structure: PASS.**

---

## 7. Predeclared deterministic sign witness

The Candidate Freeze fixed, before any effect calculation,

\[
m=1,\qquad c_{11}=1,\qquad c_{12}=i,
\]

with all other coefficients zero and exact real-field conjugate reconstruction.

Using the assembled quadratic matrix gives

\[
\boxed{x_K^\dagger Q_{{\rm shift},K}x_K=+0.03388302885311917}.
\]

An independent direct 1024-point spatial evaluation of

\[
\frac{\int g^{*\prime}(y^*)\overline{u'v'}(y^*)dy^*}{G_g^*}
\]

gives

\[
\boxed{q_{\rm shift,direct}^*=+0.03388302885311881}.
\]

The absolute discrepancy is

\[
3.61\times10^{-16},
\]

or about \(1.06\times10^{-14}\) relative.

Replacing \(c_{12}=i\) by \(c_{12}=-i\) yields

\[
q_{\rm shift,Q}^*=-0.03388302885311917,
\qquad
q_{\rm shift,direct}^*=-0.03388302885311881,
\]

while the kinetic energy is unchanged:

\[
E_+^*=E_-^*=13.81744616152510.
\]

Thus the frozen sign convention and signed cross-phase dependence are reproduced exactly to roundoff.

**Signed-channel reproduction: PASS.**

---

## 8. Complete spectral qualification

The complete eigenvalue spectrum of every frozen modal block \(A_m\) was computed in complex IEEE double precision at every rung. No zonal mode was selected or discarded in response to the result.

| role | \(M_x\) | \(N_y\) | \(\alpha(A_K)\) nondim. | dimensional \(\alpha\) | worst \(\kappa_2(D_m)\) | worst normalized eig. residual |
|---|---:|---:|---:|---:|---:|---:|
| structural smoke | 8 | 16 | -0.05787037037037 | -0.100000000000 d\(^{-1}\) | 128.5 | 2.66e-15 |
| coarse audit | 12 | 24 | -0.05787037037037 | -0.100000000000 d\(^{-1}\) | 288.5 | 3.52e-15 |
| primary | 16 | 32 | -0.05787037037037 | -0.100000000000 d\(^{-1}\) | 512.5 | 5.33e-15 |
| confirmation | 20 | 40 | -0.05787037037036 | -0.100000000000 d\(^{-1}\) | 800.5 | 4.06e-15 |
| high-resolution audit | 24 | 48 | -0.05787037037036 | -0.100000000000 d\(^{-1}\) | 1152.5 | 6.42e-15 |

Across the entire frozen ladder, every computed eigenvalue satisfies

\[
\Re\lambda=-r^*
\]

within a maximum absolute deviation of

\[
\boxed{1.13\times10^{-14}}.
\]

Therefore

\[
\boxed{\alpha(A_K)<0}
\]

at every frozen resolution without any retuning.

The worst normalized eigenpair residual is

\[
\boxed{6.42\times10^{-15}\ll10^{-10}},
\]

so the result is not limited by eigensolver accuracy. The worst Laplacian-block condition number, 1152.5 at the high-resolution audit, is modest for double precision and does not compromise the spectral conclusion.

**Spectral-stability gate: PASS.**

---

## 9. Nested spectral refinement audit

For every zonal wavenumber present in two adjacent rungs, each coarse eigenvalue was compared with its nearest fine-resolution eigenvalue in the same \(m\) block. These branch-distance diagnostics were not used as a post-hoc selection rule; no convergence threshold beyond numerical spectral reliability had been preregistered for imaginary frequencies.

| adjacent rungs | median nearest defect | 95th percentile | max defect | \(|\Delta\alpha|\) |
|---|---:|---:|---:|---:|
| 8x16 → 12x24 | 7.76e-4 | 1.23e-1 | 1.96e-1 | 1.26e-15 |
| 12x24 → 16x32 | 1.88e-3 | 1.31e-1 | 1.92e-1 | 2.14e-15 |
| 16x32 → 20x40 | 2.25e-3 | 1.05e-1 | 1.48e-1 | 4.86e-16 |
| 20x40 → 24x48 | 2.86e-3 | 1.00e-1 | 2.14e-1 | 5.56e-15 |

As expected for an expanding Galerkin approximation, truncation-edge imaginary-frequency branches shift when additional short meridional scales are admitted. The stability-relevant rightmost spectral boundary, however, is invariant to machine precision:

\[
\alpha(A_{8,16})=\alpha(A_{12,24})=\alpha(A_{16,32})
=\alpha(A_{20,40})=\alpha(A_{24,48})=-r^*+O(10^{-14}).
\]

Thus refinement robustly supports the only spectral conclusion required at this gate: the entire frozen one-shot candidate remains asymptotically stable on every prescribed rung.

**Resolution/stability conclusion: ROBUST.**

---

## 10. Regression test

A qualification-only regression test was added at

`tests/test_climate_intra_domain_contrast_numerical_qualification_0_1.py`.

It checks:

- all five frozen 512-versus-1024 quadrature audits;
- kinetic-energy positivity and channel Hermiticity/indefiniteness;
- parity selection rules;
- the predeclared \(c_{11}=1,c_{12}=\pm i\) sign witness;
- complete modal spectral stability on all frozen rungs;
- normalized eigenpair residuals.

It constructs no finite-time CORE operator and uses no horizon.

Local test result before commit:

`3 passed`.

---

## 11. Qualification verdict

All mandatory qualification gates pass:

1. frozen 512-point assembly and 1024-point audit: PASS;
2. \(M_K=M_K^\dagger\succ0\): PASS;
3. \(Q_{{\rm shift},K}=Q_{{\rm shift},K}^\dagger\), nontrivial and indefinite: PASS;
4. exact parity structure: PASS;
5. deterministic signed-channel witness: PASS;
6. complete spectral stability at every frozen rung: PASS;
7. nested refinement supports a robust stable rightmost boundary: PASS;
8. conditioning/eigenresidual checks: PASS.

Therefore the unique preregistered verdict is

\[
\boxed{\text{QUALIFIED}}.
\]

---

## 12. Allowed and forbidden interpretation

### Allowed

Climate-B is now a structurally consistent, resolution-audited and spectrally stable finite-dimensional realization of the frozen equivalent-barotropic Bickley-jet problem with a positive perturbation-energy metric and an independently signed jet-translation-forcing channel.

### Forbidden

This qualification says nothing yet about finite-time objective nonredundancy. In particular, this task did **not** construct or inspect

\[
K_M(T),\quad K_{\rm shift}(T),\quad G_M(T),\quad J_{\rm shift}^{\pm}(T),
\]

any optimizer direction/subspace, optimizer angle, performance gap, horizon dependence, or Energy-vs-Shift separation.

No horizon ladder was selected in this qualification. No physical parameter, resolution role, channel definition, admissible geometry, or Climate-A result was changed.

The next action requires a new committed MASTER instruction.

\[
\boxed{\text{CLIMATE-B NUMERICAL QUALIFICATION COMPLETE — RETURN TO MASTER}}
\]

**STOP.**