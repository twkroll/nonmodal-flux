# Fusion model audit for nonmodal-flux

**Status:** working decision note  
**Date:** 2026-09-01  
**Goal:** compare reduced plasma models for a fusion-facing continuation of `nonmodal-flux` without freezing a convention prematurely.

## Decision criteria

A useful next model should satisfy as many of the following as possible:

1. **Positive physical metric:** an explicit free-energy/Helmholtz-energy functional that can define \(M\succ0\).
2. **Physical transport observables:** at least one genuine particle or heat flux derived from the model, not an ad-hoc weighted state norm.
3. **Multiple channels if possible:** separate observables such as \(Q_{\Gamma_i},Q_{q_i},Q_{q_e}\).
4. **Finite-horizon tractability:** a linearized operator small enough for exact or high-accuracy propagator and Gramian work.
5. **Analytic transparency:** enough structure to derive short-time asymptotics, transport-neutral input spaces and balance identities by hand.
6. **Fusion relevance:** a credible connection to ITG/TEM turbulence and confinement physics.
7. **GENE/Jenko bridge:** a clean path from the reduced model to the free-energy and flux diagnostics used in local gyrokinetics/GENE.
8. **Low novelty risk:** the model should expose a new transport-optimal question rather than merely reproduce known free-energy optimal-growth results.

---

## Candidate A — Two-field Hasegawa–Wakatani type model

### Strengths

- Very small linear system per Fourier mode; ideal for exact \(2\times2\) or near-exact analysis.
- Natural positive quadratic disturbance energy can be defined for a fixed convention.
- Radial particle flux has the familiar cross-phase structure
  \[
  \Gamma_k\propto k_y\operatorname{Im}(n_k^*\phi_k),
  \]
  hence a Hermitian indefinite transport form \(Q_{\Gamma,k}\).
- Excellent for testing transport-neutral initialisation,
  \[
  B^\dagger Q_{\Gamma,k}B=0,
  \]
  and the transport-generation hierarchy.
- Existing nonmodal drift-wave literature makes it easy to benchmark the propagator and energy growth.

### Weaknesses

- No genuine temperature field, hence no real heat-flux channel.
- Fusion relevance is indirect; the model is primarily a drift-wave prototype rather than a quantitatively credible tokamak transport model.
- Because the state dimension is tiny, a robust mismatch between free-energy and flux optimals may be mathematically instructive but physically too weak to carry the fusion story.

### Role in the programme

**Keep as the validation and theorem benchmark, not as the ultimate fusion novelty carrier.**

---

## Candidate B — Energy-conserving gyrofluid model in the Scott/GEM family

Bruce Scott's energy-conserving gyrofluid construction is explicitly organised around fluctuation free-energy conservation. The gyrofluid free energy is derived from the underlying gyrokinetic free-energy structure, and density, potential and temperature moments are coupled in a way constrained by the energy theorem. This is a substantially stronger physical foundation than adopting a generic three-field ITG toy model.

### Strengths

- Explicit free-energy conservation is a design principle of the model.
- Temperature moments are genuine dynamical variables, giving access to heat-flux observables.
- The model was constructed for ITG-like turbulence and recovers/relates to the Cyclone Base Case in appropriate limits.
- It provides a natural middle layer between a two-field drift model and full gyrokinetics.
- The moment structure makes it plausible that physically derived transport forms can remain low-dimensional after Fourier decomposition.
- Finite-Larmor-radius effects and multiple moments offer enough structure that energy-optimal and transport-optimal perturbations need not be trivially related.

### Weaknesses

- The full GEM system is not a three-variable toy model; it can contain several moments, electromagnetic variables and closure terms.
- A careless truncation may destroy the free-energy theorem, exactly the property we want to preserve.
- We therefore cannot simply take an arbitrary “three-field ITG model” and call it a reduced GEM model. Any reduction must be derived and its free-energy balance rechecked.
- Direct relation to current GENE diagnostics is conceptually strong but not one-to-one at the state-vector level.

### Role in the programme

**Best candidate for the first fusion-facing reduced model, provided we can identify a minimal free-energy-consistent electrostatic/ITG reduction without breaking the energy theorem.**

This is the current leading reduced-model candidate.

