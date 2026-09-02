# Climate/Ocean Numerical Qualification 0.1

Status: **QUALIFIED**

Scope: numerical qualification only. This document uses the frozen **Climate/Ocean Pilot Candidate Freeze 0.1** without changing any physical parameter. No CORE optimization, no parameter search, no finite-time energy/transport operator, and no Energy-vs-Heat optimizer comparison is performed.

## 1. Frozen physical model

The dimensional perturbation equations are the damped two-layer Phillips QG system

\[
\partial_t q_i' + U_i\partial_x q_i' + \Pi_i\partial_x\psi_i'=-r q_i',\qquad i=1,2,
\]

with

\[
q_1'=\nabla^2\psi_1'+F(\psi_2'-\psi_1'),\qquad
q_2'=\nabla^2\psi_2'+F(\psi_1'-\psi_2'),
\]

\[
F=\frac{1}{2L_D^2},\qquad U_1=+U,\quad U_2=-U,
\]

and

\[
\Pi_1=\beta+\frac{U}{L_D^2},\qquad
\Pi_2=\beta-\frac{U}{L_D^2}.
\]

The frozen dimensional parameters are

\[
L_x=3.0\times10^7\ {\rm m},\qquad
L_y=1.0\times10^7\ {\rm m},
\]

\[
L_D=1.0\times10^6\ {\rm m},\qquad
\beta=1.6\times10^{-11}\ {\rm m^{-1}s^{-1}},
\]

\[
U=8\ {\rm m\,s^{-1}},\qquad
r=(10\ {\rm d})^{-1}.
\]

No value above is modified in this qualification.

## 2. Barotropic/baroclinic variables

Define

\[
\psi=\frac{\psi_1'+\psi_2'}{2},\qquad
\tau=\frac{\psi_1'-\psi_2'}{2}.
\]

For a Fourier-Galerkin mode with total horizontal squared wavenumber \(\kappa^2=k^2+\ell^2\),

\[
q_{\rm BT}=-\kappa^2\psi,
\qquad
q_{\rm BC}=-\left(\kappa^2+L_D^{-2}\right)\tau.
\]

The state ordering is frozen mode-by-mode as

\[
\boxed{x_{mn}=(\psi_{mn},\tau_{mn})^T}.
\]

The global vector is ordered lexicographically in zonal index \(m\), then meridional index \(n\), with the two-component pair \((\psi_{mn},\tau_{mn})\) contiguous.

## 3. Exact structure-preserving Fourier/Galerkin basis

Use the basis

\[
\phi_{mn}(x,y)=
\exp\!\left(i\frac{2\pi m}{L_x}x\right)
\sin\!\left(\frac{\pi n}{L_y}y\right),
\]

with

\[
m\in\{-M_x,\ldots,-1,1,\ldots,M_x\},\qquad
n=1,\ldots,N_y.
\]

This basis enforces exactly:

1. zonal periodicity;
2. \(\psi_i'=0\) at \(y=0,L_y\);
3. exclusion of every \(k_x=0\) mode.

Real physical fields are the conjugate-symmetric invariant subspace

\[
x_{-m,n}=x_{m,n}^*.
\]

The complexified Galerkin matrices below preserve this subspace exactly.

The truncation dimension is

\[
N_K=4M_xN_y.
\]

## 4. Nondimensionalization and time normalization

Freeze

\[
L_{\rm ref}=L_D,
\qquad
U_{\rm ref}=\beta L_D^2=16\ {\rm m\,s^{-1}},
\]

\[
\boxed{\tau_{\rm ref}=\frac{L_D}{U_{\rm ref}}
=6.25\times10^4\ {\rm s}
=0.7233796296\ {\rm d}}.
\]

Use

\[
x^*=x/L_D,\qquad y^*=y/L_D,\qquad t^*=t/\tau_{\rm ref},
\]

and scale the streamfunctions by

\[
\psi_{\rm ref}=U_{\rm ref}L_D.
\]

Then

\[
L_x^*=30,\qquad L_y^*=10,\qquad
\beta^*=1,\qquad U^*=\frac12,
\]

and

\[
\boxed{r^*=r\tau_{\rm ref}=0.072337962962963}.
\]

For mode \((m,n)\), define

\[
k_m^*=\frac{2\pi m}{30},\qquad
\ell_n^*=\frac{\pi n}{10},
\]

\[
a_{mn}=k_m^{*2}+\ell_n^{*2},\qquad
b_{mn}=a_{mn}+1.
\]

All numerical matrices and spectra reported below are nondimensional unless a dimensional unit is stated explicitly.

## 5. Frozen Galerkin dynamics matrix \(A_K\)

For every \((m,n)\), the Galerkin projection is exactly block diagonal. The \(2\times2\) block is

\[
\boxed{
A_{mn}=
\begin{pmatrix}
-r^*+i k_m^*/a_{mn} & -i k_m^*U^*\\[1mm]
 i k_m^*U^*(1-a_{mn})/b_{mn} & -r^*+i k_m^*/b_{mn}
\end{pmatrix}.
}
\]

Thus

\[
\boxed{A_K=\operatorname{blockdiag}_{m\ne0,\,n\ge1} A_{mn}}.
\]

The block for \(-m\) is the complex conjugate of the block for \(+m\), so the real-field conjugacy constraint is invariant.

## 6. Frozen energy matrix \(M_K\)

The frozen nondimensional perturbation energy is

\[
E_K=\frac12\int_{\Omega^*}
\left(|\nabla\psi|^2+|\nabla\tau|^2+|\tau|^2\right)dA^*.
\]

For the unnormalized basis above,

\[
S^*=\int_{\Omega^*}|\phi_{mn}|^2dA^*
=\frac{L_x^*L_y^*}{2}=150.
\]

Therefore each modal block is

\[
\boxed{
M_{mn}=S^*
\begin{pmatrix}
a_{mn}&0\\
0&b_{mn}
\end{pmatrix},
}
\]

and

\[
\boxed{M_K=\operatorname{blockdiag} M_{mn}}.
\]

Since \(m\ne0\), \(n\ge1\), one has \(a_{mn}>0\) and \(b_{mn}>1\). Consequently

\[
\boxed{M_K=M_K^\dagger\succ0}
\]

analytically at every resolution.

At the coarsest represented mode \((|m|,n)=(1,1)\),

\[
\lambda_{\min}(M_K)=21.38414287>0,
\]

and this same lowest-energy mode remains present on every nested refinement.

## 7. Frozen signed heat-flux matrix \(Q_{{\rm heat},K}\)

The positive orientation is northward/poleward. After division by the positive dimensional heat-flux scale

\[
H_{\rm ref}=C_H U_{\rm ref}^2L_D^3,
\]

the signed heat-flux functional is

\[
H_{\rm heat}^*=\int_{\Omega^*}(\partial_{x^*}\psi)\tau\,dA^*
\]

for real physical fields.

Its Hermitian complexification has the modal matrix

\[
\boxed{
Q_{{\rm heat},mn}
=\frac{S^*}{2}
\begin{pmatrix}
0&-i k_m^*\\
 i k_m^*&0
\end{pmatrix}.
}
\]

Thus

\[
\boxed{Q_{{\rm heat},K}=\operatorname{blockdiag}Q_{{\rm heat},mn}}.
\]

Exactly,

\[
Q_{{\rm heat},K}=Q_{{\rm heat},K}^\dagger.
\]

Each nonzero-zonal-wavenumber block has eigenvalues

\[
\lambda_\pm(Q_{{\rm heat},mn})
=\pm\frac{S^*|k_m^*|}{2},
\]

so

\[
\boxed{Q_{{\rm heat},K}\ \text{is indefinite at every admissible resolution}.}
\]

No absolute value, square, or positive heat-flux norm is introduced.

## 8. Direct signed-flux reproduction check

A deterministic test was made with the \((m,n)=(1,1)\) pair and its conjugate, using

\[
\psi_{1,1}=1,\qquad \tau_{1,1}=i,
\]

\[
\psi_{-1,1}=1,\qquad \tau_{-1,1}=-i.
\]

The corresponding real fields are

\[
\psi=2\cos(k_1^*x^*)\sin(\ell_1^*y^*),
\]

\[
\tau=-2\sin(k_1^*x^*)\sin(\ell_1^*y^*).
\]

Direct analytic spatial integration gives

\[
\int_{\Omega^*}(\partial_{x^*}\psi)\tau\,dA^*
=k_1^*L_x^*L_y^*
=62.8318530718.
\]

The Galerkin quadratic form gives independently

\[
\boxed{x^\dagger Q_{{\rm heat},K}x=62.8318530718},
\]

with the same positive sign. Replacing \(\tau\to-\tau\) changes both results to \(-62.8318530718\). Hence the matrix reproduces both magnitude and signed orientation of the frozen heat flux.

## 9. Pre-fixed resolution ladder

Before evaluating any spectrum, the nested ladder was fixed as

\[
\boxed{
(M_x,N_y)\in
\{(4,4),(8,8),(12,12),(16,16),(24,24)\}.
}
\]

No rung was added, removed, or changed in response to a spectral result.

## 10. Qualification results

| \(M_x\) | \(N_y\) | dim \(N_K\) | \(\alpha(A_K)\) | dimensional \(\alpha\) | \(\min\lambda(M_K)\) | \(\min\lambda(Q_K)\) | \(\max\lambda(Q_K)\) | max \(|\Im\lambda(A_K)|\) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 64 | -0.07233796296 | -0.100000 d\(^{-1}\) | 21.38414287 | -62.83185307 | 62.83185307 | 1.50667352 |
| 8 | 8 | 256 | -0.07233796296 | -0.100000 d\(^{-1}\) | 21.38414287 | -125.6637061 | 125.6637061 | 1.50667352 |
| 12 | 12 | 576 | -0.07233796296 | -0.100000 d\(^{-1}\) | 21.38414287 | -188.4955592 | 188.4955592 | 1.50667352 |
| 16 | 16 | 1024 | -0.07233796296 | -0.100000 d\(^{-1}\) | 21.38414287 | -251.3274123 | 251.3274123 | 1.81745963 |
| 24 | 24 | 2304 | -0.07233796296 | -0.100000 d\(^{-1}\) | 21.38414287 | -376.9911184 | 376.9911184 | 2.61048186 |

The Hermiticity residuals of both \(M_K\) and \(Q_{{\rm heat},K}\) are exactly zero for the assembled analytic blocks (to floating-point representation), and all eigenvalues of \(M_K\) are positive.

## 11. Spectrum and spectral abscissa

For every mode on the fixed ladder, both eigenvalues of the inviscid block have zero real part. The frozen Rayleigh damping shifts the complete spectrum by \(-r^*\). Numerically,

\[
\boxed{\alpha(A_K)=-0.072337962962963<0}
\]

for every rung, equivalent to

\[
\boxed{\alpha(A_K)=-0.1\ {\rm d}^{-1}}.
\]

No eigenvalue with real part larger than \(-r^*\) is present.

This satisfies the frozen STOP condition robustly and without parameter modification.

## 12. Resolution-convergence statement

Because the base state and coefficients are spatially homogeneous, the Galerkin operator is modal and the chosen ladder is nested. Refinement therefore does not perturb any already represented modal block: every \((m,n)\) block present at a coarser rung is algebraically identical at all finer rungs.

Define the nested common-mode spectral defect between adjacent resolutions by matching only eigenvalues belonging to modes represented on both grids. The measured defect is

\[
\boxed{\delta_{\rm spec}<10^{-14}}
\]

for every adjacent pair in the fixed ladder (machine precision).

The rightmost spectral boundary converges trivially and exactly:

\[
\boxed{\alpha(A_{4,4})=\alpha(A_{8,8})=\cdots=\alpha(A_{24,24})=-r^*.}
\]

The maximum imaginary frequency is not required to converge to a finite value as \(M_x,N_y\to\infty\), because refinement intentionally adds new, shorter-wave branches of the continuous PDE spectrum. Therefore the appropriate structure-preserving convergence criterion is convergence/invariance of fixed modal branches and of the rightmost spectral boundary, not Hausdorff convergence of the entire expanding finite spectrum as a bounded set.

## 13. Qualification verdict

All requested pre-optimization numerical gates pass:

1. \(M_K=M_K^\dagger\succ0\): **PASS**;
2. \(Q_{{\rm heat},K}=Q_{{\rm heat},K}^\dagger\) and indefinite: **PASS**;
3. signed heat-flux reproduction by \(x^\dagger Q_{{\rm heat},K}x\): **PASS**;
4. stable spectrum with \(\alpha(A_K)<0\): **PASS**;
5. nested resolution convergence of retained spectral branches and spectral abscissa: **PASS**.

Hence

\[
\boxed{\text{Climate/Ocean Numerical Qualification 0.1: QUALIFIED}}
\]

with the frozen numerical objects

\[
\boxed{(A_K,M_K,Q_{{\rm heat},K})}
\]

as defined above.

## 14. Explicit exclusions

This qualification did **not** construct or evaluate

\[
K_E(T),\qquad K_{\rm heat}(T),\qquad
w_E^\star,\qquad w_{\rm heat}^\star,
\]

nor any optimizer angle, gap, objective separation, transient gain, or other CORE-effect quantity.

No physical parameter was retuned.

**STOP.**
