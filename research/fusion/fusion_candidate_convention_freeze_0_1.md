# Fusion F1.3 — Candidate / Convention Freeze 0.1

**Date:** 2026-09-04  
**Authority:** MASTER / `research/master/prompts/fusion_candidate_convention_freeze_0_1.md`  
**Status:** `F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION`

## Scope and anti-bias boundary

This file freezes one exact reduced Fusion candidate and the conventions needed for the later numerical/spectral qualification. It uses only the already-established R1 derivation chain, physical normalization, source/free-energy structure, and a canonical Cyclone-Base-Case (CBC) projection for the parameter point.

No finite-time free-energy or heat-transport operator is constructed here. No propagator, Gramian, cumulative flux extremum, optimizer vector/subspace, principal angle, performance gap, horizon dependence, parameter scan, stability-rescue scan, FLR restoration, kinetic-electron extension, six-moment GEM calculation, GENE calculation, or Paper-1 modification is performed.

The one parameter point below is frozen **before** any finite-time objective-separation inspection. If it later fails numerical/spectral qualification, the branch must return to MASTER; it may not be retuned in F1.4 by searching for a more favorable effect or spectrum.

---

## 1. Primary candidate and role of the slab branch

The selected primary reduced candidate is

\[
\boxed{
\text{anisotropic-ZLR four-moment R1 minimal-curvature branch}
}
\]

with one gyrofluid ion species, adiabatic electrons, electrostatic/quasineutral long-wavelength polarization, and the already-derived local single-curvature-frequency reduction.

This is selected because the frozen pre-effect lineage has already established all of the following without inspecting any finite-time energy-versus-heat separation:

- a source-faithful anisotropic four-moment parent reduction;
- a closed four-component minimal-curvature generator;
- exact recovery of the slab system as `omega_d -> 0`;
- the same positive perturbation free-energy metric in slab and curvature;
- the same physical signed ion radial heat-flux operator in slab and curvature;
- a full-state admissible initial-condition geometry with positive free-energy input cost.

The slab R1 generator is frozen only as an analytic/limiting control:

\[
\boxed{
A_k^{\rm curv}\xrightarrow{\omega_d\to0}A_k^{\rm slab}.
}
\]

It is not a competing effect-selected candidate and is not promoted to primary status by any later objective result.

---

## 2. State ordering and physical normalization

The frozen state ordering is

\[
\boxed{
z_k=(N,U,P_\parallel,P_\perp)^T
}
\]

with

\[
N=\frac{\widetilde n_i}{n_0},
\qquad
U=\frac{\widetilde u_\parallel}{c_s},
\qquad
P_\parallel=\frac{\widetilde p_\parallel}{p_0},
\qquad
P_\perp=\frac{\widetilde p_\perp}{p_0},
\]

\[
c_s^2=\frac{T_{i0}}{m_i},
\qquad
p_0=n_0T_{i0}.
\]

All four state coordinates are dimensionless. Temperature is measured in energy units, consistently with `p=nT`.

The corresponding normalized temperature perturbations are

\[
\Theta_\parallel=P_\parallel-N,
\qquad
\Theta_\perp=P_\perp-N.
\]

The equilibrium is isotropic,

\[
p_{\parallel0}=p_{\perp0}=p_0=n_0T_{i0},
\qquad
u_{\parallel0}=0,
\qquad
\phi_0=0,
\]

while the perturbations retain independent parallel and perpendicular pressure moments.

---

## 3. Fourier convention and admitted sector

Use the local/WKB single-complex-mode convention

\[
\boxed{
\propto \exp\left[i(k_xx+k_yy+k_\parallel z)\right].
}
\]

The positive radial direction is `+x`. The magnetic field orientation is the one already frozen in the slab/local derivation, giving

\[
\widetilde v_{E,x}
=-\frac{c}{B_0}\partial_y\widetilde\phi
=-i\frac{ck_y}{B_0}\widetilde\phi.
\]

The admitted transport sector is nonzonal:

\[
\boxed{k_y\neq0.}
\]

For a real physical field,

\[
z_{-k}=z_k^*.
\]

