# Fusion F2.1 — Balance-Complete Two-Species Local-Gyrokinetic Candidate / Balance Specification Gate 0.1

**Date:** 2026-09-05  
**Authority:** MASTER / `research/master/prompts/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`  
**Status:** `F2.1 PASS — TWO-SPECIES GK CANDIDATE/BALANCE SPECIFIED — RETURN TO MASTER`

## Scope

This gate specifies one physically justified higher-fidelity two-species local-gyrokinetic lineage after the frozen R1 one-channel structural no-go. It freezes only the **continuous model architecture and exact free-energy/transport balance** needed to decide whether the R1 affine redundancy remains structurally forced.

No phase-space discretization, parameter scan, wavenumber scan, collision-frequency scan, trapped-particle-fraction scan, GENE run, finite-time propagator, Gramian, cumulative CORE operator, optimizer, principal angle, performance gap, horizon dependence or effect-size calculation is performed.

The selection criterion is balance completeness, source fidelity and tractability only.

---

# 1. Fidelity architecture selected

The primary reduced candidate is

\[
\boxed{
\text{electrostatic local GK ions with finite ion FLR}
\; + \;
\text{collisionless nonadiabatic bounce-averaged trapped electrons}
}
\]

in a toroidal flux-tube geometry, with passing electrons adiabatic to lowest order in the electron-transit ordering.

The higher-fidelity reference is

\[
\boxed{
\text{fully kinetic two-species electrostatic local gyrokinetics}
}
\]

with nonadiabatic ions and electrons, finite gyroaveraging retained consistently, and an H-theorem-compatible linearized gyrokinetic/Fokker–Planck collision operator.

The frozen R1 anisotropic-ZLR four-moment model remains only a structural conservative control. An FLR-only, adiabatic-electron extension is likewise retained only as a possible conservative control, not as the primary F2 lineage.

## 1.1 Why this reduced candidate is selected

The choice follows directly from the source hierarchy already frozen by the R1 literature audit:

1. finite-ion-FLR gyrokinetic ions restore the standard ion-scale phase-space dynamics without inventing a reduced moment closure;
2. bounce-averaged trapped electrons introduce a source-faithful nonadiabatic electron degree of freedom in a controlled ion-scale ordering;
3. the model has a documented two-species Helmholtz free-energy balance;
4. it keeps the electron state substantially smaller than a fully kinetic electron phase space;
5. it does not require an effect-motivated damping term or an FLR-only rescue.

Costello & Plunk (2025) derive exactly this reduced collisionless architecture: finite-FLR gyrokinetic ions plus bounce-averaged trapped electrons in the ordering where the dynamics are slow compared with the thermal-electron transit time.

---

# 2. Geometry, Fourier sector and equilibrium assumptions

Use Clebsch magnetic coordinates

\[
\mathbf B=\nabla\psi\times\nabla\alpha,
\]

with

- `psi` the radial flux coordinate, chosen to increase outward;
- `alpha` the binormal field-line label;
- `l` the coordinate along the magnetic field.

For one perpendicular Fourier component,

\[
\mathbf k_\perp
=k_\alpha\nabla\alpha+k_\psi\nabla\psi.
\]

The reduced F2.1 architecture is restricted to the nonzonal ion-scale sector

\[
\boxed{k_\alpha\neq0,\qquad k_\perp\rho_e\ll1,}
\]

with finite ion FLR,

\[
\boxed{b_i=k_\perp^2\rho_i^2\ \text{retained, not expanded away}.}
\]

The exact magnetic configuration `B(l)`, magnetic shear, `k_perp(l)`, trapped-particle fraction and numerical radial/binormal wavenumbers are **not** frozen in F2.1.

Assume a local Maxwellian equilibrium for a hydrogenic plasma,

\[
F_{a0}=F_{a0}(n_a(\psi),T_a(\psi)),
\qquad n_i=n_e=n,
\]

