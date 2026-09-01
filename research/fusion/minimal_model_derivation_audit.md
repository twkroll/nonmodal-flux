# Fusion B3 — Minimal-model derivation audit

**Status:** completed audit; no model convention frozen yet  
**Date:** 2026-09-01  
**Purpose:** identify the smallest physically defensible fusion-facing gyrofluid model from which `nonmodal-flux` can later derive a positive perturbation metric and genuine signed particle/heat-flux forms.

## Executive conclusion

The preferred **minimal derivation target** is the electrostatic four-moment gyrofluid model of Strintzi, Scott & Brizard (Phys. Plasmas 12, 052517, 2005; arXiv:physics/0410276), with state moments

\[
(n,\,u_\parallel,\,p_\parallel,\,p_\perp)
\]

for each retained species and electrostatic potential \(\phi\) determined by the polarization constraint.

It is the best compromise found between analytical size and physical structure:

- it is explicitly electrostatic and low-\(\beta\);
- it contains distinct parallel and perpendicular temperatures;
- its Lagrangian construction yields an exact nonlinear energy conservation law;
- it is materially smaller than the six-moment GEM model;
- it remains close enough to the Scott/GEM energetic programme to provide a credible bridge toward ITG/GENE physics.

However, **this audit does not yet justify writing a unique matrix \(A_k\), \(M_k\), \(Q_{\Gamma,k}\), or \(Q_{q,k}\)**. Several physically consequential conventions remain to be fixed first. Freezing any one of them silently would violate project decisions D2 and D5.

---

## 1. Candidate hierarchy after the derivation audit

### 1.1 Single-temperature Strintzi–Scott predecessor

The four-moment paper states that its preceding electrostatic model evolved density, momentum and a single/perpendicular temperature together with a polarization equation, and that it satisfied an exact energy theorem. This is apparently the smallest member of the relevant energy-conserving family.

**Use:** algebraic sanity check only.

**Reason not to make it the fusion-facing model:** the four-moment extension was introduced specifically because the single-temperature model lacks parallel-temperature effects needed for quantitatively accurate turbulence in magnetized plasmas. A model selected to study heat-transport optimality should not deliberately remove the temperature structure that motivated the improved model.

### 1.2 Four-moment Strintzi–Scott–Brizard model — preferred minimal target

The model uses the four gyrofluid moments

\[
n,\qquad u_\parallel,\qquad p_\parallel,\qquad p_\perp,
\]

with

\[
T_\parallel=p_\parallel/n,\qquad T_\perp=p_\perp/n,
\]

and \(\phi\) supplied by a polarization equation. The gyroaveraged electrostatic potential depends on \(T_\perp\), so finite-Larmor-radius structure is already coupled to the thermodynamic variables.

The source Lagrangian contains kinetic \(u_\parallel\) and \(E\times B\) energy, parallel/perpendicular thermal energy, electrostatic coupling and electric-field energy. Noether's theorem then provides an exact conserved total energy for the nonlinear model.

**Use:** first fusion-facing reduced derivation.

**Why it is attractive for `nonmodal-flux`:** it is the first candidate in the hierarchy that is simultaneously small, temperature-resolved, electrostatic, and constrained by an exact energy theorem.

### 1.3 Six-moment Scott/GEM model — mandatory follow-up validation

The Scott/GEM construction extends the moment hierarchy to include temperature and conductive heat-flux dynamics, with the usual six moments

\[
\tilde n,\quad \tilde u_\parallel,\quad
\tilde T_\parallel,\quad \tilde T_\perp,\quad
\tilde q_\parallel,\quad \tilde q_\perp.
\]

Its fluctuation free-energy structure is a design constraint, not an after-the-fact norm choice. Scott's later systematic derivation starts from the gyrokinetic delta-f free-energy functional and derives the gyrofluid free energy using Hermite moments.

**Use:** physics validation after the four-moment prototype.

**Reason not to start here:** the extra heat-flux moments and closure/geometry terms increase the state dimension and derivational burden before the core finite-horizon transport theory has been stress-tested.

### 1.4 Local gyrokinetics / GENE — later validation layer

A local electrostatic gyrokinetic initial-value problem remains the preferred end point for a fusion-facing validation. In this setting the physical particle and heat fluxes are velocity-space moments correlated with the radial generalized \(E\times B\) drift, and therefore naturally produce bilinear/cross-phase observables after linearization and discretization.

**Use:** validate that the distinction between free-energy optimal and finite-horizon heat-flux optimal survives beyond moment closures.

---

## 2. What the four-moment source gives us directly

For one species, the source Lagrangian density can be written schematically as

\[
\mathcal L_f
=
\frac12 nm\left(u_\parallel^2+|\mathbf u_E|^2\right)
-\left(p_\perp+\frac12p_\parallel\right)
+en\left(\mathbf A\cdot\frac{\mathbf u}{c}-\|\phi\|\right),
\]

with

\[
\mathbf u_E=\frac{c}{B}\,\hat{\mathbf b}\times\nabla\phi.
\]