The single-complex-mode convention is primary; the real conjugate-pair value is twice the single-mode energy and heat flux, leaving all normalized balance identities unchanged.

For the frozen parameter point below, choose the representative orientation

\[
\boxed{k_y>0,\qquad k_\parallel>0.}
\]

---

## 4. Electrostatic / polarization closure

Use the already-frozen nonzonal adiabatic-electron response

\[
N_e=\tau_i\Phi,
\qquad
\tau_i\equiv\frac{T_{i0}}{T_{e0}}>0,
\]

with

\[
\Phi\equiv\frac{e\widetilde\phi}{T_{i0}}.
\]

Retain long-wavelength ion polarization inertia but no full FLR gyroaveraging:

\[
N-N_e-b_P\Phi=0,
\]

\[
\boxed{
b_P=k_\perp^2\rho_i^2,
\qquad
\rho_i^2=\frac{m_ic^2T_{i0}}{e^2B_0^2}.
}
\]

Thus

\[
\boxed{
\Phi=\mathcal C_kN,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P}>0.
}
\]

R1 is ZLR in the gyroaveraging/moment operators; retaining `b_P` in the long-wavelength polarization relation is part of the frozen R1 closure and is not an R2/FLR restoration.

The ion particle-flux channel remains identically collapsed:

\[
\boxed{Q_{\Gamma_i,k}=0.}
\]

No nonadiabatic electron response is introduced in F1.3.

---

## 5. Primary minimal-curvature generator

Define

\[
\kappa_\parallel\equiv k_\parallel c_s,
\]

and the gradient coefficients

\[
G_n
=i\frac{ck_yT_{i0}}{eB_0}\frac{d\ln n_0}{dx},
\qquad
G_p
=i\frac{ck_yT_{i0}}{eB_0}\frac{d\ln p_0}{dx}.
\]

The frozen primary dimensional generator is

\[
\boxed{
A_k^{\rm curv}=
\begin{pmatrix}
\mathcal C_kG_n-2i\omega_d\mathcal C_k
&-i\kappa_\parallel
&-i\omega_d
&-i\omega_d\\
-i\kappa_\parallel\mathcal C_k
&-2i\omega_d
&-i\kappa_\parallel
&0\\
\mathcal C_kG_p+4i\omega_d(1-\mathcal C_k)
&-3i\kappa_\parallel
&-7i\omega_d
&-i\omega_d\\
\mathcal C_kG_p+3i\omega_d(1-\mathcal C_k)
&-i\kappa_\parallel
&-i\omega_d
&-5i\omega_d
\end{pmatrix}.
}
\]

Every entry has units of inverse time.

The slab control is obtained exactly by `omega_d=0`:

\[
\boxed{
A_k^{\rm slab}=
\begin{pmatrix}
\mathcal C_kG_n & -i\kappa_\parallel & 0 & 0\\
-i\kappa_\parallel\mathcal C_k & 0 & -i\kappa_\parallel & 0\\
\mathcal C_kG_p & -3i\kappa_\parallel & 0 & 0\\
\mathcal C_kG_p & -i\kappa_\parallel & 0 & 0
\end{pmatrix}.
}
\]

No extra damping term is included in either matrix at this freeze.

---

## 6. Positive free-energy metric and energy normalization

The frozen perturbation free energy is

\[
\boxed{
W_k=\frac{p_0}{2}z_k^\dagger M_kz_k
}
\]

with

\[
\boxed{
M_k=
\begin{pmatrix}
\frac52+\mathcal C_k & 0 & -\frac12 & -1\\
0 & 1 & 0 & 0\\
-\frac12 & 0 & \frac12 & 0\\
-1 & 0 & 0 & 1
\end{pmatrix}.
}
\]

Equivalently,

\[
\frac{2W_k}{p_0}
=(1+\mathcal C_k)|N|^2+|U|^2
+\frac12|P_\parallel-N|^2
+|P_\perp-N|^2.
\]

Hence

\[
\boxed{M_k=M_k^\dagger\succ0.}
\]

The same `M_k` applies to both slab and minimal curvature.

---

## 7. Physical signed ion heat-flux operator

Define the signed velocity scale

