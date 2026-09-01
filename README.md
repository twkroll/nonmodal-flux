# nonmodal-flux

`nonmodal-flux` is a research codebase for **transport-optimal nonmodal stability**: finite-time optimization of physically derived, signed transport observables under independent positive energy/free-energy metrics and physically admissible initial disturbances.

The project is intentionally theory-first. It follows the research program *Transportoptimale nonmodale Stabilität* and is organized around explicit decision gates before model complexity or parameter sweeps are increased.

## Core principle

We keep the disturbance-size metric and the transport observable separate:

- `M = M† > 0` measures initial disturbance size / energy / free energy.
- `Q = Q†` represents a **physics-derived signed transport form** and may be indefinite.
- `x0 = B u` encodes admissible initial disturbances.
- `Rin = Rin† > 0` measures input cost.

Transport observables are derived from the continuous physical flux expression before discretization. We do **not** replace them by ad-hoc weighted sums of state amplitudes. Cross terms, signs, quadrature/mass weights, orientations, and separate transport channels are preserved.

## Current phase: Phase 0 / Gate 0

Before freezing a plasma convention or running parameter sweeps, we are auditing novelty and model conventions.

Current priorities:

1. maintain a claim matrix against the closest literature;
2. formalize finite-horizon signed transport optimization;
3. analyze transport-neutral admissible input spaces, in particular `B† Q B = 0`;
4. derive theorem candidates and falsification tests;
5. only then implement model-independent JAX kernels (C0–C5);
6. freeze a Hasegawa–Wakatani convention only after a documented PDE-to-matrix derivation.

## Repository layout

```text
nonmodal-flux/
├── decisions/
│   └── registry.md
├── research/
│   ├── claim_matrix.md
│   └── literature_notes.md
├── src/
│   └── nonmodal_flux/
│       └── __init__.py
├── tests/
│   └── test_environment.py
├── pyproject.toml
└── README.md
```

No application model is frozen at this stage.

## Research gates

- **G0 — Novelty:** pursue a standalone foundations paper only if at least one theorem-level gap and one nontrivial plasma transport result survive the audit.
- **G1 — Theory:** require at least three precise results, with at least one beyond standard linear-quadratic / Gramian theory.
- **G2 — Numerics:** no application sweeps until analytic, Hermiticity, coordinate-invariance, and precision tests pass.
- **G3 — Plasma pilot:** require a robust distinction between energy/free-energy optimal and signed flux optimal under restricted/transport-neutral initializations.

## Numerical policy

JAX computations use 64-bit precision. Generalized Hermitian eigenproblems will be solved by Cholesky whitening rather than explicit matrix inversion. Scientific model construction, solvers, and plotting remain separated.

## Status

Research scaffold only. No Hasegawa–Wakatani, gyrofluid, swing, or port-Hamiltonian model equations are committed yet.