---

## Candidate C — Local electrostatic gyrokinetics with one kinetic ion species and adiabatic electrons

This is close to the standard Cyclone-Base-Case style setting used in GENE free-energy studies. The 2011 GENE free-energy-balance work of Bañón Navarro et al. explicitly analyses ITG-driven turbulence in this setting and separates gradient drive, dissipation, curvature/parallel transfer and the nonlinear conservative redistribution of free energy.

The Helander–Plunk energetic-bounds framework provides an especially clean abstract formulation of the gyrokinetic Helmholtz free energy and shows that gradient drive can be written in terms of radial particle and heat fluxes.

### Strengths

- Direct fusion relevance: local ITG gyrokinetics is a standard first-principles framework for core turbulent transport.
- The positive free-energy metric is not an invention of our method; it is part of the established gyrokinetic energetic structure.
- The ion heat flux is a genuine physical transport observable entering the free-energy drive.
- Very direct conceptual bridge to GENE and to Jenko's free-energy/cascade work.
- The linear initial-value problem is exactly the setting required by our propagator formulation.
- The model can later be discretised in parallel coordinate and velocity space while preserving the distinction between \(M\) and \(Q_q\).

### Weaknesses

- It is no longer a tiny matrix problem; phase-space discretisation can make the operator large.
- With adiabatic electrons, some particle-flux channels can be constrained or vanish in particular simplified settings, reducing the usefulness of a multi-channel transport geometry.
- Wave–particle resonance and magnetic geometry make analytic proofs more difficult.
- Helander & Plunk already optimise instantaneous **free-energy growth**, so our novelty must be unambiguously finite-horizon **signed heat/particle transport**, not another energetic bound.

### Role in the programme

**Best first gyrokinetic validation target after the reduced gyrofluid step.**

A linear local electrostatic ITG case with adiabatic electrons is likely the cleanest bridge from our theory to GENE-compatible physics.

---

## Candidate D — Local gyrokinetics with kinetic ions and kinetic electrons

### Strengths

- Provides genuinely separate species-resolved transport channels:
  \[
  \Gamma_i,\quad \Gamma_e,\quad q_i,\quad q_e.
  \]
- This is the natural setting for a finite-time multi-channel transport body,
  \[
  \mathscr T_T=\{(\Gamma_i,\Gamma_e,q_i,q_e)_T:W(0)=1\}.
  \]
- Strongest direct connection to confinement physics and to modern GENE applications.
- Offers the most interesting possibility that
  \[
  u_W\neq u_{q_i}\neq u_{q_e}\neq u_{\Gamma}.
  \]
- Kinetic electrons also make trapped-electron and TEM-related questions possible later.

### Weaknesses

- Highest dimensionality and strongest dependence on geometry, velocity resolution, collisions and closure-free kinetic effects.
- Poor choice for the first theorem-development stage.
- Large parameter space makes it easy for numerical exploration to outrun the theory.
- A clean transport-neutral input subspace requires more care because the admissible perturbation space includes multiple species and field constraints.

### Role in the programme

**Strongest eventual fusion application, but not the next model to implement.**

---

## Comparison matrix

| Criterion | A: HW | B: energy-conserving gyrofluid | C: GK ions + adiabatic e | D: GK kinetic i+e |
|---|---:|---:|---:|---:|
| Explicit positive free energy | medium | **high** | **high** | **high** |
| Genuine particle flux | **high** | high | medium/high | **high** |
| Genuine heat flux | no | **high** | **high** | **high** |
| Multiple independent channels | low | medium/high | medium | **very high** |
| Small analytic operator | **very high** | medium | low | very low |
| Transport-neutral analysis | **very high** | high | medium | medium |
| Direct GENE/Jenko bridge | low | medium/high | **very high** | **very high** |
| Fusion credibility | low/medium | **high** | **very high** | **very high** |
| Suitable now | **yes, benchmark** | **yes, next fusion model** | later | later |

---

## Current recommendation

The model hierarchy should be

\[
\boxed{
\text{HW benchmark}
\;\longrightarrow\;
\text{minimal free-energy-consistent gyrofluid ITG model}
\;\longrightarrow\;
\text{local linear gyrokinetics/GENE-compatible test}
}
\]

