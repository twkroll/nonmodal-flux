# Fusion F2.2 Geometry / Kinetic-Convention Integration Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Status:** `STABLE — F2.2 GEOMETRY/CONVENTIONS FROZEN / F2.3 PHYSICAL PARAMETER FREEZE RELEASED`

## Scope

This MASTER freeze integrates only the completed `Fusion F2.2 — Local Magnetic-Geometry Family / Kinetic Convention Freeze 0.1`. It performs no parameter or wavenumber scan, no phase-space discretization, no kinetic-input optimization, no numerical/spectral calculation, no GENE execution, no finite-time objective calculation and no modification of the frozen first-paper content.

Canonical branch result:

`research/fusion/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

Branch verdict:

\[
\boxed{\text{F2.2 PASS — LOCAL MAGNETIC-GEOMETRY / KINETIC CONVENTIONS FROZEN — RETURN TO MASTER}}
\]

F2.2 branch commit:

`19dcf169ffe36c7b5f64f560f1f22294fa8ee239`

Python CI #355 = `SUCCESS`.

## Frozen geometry family

The primary reduced F2-R lineage now uses

\[
\boxed{
\text{large-aspect-ratio circular local tokamak}
+\hat s\text{-}\alpha_{\rm MHD}\text{ flux-tube geometry in ballooning space}
}
\]

with the already-frozen F2-R kinetic architecture

\[
\text{finite-ion-FLR local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}.
\]

The geometry family is a source-consistent specialization of the F2.1 general local toroidal flux tube and is selected for transparent trapped-particle structure, analytic tractability and later local-GK/GENE mapping, not for spectral or finite-time effect size.

## Frozen continuous conventions

F2.2 fixes, among other items:

- Clebsch orientation `B = grad psi x grad alpha`, outward `psi`, `l` along `B`;
- `theta=0` at the outboard midplane and infinite ballooning line `theta in R`;
- Fourier factor `exp[i(k_psi psi+k_alpha alpha)]` with `k_alpha != 0`;
- `B(theta)=B0/[1+epsilon cos(theta)]`;
- `dl/dtheta=q R0[1+epsilon cos(theta)]` and the corresponding spatial Jacobian;
- `Lambda(theta)=kx0/ky + shat theta - alpha_MHD sin(theta)` and `k_perp^2=ky^2[1+Lambda^2]`;
- the positive twist sign `kx(theta+2pi)-kx(theta)=+2pi shat ky`;
- signed magnetic drift `omega_da=k_perp dot v_da` entering as `+i omega_da g_a`, with curvature and grad-B pieces explicit;
- trapped/passing classification from `lambda B(theta)`, circular bounce points and the exact orbit-time bounce-average measure;
- trapped-electron well labeling, adiabatic leading passing electrons, finite ion FLR and `k_perp rho_e << 1` on the retained electron-support region;
- no parity reduction.

No numerical geometry or thermodynamic values are frozen by F2.2.

## Remaining pre-effect objects

The following still block any numerical or finite-time execution:

1. one physical geometry/gradient/wavenumber point;
2. kinetic admissible input map `B` and input cost `R_in`;
3. structure-preserving phase-space discretization and bounce/separatrix quadrature;
4. discrete reconstruction of the physical particle and ion/electron heat channels;
5. numerical/free-energy/spectral qualification;
6. later fully kinetic collisional-reference parameters and GENE-compatible normalization/diagnostic mapping.

## MASTER next-gate decision

A narrower geometry-only numerical gate is not required before the physical parameter freeze. F2.2 has already fixed the geometry family and all continuous geometric conventions; the remaining geometry numbers, equilibrium gradients and perpendicular wavenumber point are physically coupled parts of one benchmark specification and should be frozen together before input-geometry and discretization choices.

The next task is therefore:

**Fusion F2.3 — Physical Geometry / Gradient / Wavenumber Parameter Freeze 0.1**.

The gate must select exactly one source-supported physical benchmark point for the frozen F2-R family before any spectral or finite-time effect is inspected. A CBC-compatible point may be preferred only if the required two-species reduced-GK quantities can be assigned coherently from source-supported benchmark conventions. If the needed electron-gradient, geometry or wavenumber choices cannot be justified without mixing incompatible benchmarks or effect-guided tuning, F2.3 must return `HOLD` rather than inventing values.

Expected optimizer separation, nonnormality, spectral stability or heat-flux magnitude are forbidden selection criteria.

Canonical handoff:

`research/master/prompts/fusion_f2_3_physical_parameter_freeze_0_1.md`

## Rollback / STOP

This file is a new protected post-paper rollback point after the F2.1 Two-Species GK Balance Integration Freeze and the completed F2.2 branch result.

Frozen conclusions:

- F2.2 geometry/convention package is accepted and protected;
- circular `s-alpha` ballooning geometry is the primary F2-R geometry family;
- no numerical CBC or other parameter point has yet been inspected for finite-time behavior;
- the next task is a single physical geometry/gradient/wavenumber freeze, not a parameter scan or narrower effect-guided geometry gate.

**STOP — F2.2 INTEGRATED; F2.3 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**
