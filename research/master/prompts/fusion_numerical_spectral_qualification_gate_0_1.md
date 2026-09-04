# Fusion F1.4 — Numerical / Spectral Qualification Gate 0.1

**Date:** 2026-09-04  
**Authority:** MASTER  
**Branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Qualify exactly the frozen F1.3 anisotropic-ZLR four-moment R1 minimal-curvature candidate at the frozen CBC-projected parameter point, before any finite-time free-energy-versus-heat objective inspection.

Canonical inputs:

- `research/fusion/fusion_candidate_convention_freeze_0_1.md`
- `research/fusion/B5_4B_curvature_free_energy_check.md`
- `research/fusion/B5_5_ion_heat_flux_observable.md`
- `research/fusion/fusion_admissible_input_geometry_input_cost_gate_0_1.md`
- `research/master/fusion_f1_3_candidate_convention_integration_freeze_0_1.md`

## Absolute prohibitions

Do **not** change the frozen candidate, parameter point, state ordering, closure, curvature sign, parallel wavenumber, gradient convention, `M_k`, `Q_{q_i,k}`, `B`, or `R_in`.

Do **not** add damping, viscosity/diffusion, collisions, Landau-fluid terms or any other spectral rescue. Do not scan parameters or wavenumbers.

Do **not** construct or inspect finite-time energy/heat propagator objectives, cumulative channel operators, Gramians for objective optimization, optimizer vectors/subspaces, principal angles, performance gaps, horizon dependence, transient-growth curves or effect sizes.

Do not restore FLR/R2, kinetic electrons, six-moment GEM or GENE. Do not open MODES/CONT/CASCADE or protected collaboration branches. Do not modify Paper 1.

## Frozen point

Use exactly

\[
\tau_i=1,
\quad R_0/L_n=2.2,
\quad R_0/L_T=6.9,
\quad q=1.4,
\quad k_x\rho_i=0,
\quad k_y\rho_i=0.3,
\quad \tau_{\rm ref}=R_0/c_s.
\]

Use the minimal-curvature generator as primary and the slab generator only as an analytic `omega_d -> 0` implementation control. Do not compare their later objective effects.

## Required qualification checks

1. **Exact numerical reconstruction.** Construct the dimensionless frozen matrices at the single frozen point, preferably with
   \[
   \widetilde A=\tau_{\rm ref}A,
   \qquad
   \widehat Q_q=Q_{q_i,k}/(p_0c_s),
   \]
   together with `M_k`, `B=I_4`, `R_in=M_k`. Record the numerical matrices and all dimensionless coefficients used.

2. **Algebraic structure.** Verify numerically to a stated tolerance:
   \[
   M_k=M_k^\dagger\succ0,
   \qquad
   Q_{q_i,k}=Q_{q_i,k}^\dagger,
   \]
   `rank(Q_q)=2`, signature `(1,1,2)`, `rank(B)=4`, and `R_in=M_k\succ0`.

3. **Free-energy balance identity.** In dimensionless form verify the frozen identity
   \[
   \widetilde A^\dagger M_k+M_k\widetilde A
   =2\frac{R_0}{L_T}\,\widehat Q_q,
   \]
   with the frozen sign conventions. Also verify that the source-free/minimal-curvature part is `M_k`-skew-adjoint to numerical precision when the equilibrium gradients are removed, as established in B5.4B.

4. **Physical heat-channel reconstruction.** For a small deterministic set of non-optimized test states, verify that `z^dagger Q_q z` agrees with the independently frozen cross-phase expression for the radial ion heat flux. This is an implementation check only; do not search over states.

5. **Coordinate consistency.** Optionally but preferably reconstruct the same metric/channel in the temperature-coordinate basis `(N,U,Theta_parallel,Theta_perp)` and verify congruence/inertia and equality of physical quadratic values. No reduced projection is allowed.

6. **Complete spectrum at the frozen point.** Compute and report all eigenvalues of the exact frozen primary `A` (or `A_tilde`), the spectral abscissa
   \[
   \alpha(A)=\max_j\Re\lambda_j,
   \]
   and a clearly defined numerical tolerance for classifying stable/marginal/unstable. Do not omit unstable eigenvalues and do not modify the model if they occur.

7. **Numerical conditioning.** Report condition numbers relevant to reliable implementation (`M_k`, whitening factor if used only for conditioning, and eigenvector basis if diagonalizable). Nonnormality may be reported descriptively only; do not compute transient-growth objectives.

8. **Independent reproduction.** Where practical, reproduce the matrix identities and spectrum using a second numerical path or higher precision/direct symbolic evaluation. This is a numerical audit, not a resolution or parameter scan.

## Spectral decision rule

Use a documented tolerance, for example a scale-aware threshold based on machine precision and `||A_tilde||`.

- If `alpha(A)` is clearly negative and all structural checks pass: `F1.4 PASS — SPECTRALLY STABLE / NUMERICALLY QUALIFIED — RETURN TO MASTER`.
- If `alpha(A)` is numerically marginal: `F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER`.
- If `alpha(A)` is clearly positive: `F1.4 HOLD — SPECTRALLY UNSTABLE FROZEN POINT — RETURN TO MASTER`.
- If matrix identities, physical reconstruction or conditioning fail materially: `F1.4 FAIL — RETURN TO MASTER`.

A `HOLD` due to instability is **not** permission to add damping or choose another parameter point. MASTER must decide the scientific regime explicitly.

## Canonical outputs

Write the full result to

`research/fusion/fusion_numerical_spectral_qualification_gate_0_1.md`

including scope, exact frozen inputs, numerical matrices, tolerances, all required checks, spectrum, conditioning, PASS/HOLD/FAIL verdict, allowed/forbidden interpretations and final STOP.

If code/tests are needed, commit transparent source/test files that execute only this qualification and contain assertions against parameter/horizon scanning and finite-time objective construction where practical.

Update `research/fusion/STATUS.md` to `RETURN TO MASTER`, commit result + STATUS (+ tests/code if any), report canonical path, full commit hash and CI status, then STOP.

**STOP after the F1.4 qualification. Do not self-authorize the literature audit, pilot specification or any finite-time execution.**