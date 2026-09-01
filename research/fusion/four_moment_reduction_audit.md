# B4 — Four-moment gyrofluid reduction audit

**Status:** completed model-reduction audit; no convention frozen yet  
**Date:** 2026-09-01  
**Parent notes:** `research/fusion/model_audit.md`, `research/fusion/minimal_model_derivation_audit.md`

## Purpose

The goal is to identify a reduction of the Strintzi–Scott–Brizard electrostatic four-moment gyrofluid model that is small enough for exact finite-horizon `nonmodal-flux` analysis while preserving the energetic structure needed for a fusion-facing result.

The parent model evolves, for each species, the moments

\[
(n,u_\parallel,p_\parallel,p_\perp),
\]

with the electrostatic potential \(\phi\) fixed by a polarization equation. Its Lagrangian construction yields an exact nonlinear energy conservation law. The gyro-averaged electrostatic potential tends to \(\phi\) in the zero-Larmor-radius (ZLR) limit. The paper also states that the introduction of \(T_\parallel\) does not alter the polarization equation and that the two-temperature model reduces toward the previous one-temperature construction when pressure-anisotropy contributions are removed.

For `nonmodal-flux`, none of these statements is yet sufficient to define the positive perturbation metric \(M\). We still need the quadratic free energy of perturbations about a specified equilibrium, not merely the total nonlinear energy.

---

## Non-negotiable modelling rules

Every candidate below must satisfy the following before implementation.

1. The state operator \(A_k\) is derived from a fixed linearization, not reverse-engineered from a desired matrix form.
2. \(M_k\succ0\) is obtained from a perturbation free-energy/second-variation calculation on the admissible state space.
3. Particle and thermal transport forms are derived from physical radial fluxes. Schematically,
   \[
   \Gamma_k=\langle \widetilde n\,\widetilde v_{E,r}\rangle,
   \]
   and a thermal-energy/heat-flux observable has the corresponding pressure/temperature–\(E\times B\) cross-correlation. The precise thermodynamic pressure combination must be fixed from the chosen model balance; it may not be guessed.
4. Finite-Larmor-radius (FLR) operators may only be retained if their adjoint/polarization pairing is kept consistently enough to preserve the energy identity.
5. Setting a field, gradient or parallel derivative to zero is accepted only if the resulting subsystem is closed under the linearized equations and its free-energy balance remains valid.

---

## Candidate R0 — isotropic-temperature / ZLR analytic reduction

### Definition

Take the ZLR limit of the electrostatic model,

\[
\langle\phi\rangle_{\rm gyro}\rightarrow\phi,
\]

and impose the one-temperature/isotropic reduction inherited from the earlier consistent model,

\[
T_\parallel=T_\perp=T.
\]

After eliminating \(\phi\) through the linearized polarization/quasineutrality relation, the natural dynamic variables are of the form

\[
z_k=(\delta n_k,\delta u_{\parallel,k},\delta T_k)^\top,
\]

with further dimensional reduction possible only after checking the chosen geometry and \(k_\parallel\) limit.

### Advantages

- Smallest plausible fusion-facing temperature model in this family.
- Retains a physical temperature perturbation, so a radial thermal transport observable can be defined from the underlying pressure/energy flux.
- ZLR removes nonlocal gyroaveraging operators and makes hand derivation of \(A_k\), short-time series and transport-neutral subspaces much easier.
- The parent literature explicitly reports agreement of the four-moment construction with the earlier model in the appropriate ZLR/isotropy sector.

### Limitations

- Removes the pressure anisotropy that motivated the four-moment extension.
- Removes the main ion-gyroradius physics that distinguishes gyrofluid from ordinary drift-fluid reductions.
- A positive result here would still need an FLR check before carrying a strong fusion claim.
- If \(k_\parallel\) is also suppressed, the parallel-velocity moment may decouple; this must be established from the chosen local geometry rather than assumed.

### Role

**Analytic bridge only.** Useful if an explicit \(3\times3\) model is needed to understand mechanisms, but not the preferred final reduced fusion result.

---

## Candidate R1 — anisotropic four-moment ZLR model

### Definition

Retain the full anisotropic moment set

\[
z_k=(\delta n_k,\delta u_{\parallel,k},\delta p_{\parallel,k},\delta p_{\perp,k})^\top,
\]

eliminate \(\phi_k\) with the linearized electrostatic polarization relation, but take the ZLR limit in the gyro-averaging operators.

This keeps the four thermodynamic/dynamic moments while removing the most technically delicate FLR operator dependence.

### Advantages

