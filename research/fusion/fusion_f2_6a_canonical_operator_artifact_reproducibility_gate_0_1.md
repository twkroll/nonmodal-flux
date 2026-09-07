# Fusion F2.6A — Canonical Matrix-Free Operator Artifact / Reproducibility Freeze 0.1

**Date:** 2026-09-07  
**Authority:** MASTER / `research/master/prompts/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`  
**Status:** `F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER`

## Executive verdict

F2.6A cannot publish an executable matrix-free artifact and claim exact equivalence to the already-qualified F2.6 `0_3` operator from the current canonical repository state.

The required target is

\[
E_K\dot x_K=F_Kx_K,
\qquad
A_K=E_K^{-1}F_K,
\]

on K0/K1/K2 with the frozen repaired ladder

\[
\boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
\]

The canonical F2.6 `0_3` report and diagnostics specify and qualify the operator structure, but they do not contain a source-level implementation or serialized factor set sufficient to reproduce the exact numerical maps

\[
x\mapsto E_Kx,\qquad x\mapsto F_Kx,\qquad x\mapsto E_K^{-1}x
\]

without making additional implementation choices.

Creating a new builder from the prose would therefore be a new implementation, not a reproducibility freeze of the exact previously qualified realization. The controlling handoff explicitly forbids that substitution.

\[
\boxed{\text{F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER}.}
\]

## 1. Frozen upstream lineage preserved

No F2.1–F2.5R object is changed. In particular, the F2-R physical model, F2.3 point, F2.4 input geometry, local-\(B\) ion-FLR convention, K0/K1/K2 windows and bases, trapped-electron treatment, quasineutrality treatment, weak/SBP design constraint and repaired magnetic-moment ladder remain frozen.

F2.6 `0_3` remains a qualified algebraic result. F2.6A does not revoke its PASS conclusion.

F2.7 `0_1` remains spectrally indeterminate because no eigensolver may be run against a substitute operator.

## 2. Canonical F2.6 `0_3` information that is available

The repository canonically contains:

- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`;
- `research/master/fusion_f2_6_discrete_algebra_pass_integration_freeze_0_1.md`;
- the F2.5/F2.5R numerical specification and repair artifacts.

The qualified factorized relations include

\[
C_K\phi_K=S_Kx_K,
\qquad
P_K=C_K^{-1}S_K,
\]

\[
R_K=D_K^{-1}S_K^\dagger,
\qquad
E_K=I-R_KC_K^{-1}S_K,
\]

and

\[
E_K^{-1}y
=
y+R_K(C_K-S_KR_K)^{-1}S_Ky.
\]

The diagnostics also freeze level dimensions, probe seeds, structural residuals and the PASS-scale values for FLR, quasineutrality, positive metric, channel Hermiticity, ambipolarity and complete free-energy balance.

These data constrain the realization strongly but do not uniquely identify the complete numerical operator.

## 3. Missing exact numerical objects

The following concrete objects are not canonically serialized or implemented for F2.6 `0_3`:

1. the exact K0/K1/K2 coefficient-level weak/SBP ion streaming-plus-mirror action, including its precise split/skew assembly and coefficient ordering;
2. the full trapped-electron bounce/orbit projection matrices mapping the regularized `chi` quadrature to the ballooning-field basis and back to the electron state;
3. the concrete numerical `D_K`, `S_K`, `C_K`, `R_K` and all level-specific sparse/index maps needed to reproduce the exact field and time-derivative coupling rather than merely their abstract factorization;
4. the complete coefficient-level source-free drift and gradient-drive action defining `F_K`, including the exact layout and normalization used in the qualified realization;
5. the exact source-level random-probe construction and state indexing needed to reproduce the reported residual values as a regression signature of the same implementation.

The F2.5 freeze specifies the representation family and structural requirements, but its phrases such as split/skew weak/SBP assembly do not by themselves uniquely determine the source-level matrix entries. Multiple implementations can satisfy the same conservation identities and reported residual scales.

Therefore matching the existing structural diagnostics would be necessary but not sufficient to prove identity with the original F2.6 `0_3` realization.

## 4. Commit and CI audit

The F2.6 `0_3` branch commit is

`4db62c37d3465726be061dc7b49cbc3a81d87a55`.

Its canonical work package contains the report, machine-readable diagnostics and `STATUS.md`; it does not contain a versioned `0_3` operator source file or serialized operator factors.

GitHub Actions run #412 (`Python tests`) checked out exactly that commit and completed successfully with `210 passed`. The workflow published no artifacts. It therefore confirms repository consistency but does not recover the missing operator implementation.

No hidden CI-generated executable or factor archive is available from that run.

## 5. Why F2.6A does not create a substitute artifact

The F2.6A handoff requires exact equivalence before PASS. Reconstructing a plausible operator from the continuous equations and F2.5 prose would require choices about the concrete split weak form, orbit-to-field interpolation/projection, sparse indexing and normalization.

Those choices could produce an algebraically valid operator and might even reproduce the F2.6 structural tolerances. That would still not establish that it is the same numerical realization qualified in F2.6 `0_3`.

Accordingly no executable `apply_E` / `apply_F` / `solve_E` artifact is committed in this HOLD result. This is deliberate: publishing one would falsely canonize a newly reconstructed implementation as the historical F2.6 `0_3` operator.

## 6. Exact MASTER action required

To turn F2.6A into PASS, MASTER needs one of the following exact provenance objects:

- the original source-level builder used to generate the F2.6 `0_3` diagnostics; or
- a serialized level-wise factor set sufficient to instantiate the exact `E_K`, `F_K` and `E_K^{-1}` maps; or
- an independently preserved source snapshot whose hashes/probe outputs can be tied unambiguously to the F2.6 `0_3` diagnostics.

If no such provenance object exists, the scientifically clean alternative is not to call a reconstruction “F2.6 `0_3` exact.” MASTER would need to authorize a new versioned operator-implementation freeze, re-run the complete algebraic qualification on that implementation, and only then re-release spectral qualification.

## 7. Forbidden-work audit

F2.6A computed no eigenvalue, Ritz pair, spectral abscissa, growth rate, pseudospectrum or eigenvector. It constructed no propagator, matrix exponential, Gramian, cumulative objective, optimizer, angle, gap or horizon curve. It changed no physical parameter, channel, input space, repaired resolution or upstream numerical convention.

## Verdict

The canonical repository still lacks the provenance needed to prove exact source-level identity with the previously qualified numerical realization.

\[
\boxed{\text{F2.6A HOLD — EXACT OPERATOR EQUIVALENCE NOT ESTABLISHED — RETURN TO MASTER}.}
\]

**STOP / RETURN TO MASTER.**