with no equilibrium flow and electrostatic low-beta dynamics.

The reduced candidate requires a toroidal magnetic well with a trapped-electron region of nonzero measure. The exact well geometry is a later convention gate.

---

# 3. Dynamic state variables

## 3.1 Ion state

For each retained perpendicular Fourier component, the ion nonadiabatic gyrocentre distribution is

\[
\boxed{g_{i,\mathbf k}=g_{i,\mathbf k}(l,E_i,\mu_i,\sigma,t),}
\]

where

\[
E_i=\frac{m_i v^2}{2},
\qquad
\mu_i=\frac{m_i v_\perp^2}{2B},
\qquad
\sigma=\operatorname{sgn}v_\parallel.
\]

The ion gyroaverage is retained through

\[
J_{0i}=J_0\!\left(\frac{k_\perp v_\perp}{\Omega_i}\right).
\]

The linear single-`k` reduced ion equation is the source gyrokinetic equation with the nonlinear convolution omitted:

\[
\boxed{
\frac{\partial g_i}{\partial t}
+v_\parallel\frac{\partial g_i}{\partial l}
+i\omega_{di}g_i
=
\frac{eF_{i0}}{T_i}
\left(\frac{\partial}{\partial t}+i\omega_{*i}^T\right)
J_{0i}\phi.
}
\tag{F2-i}
\]

Here

\[
\omega_{*i}^T
=\omega_{*i}
\left[
1+\eta_i\left(\frac{E_i}{T_i}-\frac32\right)
\right],
\]

\[
\omega_{*i}
=\frac{k_\alpha T_i}{e}\frac{d\ln n_i}{d\psi},
\qquad
\eta_i=\frac{d\ln T_i}{d\ln n_i},
\]

and `omega_di` is the physical ion magnetic-drift frequency.

## 3.2 Bounce-averaged trapped-electron state

Order the dynamics such that

\[
\boxed{\tau_D\gg L/v_{Te}.}
\]

To leading order, the nonadiabatic electron distribution is constant along a bounce orbit. For `k_alpha != 0` in toroidal ballooning space, the incoming boundary conditions force the passing-electron nonadiabatic response to vanish at this order. Thus the reduced dynamic electron state is

\[
\boxed{
g_{e,\mathbf k}^{\rm tr}
=g_{e,\mathbf k}^{\rm tr}(E_e,\lambda,w,t),}
\]

where

\[
\lambda=\frac{v_\perp^2}{v^2B}
\]

is the pitch-angle coordinate and `w` labels a trapping well when more than one inequivalent well exists.

For trapped particles, the bounce points satisfy

\[
\lambda B(l_{1,2})=1,
\]

and the bounce average is

\[
\boxed{
\overline{f}
=
\frac{\displaystyle\int_{l_1}^{l_2} f\,dl/|v_\parallel|}
{\displaystyle\int_{l_1}^{l_2} dl/|v_\parallel|}.
}
\]

With `k_perp rho_e << 1`, so `J_0e -> 1`, the linear bounce-averaged electron equation is

\[
\boxed{
\frac{\partial g_e^{\rm tr}}{\partial t}
+i\overline{\omega}_{de}g_e^{\rm tr}
=
-\frac{eF_{e0}}{T_e}
\left(\frac{\partial}{\partial t}+i\omega_{*e}^T\right)
\overline{\phi}.
}
\tag{F2-e}
\]

The electron charge is `e_e=-e`; the displayed sign follows the Costello–Plunk convention.

For the passing region,

\[
\boxed{g_e^{\rm pass}=0}
\]

at this order. Passing electrons therefore remain Boltzmann/adiabatic in the reduced model.

---

# 4. Electrostatic closure and reconstructed field

The electrostatic potential is not an independent dynamical coordinate. It is reconstructed at each time from quasineutrality.

For the two-species electrostatic system,

