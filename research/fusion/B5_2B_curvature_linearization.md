# B5.2B — Minimal-curvature linearization of the anisotropic-ZLR four-moment model

**Status:** completed source-faithful curvature linearization audit; no toroidal scalar closure, electrostatic closure, free-energy metric, or transport operator frozen yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_1_source_convention.md`, `research/fusion/B5_2A_slab_linearization.md`

## Scope

This note constructs the curvature counterpart of B5.2A as far as it can be done without inventing a local toroidal geometry that is not fixed by the fully inhomogeneous Strintzi–Scott–Brizard source model.

The source equations contain two distinct magnetic-geometric structures:

\[
\mathcal K(f),
\qquad
\mathbf C=\frac{c}{eB_\parallel^*}\widehat{\mathbf b}\times
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}),
\]

with \(\mathcal K\) defined through the divergence identity used for the diamagnetic cancellations.  In a particular local toroidal model these structures are related by the chosen magnetic geometry, but the source paper does not impose a unique local relation.  B5.2B therefore keeps \(\mathcal K\) and \(\mathbf C\cdot\nabla\) explicit instead of silently replacing them by an arbitrary multiple of \(\partial_y\).

The result is a linear differential–algebraic curvature system for

\[
(\widetilde n,\widetilde u_\parallel,
\widetilde p_\parallel,\widetilde p_\perp,\widetilde\phi),
\]

with all curvature-dependent terms inherited from the source equations visible.

---

## A. Local equilibrium chosen for the curvature audit

To make the curvature branch comparable to a physically standard gyrokinetic equilibrium while retaining anisotropic perturbations, use an **isotropic equilibrium**

\[
p_{\parallel0}=p_{\perp0}=p_0=n_0T_0,
\qquad
p_{\Delta0}=0,
\]

with

\[
u_{\parallel0}=0,\qquad \phi_0=0,
\]

and one-dimensional equilibrium gradients in a local radial coordinate \(x\):

\[
n_0=n_0(x),\qquad T_0=T_0(x),\qquad p_0=p_0(x).
\]

The perturbations may still be anisotropic,

\[
\widetilde p_\Delta
=\widetilde p_\parallel-\widetilde p_\perp\neq0.
\]

This choice removes an equilibrium anisotropy-curvature drift while preserving the four-moment thermodynamic state.  It is the natural subset of the slab equilibrium in B5.2A for a later like-for-like comparison.

At the local reference point we use the standard tangent-model assumptions

\[
\nabla\cdot\widehat{\mathbf b}=0,
\qquad
\partial_\parallel n_0
=\partial_\parallel p_0
=\partial_\parallel T_0=0,
\]

and treat the magnetic geometry as prescribed and time independent.  Equilibrium force balance and any slow source terms that maintain the background profiles are not part of the perturbation state.

---

## B. ZLR perturbation drifts

At first order, \(\delta\psi=\widetilde\phi\).  Define

\[
\mathbf u_E^{(1)}
=\frac{c}{B_0}\widehat{\mathbf b}\times\nabla\widetilde\phi,
\]

\[
\mathbf u_C^{(1)}
=\frac{\widetilde p_\Delta}{n_0}\,\mathbf C,
\]

and

\[
\mathbf u_D^{(1)}
=\delta\left[
\frac{c}{enB_0}\widehat{\mathbf b}\times\nabla p_\perp
\right].
\]

Because \(p_{\Delta0}=0\), the equilibrium curvature drift \(\mathbf u_{C0}\) vanishes.  The diamagnetic drift of the equilibrium need not vanish; it is retained in the pressure-equation linearization until the source heat-flux cancellations are accounted for.

For the linearized parallel dynamics,

\[
\widehat{\mathbf b}^*=\widehat{\mathbf b}+O(\widetilde u_\parallel),
\]

and the correction proportional to \(\widetilde u_\parallel\mathbf C\) does not couple to the purely radial equilibrium gradients in the minimal local ordering.

---

## C. Density equation — curvature terms are unambiguous

The ZLR density equation from B5.1 is

\[
\frac{d_E n}{dt}
+\nabla\cdot\left[n\left(u_\parallel\widehat{\mathbf b}^*+\mathbf u_C\right)\right]
=\mathcal K(p_\perp)+n\,\mathcal K(e\psi).
\]

Using \(n\mathbf u_C=p_\Delta\mathbf C\), the first-order equation is

\[
\boxed{
\partial_t\widetilde n
+\mathbf u_E^{(1)}\cdot\nabla n_0
+n_0\partial_\parallel\widetilde u
+\nabla\cdot(\widetilde p_\Delta\mathbf C)
=\mathcal K(\widetilde p_\perp)
+n_0\mathcal K(e\widetilde\phi)
}
\tag{C-n}
\]

under the local assumption that the equilibrium part of the curvature operator is absorbed into the stationary background balance.

If \(\mathbf C\) is locally divergence free, this becomes

\[
\partial_t\widetilde n
+\mathbf u_E^{(1)}\cdot\nabla n_0
+n_0\partial_\parallel\widetilde u
+\mathbf C\cdot\nabla
(\widetilde p_\parallel-\widetilde p_\perp)
=\mathcal K(\widetilde p_\perp)
+n_0\mathcal K(e\widetilde\phi).
\tag{C-n-local}
\]

Relative to slab, the new structures are therefore explicitly

\[
\mathcal K(\widetilde p_\perp),\qquad
n_0\mathcal K(e\widetilde\phi),\qquad
\mathbf C\cdot\nabla\widetilde p_\Delta.
\]

---

## D. Parallel-momentum equation — curvature terms are also unambiguous

The ZLR source equation is

\[
mn\left(
\frac{\partial u_\parallel}{\partial t}
+\mathbf u'\cdot\nabla u_\parallel
\right)
-p_\perp\mathcal K(mu_\parallel)
=-\widehat{\mathbf b}^*\cdot
(en\nabla\psi+\nabla p_\perp)
-\nabla\cdot(p_\Delta\widehat{\mathbf b}).
\]

Because \(u_{\parallel0}=p_{\Delta0}=0\), the advective term is quadratic at first order and the pressure forces again combine to the parallel-pressure perturbation.  Hence

\[
\boxed{
mn_0\partial_t\widetilde u
-p_0\mathcal K(m\widetilde u)
=-en_0\partial_\parallel\widetilde\phi
-\partial_\parallel\widetilde p_\parallel
}
\tag{C-u}
\]

or

\[
\boxed{
\partial_t\widetilde u
=\frac{p_0}{n_0}\mathcal K(\widetilde u)
-\partial_\parallel\left(
\frac{e}{m}\widetilde\phi
+\frac{\widetilde p_\parallel}{mn_0}
\right).
}
\tag{C-u2}
\]

The source paper explicitly notes that this magnetic term is \(\mathcal K(u_\parallel)\) in its four-moment closure, whereas the Beer–Hammett model contains \(2\mathcal K(u_\parallel)\); that factor must therefore not be changed by hand.

---

## E. Pressure equations — exact first-order form before toroidal scalar reduction

This is where the curvature branch differs qualitatively from slab.  The source heat fluxes are essential to the curvature-dependent diamagnetic cancellation, so they must be linearized together with the pressure equations.

In ZLR,

\[
\mathbf q_{\parallel\perp}
=\frac12\frac{cp_\perp\widehat{\mathbf b}}{eB_0}
\times\nabla T_\parallel
+p_\parallel\mathbf u_C,
\]

\[
\mathbf q_{\perp\perp}
=2\frac{cp_\perp\widehat{\mathbf b}}{eB_0}
\times\nabla T_\perp.
\]

Let

\[
\widetilde T_\parallel
=\frac{\widetilde p_\parallel-T_0\widetilde n}{n_0},
\qquad
\widetilde T_\perp
=\frac{\widetilde p_\perp-T_0\widetilde n}{n_0}.
\]

Then, with prescribed magnetic geometry, the first-order heat-flux perturbations are

\[
\boxed{
\begin{aligned}
\delta\mathbf q_{\parallel\perp}
={}&\frac12\frac{c\widehat{\mathbf b}}{eB_0}\times
\left[p_0\nabla\widetilde T_\parallel
+\widetilde p_\perp\nabla T_0\right]
+p_0\frac{\widetilde p_\Delta}{n_0}\mathbf C,
\end{aligned}
}
\tag{C-q||}
\]

and

\[
\boxed{
\delta\mathbf q_{\perp\perp}
=2\frac{c\widehat{\mathbf b}}{eB_0}\times
\left[p_0\nabla\widetilde T_\perp
+\widetilde p_\perp\nabla T_0\right].
}
\tag{C-qperp}
\]

The corresponding first-order pressure equations, directly from source Eqs. (69)–(70) with \(\Omega=0\), are

\[
\boxed{
\begin{aligned}
\partial_t\widetilde p_\parallel
={}&-\delta\nabla\cdot
\left(
 p_\parallel\mathbf u
+2p_\parallel u_\parallel\widehat{\mathbf b}
+2\mathbf q_{\parallel\perp}
\right)\\
&+2\,\delta\left[
\mathbf u\cdot\nabla\cdot
(p_\parallel\widehat{\mathbf b}\widehat{\mathbf b})
\right]
+4\,\delta\left[
\mathbf q_{\parallel\perp}\cdot
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b})
\right],
\end{aligned}
}
\tag{C-p||-exact}
\]

\[
\boxed{
\begin{aligned}
\partial_t\widetilde p_\perp
={}&-\delta\nabla\cdot\Big[
 p_\perp\mathbf u
+p_\perp(\mathbf I-\widehat{\mathbf b}\widehat{\mathbf b})\cdot\mathbf u
+\mathbf q_{\perp\perp}
\Big]\\
&+\delta\left[
\mathbf u\cdot\nabla\cdot
\big(p_\perp(\mathbf I-\widehat{\mathbf b}\widehat{\mathbf b})\big)
\right]
-2\,\delta\left[
\mathbf q_{\parallel\perp}\cdot
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b})
\right].
\end{aligned}
}
\tag{C-pperp-exact}
\]

These equations are already linear: the \(\delta[\cdots]\) notation means the Frechet derivative of the displayed source flux about the chosen equilibrium, with the perturbation drifts and heat fluxes defined above.  They deliberately preserve the source cancellation structure instead of expanding it under an arbitrary local geometry.

---

## F. Why the slab simplification cannot simply be reused

In slab,

\[
\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}=0,
\qquad
\mathcal K=0,
\]

and the combined diamagnetic pressure/heat fluxes reduce to divergences of cross-gradients whose divergence vanishes identically.  That is why B5.2A produced the simple CGL-like coefficients \(3p_{\parallel0}\) and \(p_{\perp0}\).

With curvature, the source gives instead the exact identities

\[
-2\nabla\cdot\mathbf q_{\parallel\perp}
+4\mathbf q_{\parallel\perp}\cdot\boldsymbol\kappa
=
 n\mathbf u_D\cdot\nabla T_\parallel
+p_\perp\mathcal K(T_\parallel)
-2p_\perp\mathbf C\cdot\nabla T_\parallel
-2\nabla\cdot(T_\parallel p_\Delta\mathbf C),
\]

\[
-\nabla\cdot\mathbf q_{\perp\perp}
-2\mathbf q_{\parallel\perp}\cdot\boldsymbol\kappa
=
2n\mathbf u_D\cdot\nabla T_\perp
+2p_\perp\mathcal K(T_\perp)
+p_\perp\mathbf C\cdot\nabla T_\parallel,
\]

where

\[
\boldsymbol\kappa
=\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}.
\]

Therefore the cancellation leaves genuine \(\mathcal K\)- and \(\mathbf C\)-dependent pressure couplings.  Replacing all of them by a single guessed curvature frequency would destroy the very coefficient structure whose energetic consistency we are trying to preserve.

---

## G. Local Fourier bookkeeping without a hidden geometry convention

For comparison with B5.2A, retain

\[
(\widetilde n,\widetilde u,
\widetilde p_\parallel,\widetilde p_\perp,
\widetilde\phi)
\propto
\exp[i(k_xx+k_yy+k_\parallel z)].
\]

Define two geometry symbols only as bookkeeping devices,

\[
\mathcal K(f_k)=i\omega_{K}(k)\,f_k,
\qquad
\mathbf C\cdot\nabla f_k=i\omega_C(k)\,f_k,
\]

without yet imposing a relation between \(\omega_K\) and \(\omega_C\).

Then the density and momentum equations become

\[
\boxed{
\begin{aligned}
\partial_t\widetilde n_k
={}&i\frac{ck_y}{B_0}n_0'\widetilde\phi_k
-i k_\parallel n_0\widetilde u_k\\
&-i\omega_C
(\widetilde p_{\parallel,k}-\widetilde p_{\perp,k})
+i\omega_K\widetilde p_{\perp,k}
+i\omega_K n_0 e\widetilde\phi_k,
\end{aligned}
}
\tag{CF-n}
\]

and

\[
\boxed{
\partial_t\widetilde u_k
=i\frac{p_0}{n_0}\omega_K\widetilde u_k
-i k_\parallel
\left(
\frac{e}{m}\widetilde\phi_k
+\frac{\widetilde p_{\parallel,k}}{mn_0}
\right).
}
\tag{CF-u}
\]

The pressure rows can likewise be represented as a linear operator once a geometry fixes the action of the divergence and curvature contractions in Eqs. (C-p||-exact) and (C-pperp-exact).  B5.2B does **not** assign those coefficients by analogy with an unrelated three-field ITG model.

---

## H. Result of the branch comparison so far

B5.2B establishes three useful facts.

1. **Curvature adds genuinely new four-moment couplings already before electrostatic closure.**  Density couples directly to \(\widetilde p_\perp\), \(\widetilde p_\Delta\), and \(\widetilde\phi\) through \(\mathcal K\) and \(\mathbf C\), while parallel velocity acquires a magnetic-curvature term.
2. **The pressure sector is more constrained than in slab.**  The diamagnetic heat fluxes are inseparable from the curvature terms if the parent energy theorem is to be respected.
3. **The fully inhomogeneous four-moment paper is not sufficient by itself to define a unique local toroidal \(4\times4\) matrix.**  A local model must additionally specify the magnetic metric/curvature operator and the ordering used to maintain the equilibrium gradients.

This is not a failure of the curvature branch; it is precisely the modelling ambiguity that B5 was meant to expose before implementation.

---

## I. Consequence for the next step

The two branches can still be carried in parallel, but not by pretending they are equally closed at this stage:

\[
\boxed{
\text{Slab: source equations already reduce cleanly}
}
\]

whereas

\[
\boxed{
\text{Curvature: one additional local-geometry source audit is required}
}
\]

before eliminating \(\phi\) and assembling \(A_k^{\rm curv}\).

The natural source for that extra audit is Scott's 2005 local free-energy-conserving gyrofluid formulation, whose purpose is specifically to fix the polarization, compression, and curvature couplings so that the **fluctuation free energy** is conserved in a local/flux-tube model.  This is preferable to inventing a toroidal curvature replacement inside the fully inhomogeneous Strintzi model.

No user-level scientific choice is required yet.  The branch comparison should continue until both models possess explicit operators and balance identities.

---

## Source checks used in B5.2B

- Strintzi, Scott & Brizard, Phys. Plasmas **12**, 052517 (2005), arXiv:physics/0410276:
  - Eq. (24): magnetic-curvature vector entering \(\widehat{\mathbf b}^*\);
  - Eqs. (27)–(28): curvature drift and FLR corrections;
  - Eq. (48): energy-preserving diamagnetic correction to parallel momentum;
  - Eq. (49): definition of \(\mathcal K\);
  - Eqs. (53)–(56): diamagnetic heat fluxes and their curvature identities;
  - Eqs. (67)–(70): final density, parallel-velocity, parallel-pressure and perpendicular-pressure equations;
  - discussion following Eq. (70): the four-moment source has \(\mathcal K(u_\parallel)\), not the \(2\mathcal K(u_\parallel)\) coefficient of Beer–Hammett.
- B. D. Scott, Phys. Plasmas **12**, 102307 (2005), *Free-energy conservation in local gyrofluid models*: establishes the local fluctuation-free-energy construction and the coupling of polarization, density, perpendicular temperature, and compressional terms; this is the appropriate source family for the next curvature specialization.

**B5.2B stop:** no guessed toroidal factor, no electron closure, no \(A_k^{\rm curv}\), no \(M_k\), and no transport matrix has been committed.