\[
\boxed{
\mathcal V_k
\equiv\frac{ck_yT_{i0}}{eB_0}
=k_y\rho_i c_s.
}
\]

For `k_y>0`, `mathcal V_k>0` in the frozen coordinate orientation.

The physical single-complex-mode ion radial thermal-energy/heat flux is

\[
q_{i,k}=z_k^\dagger Q_{q_i,k}z_k,
\]

with

\[
\boxed{
Q_{q_i,k}
=p_0\mathcal V_k\mathcal C_k
\begin{pmatrix}
0&0&i/4&i/2\\
0&0&0&0\\
-i/4&0&0&0\\
-i/2&0&0&0
\end{pmatrix}.
}
\]

Equivalently,

\[
q_{i,k}
=-p_0\mathcal V_k\mathcal C_k
\operatorname{Im}\left[
N^*\left(\frac12P_\parallel+P_\perp\right)
\right].
\]

This is the radial `E x B` transport of

\[
\frac12\widetilde T_{i\parallel}+\widetilde T_{i\perp},
\]

multiplied by `n_0`. It has units pressure times velocity.

For `k_y!=0`,

\[
\boxed{
Q_{q_i,k}=Q_{q_i,k}^\dagger,
\qquad
\operatorname{rank}(Q_{q_i,k})=2,
\qquad
\operatorname{signature}(Q_{q_i,k})=(1,1,2).
}
\]

The same instantaneous physical heat operator applies to slab and curvature.

---

## 8. Admissible input geometry and cost

F1.2 is carried forward unchanged:

\[
\boxed{
B=I_4,
\qquad
R_{\rm in}=M_k,
\qquad
\operatorname{rank}(B)=4.
}
\]

`B=I_4` means that the initial-condition problem ranges over the full already-closed R1 tangent state. It is not a claim that an experiment independently actuates density, parallel flow, parallel pressure, and perpendicular pressure.

The dimensional input free-energy budget is

\[
\frac{p_0}{2}a^\dagger R_{\rm in}a.
\]

The instantaneous restricted heat channel remains

\[
B^\dagger Q_{q_i,k}B=Q_{q_i,k};
\]

transport neutrality is not imposed.

---

## 9. Equilibrium-gradient convention

Freeze outward-decreasing equilibrium profiles by

\[
\boxed{
L_n^{-1}\equiv-\frac{d\ln n_0}{dx}>0,
\qquad
L_T^{-1}\equiv-\frac{d\ln T_{i0}}{dx}>0.
}
\]

Because `p_0=n_0T_{i0}`,

\[
L_p^{-1}=L_n^{-1}+L_T^{-1}.
\]

For `k_y>0`,

\[
\boxed{
G_n=-i\frac{\mathcal V_k}{L_n},
\qquad
G_p=-i\mathcal V_k\left(\frac1{L_n}+\frac1{L_T}\right).
}
\]

The temperature-gradient rate appearing in the balance is

\[
\gamma_T
=\mathcal V_k\frac{d\ln T_{i0}}{dx}
=-\frac{\mathcal V_k}{L_T}.
\]

The positive drive coefficient used in the physical balance is

\[
\boxed{g_T=L_T^{-1}>0.}
\]

The density-gradient contribution cancels from the Hermitian free-energy injection in this frozen adiabatic-electron R1 closure; it remains in the generator but not as an independent particle-flux work channel.

---

## 10. Curvature-frequency convention

Use the already-audited local Scott convention

\[
\boxed{
\widehat{\mathcal K}f_k=-2i\omega_df_k,
\qquad
\mathbf C\cdot\nabla f_k=i\omega_df_k.
}
\]

The `y` orientation for the frozen positive-`k_y` representative is chosen so that the minimal large-aspect-ratio local drift frequency is positive:

\[
\boxed{
\omega_d=\frac{k_y\rho_i c_s}{R_0}>0.
}
\]

Here `R_0` is the local tokamak major-radius reference scale used for the CBC projection and the time normalization below.

This fixes the sign convention rather than searching over curvature signs. The factor-of-two relation in the curvature operator remains source/free-energy constrained.

---

## 11. Parallel wavenumber and retained/suppressed geometry

