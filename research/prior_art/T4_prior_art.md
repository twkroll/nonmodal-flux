# Prior-art audit for T4: short-time energy-versus-transport separation

**Date:** 2026-09-01  
**Status:** targeted first pass; novelty not established

## Result

No direct plasma paper was found in this pass that optimizes a finite-horizon **signed particle/heat-flux form** over initially transport-neutral perturbations and compares the resulting optimal direction with the physical free-energy optimal.

This absence is not a novelty proof. The ingredients around T4 are individually close to standard results.

## Established neighboring ideas

### 1. Short-time optimal energy growth

Classical nonmodal stability theory characterizes short-time energy growth through the Hermitian energy-production operator. Thus the expansion

```math
K_E(T)=I+T E_1+O(T^2)
```

and selection of the dominant eigenspace of `E_1` are standard perturbation ideas.

### 2. Objective-dependent optimal perturbations

Output-specific transient-growth and semi-norm formulations already show that changing the measured quantity changes the optimal perturbation. Therefore T4 cannot claim novelty from `u_E != u_Q` alone.

### 3. Gyrokinetic optimal free-energy growth

Plunk/Helander and follow-up work construct optimal modes of instantaneous free-energy growth and energetic bounds. These are the closest plasma-side relatives of the `E_1` problem, but they do not in the sources checked here replace the objective by a finite-horizon signed particle- or heat-flux functional.

### 4. Hasegawa-Wakatani nonmodal energetics

Camargo, Tippett and Caldas analyze nonmodal energy amplification and phase evolution in resistive drift waves. This means that nonmodal cross-phase dynamics are known. The unresolved question for this project is whether the **flux itself**, represented by its physical indefinite cross-form, has been used as the optimized finite-horizon initial-condition objective under a whole transport-neutral admissible subspace.

### 5. Landreman, Plunk and Dorland (2015)

The generalized universal-instability work explicitly discusses transient linear amplification in stable kinetic plasma and notes that optimal-perturbation techniques exist for maximum amplification. Particle flux is an important physical diagnostic and is discussed in relation to profile relaxation, but the checked material does not provide the same signed-flux initial-condition optimization proposed here.

## Control-theory overlap

The geometry around T4 also touches established output-nulling and dissipativity theory:

- output-nulling subspaces are a standard systems concept;
- indefinite quadratic performance and quadratic supply rates are standard;
- Hermitian eigenvector perturbation theory is standard.

Our condition `B^\dagger Q B=0` is not the same as a conventional linear-output nulling condition: for an indefinite `Q`, `range(B)` can be totally `Q`-isotropic while `QB` remains nonzero. This allows an `O(T^2)` accumulated signed-transport onset, unlike a positive-semidefinite output energy where `B^\dagger Q B=0` forces `QB=0` and delays the onset. This distinction is mathematically useful but still requires deeper prior-art checking.

## Updated novelty assessment

**T4 itself: supporting theorem, not headline novelty.**

The potentially publishable package is the combination:

1. physics-derived indefinite flux form `Q` (not an ad-hoc score),
2. physical free-energy metric `M`,
3. physically justified transport-neutral input space,
4. finite-horizon signed flux extremals,
5. a robust energy/flux optimal mismatch with mechanism,
6. channel-resolved balance bounds or asymptotics.

## References / anchors for continued citation chasing

- P. J. Schmid, *Nonmodal Stability Theory*, Annual Review of Fluid Mechanics 39 (2007).
- S. J. Camargo, M. K. Tippett, I. L. Caldas, *Nonmodal Energetics of Resistive Drift Waves*, Phys. Rev. E 58 (1998).
- M. Landreman, G. G. Plunk, W. Dorland, *Generalized Universal Instability: Transient Linear Amplification and Subcritical Turbulence*, J. Plasma Phys. 81 (2015).
- P. Helander, G. G. Plunk / G. G. Plunk, P. Helander, *Energetic bounds on gyrokinetic instabilities*, Parts 1-2 (2022).
- J. C. Willems, *Dissipative Dynamical Systems, Part II: Linear Systems with Quadratic Supply Rates* (1972), as background for what must not be claimed as new.

## Next literature question

After fixing a specific plasma convention, search the exact physical flux name and formula together with `optimal perturbation`, `singular vector`, `transient growth`, `finite time`, and `cross phase`. The model-specific citation graph is more likely to settle novelty than further generic systems searches.