- Still only a \(4\times4\) state per local Fourier degree of freedom after field elimination in the simplest setting.
- Retains the parallel/perpendicular pressure distinction and therefore a genuinely nontrivial thermodynamic state geometry.
- The original four-moment paper reports very good agreement with previous gyrofluid models for the ZLR terms, so this sector is the cleanest place to audit the linear operator term by term.
- Gives enough state dimension for three distinct optimizations to be meaningfully different:
  \[
  u_W,\qquad u_\Gamma,\qquad u_q.
  \]
- Keeps parallel dynamics available rather than deleting it before we know whether it controls the transport-generation order.
- Ideal for checking whether the transport-generation index and energy/transport mismatch survive a model with real temperature physics.

### Limitations

- No finite-ion-gyroradius response.
- The exact perturbation heat/thermal-energy flux is not yet fixed. The parent four-moment paper contains diamagnetic heat-flux terms \(q_{\parallel\perp}\) and \(q_{\perp\perp}\), but these are not automatically identical to the radial turbulent heat-flux observable we need. That observable must be derived from the local background-gradient/free-energy balance.
- Toroidal curvature, parallel compression and equilibrium-gradient conventions still have to be chosen before writing \(A_k\).

### Role

**Recommended first derivation target.** It is the best compromise between exact hand analysis and retention of the four-moment thermodynamics.

---

## Candidate R2 — FLR four-moment ITG model with adiabatic electrons

### Definition

Retain the four ion moments and the finite-Larmor-radius gyroaveraging/polarization structure, with electrons treated adiabatically in a local electrostatic ITG setting. After the electron response and polarization relation are imposed, \(\phi\) is a constrained field rather than an independent dynamical degree of freedom.

For a fixed local perpendicular Fourier mode, the state remains based on

\[
z_k=(\delta n_i,\delta u_{\parallel i},\delta p_{\parallel i},\delta p_{\perp i})^\top,
\]

but the coefficients become nontrivial functions of \(k_\perp\rho_i\) through the gyroaveraging/polarization operators.

### Advantages

- Keeps the characteristic gyrofluid FLR physics and is therefore much closer to the intended ITG application.
- Scott's free-energy-conserving local gyrofluid programme explicitly links the polarization equation, density and perpendicular-temperature combinations to fluctuation free-energy conservation.
- In globally consistent flux-tube form, the adiabatic-electron model was reported to be consistent with Cyclone-Base-Case gyrokinetic results, making this a credible bridge toward GENE.
- A single \(k_\perp\rho_i\) parameter gives a controlled way to test whether the finite-horizon transport geometry survives beyond ZLR.

### Limitations

- The gyroaveraging operator depends on perpendicular temperature in the nonlinear parent model. Linearization therefore has to retain all first-order contributions consistently; inserting an FLR factor by hand is not acceptable.
- The polarization equation is part of the energy-conserving structure, so changing its Padé/gyroaverage approximation changes \(M_k\) and potentially the flux forms.
- Adiabatic electrons reduce the number of independent species-resolved transport channels.
- It is less suitable than R1 for the first exact symbolic derivation.

### Role

**Recommended validation extension immediately after R1.** It should be treated as a controlled deformation of the ZLR result, not as a separate modelling branch.

---

## Candidate R3 — FLR four-moment model with parallel structure retained

### Definition

Use the R2 thermodynamic/FLR content but retain nonzero parallel derivatives or a minimal field-line discretization rather than collapsing the dynamics to a purely perpendicular local mode.

The state becomes either one four-component block for a fixed \(k_\parallel\),

\[
z_{k_\perp,k_\parallel}\in\mathbb C^4,
\]

or a block vector if the parallel coordinate is discretized.

### Advantages

- Preserves parallel electric/thermal-force and compression pathways that are explicit in the four-moment model.
- Better connection to realistic ITG eigenmode structure and, later, to local gyrokinetic flux-tube calculations.
- Lets us test whether apparent nonmodal transport in a 2-D reduction is robust to the restoration of parallel phase mixing/compression.

### Limitations

- Introduces geometry and boundary-condition choices before the core transport theorem has been tested in this model family.
- May obscure the mechanism by increasing the state dimension too early.
- A field-line discretization moves the project away from the desired small analytic benchmark.

### Role

**Deferred robustness test.** Do not use as the first four-moment implementation.

---

## Comparison

| Criterion | R0 isotropic ZLR | R1 anisotropic ZLR | R2 anisotropic FLR + adiabatic e | R3 FLR + parallel structure |
|---|---:|---:|---:|---:|
| Small analytic state | **very high** | **high** | high | medium/low |
| Parent energy structure retained | medium/high | **high** | **high** if FLR kept consistently | **high** if discretization is structure-aware |
| Temperature/heat-flux physics | medium | **high** | **high** | **high** |
| Pressure anisotropy | no | **yes** | **yes** | **yes** |
| FLR physics | no | no | **yes** | **yes** |
| Parallel dynamics available | optional/reduced | **yes** | **yes** | **explicitly central** |
| Direct CBC/GENE bridge | low | medium | **high** | **very high** |
| Best for hand theorem work | high | **very high** | medium | low |
| Best immediate role | auxiliary | **primary derivation** | **first validation** | later |