The R1 candidate is a single local Fourier block, not a resolved field-line model. Retain one nonzero parallel harmonic.

For the CBC-projected point, take the standard connection-length scale

\[
L_\parallel=2\pi qR_0
\]

and freeze the fundamental positive Fourier harmonic

\[
\boxed{
k_\parallel=\frac{2\pi}{L_\parallel}=\frac{1}{qR_0}>0.
}
\]

Thus

\[
\kappa_\parallel=\frac{c_s}{qR_0}.
\]

Retained geometric effects:

- one local radial equilibrium coordinate `x`;
- one binormal Fourier coordinate `y`;
- one nonzero parallel Fourier harmonic;
- the single free-energy-consistent local curvature frequency `omega_d`;
- parallel compression and electrostatic parallel force already present in the four-moment equations.

Suppressed at R1:

- field-line dependence of `k_perp`;
- magnetic shear as an explicit dynamical/geometric operator;
- ballooning-angle structure;
- `nabla_parallel ln B` terms in the minimal four-moment comparison;
- trapped-particle dynamics;
- full FLR gyroaveraging operators;
- electromagnetic fluctuations;
- kinetic electron dynamics;
- independent conductive heat-flux moments.

Therefore the point below is a **CBC projection onto the frozen R1 minimal-curvature model**, not a claim that R1 reproduces the complete CBC flux-tube geometry.

---

## 12. Dissipation and closure freeze

The R1 source/free-energy lineage is nondissipative before profile drive. Freeze that source-faithful choice:

\[
\boxed{
\nu_{\rm coll}=0,
\qquad
D_{\rm visc}=0,
\qquad
D_{\rm diff}=0,
\qquad
\text{no Landau-fluid closure term},
\qquad
\text{no artificial }-\nu I_4\text{ damping}.
}
\]

The electron closure remains strictly adiabatic and algebraic as in Sec. 4.

This choice is made for two pre-effect reasons:

1. it is the exact energetic R1 model already derived and checked;
2. collisionless CBC is a canonical reference regime in gyrokinetic benchmarking.

No damping coefficient is tuned to make the spectrum stable. F1.4 must qualify the frozen operator as it stands. If its spectral properties are incompatible with the intended later pilot criteria, F1.4 must return that fact to MASTER rather than search for a stabilizing parameter or damping rate.

---

## 13. Frozen physical parameter point: CBC-projected R1

Use the standard Cyclone-Base-Case dimensionless equilibrium values relevant to the present reduced model:

\[
\boxed{
\tau_i=\frac{T_{i0}}{T_{e0}}=1,
\qquad
\frac{R_0}{L_n}=2.2,
\qquad
\frac{R_0}{L_T}=6.9,
\qquad
q=1.4.
}
\]

These are canonical CBC values originating in the Dimits et al. benchmark lineage. They are adopted as external benchmark conventions, not selected from any nonmodal result.

Freeze one standard ion-scale single-mode representative

\[
\boxed{
k_x\rho_i=0,
\qquad
k_y\rho_i=0.3,
}
\]

with `k_y>0`. The value `k_y rho_i=0.3` is a standard linear-CBC ion-scale choice used in published CBC analyses; it is not obtained by scanning this R1 model.

Then

\[
b_P=k_\perp^2\rho_i^2=0.09,
\]

\[
\boxed{
\mathcal C_k=\frac{1}{1+0.09}
=\frac{100}{109}
\approx0.9174311927.
}
\]

The frozen gradient derivatives are

\[
\frac{d\ln n_0}{dx}=-\frac{2.2}{R_0},
\qquad
\frac{d\ln T_{i0}}{dx}=-\frac{6.9}{R_0},
\qquad
\frac{d\ln p_0}{dx}=-\frac{9.1}{R_0}.
\]

The parallel and curvature rates are

\[
\boxed{
k_\parallel R_0=\frac{1}{1.4}=\frac57,
\qquad
\omega_d\frac{R_0}{c_s}=0.3.
}
\]

The model remains electrostatic (`beta` effects absent by construction) and collisionless at this freeze.

### Why this point is admissible without effect inspection

