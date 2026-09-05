# Fusion F2.2 — Local Magnetic-Geometry Family / Kinetic Convention Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Freeze one source-faithful local toroidal magnetic-geometry family and all continuous geometric/phase-space conventions required by the already-frozen F2-R candidate

\[
\boxed{
\text{finite-ion-FLR local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

before any physical parameter point, phase-space discretization, kinetic input geometry, numerical qualification, GENE execution or finite-time objective calculation is opened.

This gate is **pre-effect**. Selection must use physical/source fidelity, transparent trapped-particle structure, analytical/numerical tractability and compatibility with later fully kinetic local-GK/GENE mapping only.

## Canonical inputs

Read and preserve:

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`;
- `research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`;
- the shared MASTER Prompt Handoff Protocol.

R1 remains a frozen structural no-go control and must not be modified.

## Required work

Using source-supported gyrokinetic geometry only, select exactly one local toroidal geometry **family/convention package** for the primary reduced F2-R lineage. A standard large-aspect-ratio circular-concentric / s-alpha / Cyclone-Base-Case-compatible local tokamak geometry is the leading candidate only if it is genuinely consistent with the F2-R source equations and trapped-electron bounce-average structure. If not, return `HOLD` with the exact reason rather than substituting an effect-motivated model.

Freeze and document explicitly:

1. magnetic coordinates and orientation: `psi`, `alpha`, parallel coordinate (`l`, `theta` or equivalent), outward radial sign, field-line orientation and Fourier/ballooning convention;
2. the analytic geometry family: `B(theta)` or equivalent, metric/Jacobian factors needed for the linear GK equations, and the source-consistent relationship between `dl` and the chosen angular coordinate;
3. `k_perp(theta)` construction, including the role and sign conventions of magnetic shear, ballooning/radial wavenumber and binormal wavenumber;
4. ion and electron magnetic-drift frequency conventions, including curvature and grad-B contributions and the sign of `omega_da` relative to the Fourier convention;
5. trapped/passing classification in terms of pitch angle and `B(theta)`, bounce points, trapping wells and well labels;
6. the exact bounce-average measure used for trapped electrons and how multiple wells would be handled;
7. the electron slow-transit ordering and `k_perp rho_e << 1` convention already required by F2.1, checked against the selected geometry;
8. the geometry parameters that remain symbolic in F2.2 and must be assigned numerically only in the later physical-parameter freeze;
9. the mapping targets needed later for a fully kinetic local-GK/GENE-compatible reference, without running GENE;
10. any boundary, periodicity, parity or ballooning-space conventions that must be fixed before phase-space discretization.

The result must clearly distinguish:

- **frozen geometry family/conventions**;
- **still-unfrozen numerical geometry parameters** (e.g. values of aspect ratio, `q`, magnetic shear, ballooning angle, wavenumbers if not logically part of the family definition);
- **later discretization choices**.

## Anti-bias and forbidden work

Do **not**:

- choose between geometry families by spectral stability, nonnormality, transient growth, optimizer separation or expected heat-flux effect;
- freeze density/temperature gradients or transport-drive amplitudes in this gate unless a value is mathematically inseparable from the geometry definition;
- scan `q`, shear, aspect ratio, trapped fraction, `k_y`, `k_x`, ballooning angle or any other geometry/wavenumber parameter;
- discretize `l`, velocity, energy, pitch angle or well coordinates;
- define or optimize kinetic `B` or `R_in`;
- construct discrete `A`, `M`, `Q`, propagators, Gramians, cumulative objectives, optimizer directions, angles or performance gaps;
- run GENE or another GK solver;
- add collisions to the reduced F2-R candidate;
- reopen R1, FLR-only rescue, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Required output

Create:

`research/fusion/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

Update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.2 PASS — LOCAL MAGNETIC-GEOMETRY / KINETIC CONVENTIONS FROZEN — RETURN TO MASTER`;
- `F2.2 HOLD — SPECIFIC GEOMETRY/SOURCE DECISION REQUIRED — RETURN TO MASTER`;
- `F2.2 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected next MASTER decision after PASS

If F2.2 passes, MASTER should decide whether the next pre-effect gate is the single physical geometry/gradient/wavenumber parameter freeze or whether a narrower geometry-parameter gate is required first. The Fusion branch must not decide this itself.

**STOP / RETURN TO MASTER AFTER F2.2.**