---

## Key conclusion: no user-level model fork is needed yet

The audit does **not** reveal two equally good competing routes. The scientifically cleaner strategy is sequential:

\[
\boxed{
\text{R1: anisotropic ZLR four-moment derivation}
\;\longrightarrow\;
\text{R2: restore FLR consistently}
\;\longrightarrow\;
\text{R3: restore richer parallel structure}
}
\]

R0 is retained only as an emergency analytic simplification if R1 proves algebraically opaque.

This ordering lets us separate three questions that should not be conflated:

1. Does signed finite-horizon transport optimization produce genuinely new structure once temperature anisotropy is present?
2. Does that structure survive finite-Larmor-radius physics?
3. Does it survive realistic parallel dynamics?

A positive result at each stage raises physical credibility without changing the central mathematical observable.

---

## What can already be stated about the operators

After a local equilibrium and Fourier convention are fixed, each retained reduction should have

\[
\dot z_k=A_k z_k,
\]

with the electrostatic potential eliminated through the linearized polarization/quasineutrality constraint.

The input metric must take the form

\[
W_k=\frac12 z_k^\dagger M_k z_k,
\qquad M_k\succ0,
\]

where \(M_k\) is derived from the perturbation free energy, including the electrostatic/polarization contribution generated by eliminating \(\phi_k\).

A radial particle-flux form should follow from

\[
\Gamma_k=\langle \widetilde n\,\widetilde v_{E,r}\rangle
      =z_k^\dagger Q_{\Gamma,k}z_k,
\]

while the thermal/heat flux must be derived from the radial flux of the relevant thermodynamic energy/enthalpy combination,

\[
q_k=z_k^\dagger Q_{q,k}z_k.
\]

The audit deliberately leaves \(Q_{q,k}\) symbolic: identifying the exact pressure combination is the next derivation task and is part of the physics, not a free modelling choice.

---

## Stop conditions for R1

Do **not** implement R1 if the next derivation fails any of these checks:

- the equilibrium linearization does not give a positive perturbation free-energy metric on the admissible space;
- eliminating \(\phi\) makes the metric singular without a clearly understood gauge/nullspace reduction;
- the proposed heat-flux form cannot be tied to the background-gradient/free-energy balance;
- the reduced ZLR equations are not closed after the intended geometric simplifications;
- the operator identity between free-energy rate, gradient drive/transport and dissipation cannot be verified.

If one of these fails, move to Scott's explicitly local free-energy-conserving GEM formulation rather than repairing the equations ad hoc.

---

## Immediate next task — B5

Derive **R1 only**, in one fixed source convention, before any code:

1. choose the simplest local electrostatic equilibrium/geometry for which the anisotropic ZLR four-moment subsystem is closed;
2. linearize the density, parallel-momentum, parallel-pressure and perpendicular-pressure equations;
3. eliminate \(\phi_k\) using the corresponding linearized polarization/quasineutrality relation;
4. derive the perturbation free-energy Hessian \(M_k\);
5. derive \(Q_{\Gamma,k}\) and the thermodynamically correct \(Q_{q,k}\) from radial flux expressions;
6. verify
   \[
   A_k^\dagger M_k+M_kA_k
   =\sum_\alpha g_\alpha Q_{\alpha,k}-R_k
   \]
   with all convention-dependent coefficients explicit;
7. only after this identity passes should R1 be frozen in code.

No user decision is required before B5. If the source equations do not permit a unique minimal local closure without an additional geometry choice, B5 must stop and present that choice explicitly rather than silently imposing one.

---

## Literature anchors

- D. Strintzi, B. D. Scott, A. J. Brizard, *Nonlocal Nonlinear Electrostatic Gyrofluid Equations: A four-moment model*, Phys. Plasmas **12**, 052517 (2005), arXiv:physics/0410276. The model evolves \((n,u_\parallel,p_\parallel,p_\perp)\), uses an electrostatic polarization equation, includes anisotropic temperatures, and derives exact energy conservation from a Lagrangian/Noether construction.
- B. D. Scott, *Free-energy conservation in local gyrofluid models*, Phys. Plasmas **12**, 102307 (2005). The fluctuation free-energy structure links polarization, \(E\times B\) eddy energy, density and perpendicular temperature; the globally consistent adiabatic-electron formulation is reported to agree with Cyclone-Base-Case gyrokinetic results.
- B. D. Scott, *Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities*, Phys. Plasmas **17**, 102306 (2010), arXiv:0710.4899. The gyrokinetic \(\delta f\) free-energy functional is used explicitly to constrain the moment model and its polarization structure.
