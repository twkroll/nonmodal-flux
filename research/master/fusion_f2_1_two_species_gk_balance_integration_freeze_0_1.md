# Fusion F2.1 Two-Species GK Balance Integration Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Status:** `STABLE — F2.1 TWO-SPECIES GK BALANCE FROZEN / F2.2 GEOMETRY-CONVENTION GATE RELEASED`

## Scope

This MASTER freeze integrates only the completed Fusion F2.1 continuous two-species local-gyrokinetic candidate/balance specification. It performs no phase-space discretization, parameter or wavenumber scan, GENE run, numerical/spectral qualification, finite-time propagator/Gramian construction, optimizer calculation, objective-separation inspection, R1 retuning, or modification of the frozen first-paper content.

Canonical branch result:

`research/fusion/fusion_f2_1_two_species_local_gyrokinetic_balance_specification_gate_0_1.md`

Branch verdict:

\[
\boxed{\text{F2.1 PASS — TWO-SPECIES GK CANDIDATE/BALANCE SPECIFIED — RETURN TO MASTER}}
\]

F2.1 branch commit:

`93e855b1618a92a6a20724a09549897112b23b7d`

Python CI #347 = `SUCCESS`.

## Frozen reduced and reference architectures

The primary reduced higher-fidelity candidate is frozen as

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

with passing electrons adiabatic at leading order in the slow-electron-transit ordering.

The higher-fidelity reference is frozen as

\[
\boxed{
\text{fully kinetic two-species electrostatic local GK}
+\text{H-theorem-compatible physical collisions}
}
\]

subject to later explicit normalization, collision-operator implementation and numerical-reference gates.

The reduced continuous state is

\[
x=(g_i(l,E_i,\mu_i,\sigma),\,g_e^{\rm tr}(E_e,\lambda,w)),
\]

with the electrostatic potential reconstructed linearly from quasineutrality. No discrete matrix representation is yet authorized.

## Frozen free-energy and transport structure

F2.1 specifies a positive continuous Helmholtz free-energy functional and corresponding positive kinetic Riesz metric

\[
\boxed{\mathcal M_{F2}\succ0}.
\]

The species particle and heat transport channels are defined independently from the physical radial gyrocentre flux integrals, not backwards from the balance identity.

Electrostatic quasineutrality imposes the ambipolar charge-flux constraint

\[
\sum_a e_a\Gamma_a=0,
\]

so for a hydrogenic plasma the ion and trapped-electron particle fluxes reduce to one ambipolar particle channel,

\[
\Gamma_i=\Gamma_e^{\rm tr}\equiv\Gamma.
\]

No corresponding closure identity forces

\[
q_i=q_e^{\rm tr}.
\]

The reduced collisionless free-energy balance is frozen as

\[
\boxed{
\frac{dW}{dt}
=G_\Gamma\Gamma
+G_{T,i}q_i
+G_{T,e}q_e^{\rm tr}.
}
\]

At the continuous-operator level this corresponds to

\[
\mathcal A_{F2}^\dagger\mathcal M_{F2}
+\mathcal M_{F2}\mathcal A_{F2}
=2\left(
G_\Gamma\mathcal Q_\Gamma
+G_{T,i}\mathcal Q_{q_i}
+G_{T,e}\mathcal Q_{q_e}
\right),
\]

where the individual channel forms remain physically defined by the radial flux integrals.

For the fully kinetic collisional reference, the total free-energy balance must include an H-theorem-compatible nonnegative dissipation form

\[
\mathcal D_{\rm coll}\succeq0.
\]

## Structural consequence relative to R1

The frozen R1 no-go had one thermodynamic source channel and no independent positive dissipation, forcing cumulative ion heat to be an affine function of final free energy.

F2.1 contains an ambipolar particle-work channel and distinct ion- and trapped-electron heat-work channels. Therefore

\[
G_{T,i}\int_0^T q_i\,dt
=W(T)-W(0)
-G_\Gamma\int_0^T\Gamma\,dt
-G_{T,e}\int_0^T q_e^{\rm tr}\,dt.
\]

Hence the exact R1 two-operator affine redundancy is

\[
\boxed{\text{not structurally forced in F2.1}.}
\]

This is only a possibility-in-principle statement. It does **not** establish nonzero optimizer angles, different optimal directions, a positive performance gap, transient growth, or any useful effect size.

## Frozen fidelity restrictions

- The primary reduced F2 candidate remains collisionless because that is the source-faithful bounce-averaged trapped-electron ordering. A collisional reduced variant would require a separately derived trapped/passing collision model.
- Finite ion FLR is retained consistently in gyroaveraging, polarization/free-energy geometry and physical flux kernels, but it is not an independent source/sink and is not the redundancy-breaking mechanism by itself.
- The fully kinetic reference must use a physical H-theorem-compatible collision operator; no ad hoc damping is authorized.
- R1 remains a structural no-go control and may not be retuned or rescued.

## Unresolved pre-effect objects

The following remain intentionally open and block any numerical/finite-time execution:

1. exact local magnetic-geometry family and geometric conventions;
2. physical geometry/gradient/wavenumber parameter point;
3. kinetic admissible initial-condition map `B` and input cost `R_in`;
4. phase-space discretization, quadrature and boundary conditions;
5. discrete reconstruction of `Q_Gamma`, `Q_qi`, `Q_qe` from the physical integrals;
6. structure-preserving and spectral numerical qualification;
7. fully kinetic reference collision parameters and implementation;
8. GENE-compatible normalization and diagnostic mapping.

## Next gate released

The next authorized scientific task is

**Fusion F2.2 — Local Magnetic-Geometry Family / Kinetic Convention Freeze 0.1**.

Its purpose is to freeze one source-faithful local toroidal geometry family and the coordinate/trapping/bounce-average conventions required by F2-R before any numerical parameter point or phase-space discretization is chosen.

Canonical handoff:

`research/master/prompts/fusion_f2_2_local_magnetic_geometry_kinetic_convention_freeze_0_1.md`

The gate may prefer a standard circular-concentric / s-alpha / Cyclone-Base-Case-compatible local tokamak geometry only if that choice is source-consistent with the F2-R equations and is justified by physical transparency, trapped-particle structure, tractability and later GK-code mapping. Expected objective-separation magnitude is forbidden as a selection criterion.

## Rollback and STOP

This file is a new protected post-paper rollback point after the R1 literature integration freeze and the F2.1 branch result.

**STOP — F2.1 INTEGRATED; F2.2 MAY PROCEED ONLY VIA THE COMMITTED HANDOFF.**