\[
\boxed{
\sum_{a=i,e}\frac{e_a^2n}{T_a}\phi_{\mathbf k}(l)
=
\sum_{a=i,e}e_a
\int g_{a,\mathbf k}J_{0a}\,d^3v.
}
\tag{QN-g}
\]

For the reduced candidate,

\[
J_{0e}=1,
\]

`g_e` is nonzero only on the trapped domain, while the local trapped integration region depends on `B(l)`.

Equivalently, define the gyrocentre distribution perturbation

\[
\boxed{
\delta F_a
=g_a-\frac{e_aJ_{0a}\phi}{T_a}F_{a0}.
}
\tag{dF}
\]

Then quasineutrality may be written

\[
\boxed{
\sum_a\frac{n e_a^2}{T_a}
\left[1-\Gamma_{0a}(b_a)\right]\phi
=
\sum_a e_a\int \delta F_aJ_{0a}\,d^3v,
}
\tag{QN-dF}
\]

where

\[
\Gamma_{0a}(b_a)=I_0(b_a)e^{-b_a}.
\]

In the reduced electron ordering `b_e -> 0`, so `Gamma_0e -> 1`; electron polarization is negligible while ion polarization is retained exactly at the chosen local-GK FLR level.

The continuous state for later operator language is therefore

\[
\boxed{x=(g_i,g_e^{\rm tr}),}
\]

with `phi=P_QN x` a reconstructed linear field determined by quasineutrality and then bounce-averaged where required in the electron equation.

---

# 5. Positive Helmholtz free energy

Use the standard gyrokinetic Helmholtz free energy, restricted to the reduced state subspace.

For one Fourier component, Costello & Plunk write

\[
H_{\mathbf k}
=
\sum_a
\left\langle
T_a\int\frac{|g_{a,\mathbf k}|^2}{F_{a0}}\,d^3v
-
\frac{e_a^2n}{T_a}|\phi_{\mathbf k}|^2
\right\rangle.
\tag{H-g}
\]

For the project convention define

\[
\boxed{W_{\mathbf k}=\frac12H_{\mathbf k}.}
\]

For positivity, use the equivalent standard gyrokinetic form in `delta F` variables:

\[
\boxed{
2W_{\mathbf k}
=
\sum_a\left\langle
T_a\int\frac{|\delta F_{a,\mathbf k}|^2}{F_{a0}}\,d^3v
+
\frac{ne_a^2}{T_a}
\left[1-\Gamma_{0a}(b_a)\right]
|\phi_{\mathbf k}|^2
\right\rangle.
}
\tag{W+}
\]

For the reduced candidate `Gamma_0e -> 1`, so the explicit polarization field term is ion dominated, but the electron entropy term remains present, including the adiabatic passing response contained in `delta F_e`.

Every term in (W+) is nonnegative. On the admitted nonzonal finite-ion-FLR sector, with Maxwellian `F_a0>0`, the functional vanishes only for the zero physical perturbation after quasineutrality. Hence

\[
\boxed{W[x]>0\quad\text{for every nonzero admissible perturbation}.}
\]

After elimination of `phi`, `W` is a positive quadratic functional of `(g_i,g_e^tr)` and therefore defines a positive self-adjoint continuous metric/Riesz operator

\[
\boxed{\mathcal M_{F2}\succ0}
\]

on the admissible kinetic Hilbert space.

F2.1 does **not** discretize `mathcal M_F2` and does not yet freeze the kinetic input map `B` or `R_in`.

---

# 6. Physical particle and heat transport channels

The transport channels are defined independently from physical radial gyrocentre fluxes, not reconstructed backwards from the free-energy identity.

For electrostatic fluctuations, the perturbed radial gyrocentre velocity is

