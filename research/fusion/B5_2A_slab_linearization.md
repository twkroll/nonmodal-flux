# B5.2A — Slab linearization of the anisotropic-ZLR four-moment model

**Status:** completed linearization for the straight-field branch; no potential elimination, free-energy metric, or transport operator frozen yet  
**Date:** 2026-09-01  
**Parent source convention:** `research/fusion/B5_1_source_convention.md`

## Scope

This note performs only the **slab/straight-field linearization** of R1.  It does not yet construct the finite-dimensional operator after electrostatic closure, and it does not define the perturbation metric or transport observables.

The result is therefore an intermediate differential-algebraic system for

\[
(\delta n,\delta u_\parallel,\delta p_\parallel,\delta p_\perp,\delta\phi).
\]

The four moment equations are dynamic; \(\delta\phi\) remains constrained by the linearized polarization/quasineutrality relation and will be eliminated only in B5.3A.

---

## A. Slab assumptions

Choose Cartesian coordinates \((x,y,z)\) with a straight, uniform magnetic field

\[
\mathbf B=B_0\widehat{\mathbf z},\qquad
\widehat{\mathbf b}=\widehat{\mathbf z},\qquad
\nabla B_0=0,
\]

so that

\[
\nabla\times\widehat{\mathbf b}=0,
\qquad
\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}=0.
\]

Consequently, in the source notation,

\[
\mathbf B^*=\mathbf B,
\qquad
B_\parallel^*=B_0,
\qquad
\widehat{\mathbf b}^*=\widehat{\mathbf b},
\qquad
\mathbf C=0,
\qquad
\mathbf u_C=0,
\qquad
\mathcal K=0.
\]

At linear order about an equilibrium with no electrostatic flow, the nonlinear polarization correction in \(\psi\) is second order, so

\[
\delta\psi=\delta\phi.
\]

The retained perpendicular drifts are therefore

\[
\mathbf u_E=\frac{c}{B_0}\widehat{\mathbf z}\times\nabla\phi,
\qquad
\mathbf u_D=\frac{c}{enB_0}\widehat{\mathbf z}\times\nabla p_\perp.
\]

---

## B. Local equilibrium

Take a stationary one-dimensional equilibrium

\[
n=n_0(x),\qquad
p_\parallel=p_{\parallel0}(x),\qquad
p_\perp=p_{\perp0}(x),
\]

with

\[
u_{\parallel0}=0,\qquad \phi_0=0,
\]

and no equilibrium variation along the field:

\[
\partial_z n_0=
\partial_z p_{\parallel0}=
\partial_z p_{\perp0}=0.
\]

The background diamagnetic drift need not vanish.  It is **not** deleted by hand; instead the source heat-flux terms are retained until their slab cancellations are shown below.

Write

\[
n=n_0+\widetilde n,
\qquad
u_\parallel=\widetilde u,
\qquad
p_\parallel=p_{\parallel0}+\widetilde p_\parallel,
\qquad
p_\perp=p_{\perp0}+\widetilde p_\perp,
\qquad
\phi=\widetilde\phi,
\]

and keep only first-order terms.

---

## C. Exact slab diamagnetic cancellations before linearization

The simplification of the pressure equations is not an ad-hoc omission of diamagnetic terms.  It follows from the heat-flux structure inherited from the energy-conserving parent equations.

### C.1 Parallel-pressure diamagnetic flux

In slab/ZLR,

\[
\mathbf q_{\parallel\perp}
=
\frac12\frac{cp_\perp}{eB_0}
\widehat{\mathbf z}\times\nabla T_\parallel,
\qquad
T_\parallel=\frac{p_\parallel}{n}.
\]

Hence

\[
p_\parallel\mathbf u_D+2\mathbf q_{\parallel\perp}
=
\frac{c}{eB_0}
\widehat{\mathbf z}\times
\nabla\!\left(\frac{p_\parallel p_\perp}{n}\right).
\]

For constant \(B_0\) and constant \(\widehat{\mathbf z}\),

\[
\nabla\cdot(\widehat{\mathbf z}\times\nabla F)=0,
\]