The gyroaveraged potential \(\|\phi\|\) is a nonlocal operator depending on the perpendicular Larmor radius, hence on \(T_\perp\). The model's variational fields are the density, flow, parallel/perpendicular pressures and electrostatic potential.

The source's exact conserved energy contains, schematically,

\[
\mathcal E
=
\int d^3x\left[
\frac12 nm\left(u_\parallel^2+|\mathbf u_E|^2\right)
+p_\perp+\frac12p_\parallel
+\frac{|\mathbf E|^2}{8\pi}
\right],
\]

with the polarization/electrostatic structure supplying the required exchange terms.

### Critical distinction for this project

The nonlinear conserved total energy above is **not automatically the positive quadratic perturbation free energy** needed for

\[
E_M(\delta x)=\delta x^\dagger M\,\delta x.
\]

For `nonmodal-flux`, \(M\) must be obtained from the second variation / delta-f fluctuation-energy balance about the chosen equilibrium and after elimination of constrained field variables. Positivity must be proved on the actual admissible perturbation space. We must not simply read the nonlinear energy density and declare its coefficients to be \(M\).

---

## 3. Candidate state vector after Fourier decomposition

Once an equilibrium and geometry are fixed, a natural primitive perturbation vector is of the form

\[
\delta z_k=
\begin{pmatrix}
\delta n_k\\
\delta u_{\parallel,k}\\
\delta T_{\parallel,k}\\
\delta T_{\perp,k}
\end{pmatrix},
\]

with \(\phi_k\) determined by the linearized polarization relation. Alternatively, one may keep \(\phi_k\) as a state component and impose the polarization equation through a constrained/descriptor formulation.

These two choices are physically equivalent only after the constraint and metric are transformed consistently. The project should later verify invariance under this elimination explicitly.

No explicit \(A_k\) is recorded at B3 because its entries depend on the geometry, equilibrium gradients, FLR approximation, species closure and normalization chosen in B4.

---

## 4. Physical signed transport forms

### 4.1 Particle flux

For electrostatic fluctuations the radial particle flux has the generic physical structure

\[
\Gamma_s=\langle \delta n_s\,\delta v_{E,r}\rangle.
\]

For a perpendicular Fourier mode, \(\delta v_{E,r}\) is proportional to \(i k_y\phi_k\) up to the geometry/sign/normalization factor. Therefore one expects

\[
\Gamma_{s,k}
= C_{\Gamma,s}(k)\,\operatorname{Im}
\left(\delta n_{s,k}^*\phi_k\right)
= z_k^\dagger Q_{\Gamma_s,k}z_k.
\]

This is only the **structural form**. The coefficient and sign must be derived from the chosen coordinates and radial orientation in B4/B5.

### 4.2 Heat / thermal-energy flux

A fluid radial thermal-energy flux generated by \(E\times B\) advection must likewise correlate the radial drift with the appropriate pressure/temperature combination. Thus the Fourier observable will have a cross-phase form schematically like

\[
q_{s,k}
= C_{q,s}(k)\,
\operatorname{Im}\left(P_{s,k}^*\phi_k\right),
\]

where \(P_{s,k}\) is the **physically required combination** of \(\delta p_{\parallel,k}\), \(\delta p_{\perp,k}\), and possibly density/equilibrium-temperature terms, depending on the adopted definition of heat flux versus total energy flux.

The exact \(P_{s,k}\) is deliberately left unresolved here. Choosing it ad hoc would violate D5.

### 4.3 Important limitation of the four-moment model

The four-moment model contains parallel/perpendicular pressure dynamics, but its conductive heat-fluxes are not independent dynamical state moments in the same sense as in six-moment GEM. Heat-flux terms enter pressure equations/closures. Therefore:

- the four-moment model is adequate for a first **radial thermal-energy/pressure-transport** observable based on \(E\times B\) advection;
- a quantitatively stronger treatment of conductive heat-flux dynamics should be checked in the six-moment model;
- we must distinguish radial turbulent heat transport from the model's parallel closure heat-flux variables.

---

## 5. Balance structure to be derived, not assumed

The target linearized identity remains

\[
A_k^\dagger M_k+M_kA_k
=
\sum_\alpha g_\alpha Q_{\alpha,k}-R_k,
\qquad R_k\succeq0.
\]

For an ITG-facing reduction, the channel list should at minimum distinguish the background-gradient work associated with density/particle transport and temperature/thermal transport whenever both survive the chosen closure.

The audit does **not** yet establish that a chosen four-moment truncation will yield exactly this simple finite-dimensional form with a positive semidefinite \(R_k\). That must be demonstrated after the equilibrium and dissipative closure are fixed.

A failure to obtain this identity cleanly is a valid falsification outcome and would promote six-moment GEM or a direct gyrokinetic discretization instead of patching the reduced model.

---

## 6. Conventions that must be fixed before matrices are allowed

The following choices materially change \(A_k\), \(M_k\), and the flux forms. They are therefore part of the physics, not implementation details.