- `Ti/Te=1`, `R/L_n=2.2`, `R/L_Ti=6.9`, and `q=1.4` are standard CBC benchmark values.
- `k_y rho_i=0.3` is a standard single-mode ion-scale CBC convention used in linear studies.
- `k_x=0` is the minimal local single-mode radial choice and avoids introducing an arbitrary radial phase tilt before any continuation/ballooning geometry exists.
- `k_parallel=1/(qR_0)` is the fundamental harmonic associated with the standard connection length `2 pi q R_0` in this one-Fourier-harmonic R1 reduction.
- `omega_d=k_y rho_i c_s/R_0` is the minimal large-aspect-ratio local curvature-rate convention consistent with the already-frozen `K -> -2 i omega_d` operator.
- no value was chosen by inspecting finite-time heat/energy separation, transient growth, optimizer geometry, or a stability search.

---

## 14. Time normalization and dimensional mapping

Freeze the major-radius sound time

\[
\boxed{
\tau_{\rm ref}=\frac{R_0}{c_s}.
}
\]

Define

\[
\widehat t=\frac{t}{\tau_{\rm ref}},
\qquad
\widehat A_k=\tau_{\rm ref}A_k.
\]

Then

\[
A_k=\frac{c_s}{R_0}\widehat A_k.
\]

The normalized rate parameters are

\[
\widehat\kappa_\parallel
=\kappa_\parallel\tau_{\rm ref}
=k_\parallel R_0,
\]

\[
\widehat\omega_d
=\omega_d\tau_{\rm ref},
\]

\[
\widehat G_n=\tau_{\rm ref}G_n,
\qquad
\widehat G_p=\tau_{\rm ref}G_p.
\]

Using

\[
\mathcal V_k=k_y\rho_i c_s,
\]

one obtains generally

\[
\widehat G_n
=-i(k_y\rho_i)\frac{R_0}{L_n},
\]

\[
\widehat G_p
=-i(k_y\rho_i)
\left(\frac{R_0}{L_n}+\frac{R_0}{L_T}\right).
\]

At the frozen point,

\[
\boxed{
\widehat\kappa_\parallel=\frac57\approx0.7142857143,
\qquad
\widehat\omega_d=0.3,
}
\]

\[
\boxed{
\widehat G_n=-0.66i,
\qquad
\widehat G_p=-2.73i.
}
\]

The heat-flux normalization is

\[
\boxed{
\widehat Q_{q_i,k}
\equiv\frac{Q_{q_i,k}}{p_0c_s}
=(k_y\rho_i)\mathcal C_k\mathsf Q_0,
}
\]

where

\[
\mathsf Q_0=
\begin{pmatrix}
0&0&i/4&i/2\\
0&0&0&0\\
-i/4&0&0&0\\
-i/2&0&0&0
\end{pmatrix}.
\]

Thus

\[
\frac{q_{i,k}}{p_0c_s}
=z_k^\dagger\widehat Q_{q_i,k}z_k.
\]

At the frozen point,

\[
(k_y\rho_i)\mathcal C_k
=\frac{30}{109}
\approx0.2752293578.
\]

The physical dimensional mappings needed later are therefore

\[
t=\frac{R_0}{c_s}\widehat t,
\qquad
A=\frac{c_s}{R_0}\widehat A,
\qquad
W=\frac{p_0}{2}z^\dagger Mz,
\qquad
q_i=p_0c_s\,z^\dagger\widehat Q_{q_i}z.
\]

No absolute SI/cgs equilibrium scale is required to define the normalized candidate; if later dimensional numbers are desired, they must use one internally consistent species/unit convention without altering the normalized freeze.

---

## 15. Explicit normalized primary matrix at the frozen point

Substitution into the already-derived generator gives

\[
\boxed{
\widehat A_k^{\rm curv}
=-i
\begin{pmatrix}
1.1559633028&0.7142857143&0.3&0.3\\
0.6553079948&0.6&0.7142857143&0\\
2.4055045872&2.1428571429&2.1&0.3\\
2.4302752294&0.7142857143&0.3&1.5
\end{pmatrix}.
}
\]

