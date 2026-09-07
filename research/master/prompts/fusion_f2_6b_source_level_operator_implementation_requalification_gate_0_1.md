# MASTER Handoff — Fusion F2.6B Source-Level Operator Implementation Freeze / Algebraic Requalification Gate 0.1

**Date:** 2026-09-07  
**Target chat:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`  
**Authority:** MASTER  
**Status:** `ACTIVE HANDOFF`

## Objective

Create and freeze a **new versioned, source-level, reproducible matrix-free implementation** of the already-frozen F2-R discrete model, then rerun the complete pre-spectral algebraic qualification on that implementation.

This is not an attempt to claim exact source identity with the historical F2.6 `0_3` realization. F2.6A established that such historical identity cannot be proven from canonical provenance.

The new gate is

\[
\boxed{\text{F2.6B — Source-Level Matrix-Free Operator Implementation Freeze / Algebraic Requalification Gate 0.1}.}
\]

## Read first

Before doing any work, read:

1. `research/fusion/STATUS.md`;
2. `research/master/fusion_f2_6a_reproducibility_hold_integration_freeze_0_1.md`;
3. `research/fusion/fusion_f2_6a_canonical_operator_artifact_reproducibility_gate_0_1.md`;
4. `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`;
5. `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`;
6. `research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`;
7. `research/fusion/fusion_f2_5_structure_preserving_discretization_specification_freeze_0_1.md`;
8. `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`;
9. `research/master/prompt_handoff_protocol_0_1.md`.

## Frozen upstream objects — do not change

Preserve exactly:

- F2.1 reduced two-species physical model and physical transport-channel definitions;
- F2.2 local tokamak / `s-alpha` geometry, Fourier signs, drift signs, trapping and bounce conventions;
- F2.3 physical benchmark point and normalization;
- F2.4 continuous input geometry/input cost;
- MASTER local-B ion-FLR convention;
- F2.5 representation family, K0/K1/K2 ballooning windows, theta elements/LGL basis, compact-support treatment, ion Hermite representation, trapped-electron representation, bounce quadrature and quasineutrality treatment;
- F2.5R repaired ion Gauss--Laguerre orders
  \[
  \boxed{N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.}
  \]

Do not retune any physical parameter, wavenumber, gradient, input subspace, channel or resolution ladder.

## Authorized new work

You may now make explicit and freeze the source-level implementation choices that were not historically serialized. These choices must be derived only from the frozen equations, representation and structure-preserving requirements, not from any spectral or finite-time outcome.

At minimum freeze and implement:

1. exact K-level state vector layout, species blocks, coefficient ordering and index maps;
2. exact LGL/SBP derivative, mass and interface assembly used by the ion parallel-streaming plus mirror term;
3. exact split/skew weak form and boundary treatment consistent with the frozen compact-support specification;
4. exact ion magnetic-drift action;
5. exact trapped-electron regularized bounce/orbit projection from field basis to orbit quadrature and back to state;
6. exact quasineutrality factors/constructors `D_K`, `S_K`, `C_K`, `R_K`, field reconstruction and low-rank `E_K^{-1}` solve;
7. exact gradient-drive/source-free action defining `F_K` with all signs/normalizations documented;
8. exact independently constructed physical quadratic channel implementations `Q_Gamma,K`, `Q_qi,K`, `Q_qe,K`;
9. stable public matrix-free interfaces equivalent to
   `apply_E(level,x)`, `apply_F(level,x)`, `solve_E(level,x)`;
10. deterministic probe seeds, regression signatures/hashes and enough metadata to reproduce every qualified K0/K1/K2 result without relying on prose reconstruction.

Prefer source-controlled deterministic constructors over huge serialized dense arrays. Sparse/factorized/matrix-free representations are expected.

## Required algebraic requalification

On the new source-level implementation, rerun the complete F2.6 pre-spectral qualification on K0/K1/K2. Required checks include:

- repaired full-support local-B FLR identity on active nodes and independent between-node envelope;
- Maxwellian moments / positive quadrature weights;
- quasineutrality residuals;
- canonical positive Helmholtz metric construction, Hermiticity and strict positivity without loading/clipping/nullspace deletion;
- `B_K=I`, `R_in,K=M_K`;
- ion streaming/mirror adjoint/skew structure;
- complete source-free conservative phase-space adjoint/skew structure;
- independent physical-channel reconstruction and Hermiticity;
- hydrogenic particle ambipolarity;
- complete F2.1 discrete balance
  \[
  A_K^\dagger M_K+M_KA_K
  =2\left(G_\Gamma Q_{\Gamma,K}+G_{T,i}Q_{q_i,K}+G_{T,e}Q_{q_e,K}\right),
  \]
  with the physical channels constructed before and independently of this comparison;
- a deterministic structural convergence/regression diagnostic across K0/K1/K2;
- exact reproducibility of the new implementation from committed source and metadata.

Do **not** force numerical values to match historical F2.6 `0_3` residuals exactly. The new implementation is a new versioned realization. It must instead satisfy the same frozen algebraic/physical requirements at defensible roundoff/quadrature accuracy. Any material discrepancy from the historical qualified behavior must be reported, not hidden.

## Mandatory implementation artifact

Commit a canonical executable implementation sufficient for later spectral work. It must expose the exact matrix-free generalized operator used in the requalification and must not require re-deriving numerical choices from prose.

Also commit machine-readable diagnostics containing at least:

- version/gate identifier;
- K-level dimensions/order metadata;
- source/artifact paths and hashes if practical;
- interface names;
- state-layout metadata;
- all structural residuals and tolerances;
- deterministic seeds/probe policy;
- algebraic verdict per K level;
- explicit flags confirming that no spectral or finite-time work was performed.

## Forbidden

Do not compute or inspect:

- eigenvalues/eigenvectors;
- Ritz values or spectral abscissa;
- growth rates or pseudospectra;
- matrix exponentials, propagators or Gramians;
- cumulative particle/heat/energy objectives;
- finite-time optimizers, principal angles or performance gaps;
- horizon curves.

Also forbidden:

- physical-parameter/wavenumber/input-subspace scans;
- resolutions outside frozen repaired K0/K1/K2;
- GENE;
- collisions, damping, filtering, hypercollision, artificial viscosity or absorbing layers;
- retuning F2.3/F2.4/F2.5R;
- changes to the physical channel definitions;
- reopening R1, MODES, CONT, CASCADE, CORE 0.2, Power Grid, Photonics or Paper-1 work.

## Decision discipline

If a source-level implementation choice is genuinely underdetermined by the frozen physics/numerical specifications and cannot be selected from structure-preserving/reproducibility criteria alone, return HOLD and name the exact choice required. Do not use spectral expectations or desired transport behavior to decide it.

If the new implementation cannot satisfy the full algebraic qualification without changing frozen upstream objects, return FAIL. Do not repair by retuning.

## Required outputs

Create versioned `0_1` F2.6B outputs, including:

- a canonical report under `research/fusion/`;
- the executable source-level operator implementation under `research/fusion/` or the repository's established research-code location;
- machine-readable diagnostics/manifest;
- any focused tests needed for regression/reproducibility;
- updated `research/fusion/STATUS.md`.

Do not overwrite F2.6 `0_1`, `0_2`, `0_3`, F2.6A or F2.5R historical artifacts.

## Expected return

Exactly one of:

- `F2.6B PASS — SOURCE-LEVEL MATRIX-FREE OPERATOR IMPLEMENTATION FROZEN / ALGEBRA REQUALIFIED — RETURN TO MASTER`;
- `F2.6B HOLD — SPECIFIC SOURCE-LEVEL IMPLEMENTATION DECISION REQUIRED — RETURN TO MASTER`;
- `F2.6B FAIL — RETURN TO MASTER`.

After completing the assigned work, commit result + updated Fusion STATUS, report the canonical paths and commit hash, then STOP / RETURN TO MASTER.

No branch-side next gate is self-authorized.