\[
\boxed{
V_{\psi,a,\mathbf k}
\equiv
\delta\dot{\mathbf R}_{a,\mathbf k}\cdot\nabla\psi,
\qquad
\delta\dot{\mathbf R}_{a,\mathbf k}
=
\frac{iJ_{0a}\phi_{\mathbf k}\,\mathbf b\times\mathbf k}{B}.
}
\]

Positive `V_psi` is outward because `psi` is chosen to increase outward.

The species particle flux is

\[
\boxed{
\Gamma_a
=
\operatorname{Re}
\left\langle
\int
\delta F_a
V_{\psi,a}^*\,d^3v
\right\rangle.
}
\tag{Gamma}
\]

The species heat flux is

\[
\boxed{
q_a
=
\operatorname{Re}
\left\langle
\int
\delta F_a
\left(E_a-\frac52T_a\right)
V_{\psi,a}^*\,d^3v
\right\rangle.
}
\tag{q}
\]

This is the source-standard gyrokinetic heat-flux convention; the subtraction of `5T_a/2` separates heat transport from the pressure/particle-work contribution in the Helmholtz free-energy drive.

For the reduced electron model, define

\[
\Gamma_e^{\rm tr},\qquad q_e^{\rm tr}
\]

by the same expressions restricted to the trapped nonadiabatic electron region. The adiabatic passing response contributes no radial cross-phase flux at this order, so these are also the total nonadiabatic electron transport contributions of the reduced model.

---

# 7. Quasineutrality constraint on particle transport

The species particle fluxes are physical channels but are not all independent.

Multiplying (QN-dF) by the common electrostatic radial phase factor and taking the real part gives, for each local electrostatic Fourier block,

\[
\boxed{
\sum_a e_a\Gamma_a=0.
}
\tag{amb}
\]

because the polarization term is a real scalar multiple of `|phi|^2` and therefore contributes no radial cross phase.

For singly charged hydrogen,

\[
\boxed{
\Gamma_i=\Gamma_e^{\rm tr}\equiv\Gamma.
}
\]

Thus F2.1 does **not** count ion and electron particle fluxes as two independent source channels.

No analogous quasineutrality identity forces

\[
q_i=q_e^{\rm tr}.
\]

The ion and trapped-electron heat channels remain physically distinct.

---

# 8. Exact collisionless reduced free-energy balance

The general local-GK Helmholtz drive for species `a` is

\[
\boxed{
D_a
=-\left[
T_a\Gamma_a\frac{d\ln p_a}{d\psi}
+
q_a\frac{d\ln T_a}{d\psi}
\right].
}
\tag{Da}
\]

Choose outward-decreasing equilibrium profiles to have positive gradient coefficients

\[
G_{p,a}\equiv-\frac{d\ln p_a}{d\psi},
\qquad
G_{T,a}\equiv-\frac{d\ln T_a}{d\psi}.
\]

Then

\[
D_a=T_aG_{p,a}\Gamma_a+G_{T,a}q_a.
\]

Costello & Plunk's two-species bounce-averaged system has the exact collisionless Helmholtz balance

\[
\boxed{
\frac{dW}{dt}
=D_i+D_e^{\rm tr}.
}
\tag{BAL-red-1}
\]

Equivalently,

\[
\boxed{
\frac{dW}{dt}
=
T_iG_{p,i}\Gamma_i
+G_{T,i}q_i
+T_eG_{p,e}\Gamma_e^{\rm tr}
+G_{T,e}q_e^{\rm tr}.
}
\tag{BAL-red-2}
\]

Using the electrostatic ambipolar constraint gives the minimal independent source decomposition

\[
\boxed{
\frac{dW}{dt}
=
G_\Gamma\Gamma
+G_{T,i}q_i
+G_{T,e}q_e^{\rm tr},
}
\tag{BAL-red-3}
\]

where

\[
\boxed{
G_\Gamma
=T_iG_{p,i}+T_eG_{p,e}.
}
\]

Thus the reduced F2.1 balance contains, before any parameter choice, three physically defined quadratic source forms:

