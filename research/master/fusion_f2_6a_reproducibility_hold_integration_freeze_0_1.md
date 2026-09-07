# Fusion F2.6A Reproducibility HOLD Integration Freeze 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Status:** `STABLE — F2.6A HOLD INTEGRATED / F2.6B SOURCE-LEVEL IMPLEMENTATION REQUALIFICATION RELEASED`

## Scope

This freeze integrates only the completed

`Fusion F2.6A — Canonical Matrix-Free Operator Artifact / Reproducibility Freeze 0.1`.

Canonical branch result:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

Machine-readable manifest:

`research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_manifest_0_1.json`

Branch verdict:

\[
\boxed{\text{F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER}.}
\]

Branch commit:

`1ac71cd2ad0d5e9c7388c5b21229629484323aa2`

Python CI #426 = `SUCCESS`.

## Integrated factual result

F2.6A confirms that the canonical repository and the historical F2.6 `0_3` CI provenance do not contain a recoverable source-level or serialized realization sufficient to prove exact identity of the previously qualified matrix-free maps

\[
x\mapsto E_Kx,\qquad x\mapsto F_Kx,\qquad x\mapsto E_K^{-1}x
\]

on K0/K1/K2.

The available F2.6 `0_3` report and diagnostics freeze the abstract factorization and structural residuals, but do not uniquely determine the coefficient-level implementation. Missing canonical provenance includes the exact weak/SBP streaming--mirror assembly, trapped-electron orbit projection maps, complete level-wise `D_K/S_K/C_K/R_K` factors and state layouts, the full source-level `F_K` action, and the exact probe/index realization used to bind the diagnostics to one implementation.

GitHub Actions run #412 checked out the F2.6 `0_3` PASS commit and completed the generic test suite (`210 passed`) but published no workflow artifacts. Thus no hidden operator builder or serialized factor archive can be recovered from that run.

F2.6A correctly committed no substitute `apply_E/apply_F/solve_E` implementation. Reconstructing one from prose and calling it the historical F2.6 `0_3` operator would violate the exact-equivalence requirement.

## Interpretation boundary

This HOLD is a **numerical provenance / reproducibility limitation**. It does not revoke the scientific or algebraic conclusions frozen in F2.6 `0_3`.

In particular, the F2.6 `0_3` local-B FLR qualification, quasineutrality, positive Helmholtz metric, conservative phase-space structure, independently reconstructed physical channels, ambipolarity and complete discrete free-energy balance remain historical qualified results.

However, those historical diagnostics alone are not sufficient to instantiate a uniquely identified operator for spectral work. F2.7 therefore remains spectrally indeterminate and blocked.

## MASTER provenance decision

MASTER chooses the second provenance-clean path identified by F2.6A for the canonical project continuation:

\[
\boxed{\text{F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1}.}
\]

Reason: no original F2.6 `0_3` builder or exact serialized factor set is present in the canonical repository or recoverable CI artifacts. MASTER therefore will not claim historical source-level identity that cannot be demonstrated.

F2.6B is a **new versioned numerical implementation freeze**, not a reconstruction labeled as the historical F2.6 `0_3` implementation. It must implement the already-frozen F2-R equations and numerical architecture, explicitly freeze every source-level choice previously left implicit, publish a reproducible matrix-free interface, and then rerun the complete pre-spectral algebraic qualification on that implementation.

## F2.6B frozen upstream boundary

F2.6B may not alter:

- F2.1 reduced two-species physics or the physical particle / ion-heat / trapped-electron-heat channel definitions;
- F2.2 magnetic geometry, signs, trapping/bounce conventions or local gyroaverage;
- F2.3 physical benchmark point or normalization;
- F2.4 admissible input geometry and input cost;
- the MASTER local-B ion-FLR convention;
- the F2.5 structure-preserving representation family, ballooning windows/basis, ion Hermite representation, trapped-electron representation, bounce quadrature or quasineutrality treatment;
- the F2.5R repaired ion magnetic-moment ladder
  \[
  N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.
  \]

The only newly authorized work is to make the previously implicit coefficient-level implementation choices explicit, source-controlled and reproducible while respecting all frozen structural constraints.

## Required F2.6B deliverables

F2.6B must provide a versioned source-level builder or equivalent deterministic factor-generation package that exposes, for each K0/K1/K2 level,

\[
\boxed{\operatorname{apply\_E}(x),\quad \operatorname{apply\_F}(x),\quad \operatorname{solve\_E}(x)}
\]

and fixes at minimum:

1. exact state layout and coefficient ordering;
2. exact weak/SBP streaming-plus-mirror split/skew assembly;
3. exact trapped-electron orbit/bounce projection maps;
4. exact level-wise quasineutrality and field-coupling factors `D_K,S_K,C_K,R_K` or deterministic constructors for them;
5. exact drift and gradient-drive implementation defining `F_K`;
6. exact physical-channel reconstruction implementation;
7. deterministic regression seeds/signatures sufficient to reproduce the implementation and its structural diagnostics.

The implementation must then rerun the complete F2.6 algebraic qualification, including full-support FLR, quasineutrality, positive/Hermitian canonical metric, `B_K=I`, `R_in,K=M_K`, conservative adjoint/skew structure, independently reconstructed Hermitian transport channels, ambipolarity and the complete F2.1 discrete balance.

Passing requires both source-level reproducibility and algebraic qualification on K0/K1/K2. Structural agreement may not be achieved by fitting terms backwards from the balance identity.

## Anti-bias / pre-spectral boundary

F2.6B remains strictly pre-spectral and pre-effect. It may not inspect or compute eigenvalues, Ritz pairs, spectral abscissae, growth rates, pseudospectra, propagators, Gramians, cumulative objectives, optimizers, principal angles, performance gaps or horizon dependence.

No physical-parameter scan, resolution outside frozen K0/K1/K2, GENE run, collision/damping addition or upstream retuning is authorized.

Implementation decisions must be justified from the frozen equations, representation, discrete conservation/adjoint requirements and reproducibility needs only; spectral or finite-time outcomes may not guide them.

## Consequence for F2.7

F2.7 remains blocked. Only after `F2.6B PASS` and MASTER integration may a new versioned F2.7 rerun be released against the newly frozen executable operator implementation.

The historical F2.6 `0_3` PASS remains an audit/qualification result; the future spectral calculation must use the F2.6B-qualified implementation, not an unverifiable claim of source identity with the historical realization.

Canonical handoff:

`research/master/prompts/fusion_f2_6b_source_level_operator_implementation_requalification_gate_0_1.md`

## Rollback / STOP

This integration freeze is a new protected post-paper savepoint. F2.7 HOLD, F2.6 `0_3` PASS, F2.5R and the historical F2.5/F2.6 failure lineage remain preserved.

Do not resume F2.7, inspect spectra or finite-time effects, retune frozen physics/numerics, or open parked/protected branches.

**STOP — F2.6A HOLD INTEGRATED / F2.6B MAY PROCEED ONLY THROUGH THE COMMITTED HANDOFF.**