so this combined diamagnetic contribution has identically zero divergence.

### C.2 Perpendicular-pressure diamagnetic flux

Likewise,

\[
\mathbf q_{\perp\perp}
=
2\frac{cp_\perp}{eB_0}
\widehat{\mathbf z}\times\nabla T_\perp,
\qquad
T_\perp=\frac{p_\perp}{n},
\]

and therefore

\[
2p_\perp\mathbf u_D+\mathbf q_{\perp\perp}
=
2\frac{c}{eB_0}
\widehat{\mathbf z}\times
\nabla\!\left(\frac{p_\perp^2}{n}\right),
\]

whose divergence also vanishes identically.  Moreover,

\[
\mathbf u_D\cdot\nabla p_\perp=0.
\]

These identities are the reason the straight-field pressure equations reduce to the CGL-like forms below; the diamagnetic pieces have cancelled rather than being discarded.

---

## D. Linearized continuous equations

Because \(\nabla\cdot\mathbf u_E=0\) for uniform \(B_0\), the density equation becomes

\[
\boxed{
\partial_t\widetilde n
+\mathbf u_E^{(1)}\cdot\nabla n_0
+n_0\,\partial_\parallel\widetilde u=0
}
\tag{S-n}
\]

with

\[
\mathbf u_E^{(1)}
=\frac{c}{B_0}\widehat{\mathbf z}\times\nabla\widetilde\phi.
\]

The parallel-momentum equation simplifies because

\[
-\partial_\parallel\widetilde p_\perp
-\partial_\parallel
(\widetilde p_\parallel-\widetilde p_\perp)
=-\partial_\parallel\widetilde p_\parallel,
\]

so

\[
\boxed{
mn_0\,\partial_t\widetilde u
=-en_0\,\partial_\parallel\widetilde\phi
-\partial_\parallel\widetilde p_\parallel
}
\tag{S-u}
\]

The parallel-pressure equation reduces to

\[
\boxed{
\partial_t\widetilde p_\parallel
+\mathbf u_E^{(1)}\cdot\nabla p_{\parallel0}
+3p_{\parallel0}\,\partial_\parallel\widetilde u=0
}
\tag{S-p||}
\]

and the perpendicular-pressure equation to

\[
\boxed{
\partial_t\widetilde p_\perp
+\mathbf u_E^{(1)}\cdot\nabla p_{\perp0}
+p_{\perp0}\,\partial_\parallel\widetilde u=0.
}
\tag{S-pperp}
\]

Thus the pressure anisotropy is retained dynamically even though magnetic curvature and FLR effects have been removed.

---

## E. Local Fourier form

Use the local/WKB perturbation convention

\[
(\widetilde n,\widetilde u,
\widetilde p_\parallel,\widetilde p_\perp,
\widetilde\phi)
\propto
\exp\!\left[i(k_xx+k_yy+k_\parallel z)\right],
\]

while freezing the equilibrium coefficients and their radial derivatives at a reference surface \(x=x_0\).

For the chosen orientation,

\[
\widetilde v_{E,x}
=-\frac{c}{B_0}\partial_y\widetilde\phi
=-i\frac{ck_y}{B_0}\widetilde\phi.
\]

The four dynamic equations are therefore

\[
\boxed{
\partial_t\widetilde n
=
 i\frac{ck_y}{B_0}n_0'\widetilde\phi
-i k_\parallel n_0\widetilde u
}
\tag{SF-n}
\]

\[
\boxed{
\partial_t\widetilde u
=-ik_\parallel
\left(
\frac{e}{m}\widetilde\phi
+\frac{\widetilde p_\parallel}{mn_0}
\right)
}
\tag{SF-u}
\]

\[
\boxed{
\partial_t\widetilde p_\parallel
=
 i\frac{ck_y}{B_0}p_{\parallel0}'\widetilde\phi
-3ik_\parallel p_{\parallel0}\widetilde u
}
\tag{SF-p||}
\]

\[
\boxed{
\partial_t\widetilde p_\perp
=
 i\frac{ck_y}{B_0}p_{\perp0}'\widetilde\phi
-ik_\parallel p_{\perp0}\widetilde u.
}
\tag{SF-pperp}
\]

