# Fusion F2.7 — Numerical / Spectral Qualification Gate 0.1

**Date:** 2026-09-07  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Qualify the modal/spectral regime and numerical robustness of the already algebraically qualified F2-R discrete operators **before any finite-time propagator or objective calculation is permitted**.

This is a spectral-regime gate, not a finite-time effect gate.

## Mandatory controlling inputs

Read and preserve:

- `research/master/fusion_f2_6_discrete_algebra_pass_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_qualification_gate_0_3.md`;
- `research/fusion/fusion_f2_6_discrete_operator_channel_algebraic_diagnostics_0_3.json`;
- `research/master/fusion_f2_5r_quadrature_repair_integration_freeze_0_1.md`;
- `research/master/fusion_f2_6_ion_flr_convention_erratum_0_1.md`;
- F2.1–F2.4 integration freezes;
- the shared MASTER Prompt Handoff Protocol.

Use exactly the repaired K0/K1/K2 ladder with

\[
N_{\mu,K0}=16,\qquad N_{\mu,K1}=24,\qquad N_{\mu,K2}=40.
\]

No physical or numerical retuning is allowed.

## Frozen operator form

Use the F2.6-qualified matrix-free factorization

\[
E_K\dot x_K=F_Kx_K,
\qquad
A_K=E_K^{-1}F_K,
\]

with the already qualified canonical metric `M_K`, quasineutrality reconstruction, and repaired discrete state spaces. Do not replace this operator by a differently regularized or projected one.

## Required qualification

For K0/K1/K2:

1. determine the rightmost modal spectrum sufficiently to classify the spectral abscissa
   \[
   \alpha_K=\max\operatorname{Re}\sigma(A_K),
   \]
   using reproducible matrix-free sparse/generalized eigensolver methods appropriate to the qualified dimensions;
2. report every retained rightmost eigenvalue used in the classification, its residual norm, solver tolerance, iteration/convergence information and the number of requested/converged Ritz pairs;
3. repeat the rightmost calculation with at least one independent numerical configuration (for example a different Krylov dimension/shift/start vector) to demonstrate that the reported spectral edge is not a single-run artifact;
4. compare the rightmost spectral structure across K0/K1/K2 and state whether the stability classification is robust under the frozen refinement ladder;
5. report conditioning diagnostics relevant to the generalized/matrix-free spectral solve, including the already factorized `E_K`/quasineutrality solves and any shift-invert linear systems actually used;
6. where a converged left/right eigenpair is available, report a standard eigenvalue condition/sensitivity indicator, but do not reinterpret it as a transport optimizer;
7. distinguish clearly between:
   - `spectrally stable`: robustly `alpha_K<0` beyond numerical uncertainty;
   - `marginal/indeterminate`: the spectral edge is numerically consistent with zero or not robustly resolved;
   - `spectrally unstable`: robustly `alpha_K>0` beyond numerical uncertainty.

A full dense spectrum is **not** required at K1/K2 and should not be attempted merely for completeness. The gate must instead provide a defensible rightmost-spectrum classification with residual certification and K0/K1/K2 robustness. If a complete spectrum happens to be computationally practical at a smaller level, it may be reported, but it is not necessary for PASS.

## Spectral qualification boundaries

A spectrally unstable frozen point is not automatically a discretization failure. If the rightmost spectrum is robustly unstable while all F2.6 algebra remains intact, return a qualified unstable-regime result to MASTER. Do **not** add damping, collisions, filters or search for a stable point.

If the spectral edge is marginal or solver convergence does not support a reliable sign classification, return HOLD with the exact unresolved numerical object.

If the spectrum reveals a new inconsistency that invalidates the already qualified operator representation itself, return FAIL and identify the specific inconsistency. Do not repair it silently.

## Explicitly forbidden work

Do **not**:

- compute `exp(A_K t)` or any time propagator;
- construct Gramians, cumulative channel operators or finite-time energy operators;
- compute energy-, particle- or heat-optimal initial conditions;
- compute principal angles, performance gaps, horizon dependence or transient amplification curves;
- scan physical parameters, gradients, wavenumbers, ballooning angles, input subspaces or resolutions outside K0/K1/K2;
- alter F2.3/F2.4/F2.5R or the local-B FLR convention;
- add collisions, damping, hypercollision, diffusion, filtering, absorbing layers or metric regularization;
- run GENE or another external GK solver;
- reopen R1, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

Do not use a pseudospectral scan as a substitute for the requested spectral-edge qualification unless a specific convergence ambiguity requires a small local diagnostic; if that occurs, document it narrowly and do not turn F2.7 into a nonmodal analysis.

## Required output

Create:

`research/fusion/fusion_f2_7_numerical_spectral_qualification_gate_0_1.md`

Store machine-readable spectral diagnostics under `research/fusion/` with a clearly versioned F2.7 filename.

Update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.7 PASS — SPECTRALLY STABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 PASS — SPECTRALLY UNSTABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`;
- `F2.7 HOLD — MARGINAL OR SPECTRALLY INDETERMINATE — RETURN TO MASTER`;
- `F2.7 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected MASTER decision after return

After F2.7, MASTER must explicitly accept or reject the qualified spectral regime before any finite-time pilot specification. If the point is stable, the next likely dependency is the targeted exact-question Fusion literature/positioning audit followed by a pre-effect pilot specification. If the point is unstable, MASTER must first decide whether an unstable-regime finite-time transport-optimality study is scientifically appropriate for this post-paper Fusion lineage.

**STOP / RETURN TO MASTER AFTER F2.7.**