with kinetic-electron gyrokinetics only after the first three stages succeed.

The key point is that the **next fusion-facing model should not be chosen merely because it has three fields**. It should be chosen because its temperature and density moments sit inside a documented free-energy theorem. Scott's energy-conserving gyrofluid programme is therefore a better starting family than an arbitrary reduced ITG system.

---

## Novelty implications

### What Candidate B can test

A free-energy-consistent gyrofluid model gives the smallest realistic setting in which we can ask simultaneously:

\[
\max W(T),\qquad
\max \int_0^T \Gamma(t)\,dt,\qquad
\max \int_0^T q(t)\,dt.
\]

The publishable target is not merely that the corresponding eigenvectors differ. We should test whether the differences persist under:

- transport-neutral initialisation;
- a fixed physical free-energy input metric;
- physically derived particle- and heat-flux forms;
- stable or weakly damped spectra;
- parameter perturbations that preserve the free-energy theorem.

If this produces robustly distinct optimal perturbations and a nontrivial multi-channel Pareto geometry, it would be substantially stronger than the HW-only result.

### What Candidate C can validate

If the same qualitative structure appears in a discretised local gyrokinetic initial-value operator with a heat-flux observable taken directly from gyrokinetic diagnostics, we obtain a credible bridge to GENE/Jenko physics without requiring nonlinear turbulence simulations.

This would give a particularly clean comparison:

\[
\text{normal-mode growth}
\quad\text{vs.}\quad
\text{instantaneous free-energy optimal growth}
\quad\text{vs.}\quad
\text{finite-horizon heat-flux optimal transport}.
\]

The third object is the one our project should own.

---

## Immediate next task

Before any model implementation, perform a **minimal-model derivation audit** inside the Scott/GEM family:

1. identify the smallest electrostatic ITG/gyrofluid subsystem with a documented free-energy theorem;
2. write its continuous equations and state variables exactly as in the source convention;
3. derive the quadratic free-energy metric \(M_k\);
4. derive particle- and heat-flux forms \(Q_{\Gamma,k}\) and \(Q_{q,k}\) directly from the physical radial fluxes;
5. derive the linear operator \(A_k\);
6. verify the operator balance
   \[
   A_k^\dagger M_k+M_kA_k
   =\sum_\alpha g_\alpha Q_{\alpha,k}-R_k;
   \]
7. only then decide whether this reduced model is safe to freeze in code.

This is a **derivation/audit task**, not yet an implementation task.

---

## Decision status

No user decision is required yet. The evidence currently supports one clear ordering:

- HW remains the mathematical benchmark.
- The Scott/GEM energy-conserving gyrofluid family is the preferred search space for the next reduced fusion model.
- Local electrostatic gyrokinetics is the preferred first GENE-facing validation layer.
- Fully kinetic multi-species gyrokinetics is deferred until the finite-horizon transport theory has survived the reduced tests.

## Literature anchors used for this audit

- B. D. Scott, *Free-energy conservation in local gyrofluid models* / GEM energy-conserving gyrofluid work (2005): free-energy conservation constrains the gyrofluid moment equations; adiabatic-electron calculations connect to the Cyclone Base Case.
- B. D. Scott, *Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities* (2010): gyrofluid equations systematically derived from gyrokinetic free energy.
- A. Bañón Navarro et al., *Free Energy Balance in Gyrokinetic Turbulence* (2011): GENE-formalism ITG free-energy balance and separation of drive, dissipation and transfer terms.
- A. Bañón Navarro et al., *Free Energy Cascade in Gyrokinetic Turbulence* (2011): nonlinear conservative redistribution of gyrokinetic free energy across perpendicular scales.
- P. Helander & G. G. Plunk; G. G. Plunk & P. Helander, *Energetic bounds on gyrokinetic instabilities*, Parts 1–3 (2022–2023): Helmholtz/generalised free-energy balances, particle/heat-flux drive terms and instantaneous optimal free-energy growth.
- P. J. Costello & G. G. Plunk, *Energetic bounds on gyrokinetic instabilities. Part 4* (2025): low-dimensional gyrofluid-like representation of gyrokinetic optimal modes in a bounce-averaged-electron setting.
