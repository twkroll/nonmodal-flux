# Climate Intra-Domain Contrast Candidate Freeze 0.1

**Status:** `CLIMATE-B CANDIDATE FROZEN`  
**Authority:** `research/master/climate_intra_domain_contrast_feasibility_gate_0_1.md` and `research/master/prompts/climate_intra_domain_contrast_candidate_freeze_0_1.md`  
**Scope:** physical/numerical candidate freeze only. No finite-time CORE operator, optimizer, angle, gap, parameter search, or retuning is performed here.

Climate-A remains permanently frozen as `CLIM-WEAK` and is not reopened.

---

## 1. Frozen Climate-B physical problem

Climate-B is exactly the one-shot equivalent-barotropic midlatitude Bickley-jet candidate authorized by MASTER.

The dimensional perturbation equation is

\[
\boxed{
\partial_t\zeta'
+U(y)\,\partial_x\zeta'
+\bigl[\beta-U''(y)\bigr]\partial_x\psi'
=-r\zeta',
\qquad
\zeta'=\nabla^2\psi'.
}
\]

The externally maintained base jet is

\[
\boxed{
U(y)=U_0\operatorname{sech}^2\!\left(\frac{y-y_0}{L}\right).
}
\]

The jet is centered in the meridional channel,

\[
y_0=0,
\qquad
-\frac{L_y}{2}\le y\le\frac{L_y}{2},
\qquad
0\le x<L_x.
\]

The physical point is frozen without alteration:

\[
\boxed{
\beta=1.6\times10^{-11}\;\mathrm{m^{-1}s^{-1}},
\quad
U_0=20\;\mathrm{m\,s^{-1}},
\quad
L=1000\;\mathrm{km},
\quad
r=(10\;\mathrm d)^{-1},
}
\]

\[
\boxed{
L_x=20000\;\mathrm{km},
\qquad
L_y=10000\;\mathrm{km}.
}
\]

No alternative parameter point, domain size, damping, jet profile, mask, EOF, or channel weight is admissible for Climate-B.

Boundary/state restrictions are frozen as

