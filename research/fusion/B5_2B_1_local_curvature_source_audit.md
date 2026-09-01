# B5.2B.1 — Local-curvature source audit

**Status:** completed source audit for the minimal local curvature convention; no electrostatic closure, free-energy metric, or transport operator frozen yet  
**Date:** 2026-09-01  
**Parent note:** `research/fusion/B5_2B_curvature_linearization.md`

## Scope

B5.2B left two geometric objects explicit,

\[
\mathcal K(f),
\qquad
\mathbf C\cdot\nabla f,
\]

because the fully inhomogeneous Strintzi–Scott–Brizard four-moment source does not itself choose a unique local toroidal reduction.  This note asks only whether the later **local, free-energy-consistent Scott/GEM formulation** supplies a controlled minimal relation between these two objects.

The answer is yes, within the standard local tokamak ordering used by Scott: curvature and grad-\(B\) are represented by a single divergence-form curvature operator.  This resolves the bookkeeping ambiguity of B5.2B without yet constructing the final linear operator.

---

## A. Local curvature operator in Scott's free-energy-consistent formulation

Scott's local gyrofluid derivation introduces a perpendicular curvature operator of the form

\[
\mathcal K
=
K^x(s)\,\partial_x+K^y(s)\,\partial_y,
\]

with the geometry coefficients chosen so that

\[
\partial_x K^x+\partial_y K^y=0.
\]

This divergence-free property is not cosmetic: it is required by the free-energy theorem.  In the corresponding linear notation Scott identifies

\[
\mathcal K\longleftrightarrow -2i\omega_d,
\]

where \(\omega_d\) is the local toroidal magnetic-drift frequency.

This provides the appropriate scalar local-curvature bookkeeping for the present project: one should not invent independent curvature frequencies for every moment equation once the local free-energy-consistent ordering has been selected.

---

## B. Relation to the Strintzi–Scott–Brizard \(\mathbf C\) drift

The four-moment source defines

\[
\mathbf C
=
\frac{c}{eB}\,
\widehat{\mathbf b}\times
(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b})
\]

in the present ZLR/local limit, while its curvature operator obeys, for constant test prefactor,

\[
\mathcal K(f)
=-\nabla\cdot
\left(
\frac{c}{eB}\widehat{\mathbf b}\times\nabla f
\right).
\]

Scott's local fluid/gyrofluid correspondence uses the standard large-aspect-ratio local approximations

\[
\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}
\simeq \nabla\ln B,
\]

and

\[
\nabla\cdot
\left(
\frac{c}{eB}\widehat{\mathbf b}\times\nabla f
\right)
\simeq
-2\nabla\ln B\cdot
\left(
\frac{c}{eB}\widehat{\mathbf b}\times\nabla f
\right).
\]

Using the scalar-triple-product identity gives

\[
\nabla\ln B\cdot
(\widehat{\mathbf b}\times\nabla f)
=
-(\widehat{\mathbf b}\times\nabla\ln B)\cdot\nabla f.
\]

Therefore, in this **minimal local tokamak ordering**,

\[
\boxed{
\mathcal K(f)
\simeq
-2\,\mathbf C\cdot\nabla f
}
\tag{LC-1}
\]

for the ion-sign convention used here.

This is the missing local relation exposed in B5.2B.

---

## C. Fourier-frequency specialization

B5.2B introduced

\[
\mathcal K(f_k)=i\omega_K f_k,
\qquad
\mathbf C\cdot\nabla f_k=i\omega_C f_k.
\]

Equation (LC-1) therefore implies

\[
\boxed{
\omega_K=-2\omega_C.
}
\tag{LC-2}
\]

Combining this with Scott's local identification

\[
\mathcal K(f_k)=-2i\omega_d f_k
\]

gives the convenient one-frequency convention

\[
\boxed{
\omega_C=\omega_d,
\qquad
\omega_K=-2\omega_d.
}
\tag{LC-3}
\]

The sign of \(\omega_d\) still depends on the orientation of \((x,y)\), the sign convention for \(k_y\), and the species charge.  Those orientation choices will be frozen only when the final normalized Fourier convention is written.  The **factor-of-two relation**, however, is fixed by the local curvature ordering above and must not be altered independently in different equations.

---

## D. Consequence for the B5.2B density equation

The density equation from B5.2B was

\[
\begin{aligned}
\partial_t\widetilde n_k
={}&i\frac{ck_y}{B_0}n_0'\widetilde\phi_k
-i k_\parallel n_0\widetilde u_k\\
&-i\omega_C
(\widetilde p_{\parallel,k}-\widetilde p_{\perp,k})
+i\omega_K\widetilde p_{\perp,k}
+i\omega_K n_0e\widetilde\phi_k.
\end{aligned}
\]

Under (LC-3), this becomes