1. the ambipolar particle-transport work channel `Gamma`;
2. the ion heat-flux channel `q_i`;
3. the trapped-electron heat-flux channel `q_e^tr`.

The gradient coefficients are not frozen numerically in F2.1. A later parameter gate may set some coefficients to zero only for an independent physical reason.

---

# 9. Conservative terms and what does not enter the source balance

The following terms alter the kinetic dynamics but do not create independent Helmholtz-free-energy supply or positive dissipation in the collisionless reduced model:

- ion parallel streaming `v_parallel partial_l`;
- ion magnetic drift `i omega_di`;
- trapped-electron bounce-averaged magnetic drift `i overline{omega_de}`;
- consistent ion FLR gyroaveraging through `J_0i`, `Gamma_0i` and quasineutrality;
- the nonlinear `E x B` convolution in the full multi-`k` system, which redistributes free energy between wavenumbers but cancels in the total Helmholtz balance.

For the linear single-`k` CORE lineage the nonlinear convolution is absent by construction.

Collisionless phase mixing, where retained, moves free energy to fine velocity-space structure; it is not classified as irreversible dissipation in the fully resolved balance.

---

# 10. Collision treatment

## 10.1 Primary reduced candidate: collisionless

The primary F2.1 reduced candidate is deliberately frozen as

\[
\boxed{C_{ab}=0.}
\]

This is a **source-fidelity choice**, not a device to increase or decrease later objective separation.

The Costello–Plunk bounce-averaged trapped-electron reduction is derived in the collisionless trapped-particle ordering. Adding a finite collision operator at this stage would require extra physics not specified by that reduced source, including trapped-passing scattering/detrapping and a collision operator compatible with the bounce-averaged state space. Such an addition would therefore constitute a separate closure choice rather than a harmless parameter.

The balance-changing mechanism that remains in the collisionless reduced model is the independent nonadiabatic trapped-electron free-energy drive `D_e^tr`.

## 10.2 Higher-fidelity reference: physical H-theorem collisions

The fully kinetic two-species reference must include an H-theorem-compatible gyroaveraged linearized collision operator of the Abel–Barnes–Cowley–Dorland–Schekochihin class or an equivalent operator with the same required properties:

- particle conservation;
- total momentum conservation;
- total energy conservation;
- vanishing on the Maxwellian equilibrium;
- Boltzmann H theorem;
- physically signed dissipation of velocity-space fine structure.

For the standard gyrokinetic collision functional

\[
C
=
\operatorname{Re}
\sum_{a,b}T_a
\left\langle
\int
\frac{g_a^*}{F_{a0}}
\left[
C_{ab}(g_a,F_{b0})+C_{ab}(F_{a0},g_b)
\right]d^3v
\right\rangle,
\]

Boltzmann's H theorem gives

\[
C\le0.
\]

Define

\[
\boxed{D_{\rm coll}\equiv-C\ge0.}
\]

The fully kinetic reference balance is then

\[
\boxed{
\frac{dW}{dt}
=D_i+D_e-D_{\rm coll}.
}
\tag{BAL-ref}
\]

Individual interspecies collision terms may exchange energy and momentum between species, but their total collision functional enters the Helmholtz balance with the nonpositive H-theorem sign. No artificial numerical damping is part of this specification.

The collision frequency, mass-ratio convention and exact implementation parameters remain unresolved pre-effect objects.

---

# 11. FLR role

Finite ion FLR is retained because it is intrinsic ion-scale gyrokinetic physics, not because it is expected to create objective separation.

Its required appearances are:

1. the ion gyroaverage
   \[
   J_{0i}(k_\perp v_\perp/\Omega_i)
   \]
   in the ion field coupling;
2. the ion polarization factor
   \[
   \Gamma_{0i}(b_i)=I_0(b_i)e^{-b_i}
   \]
   in the positive free-energy/quasineutrality geometry;