1. **Geometry:** slab/local Cartesian versus simple toroidal/flux-tube geometry.
2. **Species model:** one kinetic/gyrofluid ion species with adiabatic electrons versus dynamic electrons.
3. **Equilibrium drive:** which density and temperature gradients are retained and how they are normalized.
4. **FLR level:** zero-Larmor-radius limit versus a specific gyroaveraging approximation \(\Gamma_0,\Gamma_1,\Gamma_2\) / \(\mathcal P\).
5. **Parallel dynamics:** whether \(k_\parallel\) is retained, simplified, or set to zero.
6. **Curvature drive:** slab drift-wave limit versus toroidal ITG curvature terms.
7. **Dissipation/closure:** collision, Landau-fluid closure, viscosity/diffusion, or initially conservative benchmark.
8. **Heat-flux definition:** radial internal-energy flux, enthalpy/heat flux, or a definition deliberately matched to the later gyrokinetic/GENE diagnostic.
9. **State representation:** eliminate \(\phi\) using polarization or retain it in a constrained descriptor state.
10. **Normalization and radial sign convention.**

Until these are specified, an explicit matrix would be underdetermined.

---

## 7. Minimality versus fusion relevance

The audit produces a useful two-level strategy rather than a single final model.

### Level M0 — algebraic energy benchmark

Use the single-temperature predecessor only if needed to verify elimination, free-energy Hessians and transport-form construction in the smallest possible setting.

### Level M1 — preferred fusion-facing minimal model

Use the electrostatic four-moment anisotropic-temperature model as the **minimal derivation target**.

This is the smallest candidate found that gives us enough thermodynamic structure to ask, without inventing an observable,

\[
u_W(T)\ ?=\ u_{\Gamma}(T)\ ?=\ u_q(T).
\]

### Level M2 — mandatory robustness check

Move to six-moment GEM if M1 succeeds. The extra heat-flux moments test whether the transport-optimal result survives a more faithful moment hierarchy.

### Level M3 — GENE-facing validation

Finally test a local electrostatic gyrokinetic initial-value operator with a heat-flux form built directly from the gyrokinetic diagnostic.

---

## 8. Connection to Jenko / fusion work

This hierarchy has a historically and physically credible bridge to Jenko's programme rather than a cosmetic citation link. Jenko, Dorland, Scott and Strintzi explicitly studied temperature-gradient-driven ITG/ETG turbulence and transport together, while Scott's energy-conserving gyrofluid models were designed to reproduce key gyrokinetic behaviour and, with adiabatic electrons in a globally consistent flux-tube formulation, connect to Cyclone Base Case results.

This makes the proposed sequence scientifically coherent:

\[
\text{energy-conserving gyrofluid moments}
\longrightarrow
\text{finite-horizon signed heat-flux optimality}
\longrightarrow
\text{GENE-compatible gyrokinetic validation}.
\]

The proposed novelty remains the middle object, not the underlying gyrofluid or gyrokinetic model.

---

## 9. B3 decision

**Preferred minimal derivation target:** Strintzi–Scott–Brizard electrostatic four-moment anisotropic-temperature gyrofluid model.

**Do not freeze it in code yet.**

**Single-temperature predecessor:** retain only as an optional algebraic sanity check.

**Six-moment Scott/GEM:** retain as mandatory follow-up if the four-moment finite-horizon result is positive.

**Direct local gyrokinetics/GENE:** later validation layer, not the next derivation.

No user decision is required at B3 because the model family ranking is sufficiently clear.

---

## 10. Next package: B4 convention-freeze proposal

The next task is to derive a small set of **concrete, internally consistent reduction options** from the preferred four-moment family. B4 should compare, at minimum:

- a zero-Larmor-radius/slab or minimal-curvature analytic reduction;
- a finite-Larmor-radius local electrostatic ITG reduction with adiabatic electrons;
- optionally a slightly richer parallel-dynamic reduction if the first two erase an essential transport channel.

For each option B4 should spell out the candidate state, equilibrium gradients, polarization relation, physical free-energy Hessian, particle/thermal-flux definitions and expected matrix dimension.

Only after this comparison should one convention be frozen and used to derive \(A_k\), \(M_k\), \(Q_{\Gamma,k}\), and \(Q_{q,k}\).

If one B4 option dominates on physical and mathematical grounds, it may be selected without user intervention. If the remaining alternatives trade analytic simplicity against fusion fidelity in a scientifically consequential way, the user must explicitly choose before a convention is frozen.

---

## Primary literature anchors

- D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas 12, 052517 (2005), arXiv:physics/0410276.
- B. D. Scott, *Free-energy conservation in local gyrofluid models* / *GEM — An Energy Conserving Electromagnetic Gyrofluid Model*, Phys. Plasmas 12, 102307 (2005), arXiv:physics/0501124.
- B. D. Scott, *Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities*, Phys. Plasmas 17, 102306 (2010), arXiv:0710.4899.
- F. Jenko, W. Dorland, B. Scott, D. Strintzi, *Simulation and theory of temperature gradient driven turbulence* (Theory of Fusion Plasmas, 2002).

## Audit caveat

This note identifies the **best source model and the unresolved derivational choices**. It intentionally does not claim an explicit reduced matrix or perturbation free-energy metric before the necessary equilibrium, geometry, closure and diagnostic conventions have been fixed.