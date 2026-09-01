# B5.1 — Source convention and continuous anisotropic-ZLR equations

**Status:** completed source-convention extraction; no equilibrium, Fourier convention, or linear operator frozen yet  
**Date:** 2026-09-01  
**Primary source:** D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas 12, 052517 (2005), arXiv:physics/0410276.

## Scope of this step

This note does only one job: fix the parent equations from which the proposed R1 model must be reduced. No linearization is performed here. In particular, this file does **not** yet define \(A_k\), \(M_k\), \(Q_{\Gamma,k}\), or \(Q_{q,k}\).

The source model is electrostatic and low-beta, with anisotropic pressures

\[
p_\parallel=nT_\parallel,\qquad p_\perp=nT_\perp,
\]

and four species moments

\[
(n,u_\parallel,p_\parallel,p_\perp).
\]

The electrostatic potential is constrained by a polarization equation. The background magnetic field is time independent but may be nonuniform.

## ZLR specialization used for R1

The source gyroaverage satisfies

\[
\|\phi\|\to \phi
\]

in the zero-Larmor-radius limit. Its temperature derivative \(\Omega=\partial\|\phi\|/\partial T_\perp\) therefore vanishes in this limit, so

\[
\Omega=0,\qquad \mathbf w_\Omega=0,\qquad \mathbf w_C=0.
\]

The generalized electrostatic potential remains, before linearization,

\[
e\psi=e\phi-\frac{mc^2}{2B^2}|\nabla\phi|^2.
\]

The second term is nonlinear and will disappear only after the later small-amplitude linearization about an equilibrium with no equilibrium \(E\times B\) flow.

Define

\[
p_\Delta=p_\parallel-p_\perp,
\]

\[
\mathbf B^*=\mathbf B+\frac{mc}{e}u_\parallel\nabla\times\widehat{\mathbf b},
\qquad
B_\parallel^*=\mathbf B^*\cdot\widehat{\mathbf b},
\qquad
\widehat{\mathbf b}^*=\frac{\mathbf B^*}{B_\parallel^*},
\]

and

\[
\mathbf C=\frac{c}{eB_\parallel^*}\widehat{\mathbf b}\times
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}).
\]

The perpendicular velocities retained in R1 are

\[
\mathbf u_D=\frac{c}{enB_\parallel^*}\widehat{\mathbf b}\times\nabla p_\perp,
\]

\[
\mathbf u_\psi=\frac{c}{B_\parallel^*}\widehat{\mathbf b}\times\nabla\psi,
\qquad
\mathbf u_C=\frac{p_\Delta}{n}\mathbf C.
\]

Thus the ZLR gyrofluid velocity is

\[
\mathbf u=u_\parallel\widehat{\mathbf b}^*+\mathbf u_D+\mathbf u_\psi+\mathbf u_C,
\]

while the diamagnetic-subtracted velocity used in the parallel-momentum equation is

\[
\mathbf u'=\mathbf u-\mathbf u_D
=u_\parallel\widehat{\mathbf b}^*+\mathbf u_\psi+\mathbf u_C.
\]

The magnetic-curvature operator \(\mathcal K\) is kept in the source form defined implicitly by

\[
\nabla\cdot\left(
 g\frac{c\widehat{\mathbf b}}{eB_\parallel^*}\times\nabla f
\right)
=
\frac{c\widehat{\mathbf b}}{eB_\parallel^*}\cdot(\nabla f\times\nabla g)
-g\,\mathcal K(f).
\]

No slab or toroidal specialization of \(\mathcal K\) is made in B5.1.

## Continuous R1 equations

Starting from the final energy-conserving equations (67)–(70) of the source and setting the FLR quantities \(\Omega,\mathbf w_\Omega,\mathbf w_C\) to zero gives the following anisotropic ZLR parent system.

### 1. Density

With

\[
\frac{d_E}{dt}=\frac{\partial}{\partial t}+\mathbf u_\psi\cdot\nabla,
\]

we use

\[
\frac{d_E n}{dt}
+\nabla\cdot\left[n\left(u_\parallel\widehat{\mathbf b}^*+\mathbf u_C\right)\right]
=
\mathcal K(p_\perp)+n\,\mathcal K(e\psi).
\tag{R1-n}
\]

### 2. Parallel velocity

\[
mn\left(
\frac{\partial u_\parallel}{\partial t}
+\mathbf u'\cdot\nabla u_\parallel
\right)
-p_\perp\,\mathcal K(mu_\parallel)
=
-\widehat{\mathbf b}^*\cdot
\left(en\nabla\psi+\nabla p_\perp\right)
-\nabla\cdot\left(p_\Delta\widehat{\mathbf b}\right).
\tag{R1-u}
\]