3. the same gyroaverage in the physical radial gyrocentre velocity entering `Gamma_i` and `q_i`.

Therefore FLR changes

- the generator/operator;
- the positive metric geometry;
- quasineutrality;
- the physical flux kernels and quantitative transport values.

However, in the source-consistent collisionless balance it does **not** constitute an additional thermodynamic gradient source or a positive sink by itself.

Hence

\[
\boxed{\text{FLR alone is not classified as the F2 redundancy-breaking mechanism.}}
\]

---

# 12. Continuous operator form for later CORE use

After quasineutrality elimination, the reduced linear system can be written abstractly as

\[
\dot x=\mathcal A_{F2}x,
\qquad
x=(g_i,g_e^{\rm tr}).
\]

The free energy is

\[
W=\frac12\langle x,\mathcal M_{F2}x\rangle,
\qquad
\mathcal M_{F2}\succ0.
\]

Let the physical quadratic forms corresponding to the three independent reduced source channels be

\[
\mathcal Q_\Gamma,
\qquad
\mathcal Q_{q_i},
\qquad
\mathcal Q_{q_e}.
\]

Then the continuous balance implies the conceptual operator identity

\[
\boxed{
\mathcal A_{F2}^\dagger\mathcal M_{F2}
+\mathcal M_{F2}\mathcal A_{F2}
=2\left(
G_\Gamma\mathcal Q_\Gamma
+G_{T,i}\mathcal Q_{q_i}
+G_{T,e}\mathcal Q_{q_e}
\right)
}
\tag{OP-red}
\]

for the collisionless reduced candidate.

For the collisional fully kinetic reference,

\[
\boxed{
\mathcal A_{GK}^\dagger\mathcal M_{GK}
+\mathcal M_{GK}\mathcal A_{GK}
=2\left(
\sum_a T_aG_{p,a}\mathcal Q_{\Gamma_a}
+
\sum_a G_{T,a}\mathcal Q_{q_a}
-
\mathcal D_{\rm coll}
\right),
\qquad
\mathcal D_{\rm coll}\succeq0.
}
\tag{OP-ref}
\]

These identities are **verification targets**, not definitions of the individual channel operators. Each channel is defined first from the physical radial flux expressions in Sec. 6.

---

# 13. Structural nonredundancy test

The R1 no-go followed from a one-channel, zero-dissipation identity of the form

\[
\dot W=g_q q_i,
\]

which integrated to an affine relation between cumulative `q_i` and final free energy.

The F2.1 reduced balance instead gives

\[
W(T)-W(0)
=
G_\Gamma\int_0^T\Gamma\,dt
+G_{T,i}\int_0^Tq_i\,dt
+G_{T,e}\int_0^Tq_e^{\rm tr}\,dt.
\]

Solving for the cumulative ion heat channel gives

\[
G_{T,i}\int_0^Tq_i\,dt
=
W(T)-W(0)
-
G_\Gamma\int_0^T\Gamma\,dt
-
G_{T,e}\int_0^Tq_e^{\rm tr}\,dt.
\]

Therefore cumulative ion heat is **not** an affine function of final free energy alone unless later special choices or additional identities make all competing cumulative channels vanish or become dependent.

Neither quasineutrality nor the bounce-averaged electron closure imposes such a relation between `q_i` and `q_e^tr`. Quasineutrality only reduces the two species particle fluxes to one ambipolar particle channel.

Hence

\[
\boxed{
\text{the exact R1 two-operator affine redundancy is no longer structurally forced.}
}
\]

This is only a statement of **possibility in principle**. F2.1 does not establish that

- finite-time free-energy and ion-heat optimizers differ;
- any principal angle is nonzero;
- any performance gap is large;
- any chosen physical parameter point produces a useful effect.

Those questions remain forbidden until later pre-effect freezes are complete.