\[
\boxed{
\begin{aligned}
\partial_t\widetilde n_k
={}&i\frac{ck_y}{B_0}n_0'\widetilde\phi_k
-i k_\parallel n_0\widetilde u_k\\
&-i\omega_d\widetilde p_{\parallel,k}
-i\omega_d\widetilde p_{\perp,k}
-2i\omega_d n_0e\widetilde\phi_k.
\end{aligned}
}
\tag{LC-n}
\]

Thus the anisotropic pressure contribution collapses to the physically familiar **sum of parallel and perpendicular pressure contributions**, rather than leaving two arbitrary geometry coefficients.

This is an important cross-check: the later Scott fluid/gyrofluid correspondence states that the density curvature term is governed by the pressure-tensor combination \(p_\parallel+p_\perp\) in this local ordering.

---

## E. Consequence for parallel momentum

B5.2B obtained

\[
\partial_t\widetilde u_k
=i\frac{p_0}{n_0}\omega_K\widetilde u_k
-i k_\parallel
\left(
\frac{e}{m}\widetilde\phi_k
+\frac{\widetilde p_{\parallel,k}}{mn_0}
\right).
\]

With (LC-3),

\[
\boxed{
\partial_t\widetilde u_k
=-2i\frac{p_0}{n_0}\omega_d\widetilde u_k
-i k_\parallel
\left(
\frac{e}{m}\widetilde\phi_k
+\frac{\widetilde p_{\parallel,k}}{mn_0}
\right).
}
\tag{LC-u}
\]

The coefficient is inherited from the four-moment source; it must not be replaced by a Beer–Hammett coefficient by analogy.

---

## F. Pressure-sector lesson from the local model

The local Scott/GEM equations show that toroidal curvature, magnetic divergence, parallel compression and temperature anisotropy are **not independent decorations**.  In free-energy-consistent form, curvature acts on specific combinations of electrostatic potential, density and temperature moments, while parallel compression acts through matched combinations fixed by the polarization/free-energy structure.

For example, the later local fluid/gyrofluid correspondence writes the ion moment equations with a single \(\mathcal K\) acting on combinations such as

\[
\phi_G+p_{i\parallel}+p_{i\perp},
\]

and the temperature equations contain different but fixed curvature combinations.  Hence the remaining pressure equations in B5.2B should now be reduced using the **single operator \(\mathcal K\)** and its fixed coefficient structure, rather than by independently substituting \(\omega_K\) and \(\omega_C\) term by term from the nonlocal equations.

This is the central modelling conclusion of this audit.

---

## G. What is now fixed

For the minimal local-curvature comparison branch we may henceforth use

\[
\boxed{
\mathcal K(f_k)=-2i\omega_d f_k,
\qquad
\mathbf C\cdot\nabla f_k=i\omega_d f_k,
}
\]

subject to a later explicit orientation/sign convention for \(\omega_d\).

The following remain **unfixed**:

- electron closure / electrostatic susceptibility;
- normalized gradient lengths and dimensional normalization;
- the full reduced parallel- and perpendicular-pressure Fourier equations;
- elimination of \(\widetilde\phi\);
- \(A_k^{\rm curv}\), \(M_k^{\rm curv}\), \(Q_{\Gamma,k}^{\rm curv}\), and \(Q_{q,k}^{\rm curv}\).

---

## H. Decision for the next derivation step

No user-level geometry decision is required at this point.  The source audit supports one controlled minimal curvature convention:

\[
\boxed{
\omega_K=-2\omega_C=-2\omega_d.
}
\]

The next safe step is to use this relation to complete the **pressure-sector local curvature linearization** and verify that the resulting four moment equations reduce to the slab equations when \(\omega_d\to0\).

Only after that limit check passes should the electrostatic closure be introduced and \(\phi\) eliminated.

---

## Literature anchors

- B. D. Scott, *Free-energy conservation in local gyrofluid models*, Phys. Plasmas **12**, 102307 (2005), DOI 10.1063/1.2064968, arXiv:physics/0501124.  The model makes the polarization, thermal free energy, parallel compression and perpendicular compression mutually consistent.
- B. D. Scott, *Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities*, Phys. Plasmas **17**, 102306 (2010), arXiv:0710.4899.  The local flux-tube derivation defines a divergence-form curvature operator \(\mathcal K=K^x\partial_x+K^y\partial_y\), requires it to be divergence free for free-energy conservation, and identifies its linear form with \(-2i\omega_d\).
- B. D. Scott, *Nonlinear polarisation and dissipative correspondence between low frequency fluid and gyrofluid equations*, Phys. Plasmas **14**, 102318 (2007).  The local correspondence uses \(\widehat{\mathbf b}\cdot\nabla\widehat{\mathbf b}\simeq\nabla\ln B\), identifies \(\mathcal K(\phi)=-\nabla\cdot\mathbf v_E\), and shows how pressure anisotropy enters the density curvature term through the pressure-tensor combination.
- D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas **12**, 052517 (2005), arXiv:physics/0410276.  This remains the parent source for the four-moment anisotropic variables used in R1.