This matrix is only the direct algebraic evaluation of the frozen analytic formula. No eigenvalue, singular-value, pseudospectral, transient-growth, or finite-time transport calculation is performed in F1.3.

At the same point,

\[
\boxed{
M_k=
\begin{pmatrix}
3.4174311927&0&-0.5&-1\\
0&1&0&0\\
-0.5&0&0.5&0\\
-1&0&0&1
\end{pmatrix}.
}
\]

The normalized heat matrix is

\[
\boxed{
\widehat Q_{q_i,k}
=0.2752293578
\begin{pmatrix}
0&0&i/4&i/2\\
0&0&0&0\\
-i/4&0&0&0\\
-i/2&0&0&0
\end{pmatrix}.
}
\]

And

\[
B=I_4,
\qquad
R_{\rm in}=M_k.
\]

---

## 16. Exact identities required at F1.4 qualification

F1.4 must check the following without changing the frozen point.

### 16.1 Closure and positivity

\[
\mathcal C_k=\frac{1}{\tau_i+b_P}>0,
\]

and the closure residual must vanish:

\[
\boxed{N-(\tau_i+b_P)\Phi=0.}
\]

The metric must satisfy

\[
\boxed{M_k=M_k^\dagger\succ0.}
\]

For the frozen ordering, the exact leading principal minors are

\[
\Delta_1=\Delta_2=\frac{5+2\mathcal C_k}{2},
\qquad
\Delta_3=\frac{2+\mathcal C_k}{2},
\qquad
\Delta_4=\frac{1+\mathcal C_k}{2},
\]

all strictly positive.

### 16.2 Heat operator

\[
\boxed{
Q_{q_i,k}=Q_{q_i,k}^\dagger,
\qquad
\operatorname{rank}(Q_{q_i,k})=2,
\qquad
\operatorname{signature}(Q_{q_i,k})=(1,1,2).
}
\]

The direct reconstruction

\[
q_{i,k}
=-p_0\mathcal V_k\mathcal C_k
\operatorname{Im}\left[N^*\left(\frac12P_\parallel+P_\perp\right)\right]
\]

must agree with `z^dagger Q z` to numerical roundoff.

The particle channel must remain

\[
\boxed{Q_{\Gamma_i,k}=0.}
\]

### 16.3 Input geometry

\[
\boxed{
B=I_4,
\qquad
R_{\rm in}=M_k,
\qquad
\operatorname{rank}(B)=4,
\qquad
B^\dagger Q_{q_i,k}B=Q_{q_i,k}.
}
\]

### 16.4 Slab/curvature structural consistency

The matrix identity

\[
\boxed{
A_k^{\rm curv}(\omega_d=0)=A_k^{\rm slab}
}
\]

must hold entry by entry.

With profile gradients removed,

\[
G_n=G_p=0,
\]

the source-free curvature and slab generators must obey

\[
\boxed{
A_{0,k}^\dagger M_k+M_kA_{0,k}=0.
}
\]

Thus no spurious dissipation or source may be introduced by the curvature discretization.

### 16.5 Full gradient-drive / heat-flux balance

The exact dimensional identity is

\[
\boxed{
A_k^\dagger M_k+M_kA_k
=2\left(-\frac{d\ln T_{i0}}{dx}\right)
\frac{Q_{q_i,k}}{p_0}.
}
\]

Equivalently,

\[
\boxed{
\frac{dW_k}{dt}
=-\frac{d\ln T_{i0}}{dx}\,q_{i,k}.
}
\]

In the frozen time/heat normalization,

\[
\boxed{
\widehat A_k^\dagger M_k+M_k\widehat A_k
=2\frac{R_0}{L_T}\widehat Q_{q_i,k}.
}
\]

At the frozen point,

\[
\boxed{
\widehat A_k^\dagger M_k+M_k\widehat A_k
=13.8\,\widehat Q_{q_i,k}.
}
\]

This is an algebraic balance identity, not a finite-time objective calculation.

### 16.6 Conjugate-mode consistency

Under

\[
k\mapsto-k,
\qquad
z_{-k}=z_k^*,
\]

the reconstructed real-field heat flux must be invariant, and the real conjugate-pair energy/heat values must be twice the single-complex-mode values.

---