For the fully kinetic collisional reference the additional positive cumulative `D_coll` term provides a second, independent reason the R1 one-channel affine identity is not forced.

---

# 14. Fidelity hierarchy and limiting relations

Freeze the hierarchy

\[
\boxed{
\text{F2-R: finite-FLR GK ions + bounce-averaged trapped electrons}
}
\]

\[
\Downarrow\ \text{reference validation}
\]

\[
\boxed{
\text{F2-K: fully kinetic two-species local electrostatic GK + physical collisions}
}
\]

with the following controls/limits:

### F2-K -> F2-R

Apply the slow-electron-transit ordering

\[
\tau_D\gg L/v_{Te},
\]

set `k_perp rho_e << 1`, retain only trapped-electron nonadiabatic dynamics, bounce average the trapped-electron equation, set the reduced collision operator to zero, and keep finite ion FLR.

### F2-R -> adiabatic-electron FLR control

Set

\[
g_e^{\rm tr}\to0.
\]

Then the independent electron free-energy drive disappears. This limit is an FLR-containing conservative control; it is not the primary F2 candidate.

### Adiabatic-electron FLR control -> R1 structural control

Further take the previously frozen ZLR/moment-reduction path and the R1 four-moment closure. In the R1 lineage the particle channel collapses and the remaining balance reduces to the single ion-heat source, recovering the frozen affine no-go.

### What disappears in the limits

- removing nonadiabatic electrons removes `D_e^tr`, `q_e^tr` and the nonadiabatic electron part of the particle channel;
- imposing adiabatic electrons can collapse the particle flux in the single-species ITG limit;
- removing collisions sets `D_coll=0`;
- FLR removal changes `A`, `M` and physical flux kernels but is not by itself an independent source/sink removal or creation.

---

# 15. Next unresolved pre-effect objects

F2.1 intentionally leaves the following unresolved and therefore blocks numerical execution:

1. **Magnetic geometry:** exact tokamak/stellarator or analytic flux-tube `B(l)`, `k_perp(l)`, curvature/drift frequencies, magnetic shear and trapping wells.
2. **Physical parameter point:** density/temperature ratios, normalized gradients, safety factor/shear where applicable, `k_alpha`, `k_psi`, mass ratio and species parameters.
3. **Gradient-channel convention:** which ion/electron pressure and temperature gradients are nonzero at the eventual pilot point; no gradient may be selected for expected objective separation.
4. **Reduced-candidate collision convention:** collisionless is frozen for F2-R, but any later collisional bounce-averaged variant would require a separate physically derived trapped/passing collision model and is not implicit in F2.1.
5. **Reference collision parameters:** physical collision frequencies and exact H-theorem-compatible operator implementation for F2-K.
6. **Phase-space discretization:** parallel coordinate, ion velocity grid/basis, trapped-electron `(E,lambda,well)` representation, quadrature, boundary conditions and structure-preserving quasineutrality elimination.
7. **Kinetic admissible initial-condition geometry:** physical `B` operator on the kinetic state and whether all distribution-function directions are admissible.
8. **Input cost `R_in`:** likely tied to the positive free energy but not frozen until the kinetic admissibility gate establishes the correct input space.
9. **Discrete physical channel matrices:** `Q_Gamma`, `Q_qi`, `Q_qe` must be reconstructed from the physical integrals after discretization and checked against the continuous balance.
10. **Numerical/spectral qualification:** positivity, discrete balance, collision sign, quasineutrality consistency, conditioning, convergence and complete spectrum.
11. **Fully kinetic reference mapping:** exact GENE-compatible normalization and diagnostic mapping, including the collision implementation and species heat/particle flux conventions.

No one of these objects is solved by F2.1 unless already required above for continuous balance consistency.

---

# 16. PASS / HOLD / FAIL assessment

The F2.1 PASS conditions are satisfied:

