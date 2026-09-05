# Fusion F1.4 Marginal / Structural Integration Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER  
**Status:** `STABLE — F1.4 MARGINAL R1 QUALIFIED AS STRUCTURAL CONTROL / R1 OBJECTIVE-SEPARATION PILOT BLOCKED / LITERATURE AUDIT RELEASED`

## Scope

This MASTER freeze integrates only the completed Fusion F1.4 numerical/spectral qualification of the already-frozen anisotropic-ZLR four-moment R1 minimal-curvature candidate at the single F1.3 CBC-projected point. It performs no parameter or horizon scan, no finite-time optimization, no FLR/GK extension, no effect-guided retuning, and no modification of the frozen first-paper content.

## Integrated F1.4 result

Canonical branch result:

`research/fusion/fusion_numerical_spectral_qualification_gate_0_1.md`

Transparent reproduction code:

`research/fusion/fusion_numerical_spectral_qualification_0_1.py`

Branch verdict:

\[
\boxed{\text{F1.4 HOLD — MARGINAL SPECTRUM — RETURN TO MASTER}}
\]

At the exact frozen point

\[
\tau_i=1,\quad R_0/L_n=2.2,\quad R_0/L_T=6.9,\quad q=1.4,
\quad k_x\rho_i=0,\quad k_y\rho_i=0.3,
\]

with \(\tau_{\rm ref}=R_0/c_s\), all required structural checks pass:

- \(M_k=M_k^\dagger\succ0\);
- \(Q_{q_i,k}\) is Hermitian, rank 2 and indefinite;
- \(B=I_4\), \(R_{\rm in}=M_k\), \(\operatorname{rank}(B)=4\);
- the physical heat-flux cross-phase reconstruction agrees at roundoff;
- the frozen free-energy balance agrees at roundoff and in an exact-rational audit;
- the source-free parallel/curvature operator is \(M_k\)-skew-adjoint at roundoff and exactly in the rational audit;
- coordinate congruence is verified;
- conditioning is acceptable for the 4x4 block.

The complete dimensionless spectrum is

\[
\lambda\tau_{\rm ref}
\approx
\{-3.592939609690i,\,-1.563190668779i,\,-0.276482492169i,\,+0.076649467886i\}.
\]

The scale-aware tolerance is \(1.0850\times10^{-13}\), while the numerical spectral abscissa is \(7.34\times10^{-17}\). An independent exact-rational/high-precision reproduction confirms four distinct purely imaginary eigenvalues. The frozen point is therefore marginal: neither asymptotically stable nor clearly unstable.

F1.4 branch commit:

`f2562061e79c67a5ccdc6a3d809ae0f655594319`

Python CI #330 = `SUCCESS`.

## MASTER regime decision

The marginal collisionless R1 point is accepted only as a **qualified structural/conservative control**. It is **not** promoted to a spectrally stable finite-time demonstration candidate.

No damping, collisions, closure term, wavenumber shift or parameter retuning may be added retrospectively to convert this exact frozen point into an asymptotically stable one.

## Structural consequence from the already-frozen CORE balance

For the frozen R1 candidate there is no positive dissipation term in the free-energy balance. In the dimensionless F1.4 normalization,

\[
\widetilde A^\dagger M_k+M_k\widetilde A
=2\frac{R_0}{L_T}\,\widehat Q_q.
\]

Integrating the standard CORE balance gives, for every finite horizon \(T\),

\[
2\frac{R_0}{L_T}
\int_0^T e^{\widetilde A^\dagger t}\widehat Q_q e^{\widetilde A t}\,dt
=
 e^{\widetilde A^\dagger T}M_k e^{\widetilde A T}-M_k.
\]

Because F1.2 froze

\[
B=I_4,\qquad R_{\rm in}=M_k,
\]

whitening by the fixed input free-energy metric yields an affine operator identity between the cumulative ion-heat objective and the final free-energy operator:

\[
2\frac{R_0}{L_T}K_q(T)
=
\mathcal E_M(T)-I,
\]

where

\[
\mathcal E_M(T)
=M_k^{-1/2}e^{\widetilde A^\dagger T}M_k e^{\widetilde A T}M_k^{-1/2}.
\]

Therefore the two Hermitian operators have the same eigenspaces and the same maximizing/minimizing directions at every horizon. With fixed initial free energy, maximizing cumulative signed ion heat transport is exactly equivalent to maximizing final free energy (up to the positive affine scaling above).

This is not a newly inspected finite-time effect. It is the direct application of the already-frozen branch-independent CORE balance identity to the now fully frozen R1 objects.

## Consequence for FUSION-F1

The originally intended R1 finite-time **free-energy-optimal versus cumulative-ion-heat-optimal nonredundancy** pilot is structurally blocked:

\[
\boxed{\text{R1 cumulative heat objective and final free-energy objective are affinely equivalent.}}
\]

Hence no optimizer-angle/performance-gap execution is authorized for this R1 candidate. Running such an execution would only numerically reproduce a relation already fixed by the exact balance and would not test the intended nonredundancy question.

R1 is retained as a scientifically useful **no-go / structural-collapse baseline** for the fidelity ladder.

## What may break the R1 affine equivalence

MASTER does not choose a higher-fidelity model here. The next step must determine from the literature and established balance structures which physically necessary additions can break the one-channel collisionless affine identity without being selected for a desired effect size. Candidate mechanisms to audit include, but are not assumed to be sufficient:

- positive collisional or other physically derived dissipation;
- kinetic/nonadiabatic electron dynamics;
- multiple independently defined particle/heat/species supply channels;
- phase-mixing/Landau-fluid or kinetic entropy-transfer terms when represented consistently;
- FLR corrections, specifically whether they merely modify \(A,M,Q\) or introduce genuinely independent balance channels/sinks.

No mechanism may be promoted merely because it is expected to create optimizer separation.

## Next task released

The next authorized task is the targeted literature audit:

**Fusion R1 Structural Redundancy & Fidelity-Breaking Literature Audit 0.1**

Canonical handoff:

`research/master/prompts/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`

The audit is to be executed in the Literature branch. Fusion itself waits while the audit is active.

## Freeze / rollback classification

This file is a new post-paper rollback point after the F1.3 Candidate / Convention Integration Freeze and the F1.4 branch result.

Frozen conclusions:

- F1.4 numerical/algebraic qualification passes;
- the exact R1 spectrum is marginal and diagonalizable with four distinct imaginary-axis eigenvalues;
- no spectral rescue or retuning is permitted;
- the marginal R1 regime is accepted only as a structural control;
- the R1 cumulative ion-heat and final free-energy optimization problems are affinely equivalent under the frozen \(B=I_4\), \(R_{\rm in}=M_k\), zero-dissipation balance;
- the R1 objective-separation pilot is blocked;
- higher fidelity may proceed only after the targeted literature/balance audit and a subsequent explicit MASTER decision.

**STOP — F1.4 INTEGRATED; R1 PILOT BLOCKED; AWAIT LITERATURE AUDIT.**