# B5.2B.2 — Local-curvature pressure-sector reduction

**Status:** completed pressure-sector reduction in a dimensionally consistent local normalization; no electrostatic closure, free-energy metric, or transport operator frozen yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_2B_curvature_linearization.md`, `research/fusion/B5_2B_1_local_curvature_source_audit.md`, `research/fusion/B5_2A_slab_linearization.md`

## Scope

This step completes the minimal local-curvature density/pressure subsystem and checks the slab limit. It uses the source-faithful anisotropic four-moment structure from Strintzi–Scott–Brizard together with the single-operator local curvature structure of Scott's free-energy-consistent GEM model.

A normalization issue in the provisional bookkeeping of B5.2B/B5.2B.1 is corrected here: the raw Strintzi curvature operator acts on dimensional quantities, so a symbol called a "frequency" cannot multiply both pressure and velocity variables without the appropriate thermal-energy scale. The corrected local variables below make the curvature frequency dimensionally unambiguous. The older dimensional formulas should therefore be read as structural bookkeeping only; the normalized equations in this note supersede them for the next derivation stages.

---

## A. Local dimensionless thermodynamic variables

Use the isotropic equilibrium already chosen for the curvature branch,

\[
p_{\parallel0}=p_{\perp0}=p_0=n_0T_0,
\qquad
u_{\parallel0}=0,
\qquad
\phi_0=0,
\]

while retaining anisotropic perturbations. Define

\[
N=\frac{\widetilde n}{n_0},
\qquad
P_\parallel=\frac{\widetilde p_\parallel}{p_0},
\qquad
P_\perp=\frac{\widetilde p_\perp}{p_0},
\qquad
\Phi=\frac{e\widetilde\phi}{T_0}.
\]

The normalized temperature perturbations are

\[
\Theta_\parallel=P_\parallel-N,
\qquad
\Theta_\perp=P_\perp-N.
\]

Let

\[
c_s^2=\frac{T_0}{m}.
\]

For any dimensionless scalar \(f\), define the local curvature-rate operator

\[
\widehat{\mathcal K}f
\equiv
\mathcal K(T_0 f).
\]

Under the local Scott convention fixed in B5.2B.1,

\[
\boxed{
\widehat{\mathcal K}f_k=-2i\omega_d f_k.
}
\tag{K-rate}
\]

Now \(\omega_d\) has the dimensions of a frequency and acts consistently on all normalized state variables.

---

## B. Gradient-drive coefficients

Retain the same local Fourier convention as in the slab branch,

\[
\propto \exp[i(k_xx+k_yy+k_\parallel z)].
\]

Define, without yet introducing sign-normalized scale lengths,

\[
G_n
=
 i\frac{ck_yT_0}{eB_0}\,\frac{d\ln n_0}{dx},
\qquad
G_p
=
 i\frac{ck_yT_0}{eB_0}\,\frac{d\ln p_0}{dx}.
\]

These are exactly the normalized forms of the slab profile-advection terms. In the isotropic equilibrium both pressure equations carry the same equilibrium pressure-gradient drive \(G_p\Phi\).

---

## C. Density equation in the corrected local normalization

The dimensional B5.2B density equation, combined with

\[
\mathcal K\simeq -2\,\mathbf C\cdot\nabla,
\]

can be written exactly in the local normalized variables as

\[
\boxed{
\partial_t N
=
G_n\Phi
-i k_\parallel u
+\widehat{\mathcal K}
\left[
\Phi+\frac12(P_\parallel+P_\perp)
\right].
}
\tag{LC-N}
\]

Hence in Fourier curvature notation,

\[
\boxed{
\partial_t N
=
G_n\Phi
-i k_\parallel u
-2i\omega_d\Phi
-i\omega_d(P_\parallel+P_\perp).
}
\tag{LC-N-F}
\]

This retains the pressure-tensor combination \(P_\parallel+P_\perp\), which was the main consistency cross-check of B5.2B.1.

---

## D. Parallel-velocity equation in the same normalization

The four-moment source gives the curvature term through \(p_0\mathcal K(m u)/(mn_0)\). With the rate operator above this becomes simply \(\widehat{\mathcal K}u\). Therefore

\[
\boxed{
\partial_t u
=
\widehat{\mathcal K}u
-i k_\parallel c_s^2(\Phi+P_\parallel),
}
\tag{LC-u-norm}
\]

or

\[
\boxed{
\partial_t u
=
-2i\omega_d u
-i k_\parallel c_s^2(\Phi+P_\parallel).
}
\tag{LC-u-F}
\]

This is the dimensionally consistent version of the provisional momentum-frequency formula in B5.2B.1.

---

## E. Temperature-sector curvature structure from the local free-energy-consistent model

Scott's local GEM equations (dissipation-free Eqs. 99–102 in the 2005 model) fix the combinations that may appear under the curvature operator. In the ZLR, electrostatic, four-moment truncation used here, with parallel heat-flux moments omitted and \(\nabla_\parallel\ln B\) suppressed in the minimal local comparison, they imply the following temperature equations:

\[
\boxed{
\partial_t\Theta_\parallel
=
G_T\Phi
-2ik_\parallel u
+\widehat{\mathcal K}
\left(
\Phi+P_\parallel+2\Theta_\parallel
\right),
}
\tag{LC-T||}
\]

\[
\boxed{
\partial_t\Theta_\perp
=
G_T\Phi
+\widehat{\mathcal K}
\left(
\frac12\Phi+\frac12P_\perp+rac32\Theta_\perp
\right),
}
\tag{LC-Tperp}
\]

where

\[
G_T=G_p-G_n
\]

because \(p_0=n_0T_0\).

These equations are not guessed from a generic CGL closure. Their curvature combinations are inherited from the local free-energy-consistent moment structure, while the parallel-compression coefficients reproduce the four-moment slab limit.

---

## F. Pressure equations

Using

\[
P_\parallel=N+\Theta_\parallel,
\qquad
P_\perp=N+\Theta_\perp,
\]

and adding the density equation to the corresponding temperature equation gives the local pressure system.

### F.1 Parallel pressure

\[
\boxed{
\partial_t P_\parallel
=
G_p\Phi
-3ik_\parallel u
+\widehat{\mathcal K}
\left[
2\Phi-2N+
\frac72 P_\parallel+
\frac12 P_\perp
\right].
}
\tag{LC-P||}
\]

Therefore

\[
\boxed{
\begin{aligned}
\partial_t P_\parallel
={}&G_p\Phi-3ik_\parallel u\\
&-2i\omega_d
\left[
2\Phi-2N+
\frac72 P_\parallel+
\frac12 P_\perp
\right].
\end{aligned}
}
\tag{LC-P||-F}
\]

### F.2 Perpendicular pressure

\[
\boxed{
\partial_t P_\perp
=
G_p\Phi
-ik_\parallel u
+\widehat{\mathcal K}
\left[
\frac32\Phi-rac32N+
\frac12 P_\parallel+
\frac52 P_\perp
\right].
}
\tag{LC-Pperp}
\]

Hence

\[
\boxed{
\begin{aligned}
\partial_t P_\perp
={}&G_p\Phi-ik_\parallel u\\
&-2i\omega_d
\left[
\frac32\Phi-rac32N+
\frac12 P_\parallel+
\frac52 P_\perp
\right].
\end{aligned}
}
\tag{LC-Pperp-F}
\]

The two pressure moments therefore see different curvature combinations, as required by the anisotropic moment hierarchy; they are not related by a single arbitrary multiplicative factor.

---

## G. Complete minimal local-curvature four-moment DAE before electrostatic closure

Collecting the results,

\[
\boxed{
\begin{aligned}
\dot N={}&G_n\Phi-ik_\parallel u
-2i\omega_d\Phi
-i\omega_d(P_\parallel+P_\perp),\\
\dot u={}&-2i\omega_d u
-ik_\parallel c_s^2(\Phi+P_\parallel),\\
\dot P_\parallel={}&G_p\Phi-3ik_\parallel u
-2i\omega_d\left(2\Phi-2N+\frac72P_\parallel+\frac12P_\perp\right),\\
\dot P_\perp={}&G_p\Phi-ik_\parallel u
-2i\omega_d\left(\frac32\Phi-\frac32N+\frac12P_\parallel+\frac52P_\perp\right).
\end{aligned}
}
\tag{LC-4M}
\]

This remains a differential–algebraic system because \(\Phi\) is not yet eliminated. The electron response / polarization closure is deliberately deferred to B5.3A/B.

---

## H. Slab-limit check

Set

\[
\omega_d\to0.
\]

Then (LC-4M) becomes

\[
\dot N=G_n\Phi-ik_\parallel u,
\]

\[
\dot u=-ik_\parallel c_s^2(\Phi+P_\parallel),
\]

\[
\dot P_\parallel=G_p\Phi-3ik_\parallel u,
\]

\[
\dot P_\perp=G_p\Phi-ik_\parallel u.
\]

Multiplying the first equation by \(n_0\), the last two by \(p_0\), and using \(\widetilde\phi=(T_0/e)\Phi\) reproduces the isotropic-equilibrium subset of B5.2A exactly:

\[
\partial_t\widetilde n
=i\frac{ck_y}{B_0}n_0'\widetilde\phi
-ik_\parallel n_0\widetilde u,
\]

\[
\partial_t\widetilde u
=-ik_\parallel\left(\frac{e}{m}\widetilde\phi+\frac{\widetilde p_\parallel}{mn_0}\right),
\]

\[
\partial_t\widetilde p_\parallel
=i\frac{ck_y}{B_0}p_0'\widetilde\phi
-3ik_\parallel p_0\widetilde u,
\]

\[
\partial_t\widetilde p_\perp
=i\frac{ck_y}{B_0}p_0'\widetilde\phi
-ik_\parallel p_0\widetilde u.
\]

Thus the curvature branch has the required exact continuous connection to the slab control.

---

## I. What this step fixes and what remains open

Fixed for the branch comparison:

- a dimensionally consistent local curvature frequency \(\omega_d\);
- normalized state variables \((N,u,P_\parallel,P_\perp,\Phi)\);
- the complete minimal local-curvature four-moment differential equations before electrostatic closure;
- exact recovery of the slab branch as \(\omega_d\to0\).

Still deliberately unfixed:

- electron closure / polarization susceptibility;
- whether adiabatic electrons are sufficient for the first comparison;
- final sign-oriented definitions of \(L_n,L_T\) and \(\omega_d\);
- elimination of \(\Phi\);
- \(A_k^{\rm slab}\) and \(A_k^{\rm curv}\);
- perturbation free-energy Hessians;
- physical particle- and heat-flux matrices.

No numerical implementation should use (LC-4M) until the electrostatic closure is chosen and the resulting free-energy balance is checked.

---

## J. Next safe step

B5.3 should now treat the electrostatic closure as the only remaining algebraic ingredient needed to convert both branches into finite-dimensional ODEs. The cleanest next audit is to compare a minimal adiabatic-electron closure against the parent ZLR polarization relation and determine whether the same closure can be used for both slab and curvature without violating the intended free-energy structure.

Only after that check should \(\Phi\) be eliminated and the two matrices \(A_k^{\rm slab}\) and \(A_k^{\rm curv}\) be written.

## Literature anchors

- D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas **12**, 052517 (2005), arXiv:physics/0410276. Parent anisotropic four-moment equations and energy-conserving diamagnetic corrections.
- B. D. Scott, *GEM — An Energy Conserving Electromagnetic Gyrofluid Model*, Phys. Plasmas **12**, 102307 (2005), arXiv:physics/0501124. In particular the dissipation-free local six-moment equations (99)–(102), whose ZLR/four-moment restriction fixes the allowed density and temperature curvature combinations.
- B. D. Scott, *Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities*, Phys. Plasmas **17**, 102306 (2010), arXiv:0710.4899. Free-energy-consistent local curvature-operator structure.