- one primary reduced two-species local-GK architecture is selected on source/balance grounds;
- its dynamic ion and trapped-electron phase-space variables are explicit;
- electrostatic quasineutrality reconstructs the field;
- the exact positive Helmholtz free-energy functional is specified in continuous form;
- physical particle and heat channels are defined independently from radial gyrocentre fluxes;
- the exact source decomposition is explicit;
- quasineutrality's ambipolar particle-flux constraint is identified rather than ignored;
- the reduced collision treatment is explicitly and physically justified as collisionless;
- an H-theorem-compatible collisional fully kinetic reference is specified;
- FLR is retained consistently without being promoted as an artificial source/sink;
- the reduced model contains independent ion-heat and trapped-electron-heat source channels, so the R1 affine redundancy is no longer forced in principle;
- all numerical and finite-time effect work remains unopened.

Therefore

\[
\boxed{
\text{F2.1 PASS — TWO-SPECIES GK CANDIDATE/BALANCE SPECIFIED — RETURN TO MASTER}
}
\]

---

# 17. Allowed interpretations

F2.1 supports the statements that:

- finite-FLR ions plus bounce-averaged trapped electrons form a source-faithful reduced two-species local-GK candidate;
- the reduced collisionless Helmholtz balance contains more than the single R1 ion-heat source;
- electrostatic quasineutrality constrains the species particle fluxes through charge-weighted ambipolarity but does not identify ion and electron heat fluxes;
- nonadiabatic trapped electrons provide a physically established independent electron free-energy drive;
- a fully kinetic collisional two-species reference has an H-theorem-positive free-energy sink;
- finite ion FLR modifies conservative dynamics, metric geometry, quasineutrality and transport kernels but is not assumed to be a redundancy-breaking source by itself;
- objective nonredundancy is structurally possible, not guaranteed.

# 18. Forbidden interpretations

F2.1 does **not** establish that:

- an energy-optimal and heat-optimal initial perturbation differ;
- any optimizer angle or performance gap is nonzero;
- the reduced candidate is spectrally stable at any particular parameter point;
- a particular trapped fraction, collision rate, gradient or wavenumber is preferable;
- collisions should be added to the reduced candidate merely to force nonredundancy;
- FLR itself breaks the R1 affine identity;
- the bounce-averaged model replaces the need for fully kinetic validation;
- any GENE result has been computed.

---

# 19. Source anchors

1. P. J. Costello and G. G. Plunk, **Energetic bounds on gyrokinetic instabilities. Part 4. Bounce-averaged electrons**, *Journal of Plasma Physics* **91**, E12 (2025), DOI `10.1017/S0022377824000965`. Primary source for the finite-FLR-ion + bounce-averaged trapped-electron architecture, electron-transit ordering, quasineutrality and two-species Helmholtz balance.
2. P. Helander and G. G. Plunk, **Energetic bounds on gyrokinetic instabilities. Part 1. Fundamentals**, *Journal of Plasma Physics* **88**, 905880207 (2022), DOI `10.1017/S0022377822000277`. Primary source for the multispecies positive Helmholtz functional, physical particle/heat flux definitions, source decomposition and collision sign.
3. I. G. Abel, M. Barnes, S. C. Cowley, W. Dorland and A. A. Schekochihin, **Linearized model Fokker–Planck collision operators for gyrokinetic simulations. I. Theory**, *Physics of Plasmas* **15**, 122509 (2008), DOI `10.1063/1.3046067`. Source for the H-theorem-compatible collisional reference requirements.
4. A. Bañón Navarro et al., **Free energy balance in gyrokinetic turbulence**, *Physics of Plasmas* **18**, 092303 (2011), DOI `10.1063/1.3632077`. GENE-facing free-energy-balance anchor for later higher-fidelity validation.
5. `research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md` and `research/master/fusion_r1_structural_redundancy_literature_integration_freeze_0_1.md` remain the canonical project positioning authority.

---

**STOP / RETURN TO MASTER.**
