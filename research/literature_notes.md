# Literature Notes v0.1 — Phase 0

**Date:** 2026-09-01  
**Scope:** First targeted novelty audit for P1; not yet a systematic review.

## Lülff (2015): heat-transport POD

### Already established

- Standard POD is replaced by an objective tied directly to heat transport.
- The transport quantity is represented by a Hermitian but indefinite bilinear/quadratic form.
- Positive and negative structures correspond to opposite directions of heat transport.

### Consequence for this project

The idea of an indefinite/signed transport form is not new by itself, and neither is the observation that energy-optimal and transport-optimal structures can differ.

Our intended distinction is dynamical: optimize **initial disturbances** of a nonmodal system over a finite horizon under an independent positive disturbance metric and physically admissible inputs.

### Modeling rule extracted from Lülff

We adopt the construction principle, not merely the terminology: the transport observable must be derived from the actual continuous physical transfer quantity before discretization. Ad-hoc weighted sums of amplitudes are not acceptable substitutes.

---

## Camargo, Tippett & Caldas (1998): Hasegawa–Wakatani nonmodal energetics

### Already established

- Linearized HW dynamics are nonnormal.
- A physically relevant energy is used as the optimization norm.
- Finite-time optimal energy growth is studied.
- Density–potential phase shifts are time dependent and can differ from modal values.

### Consequence

The project must not claim novelty from “HW is nonnormal”, “stable eigenvalues miss transient behavior”, or “nonmodal evolution changes the cross-phase”.

### Open audit question

The first pass did not identify a direct optimization of **finite-horizon signed particle flux over the initial perturbation**, especially under a transport-neutral admissible input space. This requires citation chasing before any novelty claim is made.

---

## Benner, Goyal & Pontes Duff (2022): quadratic-output Gramians

### Already established

- Linear state dynamics with quadratic outputs form an established systems class.
- Gramian constructions and generalized Lyapunov equations are available.
- Energy-functional interpretations are developed for such systems.

### Consequence

```math
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt
```

must not be marketed as a new Gramian idea. Indefinite signed physical interpretation may matter, but algebra alone is not enough for novelty.

---

## Blumenthal et al. (2017): full norms, semi-norms, transient growth

### Already established

- Nonmodal optimals depend strongly on the chosen output measure.
- Semi-norm outputs can measure only part of the state.
- Initial perturbations can reside in components not directly measured by the output and later generate that output dynamically.

### Consequence

Restricted inputs and partial outputs are not novel general concepts. Our potentially distinctive structure is a **signed physical transport form** together with an admissible subspace on which the initial transport itself vanishes.

---

## Helander & Plunk / Plunk & Helander (2022): gyrokinetic energetic bounds and optimal modes

### Already established

- Instantaneous optimal growth of gyrokinetic free energy is formulated rigorously.
- Tight energetic growth bounds are derived.
- Particle- and heat-flux terms enter the free-energy budget.

### Consequence

A balance-based theory in plasma is not an empty field. Any F5-type result must be clearly different from a bound on instantaneous free-energy growth.

Our intended target is a finite-horizon **signed transport** functional under a separate positive initial metric and, ideally, transport-neutral admissible inputs.

---

## Hillebrecht (2026): L2–L2 gain bounds for quadratic output systems

This is a particularly important current reference because it is contemporaneous with the project.

### Adjacent problem

Quadratic-output systems are treated in an input-output gain framework with computable L2–L2 bounds.

### Key distinction to verify carefully

The problem is forced input-output with zero initial state, whereas our core problem is autonomous **initial-condition optimization** with `x0 = B u` over a finite horizon.

### Consequence

“Quadratic-output gain bound” is not a free novelty space in 2026. Any bound we claim must exploit the initial-state formulation, signed transport, admissible/nullspace structure, and physical balance in a genuinely new way.

---

## Maldonado et al. (2023): power-system transient growth

### Already established

