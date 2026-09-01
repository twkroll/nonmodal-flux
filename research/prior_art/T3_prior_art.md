# Prior-art audit for T3: multichannel balance and channel-resolved signed transport

**Date:** 2026-09-01  
**Status:** targeted first pass; not a systematic review

## What is clearly established

Classical dissipativity theory already permits indefinite quadratic supply rates. For linear systems, dissipativity with respect to a quadratic supply rate is routinely characterized by matrix inequalities / LMIs. Economic MPC and related control literature also uses indefinite quadratic stage costs together with dissipativity arguments. Therefore neither an indefinite quadratic balance nor an LMI representation is a viable novelty claim for this project.

Likewise, multiple/local supply-rate descriptions and interconnected dissipative systems are established topics. The project must not claim novelty merely from writing the total balance as a sum of several quadratic channels.

## What T3 adds conceptually

T3.1 makes explicit a point that is easy to miss in a physics manuscript: the total energy/free-energy balance fixes only the weighted combination

```math
\sum_\alpha g_\alpha Q_\alpha,
```

not the individual signed flux operators. This makes the physics-derived construction of each channel indispensable.

T3.2 then asks a more specific question than standard dissipativity:

> Given a physically fixed target flux operator, a physically fixed set of competing flux channels, and an admissible initial-state map, can the target finite-horizon signed transport be bounded sharply by dissipation and restricted cross-channel leakage?

The current proposed constant

```math
c_\beta(T,B)=
\sup_{x\in\mathcal R_T(B),x\ne0}
\frac{-x^\dagger g_\beta Q_\beta x}{x^\dagger Mx}
```

is intentionally reachable-subspace and input dependent. This differs in emphasis from generic global supply-rate LMIs, although a deeper control-theory audit is still required before treating it as new.

## Current risk assessment

**High risk of prior-art overlap:**
- indefinite quadratic supply rates;
- dissipation inequalities;
- finite-horizon LQ problems with indefinite costs;
- interconnected/multiple supply-rate systems;
- LMI-based gain bounds.

**More promising, but unverified:**
- signed *physical transport* as the optimized initial-condition output rather than an abstract performance cost;
- a transport-neutral initial subspace;
- separate physics-derived channel operators that are not free decision variables;
- reachable-subspace leakage constants tied to the admissible initial perturbations;
- combining the T1 short-time generation law with a channel-resolved finite-horizon balance bound.

## Literature anchors checked in this pass

1. Standard linear dissipativity with quadratic supply rates: quadratic supply matrices and storage functions lead to LMIs; this is classical and broad.
2. Olanrewaju & Maciejowski (2017), indefinite linear-quadratic economic MPC: dissipativity is explicitly analyzed for indefinite quadratic costs.
3. Work on distributed/interconnected dissipative systems uses local quadratic supply rates, so a multichannel or local decomposition is not new by itself.
4. Contemporary systems/ML work continues to use quadratic supply-rate dissipativity, including recent robustness analysis of convolutional neural networks viewed as dynamical systems.

## Provisional conclusion

T3 should be presented as a **physics-constrained specialization and refinement of dissipativity ideas**, not as a new dissipativity theory. Its publishable value will depend on whether the restricted constants can be made sharp and whether the resulting theorem explains a nontrivial plasma flux-optimal perturbation that standard energy growth or global operator-norm bounds miss.

## Next audit queries

- "multiple supply rates" + channel-specific gain + initial condition;
- "local dissipativity" + finite horizon + quadratic output;
- "restricted reachable subspace" + dissipativity / supply rate;
- "indefinite quadratic output" + initial state + finite horizon;
- plasma papers that separately bound particle and heat flux from free energy.