Here primes denote radial equilibrium derivatives evaluated at the local reference point.

No sign-normalized gradient lengths have yet been introduced.  This is deliberate: definitions such as \(L_n^{-1}=-\partial_x\ln n_0\) will be added only when a normalized convention is frozen.

---

## F. Polarization/quasineutrality remains an algebraic constraint

For uniform \(B_0\), the ZLR polarization equation linearizes locally to a relation of the schematic form

\[
\sum_j e_j\widetilde n_j
-k_\perp^2
\left(
\sum_j\frac{n_{j0}m_jc^2}{B_0^2}
+\frac{1}{4\pi}
\right)
\widetilde\phi
=0,
\tag{S-pol}
\]

up to the species closure used for the non-evolved species and the precise local ordering of equilibrium-gradient corrections in the polarization operator.

For the present ion four-moment subsystem, this means that B5.2A has produced a **four-moment DAE**, not yet a closed \(4\times4\) ODE.  Closing it requires a specified electron response (or a more general electrostatic susceptibility) and belongs to B5.3A.

A useful way to keep that next step model-independent is to write provisionally

\[
\widetilde n_e=\chi_e(k,\omega;\text{closure})\,\widetilde\phi,
\]

or, for an algebraic adiabatic closure, a frequency-independent susceptibility.  No such closure is frozen here.

---

## G. Structural observations from the slab branch

### G.1 The four-moment subsystem is dynamically nontrivial

For \(k_\parallel\neq0\), density and both pressure moments couple to \(\widetilde u\), while all three equilibrium gradients couple to \(\widetilde\phi\).  The coefficients \(3p_{\parallel0}\) and \(p_{\perp0}\) are different, so parallel and perpendicular pressure channels remain distinct even without curvature.

### G.2 Purely perpendicular limit is strongly degenerate

If \(k_\parallel=0\), then

\[
\partial_t\widetilde u=0,
\]

and the remaining moments are driven only through the electrostatic response to the equilibrium gradients.  Therefore a strictly two-dimensional slab limit is likely too degenerate to serve as the primary R1 nonmodal benchmark unless the electrostatic closure itself produces additional dynamics.

This is an important result for the branch comparison: **the analytically useful slab control should retain nonzero \(k_\parallel\)**.

### G.3 Curvature can now be isolated cleanly

B5.2B can start from exactly the same equilibrium-gradient and parallel-compression structure and add only the curvature-dependent terms.  Any difference between the two branches can then be attributed to curvature rather than to an unrelated change of thermodynamic variables or electrostatic convention.

---

## H. What is and is not fixed after B5.2A

Fixed:

- straight uniform magnetic field;
- one-dimensional radial equilibrium gradients;
- anisotropic four-moment thermodynamics;
- nonzero \(k_\parallel\) retained as the useful slab control;
- exact slab cancellation of the source diamagnetic heat-flux terms;
- linearized four dynamic moment equations.

Not fixed:

- electron closure / electrostatic susceptibility;
- normalized gradient parameters;
- elimination of \(\widetilde\phi\);
- the final \(4\times4\) matrix \(A_k^{\rm slab}\);
- perturbation free-energy Hessian \(M_k^{\rm slab}\);
- particle- and heat-flux matrices \(Q_{\Gamma,k}^{\rm slab}\), \(Q_{q,k}^{\rm slab}\).

These exclusions are intentional and preserve the derivation gates.

---

## I. Result and next branch

B5.2A succeeds as a controlled slab linearization.  It does **not** force abandonment of R1, but it reveals that the strictly \(k_\parallel=0\) slab limit is too degenerate for the intended benchmark.  The appropriate slab control retains finite parallel dynamics.

The next parallel comparison step is **B5.2B**, which should derive the corresponding minimal-curvature linearization using the same thermodynamic variables and as nearly as possible the same local equilibrium and electrostatic closure assumptions.

Only after both linearizations exist should B5.3A/B eliminate \(\phi\) and construct the two finite-dimensional operators for direct comparison.