- Large preasymptotic linear growth in power systems is optimized computationally.
- SVD-based methods are used.
- Quantities of interest can target selected state components such as rotor-speed deviations.

### Consequence

P3 cannot center on generic transient growth in power systems.

The promising differentiation is: physical Hamiltonian energy, **signed local line/cut power transfer**, global passivity versus local redistribution, and topology-based statements.

---

## Optimal heat-transport perturbations outside plasma

Optimal initial perturbations for heat transport have also been studied in other physical domains, including ocean circulation.

### Consequence

“Optimize an initial perturbation for transport” is not new as a generic idea.

The project therefore needs a precise combination of:

- physics-derived signed transport form;
- independent positive disturbance/free-energy metric;
- nonmodal finite-time dynamics;
- admissible and preferably transport-neutral initial space;
- physical energy/free-energy balance;
- theorem-level structural results;
- a nontrivial plasma mechanism.

---

# Working hypotheses after audit v0.1

## H0 — Framework novelty alone is insufficient

Strongly supported by the first audit.

## H1 — Transport-neutral inputs are the key nontriviality filter

Current algebraic prototype:

```math
B^\dagger Q B = 0.
```

This removes transport already present at the initial instant.

## H2 — Short-time transport generation is controlled by `A†Q + QA`

For neutral inputs, the leading cumulative term is expected to be

```math
\frac{T^2}{2} B^\dagger(A^\dagger Q+QA)B.
```

This should be formalized first and then searched explicitly in the prior art.

## H3 — A single-channel balance is both opportunity and risk

If

```math
A^\dagger M + MA = gQ - R,
```

then the integrated transport is exactly related to energy change and dissipation. This may yield a sharp physical bound, but it may also reveal that some apparent transport optimization is less independent than expected in a simple model. That is an early falsification test, not an inconvenience to hide.

## H4 — Strongest plasma pilot question

Not:

> Is the Hasegawa–Wakatani energy optimal nonmodal?

Instead:

> For a spectrally stable HW model and a physically admissible transport-neutral initial space, does a robust finite-horizon signed particle-flux optimal exist that differs from the free-energy optimal, and can the difference be explained asymptotically by dynamically generated cross-phase?

---

# Next literature work

1. Backward/forward citation chase from Camargo (1998) for particle flux, transport, and optimal perturbations.
2. Citation chase from the Plunk/Helander energetic-bound papers for direct particle-/heat-flux optimization.
3. Control-theory search around indefinite quadratic performance, finite horizon, initial-state optimization, and zero-initial-output subspaces.
4. Later: port-Hamiltonian literature on internal/local power transfer across cuts or subsystems.
5. Once the short-time theorem is formalized, search for the exact projected expansion under `B† Q B = 0`.

## References currently tracked

- J. Lülff, *Describing the Heat Transport of Turbulent Rayleigh–Bénard Convection by POD Methods*, arXiv:1510.06908 (2015).
- S. J. Camargo, M. K. Tippett, I. L. Caldas, *Nonmodal Energetics of Resistive Drift Waves*, Phys. Rev. E 58, 3693 (1998).
- P. Benner, P. Goyal, I. Pontes Duff, *Gramians, Energy Functionals, and Balanced Truncation for Linear Dynamical Systems With Quadratic Outputs*, IEEE TAC 67(2), 886–893 (2022).
- R. S. Blumenthal, A. K. Tangirala, R. I. Sujith, W. Polifke, *A systems perspective on non-normality in low-order thermoacoustic models: Full norms, semi-norms and transient growth* (2017).
- P. Helander, G. G. Plunk and G. G. Plunk, P. Helander, *Energetic bounds on gyrokinetic instabilities*, Parts 1–2 (2022).
- B. Hillebrecht, *L2-L2-gain bounds for quadratic output systems*, arXiv:2607.00552 (2026).
- D. A. Maldonado, E. Constantinescu, J. Zhao, M. Anitescu, *Efficient Computation of Power System Maximum Transient Linear Growth*, arXiv:2302.10388 (2023).
