# Prior-art audit — T1 transport-neutral short-time generation

**Date:** 2026-09-01  
**Scope:** targeted web/literature search, not yet exhaustive citation chasing

## Question audited

Is the following combination already standard as a named/result-level construction?

> For autonomous linear dynamics `x_dot = Ax`, optimize an integrated **signed/indefinite physical quadratic transport observable** over a finite horizon from initial conditions `x0=Bu`, subject to a positive input metric and a whole admissible subspace satisfying `B†QB=0`, so that the leading transport is dynamically generated and controlled by `B†(A†Q+QA)B`.

## Result of this pass

**No direct match was found for the full combination.** This is not a novelty proof.

The search instead found four nearby literatures that substantially reduce what can be claimed as new.

---

## 1. Classical nonmodal short-time growth

Nonmodal stability theory already uses a short-time Taylor expansion / numerical-abscissa argument to show that the initial growth of an energy norm is governed by the Hermitian part of the evolution operator. For the Euclidean norm the familiar object is `(A+A†)/2`; with a physical metric `M`, the corresponding derivative is `A†M+MA`.

### Relevance to T1

The operator `A†Q+QA` is therefore not a surprising new algebraic object. T1 is best understood as the **signed-observable, projected-input analogue** of a familiar short-time-growth calculation.

### Consequence

Do not claim novelty from the Taylor expansion itself or from the appearance of `A†Q+QA`.

---

## 2. Quadratic-output systems with nonzero initial states

The quadratic-output systems literature treats outputs of the form

```math
y_Q(t)=x(t)^T M x(t)
```

and has developed Gramian/energy-functional machinery. More recent structure-preserving/model-reduction work explicitly includes nonzero initial conditions in systems with quadratic outputs.

### Important distinction

Much of this literature studies **output energy**, commonly involving `\int |y_Q(t)|^2 dt`, observability, or model reduction. Our functional is instead the signed integral

```math
\int_0^T x(t)^\dagger Qx(t)\,dt,
```

which preserves sign and direction of physical transport.

That difference matters physically, but it does not make the underlying quadratic-output algebra new.

---

## 3. Restricted/semi-norm nonmodal optimization

The transient-growth literature already includes objectives that measure only selected state components and initial disturbances that can lie outside the directly measured subspace. Thus, dynamically creating a later output from an initially unmeasured component is not novel as a general systems idea.

### Distinction sought here

Our proposed restriction is stronger and physics-driven:

```math
B^\dagger QB=0,
```

so **every** admissible initial state has zero value of the signed physical transport form, rather than merely zero amplitude in a selected output component.

This remains a promising differentiator, but it needs citation chasing before being elevated to novelty.

---

## 4. Indefinite quadratic performance in control

Indefinite quadratic cost/performance indices are well established in optimal control, robust control, and game formulations.

### Distinction

Those problems generally optimize controlled/forced trajectories and costs rather than the autonomous finite-horizon initial-condition problem targeted here. Still, the phrase “indefinite quadratic performance” is established terminology and cannot itself support a novelty claim.

---

## 5. Flux optimization in other dynamical settings

Optimal perturbations for transport/flux exist outside the proposed plasma problem, including optimization of chaotic flux across separatrices. Therefore, “optimal perturbation for maximum flux” is also not a globally new concept.

The intended contribution must be narrower: nonmodal linear dynamics, physics-derived signed quadratic flux, positive free-energy/input metric, transport-neutral admissible initial space, and theorem-level balance structure.

---

# Assessment of T1

## Mathematical status

**Proved, elementary finite-dimensional proposition.**

## Novelty status

**Not established; likely too elementary to serve as P1's headline theorem.**

## Scientific value

High as a project diagnostic because it formalizes exactly what is meant by “dynamically generated transport rather than an initially inserted optimal cross-phase.”

It also gives a clean control experiment for the plasma pilot and a precise unit/invariance test for the JAX implementation.

## Recommended role in P1

Use T1 as one of:

- an early proposition establishing the restricted-input mechanism;
- a lemma feeding a stronger balance-based bound;
- the first member of a higher-order transport-generation hierarchy;
- an asymptotic interpretation of a physically derived HW flux-optimal calculation.

Do **not** base Gate 0 solely on T1.

---

# Stronger next theorem directions

## A. Transport-generation order

Define the smallest `r >= 0` for which the projected coefficient in

```math
B^\dagger e^{A^\dagger t}Qe^{At}B
```

is nonzero. Characterize the corresponding leading signed gain and identify structural conditions that force `r>0`.

Potential value: distinguishes merely zero initial flux from deeper dynamical decoupling/nullspace structure.

## B. Balance-constrained bound

Combine

```math
A^\dagger M+MA=\sum_\alpha g_\alpha Q_\alpha-R
```

with `B†Q_\alpha B=0` for one or more channels and derive a finite-horizon signed bound that explicitly contains dissipation and admissible-input geometry.

Potential value: much closer to the physical novelty target of the research program.

## C. Energy-optimal / flux-optimal mismatch under neutral inputs

Find conditions under which the leading transport-optimal eigenspace of

```math
B^\dagger(A^\dagger Q+QA)B
```

cannot coincide with the corresponding short-time free-energy-optimal eigenspace except under identifiable commutation/alignment conditions.

Potential value: turns the generic statement “different objectives give different optimals” into a restricted, physically interpretable theorem.

---

# Sources checked in this pass

- P. J. Schmid and related nonmodal-stability literature on numerical abscissa / short-time growth.
- R. I. Sujith, M. P. Juniper, P. J. Schmid, review of nonnormal thermoacoustic instability and short-time energy growth.
- P. Benner, P. Goyal, I. Pontes Duff, quadratic-output Gramian literature.
- Structure-preserving model-reduction work extending quadratic-output systems to nonzero initial conditions.
- R. S. Blumenthal et al., semi-norm/restricted-output transient growth.
- Literature on indefinite quadratic performance indices in control.
- S. Balasuriya, optimal perturbation for enhanced chaotic transport.

## Search limitation

This pass used keyword and semantic searches. Before any publication-level novelty statement, perform forward/backward citation chasing around:

1. Benner/Goyal/Pontes Duff and later quadratic-output initial-condition work;
2. semi-norm transient-growth literature;
3. indefinite linear-quadratic performance literature;
4. plasma papers citing Camargo (1998) and Plunk/Helander (2022);
5. exact phrases around zero initial quadratic output, isotropic/null subspaces of indefinite forms, and finite-horizon initial-state optimization.
