# MASTER Handoff — Fusion F2.6A Canonical Matrix-Free Operator Artifact / Reproducibility Freeze 0.1

**Date:** 2026-09-07  
**Selected branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Task

Create and freeze the missing canonical executable numerical artifact for the already-qualified F2.6 `0_3` operator, and do nothing else.

The controlling upstream savepoints are:

- `research/master/fusion_f2_6_discrete_algebra_pass_integration_freeze_0_1.md`;
- `research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`;
- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`.

The F2.7 HOLD to resolve is:

- `research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`.

## Required artifact

Publish a versioned executable matrix-free implementation, or equivalent serialized factor set, that deterministically instantiates for K0/K1/K2 the exact F2.6 `0_3` maps

\[
E_Kx,\qquad F_Kx,\qquad E_K^{-1}x,
\]

with the frozen repaired ladder

\[
N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.
\]

Prefer a source-level matrix-free builder over gigantic serialized dense arrays. The committed artifact must expose enough of the numerical construction that a later eigensolver can use the exact same maps without re-deriving weak/SBP, bounce, quasineutrality or field-coupling choices from prose.

## Equivalence requirement

Before PASS, the committed artifact must reproduce the already-frozen F2.6 `0_3` diagnostics at their reported scale, including at minimum:

- full-support local-B FLR manufactured identity on active nodes and independent envelope;
- quasineutrality residuals;
- canonical positive Helmholtz metric Hermiticity/positivity diagnostics;
- `B_K=I`, `R_in,K=M_K` inheritance;
- ion streaming/mirror and full conservative phase-space adjoint/skew residuals;
- independently reconstructed particle/ion-heat/trapped-electron-heat channel Hermiticity;
- hydrogenic particle ambipolarity;
- complete F2.1 discrete free-energy-balance residuals.

Record a deterministic reproducibility manifest: exact file paths, level metadata, seeds/tolerances needed to reproduce those checks, and a stable interface description for `apply_E`, `apply_F`, and `solve_E` or equivalent.

If the exact F2.6 `0_3` construction cannot be established from canonical information without introducing genuinely new implementation choices, return `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER`. Do not silently create a substitute operator.

## Frozen / forbidden

Do not change F2.1–F2.5R, the F2.3 physical point, F2.4 input geometry, local-B ion-FLR convention, K0/K1/K2 windows, repaired `N_mu` ladder, ion Hermite orders, trapped-electron representation, bounce quadrature, quasineutrality treatment, weak/SBP convention or physical channel definitions.

Do not compute or inspect eigenvalues, Ritz pairs, spectral abscissa, growth rates, pseudospectra or eigenvectors. Do not construct propagators, matrix exponentials, Gramians, cumulative objectives, optimizers, angles, gaps or horizon curves. Do not scan physical parameters/resolutions beyond the frozen K0/K1/K2 realization, run GENE, add collisions/damping/filtering, or open MODES/CONT/CASCADE/Power Grid/Photonics/Paper-1 work.

## Outputs

Create versioned canonical outputs, including:

1. a report `research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`;
2. the executable operator artifact under a clear versioned `research/fusion/` path;
3. machine-readable reproducibility diagnostics/manifest under a versioned `research/fusion/` path;
4. any minimal regression test required to verify that the committed artifact reproduces F2.6 `0_3` structural diagnostics.

Update `research/fusion/STATUS.md`, commit result + STATUS, and STOP / RETURN TO MASTER.

Expected return is exactly one of:

- `F2.6A PASS — CANONICAL MATRIX-FREE OPERATOR ARTIFACT FROZEN — RETURN TO MASTER`;
- `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER`;
- `F2.6A FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.
