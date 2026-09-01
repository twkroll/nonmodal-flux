# B5.4A — Positive slab free-energy metric

**Status:** completed derivation of the positive quadratic free-energy metric for the closed nonzonal slab R1 branch; no heat-flux operator or optimization constructed yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/B5_3_electrostatic_closure_audit.md`, `research/fusion/B5_3A_slab_generator.md`

## Scope

This step derives the positive quadratic metric to be used as the physical initial-energy constraint for the slab branch. It does **not** identify the nonlinear total energy of the Strintzi–Scott–Brizard parent model with the perturbation norm. Instead it uses the explicit delta-f gyrofluid free-energy decomposition derived by Scott and then restricts that quadratic functional to the present electrostatic four-moment, adiabatic-electron, long-wavelength state space.

The state coordinates remain

\[
z_k=\begin{pmatrix}N\\ U\\ P_\parallel\\ P_\perp\end{pmatrix},
\qquad
N=\frac{\widetilde n_i}{n_0},
\qquad
U=\frac{\widetilde u_\parallel}{c_s},
\]

\[
P_\parallel=\frac{\widetilde p_\parallel}{p_0},
\qquad
P_\perp=\frac{\widetilde p_\perp}{p_0},
\qquad
c_s^2=\frac{T_{i0}}{m_i},
\qquad
p_0=n_0T_{i0}.
\]

The closure from B5.3 is

\[
\Phi=\mathcal C_k N,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P},
\qquad
\tau_i=\frac{T_{i0}}{T_{e0}}>0,
\qquad
b_P=k_\perp^2\rho_i^2\ge0.
\]

Only the nonzonal sector \(k_y\neq0\) is considered here.

---

## A. Source-supported delta-f free-energy pieces

Scott's systematic gyrofluid derivation from the delta-f gyrokinetic free energy gives the thermal free-energy density of one species as

\[
U_t
=\frac{nT}{2}
\left[
\left(\frac{\widetilde n}{n}\right)^2
+\frac12\left(\frac{\widetilde T_\parallel}{T}\right)^2
+\left(\frac{\widetilde T_\perp}{T}\right)^2
\right],
\]

and the kinetic free-energy density as

\[
U_v
=\frac{nT}{2}
\left[
\left(\frac{\widetilde u_\parallel}{\sqrt{T/m}}\right)^2
+\cdots
\right],
\]

where the omitted terms are the parallel heat-flux moments absent from the present four-moment truncation.

For the isotropic equilibrium used in B5.2B/B5.3,

\[
\Theta_\parallel
\equiv\frac{\widetilde T_\parallel}{T_{i0}}
=P_\parallel-N,
\qquad
\Theta_\perp
\equiv\frac{\widetilde T_\perp}{T_{i0}}
=P_\perp-N.
\]

Thus the ion thermal-plus-parallel-kinetic contribution for one Fourier mode is, up to the conventional overall mode-volume/Fourier-pair factor,

\[
W_{i,k}
=\frac{n_0T_{i0}}{2}
\left[
|N|^2
+\frac12|P_\parallel-N|^2
+|P_\perp-N|^2
+|U|^2
\right].
\tag{FE-ion}
\]

This coefficient structure is not guessed from the nonlinear parent energy; it is the quadratic delta-f free energy associated with the retained density, two temperature moments, and parallel flow.

---

## B. Electrostatic and adiabatic-electron contributions

The long-wavelength ion polarization energy is the usual ExB energy,

\[
W_{E,k}
=\frac{n_0m_i}{2}\frac{c^2}{B_0^2}
|\nabla_\perp\widetilde\phi_k|^2.
\]

Using

\[
\Phi=\frac{e\widetilde\phi}{T_{i0}},
\qquad
b_P=k_\perp^2\frac{m_ic^2T_{i0}}{e^2B_0^2},
\]

this is

\[
W_{E,k}
=\frac{n_0T_{i0}}{2}\,b_P|\Phi|^2.
\tag{FE-pol}
\]

For nonzonal adiabatic electrons,

\[
N_e=\frac{\widetilde n_e}{n_0}
=\frac{e\widetilde\phi}{T_{e0}}
=\tau_i\Phi.
\]

Their quadratic thermal free energy is therefore

\[
W_{e,k}
=\frac{n_0T_{e0}}{2}|N_e|^2
=\frac{n_0T_{i0}}{2}\,\tau_i|\Phi|^2.
\tag{FE-e}
\]

Combining the two electrostatic pieces gives

\[
W_{E,k}+W_{e,k}
=\frac{n_0T_{i0}}{2}(\tau_i+b_P)|\Phi|^2.
\]

With the closure

\[
N=(\tau_i+b_P)\Phi,
\]

this becomes

\[
\boxed{
W_{E,k}+W_{e,k}
=\frac{n_0T_{i0}}{2}\,\mathcal C_k|N|^2.
}
\tag{FE-pot}
\]

This is the useful form after eliminating the electrostatic potential.

---

## C. Closed slab free energy in the four state coordinates

Adding (FE-ion) and (FE-pot),

\[
\boxed{
W_k^{\rm slab}
=\frac{n_0T_{i0}}{2}
\left[
(1+\mathcal C_k)|N|^2
+\frac12|P_\parallel-N|^2
+|P_\perp-N|^2
+|U|^2
\right].
}
\tag{FE-slab-compact}
\]

Every term is manifestly nonnegative, and because \(\mathcal C_k>0\), the sum vanishes only for

\[
N=U=P_\parallel=P_\perp=0.
\]

Hence it defines a positive-definite Hermitian quadratic form on the closed four-dimensional state space.

Expanding the temperature differences gives

\[
W_k^{\rm slab}
=\frac{n_0T_{i0}}{2}
\,z_k^\dagger M_k^{\rm slab}z_k,
\]

with

\[
\boxed{
M_k^{\rm slab}
=
\begin{pmatrix}
\frac52+\mathcal C_k & 0 & -\frac12 & -1\\
0 & 1 & 0 & 0\\
-\frac12 & 0 & \frac12 & 0\\
-1 & 0 & 0 & 1
\end{pmatrix}.
}
\tag{M-slab}
\]

The off-diagonal entries are physical consequences of using pressure coordinates rather than temperature coordinates. In the thermodynamic coordinates

\[
y_k=(N,U,\Theta_\parallel,\Theta_\perp)^\top,
\]

the same metric is diagonal:

\[
W_k^{\rm slab}
=\frac{n_0T_{i0}}{2}
\left[
(1+\mathcal C_k)|N|^2+|U|^2
+\frac12|\Theta_\parallel|^2+|\Theta_\perp|^2
\right].
\]

Thus the cross terms in (M-slab) are a coordinate effect, not an indefinite energetic contribution.

---

## D. Explicit positivity check

For the ordering \((N,U,P_\parallel,P_\perp)\), the leading principal minors are

\[
\Delta_1=\frac{5+2\mathcal C_k}{2},
\qquad
\Delta_2=\frac{5+2\mathcal C_k}{2},
\]

\[
\Delta_3=\frac{2+\mathcal C_k}{2},
\qquad
\Delta_4=\det M_k^{\rm slab}
=\frac{1+\mathcal C_k}{2}.
\]

Because

\[
\mathcal C_k=\frac{1}{\tau_i+b_P}>0,
\]

all four are strictly positive. By Sylvester's criterion,

\[
\boxed{M_k^{\rm slab}\succ0.}
\]

A second transparent proof follows from the Schur complement of the \((P_\parallel,P_\perp)\) block \(D=\operatorname{diag}(1/2,1)\):

\[
\left(\frac52+\mathcal C_k\right)
-\begin{pmatrix}-\frac12&-1\end{pmatrix}
D^{-1}
\begin{pmatrix}-\frac12\\-1\end{pmatrix}
=1+\mathcal C_k>0.
\]

---

## E. Conservative slab check against the closed generator

A physical metric should make the source-free slab dynamics conservative. Set the profile drives to zero,

\[
G_n=G_p=0.
\]

The closed slab generator from B5.3A is then

\[
A_{0,k}^{\rm slab}
=
\begin{pmatrix}
0&-i\kappa_\parallel&0&0\\
-i\kappa_\parallel\mathcal C_k&0&-i\kappa_\parallel&0\\
0&-3i\kappa_\parallel&0&0\\
0&-i\kappa_\parallel&0&0
\end{pmatrix}.
\]

Direct multiplication gives the exact identity

\[
\boxed{
(A_{0,k}^{\rm slab})^\dagger M_k^{\rm slab}
+M_k^{\rm slab}A_{0,k}^{\rm slab}=0.
}
\tag{FE-conservation}
\]

Therefore

\[
\frac{d}{dt}W_k^{\rm slab}=0
\]

for the homogeneous nondissipative slab system. This is a strong internal check that the free-energy coefficients, electrostatic closure, velocity rescaling, and pressure-coordinate transformation are mutually consistent.

When \(G_n\) and/or \(G_p\) are nonzero, the left-hand side is no longer zero: those terms represent profile-gradient free-energy injection. Their decomposition into the physical heat-flux channel is deferred to B5.5 rather than being guessed here.

---

## F. What is fixed after B5.4A

For the nonzonal adiabatic-electron slab branch, the positive physical metric is now fixed, up to an irrelevant overall positive normalization, by

\[
\boxed{
M_k^{\rm slab}
=
\begin{pmatrix}
\frac52+\mathcal C_k & 0 & -\frac12 & -1\\
0 & 1 & 0 & 0\\
-\frac12 & 0 & \frac12 & 0\\
-1 & 0 & 0 & 1
\end{pmatrix},
\qquad
\mathcal C_k=\frac{1}{\tau_i+k_\perp^2\rho_i^2}.
}
\]

It satisfies

\[
M_k^{\rm slab}\succ0
\]

and conserves free energy exactly under the source-free slab generator.

Still deliberately open:

- whether the same metric is conservative under the source-free minimal-curvature generator;
- the precise gradient-drive/free-energy balance in the curvature branch;
- the physical heat-flux matrix \(Q_{q,k}\);
- admissible input maps and transport-neutral subspaces;
- finite-horizon optimization and numerical sweeps.

The next safe step is B5.4B: test this source-derived metric against the minimal-curvature generator before introducing any transport operator.

---

## Literature anchors

- B. D. Scott, *Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities*, Phys. Plasmas **17**, 102306 (2010), arXiv:0710.4899. The gyrofluid free energy follows directly from the delta-f gyrokinetic free energy; Eq. (45) gives the thermal contribution \(nT[ N^2+\Theta_\parallel^2/2+\Theta_\perp^2]/2\), and Eq. (46) gives the parallel-flow contribution.
- B. D. Scott, *GEM — An Energy Conserving Electromagnetic Gyrofluid Model*, Phys. Plasmas **12**, 102307 (2005), arXiv:physics/0501124. The paper separates ExB, electron thermal, and ion thermal free energies, and for adiabatic electrons combines the electron response with the polarization energy into the potential-energy sector.
- D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas **12**, 052517 (2005), arXiv:physics/0410276. This remains the nonlinear four-moment parent model, but its nonlinear total energy is not used directly as the perturbation metric in this step.