## 17. Qualification-stage checks that are explicitly deferred

F1.4 may now test, at this one frozen point and without retuning:

- numerical Hermiticity/positivity and conditioning;
- exact algebraic balance residuals;
- eigenvalue/spectral qualification of the frozen generator;
- whether the spectral regime is compatible with the later pilot rules;
- representation/reconstruction consistency of the physical heat channel;
- any predeclared numerical precision/resolution checks that do not inspect finite-time objective separation.

F1.4 may **not** select a different `R/L_T`, `R/L_n`, `q`, `k_y`, `k_x`, `k_parallel`, `omega_d`, closure, or damping rate because the frozen point has an inconvenient spectrum. Any scientifically consequential failure returns to MASTER.

Finite-time free-energy-versus-heat objective separation remains forbidden until the later literature checkpoint, pilot specification, MASTER pilot freeze, and one-shot execution authorize it.

---

## 18. Allowed interpretations

This freeze supports the following statements:

- the minimal-curvature anisotropic-ZLR four-moment R1 system is the uniquely selected primary reduced candidate for FUSION-F1 at this stage;
- the slab system is its exact zero-curvature analytic/limiting control;
- the state, electrostatic closure, free-energy metric, heat-flux operator, input geometry/cost, gradient signs, curvature sign, one parallel harmonic, time normalization, and one CBC-projected physical parameter point are fixed before effect inspection;
- the benchmark point is a deliberately reduced projection of standard CBC ion-scale conditions onto R1;
- no artificial dissipation has been added to rescue or shape the spectrum.

---

## 19. Forbidden interpretations

This freeze does **not** establish that:

- the frozen generator is spectrally stable;
- it exhibits transient free-energy growth;
- energy-optimal and heat-optimal initial perturbations differ;
- any optimizer angle, performance gap, or cumulative heat-flux effect is large or small;
- the chosen `k_y rho_i=0.3` is optimal for the present method;
- the reduced R1 model reproduces full CBC magnetic shear, ballooning structure, trapped particles, FLR physics, or gyrokinetic phase-space dynamics;
- collisionless R1 must be repaired with damping if F1.4 fails;
- a later FLR/GK result may be inferred from this freeze.

---

## 20. External benchmark basis for the parameter convention

The dimensionless equilibrium values used above are the standard Cyclone Base Case introduced in the Dimits benchmark lineage, with the conventional values

\[
R_0/L_{T_i}\simeq6.9,
\qquad
R_0/L_n\simeq2.2,
\qquad
T_i/T_e=1,
\qquad
q\simeq1.4.
\]

Primary benchmark anchor:

- A. M. Dimits et al., *Comparisons and physics basis of tokamak transport models and turbulence simulations*, Phys. Plasmas **7**, 969–983 (2000), DOI `10.1063/1.873896`.

Published CBC linear studies also use `k_y rho` values around `0.3` as a standard representative ion-scale mode. That convention is used here solely to freeze one pre-effect Fourier block; no R1 scan was performed.

No literature novelty claim is made in F1.3.

---

## 21. Verdict

All F1.3 requirements can be frozen uniquely without inspecting a finite-time objective effect:

- primary candidate selected;
- slab control role fixed;
- state and normalization fixed;
- Fourier/nonzonal convention fixed;
- electrostatic closure fixed;
- exact primary generator fixed;
- positive free-energy metric fixed;
- signed physical heat-flux matrix fixed;
- `B=I_4`, `R_in=M_k` fixed;
- density/temperature-gradient signs fixed;
- curvature frequency and sign fixed;
- one nonzero parallel harmonic fixed;
- dissipation/closure frozen as collisionless/source-faithful;
- one CBC-projected physical parameter point fixed before effect inspection;
- `tau_ref=R_0/c_s` and dimensional mappings fixed;
- exact algebraic qualification identities enumerated.

Therefore

\[
\boxed{
\text{F1.3 PASS — CANDIDATE/CONVENTION FROZEN — RETURN TO MASTER FOR NUMERICAL/SPECTRAL QUALIFICATION}
}
\]

No branch-side F1.4 execution is self-authorized.

**STOP / RETURN TO MASTER.**
