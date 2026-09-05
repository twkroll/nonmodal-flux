# Fusion F2.3 — Physical Geometry / Gradient / Wavenumber Parameter Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Execution branch:** `60 – FUSION – Gyrofluid/Gyrokinetic Transport`

## Objective

Freeze exactly one physically and source-supported numerical parameter point for the already-frozen F2-R architecture and F2.2 circular `s-alpha` geometry family, before any kinetic input optimization, phase-space discretization, spectrum or finite-time objective is inspected.

This is a strict **pre-effect single-point freeze**, not a scan.

## Canonical inputs

Read and preserve:

- `research/master/fusion_f2_1_two_species_gk_balance_integration_freeze_0_1.md`;
- `research/master/fusion_f2_2_geometry_convention_integration_freeze_0_1.md`;
- `research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`;
- `research/fusion/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`;
- `research/literature/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`;
- the shared MASTER Prompt Handoff Protocol.

R1 remains a frozen structural no-go control. F2-R remains collisionless with finite ion FLR and bounce-averaged trapped electrons; passing electrons remain adiabatic at leading order.

## Required work

Using source-supported benchmark conventions only, select **one** coherent numerical point for the frozen F2-R geometry and equilibrium. A Cyclone-Base-Case-compatible point is the leading benchmark family because F2.2 was deliberately made CBC-compatible, but it may be used only if the quantities required by the two-species trapped-electron model can be assigned without silently mixing incompatible benchmark definitions.

Freeze and document explicitly, in a common nondimensionalization:

1. geometry numbers required by F2.2, including at least `epsilon`, `q`, `shat`, and `alpha_MHD` or the exact justified equivalent;
2. equilibrium species choice and mass/charge convention, `T_i/T_e` or equivalent temperature ratio, and any normalization needed by the reduced equations;
3. density and ion/electron temperature-gradient coefficients, including which of `G_Gamma`, `G_Ti`, `G_Te` are nonzero at the frozen point and why;
4. one signed nonzonal binormal wavenumber and one radial/ballooning representative (`k_y` plus `k_x0` or `theta0`) in the F2.2 convention;
5. the time, length, velocity and gyroradius normalization required to interpret the reduced equations and later code mapping;
6. the implied trapped-particle interval/fraction information that follows from the frozen `epsilon` without treating it as an independently tuned knob;
7. checks that the point is compatible with the F2.1/F2.2 assumptions, especially finite ion FLR, nonzero trapped-electron measure, slow-electron-transit ordering at the level possible before spectral execution, and `k_perp rho_e << 1` as a model-ordering target;
8. a source table identifying which benchmark/reference supports each frozen numerical value or convention.

If a single source-supported benchmark does not provide a coherent two-species trapped-electron point, use the minimal documented benchmark extension only when each added value is independently standard and physically justified. Do not combine values merely to create multiple active source channels. If ambiguity remains scientifically material, return `HOLD` with the exact unresolved parameter rather than inventing a number.

## Anti-bias / forbidden work

Do **not**:

- scan or compare multiple numerical points by spectrum, growth rate, transient growth, nonnormality, transport magnitude, optimizer angle or performance gap;
- inspect any finite-time propagator, Gramian or cumulative objective;
- tune gradients, `q`, shear, `epsilon`, `alpha_MHD`, trapped fraction, `k_y`, `k_x`, `theta0`, temperature ratio or any other parameter to obtain stability or objective separation;
- discretize `theta`, ion velocity space, trapped-electron energy/pitch/well variables or bounce integrals;
- define or optimize kinetic `B` or `R_in`;
- construct discrete `A`, `M`, `Q` matrices or calculate eigenvalues;
- run GENE or another GK solver;
- add collisions to the reduced F2-R candidate;
- reopen R1, FLR-only rescue, MODES, CONT, CASCADE, Power Grid, Photonics or Paper-1 work.

## Required output

Create:

`research/fusion/fusion_f2_3_physical_parameter_freeze_0_1.md`

Update `research/fusion/STATUS.md` in the same work package.

Return exactly one of:

- `F2.3 PASS — PHYSICAL GEOMETRY/GRADIENT/WAVENUMBER POINT FROZEN — RETURN TO MASTER`;
- `F2.3 HOLD — SOURCE-SUPPORTED PARAMETER DECISION REQUIRED — RETURN TO MASTER`;
- `F2.3 FAIL — RETURN TO MASTER`.

No branch-side next gate is self-authorized.

## Expected next MASTER decision after PASS

If F2.3 passes, MASTER should next decide the kinetic admissible initial-condition geometry and physical input-cost metric before phase-space discretization. The Fusion branch must not open that gate itself.

**STOP / RETURN TO MASTER AFTER F2.3.**