### 3. Parallel pressure

The source diamagnetic heat flux becomes in ZLR

\[
\mathbf q_{\parallel\perp}
=
\frac12\frac{cp_\perp\widehat{\mathbf b}}{eB_\parallel^*}
\times\nabla T_\parallel
+p_\parallel\mathbf u_C.
\]

The pressure equation is

\[
\frac{\partial p_\parallel}{\partial t}
=
-\nabla\cdot\left(
 p_\parallel\mathbf u
+2p_\parallel u_\parallel\widehat{\mathbf b}
+2\mathbf q_{\parallel\perp}
\right)
+2\mathbf u\cdot\nabla\cdot
\left(p_\parallel\widehat{\mathbf b}\widehat{\mathbf b}\right)
+4\mathbf q_{\parallel\perp}\cdot
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}).
\tag{R1-p||}
\]

### 4. Perpendicular pressure

The second source heat flux becomes

\[
\mathbf q_{\perp\perp}
=
2\frac{cp_\perp\widehat{\mathbf b}}{eB_\parallel^*}
\times\nabla T_\perp.
\]

Then

\[
\begin{aligned}
\frac{\partial p_\perp}{\partial t}
={}&-\nabla\cdot\Big[
 p_\perp\mathbf u
+p_\perp(\mathbf I-\widehat{\mathbf b}\widehat{\mathbf b})\cdot\mathbf u
+\mathbf q_{\perp\perp}
\Big]\\
&+\mathbf u\cdot\nabla\cdot
\Big[p_\perp(\mathbf I-\widehat{\mathbf b}\widehat{\mathbf b})\Big]
-2\mathbf q_{\parallel\perp}\cdot
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}).
\end{aligned}
\tag{R1-pperp}
\]

These four equations are the continuous nonlinear R1 parent equations. They are not yet the finite-dimensional model used by `nonmodal-flux`.

## Polarization constraint

In the same ZLR limit, the source polarization equation becomes

\[
\sum_j\left[
 e_j n_j
+\nabla_\perp\cdot\left(
 \frac{n_jm_jc^2}{B^2}\nabla_\perp\phi
\right)
\right]
+\frac{1}{4\pi}\nabla^2\phi=0.
\tag{R1-pol}
\]

The species response used to close this equation — e.g. adiabatic electrons versus an additional electron fluid/kinetic response — is deliberately **not** selected in B5.1.

## Energy identity retained from the parent model

The source total energy density is

\[
\varepsilon=
\frac12 mn\left(u_\parallel^2+|\mathbf u_E|^2\right)
+p_\perp+\frac12p_\parallel
+\frac{|\mathbf E|^2}{8\pi},
\]

with a local conservation law \(\partial_t\varepsilon+\nabla\cdot\mathbf S^*=0\) after the energy-preserving diamagnetic corrections are included. This is a **nonlinear total-energy identity**. It must not yet be identified with the positive perturbation metric \(M\); B5.4 will require the quadratic perturbation/free-energy Hessian after a specific equilibrium is chosen.

## What B5.1 resolves

- The four R1 dynamical variables are fixed at the continuous level.
- ZLR means removal of the gyroaverage/temperature-derivative FLR corrections, not deletion of pressure anisotropy or curvature by fiat.
- The diamagnetic heat-flux terms remain part of the continuous equations even at ZLR.
- The polarization equation remains an essential constraint.
- No transport observable has yet been guessed from the pressure variables.

## First unresolved fork exposed by the source

The parent equations are fully inhomogeneous and do **not** select a unique local geometry. B5.2 therefore has to choose how the equilibrium and magnetic geometry are reduced before linearization. At least two physically distinct routes are possible:

1. a straight/slab local field, which maximizes analytic transparency but removes magnetic curvature drive;
2. a minimal local toroidal/curvature model, which is closer to conventional ITG physics but introduces a curvature convention and additional coefficients.

B5.1 does not resolve this fork. It should be decided explicitly before writing the linearized operator.

## Source cross-checks

- Source Eq. (2): gyroaverage tends to \(\phi\) in ZLR.
- Source Eqs. (17), (24), (27)–(28): definitions of \(\psi\), \(\mathbf B^*\), \(\widehat{\mathbf b}^*\), and drift velocities.
- Source Eq. (32): polarization equation.
- Source Eqs. (53)–(54): diamagnetic heat fluxes.
- Source Eqs. (67)–(70): final four energy-conserving moment equations.
- Source Eqs. (42)–(47), (63): nonlinear energy density and conservation law.

**B5.1 stop:** no \(A_k\), \(M_k\), \(Q_{\Gamma,k}\), or \(Q_{q,k}\) is committed here.