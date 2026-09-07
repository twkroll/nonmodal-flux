# Fusion F2.7 HOLD / Canonical Operator-Artifact Integration Freeze 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Status:** `STABLE — F2.7 HOLD INTEGRATED / F2.6A OPERATOR-ARTIFACT REPRODUCIBILITY REPAIR RELEASED`

## Scope

This freeze integrates only the completed

`Fusion F2.7 — Numerical / Spectral Qualification Gate 0.1`.

Canonical branch result:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

Machine-readable diagnostics:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_diagnostics_0_1.json`

Branch verdict:

\[
\boxed{\text{F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER}.}
\]

Branch commit:

`e4453080cae805a4e50d019975f6722130e88903`

Python CI #419 = `SUCCESS`.

## Integrated factual result

F2.7 did not run an eigensolver and did not classify the frozen F2-R point as stable or unstable. The blocker is reproducibility, not physics and not spectral evidence:

\[
\boxed{\text{no canonical executable/serialized F2.6 `0_3` realization of }(E_K,F_K).}
\]

The repository contains the qualified F2.6 `0_3` report and diagnostics, but not a versioned numerical artifact sufficient to instantiate without new choices

\[
x\mapsto E_Kx,\qquad x\mapsto F_Kx,\qquad x\mapsto E_K^{-1}x
\]

on K0/K1/K2.

Therefore the spectral regime remains indeterminate. No conclusion from F2.6 `0_3` is revoked: its local-B FLR, quasineutrality, positive Helmholtz metric, conservative phase-space structure, independently reconstructed physical channels, ambipolarity and complete discrete free-energy balance remain frozen as qualified.

## Interpretation boundary

This HOLD is not evidence that the point is marginal. The phrase `marginal or spectrally indeterminate` is the gate's return class; the present case is specifically **spectrally indeterminate because the exact qualified operator is not canonically executable**.

No benchmark expectation, free-energy balance or newly reconstructed substitute operator may be used to infer the sign of the spectral abscissa.

## MASTER repair decision

MASTER releases one narrow reproducibility gate:

\[
\boxed{\text{F2.6A — Canonical Matrix-Free Operator Artifact / Reproducibility Freeze 0.1}.}
\]

Its only purpose is to publish and freeze a versioned executable matrix-free realization, or an equivalent serialized factor set, for the already-qualified F2.6 `0_3` maps `E_K`, `F_K` and `E_K^{-1}` on K0/K1/K2.

The artifact must reproduce the already-frozen F2.6 `0_3` structural diagnostics before it can PASS. It may not change F2.1–F2.5R, the local-B FLR convention, physical channels, quadrature ladder, weak/SBP form, bounce treatment, quasineutrality, input geometry or physical point.

If exact equivalence to the qualified F2.6 `0_3` construction cannot be established from canonical information, F2.6A must return `HOLD` with the unresolved implementation choices. It may not invent a replacement operator and call it canonical.

No eigenvalue, Ritz pair, growth rate, pseudospectrum, propagator, Gramian, cumulative objective, optimizer, angle, performance gap, parameter scan or GENE run is authorized in F2.6A.

## Consequence for F2.7

F2.7 is not re-released now. Only after F2.6A PASS and MASTER integration may a versioned F2.7 rerun be released against the frozen executable operator artifact.

Canonical handoff:

`research/master/prompts/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`

## Rollback / STOP

This integration freeze is a new protected post-paper savepoint. F2.6 `0_3` PASS, F2.5R and the entire historical F2.5/F2.6 failure lineage remain preserved.

Do not inspect spectra or finite-time effects; do not retune the model or repaired discretization; do not open MODES/CONT/CASCADE or protected branches.

**STOP — F2.7 HOLD INTEGRATED / F2.6A REPRODUCIBILITY REPAIR MAY PROCEED ONLY THROUGH THE COMMITTED HANDOFF.**