- periodicity in \(x\);
- \(\psi'=0\) at \(y=\pm L_y/2\);
- only \(k_x\ne0\) eddy perturbations are retained;
- both meridional-parity sectors are retained.

The zonal-mean component is part of the fixed base state and is not an admissible initial perturbation.

---

## 2. Frozen positive metric

The positive objective metric is the standard barotropic perturbation kinetic energy

\[
\boxed{
E'(t)=\frac12\int_\Omega |\nabla\psi'|^2\,dA
=\frac12 x^\dagger Mx.
}
\]

This metric is independent of CORE and contains no empirical weighting.

On the retained \(k_x\ne0\) Dirichlet eddy space,

\[
E'=0\Longrightarrow \psi'=0,
\]

so the Galerkin energy matrix is strictly positive definite:

\[
\boxed{M=M^\dagger\succ0.}
\]

No gauge regularization or \(\epsilon I\) term is permitted.

---

## 3. Frozen signed jet-translation channel

The infinitesimal poleward translation tangent is fixed by the base jet itself:

\[
\boxed{g(y)=-U'(y).}
\]

Indeed,

\[
U(y-\delta Y)=U(y)+\delta Y\,g(y)+O(\delta Y^2),
\]

so positive amplitude along \(g\) represents a poleward displacement when \(y\) increases poleward.

For real perturbations,

\[
u'=-\partial_y\psi',
\qquad
v'=\partial_x\psi',
\]

and the zonal-mean Reynolds stress is

\[
F_M(y,t)=\overline{u'v'}(y,t).
\]

The eddy-induced zonal-mean acceleration is

\[
\mathcal A(y,t)=-\partial_yF_M(y,t).
\]

The signed channel is frozen as

\[
\boxed{
q_{\rm shift}(t)=
\frac{\int_{-L_y/2}^{L_y/2}g(y)\,[-\partial_y\overline{u'v'}]\,dy}
{\int_{-L_y/2}^{L_y/2}g(y)^2\,dy}.
}
\]

The sign convention is

\[
\boxed{
q_{\rm shift}>0
\Longleftrightarrow
\text{eddy forcing projects onto a poleward jet translation}.
}
\]

Because \(\psi'=0\) at the walls, \(v'=\partial_x\psi'=0\) there and the boundary Reynolds stress vanishes. Hence integration by parts gives exactly

\[
q_{\rm shift}(t)=
\frac{\int g'(y)\,\overline{u'v'}(y,t)\,dy}
{\int g(y)^2\,dy}.
\]

The future cumulative observable is frozen, but not evaluated here:

\[
\boxed{
J_{\rm shift}(T)=\int_0^Tq_{\rm shift}(t)\,dt.
}
\]

Its allowed interpretation is **cumulative eddy impulse/forcing of the infinitesimal jet-translation coordinate under frozen tangent dynamics**. It is not, by itself, the realized displacement of a coupled nonlinear atmospheric jet.

---

## 4. Frozen nondimensionalization and time normalization

The nondimensionalization is chosen only from the already frozen jet scales:

\[
\boxed{L_{\rm ref}=L=10^6\;\mathrm m},
\qquad
\boxed{U_{\rm ref}=U_0=20\;\mathrm{m\,s^{-1}}}.
\]

Therefore

\[
\boxed{
\tau_{\rm ref}=\frac{L}{U_0}
=5.0\times10^4\;\mathrm s
=0.5787037037\;\mathrm d.
}
\]

This is the jet-width advective time and is fixed before any objective calculation.

Use

\[
x^*=x/L,
\qquad y^*=y/L,
\qquad t^*=t/\tau_{\rm ref},
\qquad \psi^*=\psi/(U_0L).
\]

The frozen dimensionless parameters are

\[
L_x^*=20,
\qquad
L_y^*=10,
\qquad
\beta^*=\frac{\beta L^2}{U_0}=0.8,
\]

\[
\boxed{r^*=r\tau_{\rm ref}=0.05787037037037.}
\]

With the centered coordinate \(y^*\in[-5,5]\),

\[
U^*(y^*)=\operatorname{sech}^2y^*.
\]

Writing \(s=\operatorname{sech}^2y^*\),

\[
U^{*\prime\prime}=4s-6s^2,
\qquad
g^*=-U^{*\prime}=2s\tanh y^*,
\]

\[
g^{*\prime}=-U^{*\prime\prime}=6s^2-4s.
\]

The dimensionless normalization denominator is fixed by the finite channel, not the infinite-line value:

\[
G_g^*=\int_{-5}^{5}(g^*)^2dy^*
=8\left[\frac{\tanh^3 5}{3}-\frac{\tanh^5 5}{5}\right]
\simeq1.06666660072572.
\]

The dimensionless channel is \(q_{\rm shift}^*=q_{\rm shift}/U_0\), and the dimensionless cumulative impulse satisfies \(J_{\rm shift}^*=J_{\rm shift}/L\).

---

## 5. Pre-effect Rayleigh-Kuo check

For the Bickley profile,

\[
\max_y U''(y)=\frac23\frac{U_0}{L^2}.
\]

At the frozen point,

\[
\frac23\frac{U_0}{L^2}
=1.3333333333\times10^{-11}\;\mathrm{m^{-1}s^{-1}}
<\beta.
\]

Equivalently in nondimensional variables,

\[
\min_{y^*}\left(\beta^*-U^{*\prime\prime}\right)
=0.8-\frac23
=0.1333333333>0.
\]

Thus the basic-state absolute-vorticity gradient does not change sign, so the Rayleigh-Kuo necessary condition for inviscid barotropic instability is not satisfied. This is a **pre-effect stability criterion only**.

No finite-dimensional spectral abscissa is inferred from this statement. Numerical Qualification must compute \(\alpha(A_K)\) blindly at every frozen resolution. If robust stability fails, Climate-B fails qualification; no physical retuning is allowed.

---

## 6. Structure-preserving Fourier/Galerkin representation

### 6.1 Meridional basis

Use the orthonormal sine basis on the centered dimensionless channel:

\[
\boxed{
\phi_n(y^*)=\sqrt{\frac{2}{L_y^*}}
\sin\left[\frac{n\pi(y^*+L_y^*/2)}{L_y^*}\right],
\qquad n=1,2,\ldots,N_y.
}
\]

This enforces \(\psi'=0\) at both meridional walls exactly.

Relative to the jet center \(y^*=0\):

- odd \(n\) basis functions are even;
- even \(n\) basis functions are odd.

Both parity sectors are always retained.

### 6.2 Zonal representation and real-field conjugacy

Use positive Fourier wavenumbers only as independent complex coordinates,

\[
\boxed{
k_m^*=\frac{2\pi m}{L_x^*}=\frac{2\pi m}{20},
\qquad m=1,\ldots,M_x.}
\]

For each \(m\), define

\[
f_m(y^*,t^*)=\sum_{n=1}^{N_y}c_{mn}(t^*)\phi_n(y^*).
\]

The real physical perturbation is reconstructed uniquely as

\[
\boxed{
\psi'^*(x^*,y^*,t^*)
=\sum_{m=1}^{M_x}
\left[f_m(y^*,t^*)e^{ik_m^*x^*}
+f_m^*(y^*,t^*)e^{-ik_m^*x^*}\right].
}
\]

Thus the \(-m\) coefficients are not independent numerical degrees of freedom; real-field conjugacy is imposed exactly by reconstruction. This avoids artificial duplication of the \(\pm m\) representation while retaining the complete real eddy space.

### 6.3 State ordering

For each positive zonal wavenumber,

\[
c_m=(c_{m1},c_{m2},\ldots,c_{mN_y})^T.
\]

The global complex state is ordered

\[
\boxed{x_K=(c_1^T,c_2^T,\ldots,c_{M_x}^T)^T.}
\]

The complex dimension is

\[
N_K=M_xN_y,
\]

corresponding to real dimension \(2M_xN_y\).

Within each \(m\)-block the meridional coefficients remain in ascending \(n\), so odd/even parity is explicit and can be audited without reordering the state.

---

## 7. Frozen Galerkin assembly of \(A_K\)

For each positive \(m\), define

\[
\ell_n^*=\frac{n\pi}{L_y^*}=\frac{n\pi}{10},
\qquad
\kappa_{mn}^2=k_m^{*2}+\ell_n^{*2},
\]

and the diagonal Laplacian matrix

\[
\boxed{
D_m=-\operatorname{diag}(\kappa_{m1}^2,\ldots,\kappa_{mN_y}^2).
}
\]

Since \(m\ge1\), \(D_m\) is nonsingular.

Define the real Galerkin multiplication matrices

\[
(U_N)_{pn}=\int_{-5}^{5}\phi_p(y^*)U^*(y^*)\phi_n(y^*)\,dy^*,
\]

\[
(C_N)_{pn}=\int_{-5}^{5}\phi_p(y^*)
\left[\beta^*-U^{*\prime\prime}(y^*)\right]
\phi_n(y^*)\,dy^*.
\]

Both are real symmetric. Because their weights are even about the jet center, they couple only equal-parity meridional basis functions.

The frozen modal dynamics matrix is

\[
\boxed{
A_m=-r^*I
-i k_m^*D_m^{-1}\left(U_ND_m+C_N\right).
}
\]

The full matrix is

\[
\boxed{A_K=\operatorname{blockdiag}_{m=1}^{M_x}A_m.}
\]

No zonal wavenumber is singled out or selected by an objective result.

---

## 8. Frozen Galerkin energy matrix \(M_K\)

With the positive-wavenumber representation above, the nondimensional kinetic energy

\[
E^*=E'/(U_0^2L^2)
\]

is

\[
E^*=L_x^*\sum_{m=1}^{M_x}\sum_{n=1}^{N_y}
\kappa_{mn}^2|c_{mn}|^2.
\]

Therefore, under the project convention

\[
E^*=\frac12x_K^\dagger M_Kx_K,
\]

the modal blocks are

\[
\boxed{
M_m=2L_x^*\operatorname{diag}
(\kappa_{m1}^2,\ldots,\kappa_{mN_y}^2),
}
\]

and

\[
\boxed{M_K=\operatorname{blockdiag}M_m.}
\]

Every diagonal entry is strictly positive, hence analytically

\[
\boxed{M_K=M_K^\dagger\succ0}
\]

for every admissible truncation.

---

## 9. Frozen Hermitian representation of the signed channel

For one positive zonal wavenumber, the zonal-mean Reynolds stress of the corresponding real conjugate pair is

\[
\overline{u'v'}_m
=-2k_m^*\operatorname{Im}\left[f_m'(y^*)f_m^*(y^*)\right].
\]

Define the real derivative-weight matrix

\[
\boxed{
(R_N)_{pn}
=\int_{-5}^{5}
 g^{*\prime}(y^*)\,
 \phi_p(y^*)\,\phi_n'(y^*)\,dy^*.
}
\]

Then the dimensionless shift forcing is exactly

\[
q_{\rm shift}^*
=\sum_{m=1}^{M_x}c_m^\dagger Q_{{\rm shift},m}c_m,
\]

with

\[
\boxed{
Q_{{\rm shift},m}
=\frac{i k_m^*}{G_g^*}\left(R_N-R_N^T\right).
}
\]

Since \(R_N-R_N^T\) is real skew-symmetric,

\[
\boxed{
Q_{{\rm shift},m}=Q_{{\rm shift},m}^\dagger,
\qquad
Q_{{\rm shift},K}=\operatorname{blockdiag}_mQ_{{\rm shift},m}.
}
\]

### 9.1 Parity structure and indefiniteness

Because \(g^{*\prime}=-U^{*\prime\prime}\) is even and differentiation reverses meridional parity,

- same-parity entries of \(Q_{{\rm shift},m}\) vanish;
- only opposite-parity meridional components couple.

In parity-block form,

\[
Q_{{\rm shift},m}
=\begin{pmatrix}
0&H_m\\
H_m^\dagger&0
\end{pmatrix}.
\]

The channel is nontrivial: for example, the frozen \(n=1\) even / \(n=2\) odd pair has a nonzero antisymmetric derivative-weight coupling on the fixed channel. Reversing their relative \(\pi/2\) cross-phase reverses \(q_{\rm shift}\) while leaving kinetic energy unchanged.

For any nonzero \(H_m\), the Hermitian block matrix above has eigenvalues in \(\pm\) pairs. Hence

\[
\boxed{Q_{{\rm shift},K}\ \text{is signed and indefinite}.}
\]

This is a structural statement only. No finite-time transport operator or optimizer has been constructed.

### 9.2 Deterministic sign witness for later qualification

Numerical Qualification must reproduce the sign and magnitude of the direct spatial formula using the predeclared real test field formed from

\[
m=1,\qquad c_{11}=1,\qquad c_{12}=i,
\]

with every other coefficient zero, together with its conjugate reconstruction. The test is fixed now, before any objective calculation; replacing \(c_{12}=i\) by \(-i\) must reverse the channel sign and leave energy unchanged.

---

## 10. Physical admissibility of \(B=I\) and input cost

The retained numerical state already consists only of physically admissible equivalent-barotropic eddies:

- the fast/unbalanced degrees of freedom are absent from the barotropic QG model;
- the wall conditions are built into the basis;
- \(k_x=0\) mean-flow changes are excluded;
- both parity sectors required by the physical signed channel are retained.

Therefore it is scientifically natural to admit every retained eddy initial condition:

\[
\boxed{B=I.}
\]

The input cost is the same independently established perturbation kinetic energy,

\[
\boxed{R_{\rm in}=M_K.}
\]

No spatial mask, upstream localization, stochastic covariance, EOF restriction, or empirical preconditioner is introduced for Climate-B.

---

## 11. Frozen quadrature for coefficient assembly

All one-dimensional Galerkin coefficient integrals involving \(U^*\), \(U^{*\prime\prime}\), and \(g^{*\prime}\) are defined by the exact integrals above.

Their numerical assembly in the next qualification step is frozen to **512-point Gauss-Legendre quadrature on \([-5,5]\)** in IEEE double precision.

A qualification-only assembly audit must compare these matrices against the same integrals evaluated with 1024-point Gauss-Legendre quadrature. The relative Frobenius discrepancy must satisfy

\[
\frac{\|X_{1024}-X_{512}\|_F}{\max(1,\|X_{1024}\|_F)}\le10^{-12}
\]

for \(X\in\{U_N,C_N,R_N\}\) at every frozen resolution. If this representational check fails, qualification stops; the physical point is not retuned.

Parity-forbidden entries are expected to vanish to quadrature roundoff and must be reported as a separate structural residual.

---

## 12. Frozen nested resolution ladder and roles

Before any finite-time objective is inspected, freeze the following nested ladder:

| role | \(M_x\) | \(N_y\) | complex dim. \(M_xN_y\) | equivalent real dim. |
|---|---:|---:|---:|---:|
| structural smoke | 8 | 16 | 128 | 256 |
| coarse audit | 12 | 24 | 288 | 576 |
| **primary** | **16** | **32** | **512** | **1024** |
| **confirmation** | **20** | **40** | **800** | **1600** |
| **high-resolution audit** | **24** | **48** | **1152** | **2304** |

The ladder is selected solely from the fixed physical geometry and the need to resolve a width-\(L\) localized jet inside a \(10L\)-wide channel while retaining a broad, nested set of zonal eddies. It is not based on any CORE separation.

The highest retained zonal wavenumber corresponds to a wavelength \(L_x/M_x\); at the high-resolution rung this reaches \(0.8333L\). The highest meridional sine index is \(48\). No rung may be added, removed, or reassigned after objective inspection.

---

## 13. Numerical Qualification handoff

The next step may perform **structural and spectral qualification only**. It must not yet calculate finite-time objective separation.

For every frozen rung, Numerical Qualification must:

1. assemble \(A_K,M_K,Q_{{\rm shift},K}\) exactly as frozen above;
2. verify
   \[
   M_K=M_K^\dagger\succ0;
   \]
3. verify
   \[
   Q_{{\rm shift},K}=Q_{{\rm shift},K}^\dagger
   \]
   and report positive and negative eigenvalues confirming indefiniteness;
4. reproduce the deterministic signed Reynolds-stress/jet-shift test from Section 9.2 directly in physical space and by \(x_K^\dagger Q_{{\rm shift},K}x_K\);
5. verify the exact parity selection rules for \(A_K\) and \(Q_{{\rm shift},K}\);
6. execute the frozen 512-vs-1024 quadrature assembly audit;
7. compute the complete spectrum of every modal \(A_m\) and the global spectral abscissa
   \[
   \alpha(A_K)=\max\operatorname{Re}\lambda(A_K);
   \]
8. require robust
   \[
   \boxed{\alpha(A_K)<0}
   \]
   on the complete frozen ladder;
9. assess nested spectral convergence using common retained modal branches and the rightmost spectral boundary, with no post-hoc resolution addition;
10. record conditioning of \(D_m\) and any numerical eigenresidual required to distinguish physical spectrum from discretization failure.

If the frozen work point does not remain robustly stable under this structure-preserving qualification, Climate-B stops. No change to \(U_0,L,\beta,r,L_x,L_y\), basis family, channel weight, or resolution roles is permitted.

---

## 14. Explicit exclusions

This Candidate Freeze has not constructed, evaluated, or inspected

\[
K_M(T),\qquad K_{\rm shift}(T),
\]

\[
w_M^\star,\qquad w_{\rm shift}^\star,
\]

nor any optimizer/subspace angle, target-performance gap, horizon dependence, finite-time gain, or objective-separation quantity.

No finite-time horizon ladder is selected here; any later horizon freeze requires MASTER authorization after Numerical Qualification.

Climate-A remains exactly `CLIM-WEAK` and unchanged.

---

## 15. Candidate Freeze verdict

All required physical objects are consistent without representational correction:

- frozen barotropic Bickley-jet tangent dynamics: **PASS**;
- independent positive kinetic-energy metric: **PASS**;
- physically fixed poleward-translation tangent \(g=-U'\): **PASS**;
- signed Hermitian quadratic jet-shift forcing channel: **PASS**;
- structural nontriviality/indefiniteness: **PASS**;
- \(B=I,R_{\rm in}=M_K\) admissibility: **PASS**;
- Rayleigh-Kuo pre-effect stability criterion: **PASS**;
- structure-preserving discretization handoff: **FROZEN**.

Therefore

\[
\boxed{
\text{Climate Intra-Domain Contrast Candidate Freeze 0.1 = STABLE}
}
\]

and

\[
\boxed{
\text{CLIMATE-B CANDIDATE FROZEN — RETURN TO MASTER FOR NUMERICAL QUALIFICATION}
}
\]

**STOP.**
