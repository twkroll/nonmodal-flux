# Cross-Domain Integration Gate 0.1

**Status:** PASSED  
**Date:** 2026-09-02  
**Scope:** integration and release control only. No CORE optimization, no parameter search, no objective-separation calculation.

## 1. Inputs to this gate

This gate integrates only already frozen/qualified application results:

- Plasma/D10-ZF Pilot 0.2 Result Freeze: `P2-A`, global scientific savepoint.
- Neuro Admissible Input Geometry Gate 0.1: `NB-A`.
- Climate/Ocean Numerical Qualification 0.1: `QUALIFIED`.

No new theory branch is opened.

## 2. Neuro integration

The nominated Neuro candidate remains

\[
\boxed{\text{multi-region CMC/DCM}}
\]

with primary pathway

\[
\boxed{\mathrm{SP}_j\rightarrow\mathrm{SS}_i}
\]

and

\[
Q_{j\to i}^{\rm CORE}
=
\frac12\left(A_{j\to i}^\dagger M+MA_{j\to i}\right).
\]

The previous rank-one admissible-input blocker is removed by the `NB-A` result. A physically admissible rank-two preparation geometry exists through the same accepted afferent input pathway:

\[
B_{\rm prep}^{(2)}
=
\begin{bmatrix}
 e^{A\tau_1}b_{\rm aff,j} & e^{A\tau_2}b_{\rm aff,j}
\end{bmatrix},
\qquad \tau_1\neq\tau_2,
\]

or the corresponding finite-pulse realization. The input metric remains the pre-CORE pulse-dose Gram matrix. No hidden-state actuator or `B=I` is introduced.

**Integration decision:** Neuro is released to a **Pilot Specification 0.1**, but not to CORE execution. The specification must freeze the exact CMC network, stable operating point, region identities, state ordering, exact matrices, pulse protocol, calibration, time normalization, horizons, and numerical rank/conditioning of the full frozen `B` before any objective calculation.

## 3. Climate/Ocean integration

The frozen Climate/Ocean candidate remains the damped two-layer Phillips-QG channel with

\[
(A_K,M_K,Q_{{\rm heat},K},B=I,R_{\rm in}=M_K).
\]

Numerical Qualification 0.1 established on the pre-fixed ladder

\[
(M_x,N_y)=(4,4),(8,8),(12,12),(16,16),(24,24)
\]

that

\[
M_K=M_K^\dagger\succ0,
\qquad
Q_{{\rm heat},K}=Q_{{\rm heat},K}^\dagger,
\]

with `Q_heat,K` indefinite, exact reproduction of the signed heat flux, and spectral stability

\[
\alpha(A_K)=-0.072337962962963=-0.1\,\mathrm d^{-1}<0
\]

at every fixed resolution. Nested common-mode spectral branches agree to machine precision. No CORE-effect quantity was inspected.

**Integration decision:** Climate/Ocean is released to a **Pilot Specification 0.1**, but not directly to execution. The specification must freeze horizons, primary/confirmation resolutions, reporting metrics, numerical checks, robustness rules, and verdict classes before constructing finite-time objective operators.

## 4. Shared cross-domain operator protocol

To test transferability without pretending that the physical semantics are identical, all new pilots use the same abstract finite-time reporting layer.

For a frozen application tuple

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}),
\qquad M\succ0,
\qquad Q=Q^\dagger,
\]

write

\[
x(0)=B R_{\rm in}^{-1/2}w,
\qquad \|w\|_2=1.
\]

The positive storage/state objective at horizon `T` is

\[
K_M(T)
=
R_{\rm in}^{-1/2}
B^\dagger e^{A^\dagger T}M e^{AT}B
R_{\rm in}^{-1/2},
\]

\[
G_M(T)=\lambda_{\max}(K_M(T)).
\]

For Plasma and Climate with `B=I, R_in=M`, this reduces to the familiar finite-time energy-gain operator. For Neuro it is deliberately interpreted as **final synaptic-filter storage per fixed experimental input cost**, not as metabolic brain energy.

The signed cumulative channel is

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
\]

\[
K_Q(T)
=
R_{\rm in}^{-1/2}B^\dagger P_Q(T)B R_{\rm in}^{-1/2}.
\]

Report both signed extrema

\[
J_Q^+(T)=\lambda_{\max}(K_Q(T)),
\qquad
J_Q^-(T)=\lambda_{\min}(K_Q(T)),
\]

with the positive branch pre-registered as the primary comparison unless a domain-specific physical orientation had already been frozen otherwise.

Let `w_M^*(T)` and `w_Q^*(T)` be normalized positive-objective and positive-channel optimizers in whitened input coordinates. The common angle is

\[
\vartheta(T)
=
\arccos\left|{w_M^*}^\dagger w_Q^*\right|.
\]

At degeneracy, compare optimal subspaces/projectors rather than arbitrary eigenvectors.

The common dimensionless signed-channel gap is

\[
\Delta_Q(T)
=
\frac{J_Q^+(T)-{w_M^*}^\dagger K_Q(T)w_M^*}{J_Q^+(T)},
\]

only when the positive denominator is safely nonzero. If it is near zero, the gap is marked uninterpretable rather than regularized post hoc.

## 5. Shared pre-registration rules

The cross-domain comparison freezes the following rules before any new application execution:

1. **No effect-guided model selection.** Model, operating point, `M`, `Q`, `B`, `R_in`, horizons and resolutions are selected only from domain physics, experiment design, numerical qualification and stability.
2. **No retuning after first result.** A weak/null result is retained as such.
3. **Same reporting objects.** `G_M`, `J_Q^+`, `J_Q^-`, `vartheta`, `Delta_Q` and physical optimizer diagnostics are reported wherever mathematically meaningful.
4. **Inherited operational thresholds.** The Pilot-0.2 values `vartheta >= 20 deg` and `Delta_Q >= 0.25` are retained as pre-registered framework-demonstration thresholds, not as universal physical constants.
5. **Neighboring-horizon rule.** A threshold-based claim requires at least two neighboring fixed horizons, as in Pilot 0.2.
6. **Physical interpretability required.** Vector-angle separation alone is insufficient; each branch must identify domain-specific structural differences in the optimizers.
7. **Robustness required.** Climate uses resolution robustness; Neuro must at minimum pass frozen `B` rank/conditioning and numerical reproducibility, with any further robustness study pre-registered before inspection.
8. **No universality claim.** Failure or success in one domain does not logically determine another.

## 6. Time normalization and horizons

The **dimensionless horizon ladder is inherited** as

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

However, each application must define `tau_ref` independently from pre-CORE domain physics before execution.

- Climate already has `tau_ref=L_D/(beta L_D^2)=0.7233796296 d` from its frozen nondimensionalization.
- Neuro must freeze a model-internal synaptic/filter reference time in Pilot Specification 0.1 without inspecting CORE effects.

Thus the workflow is comparable while the physical clock retains domain meaning.

## 7. Cross-domain success interpretation

The project is not trying to prove a new universal theorem that storage-optimal and transfer-optimal perturbations differ. The cross-domain test asks whether the same **physics-informed analysis workflow** repeatedly exposes nonredundancy between a positive storage/state objective and an independently defined signed transfer observable.

A strong cross-domain demonstration therefore requires, within each successful branch:

\[
\text{stable/qualified dynamics}
\; + \;
\text{finite-time positive-objective behavior}
\; + \;
\text{signed channel extrema}
\; + \;
\text{nontrivial objective separation}
\; + \;
\text{physical structure}
\; + \;
\text{robustness}.
\]

The novelty remains integration, physical interpretation, methodology and applications/predictions, not new quadratic-output mathematics.

## 8. Parallelization decision

Both application branches may now proceed **in parallel to specification only**:

\[
\boxed{
\text{Neuro Pilot Specification 0.1}
\quad\parallel\quad
\text{Climate/Ocean Pilot Specification 0.1}
}
\]

Neither branch is authorized to compute `K_M`, `K_Q`, optimizers, angles or gaps until its own specification is committed and explicitly frozen.

Power Grids, Photonics/Waves and realistic Fusion remain protected branches and are not demoted by success of Neuro or Climate. MODES, CONT and CASCADE remain waiting integration modules.

## 9. Gate verdict

\[
\boxed{\text{Cross-Domain Integration Gate 0.1 = PASSED}}
\]

with two simultaneous releases:

\[
\boxed{\text{Neuro -> Pilot Specification 0.1}}
\]

\[
\boxed{\text{Climate/Ocean -> Pilot Specification 0.1}}
\]

and **no release to application execution yet**.

## 10. Decision log

- **DEC-280:** Cross-Domain Integration Gate 0.1 passed — STABLE.
- **DEC-281:** Neuro `NB-A` accepted; rank-one blocker removed — STABLE.
- **DEC-282:** Climate Numerical Qualification accepted — STABLE.
- **DEC-283:** Neuro and Climate released in parallel to Pilot Specification only — ACTIVE.
- **DEC-284:** Shared `K_M/K_Q` reporting layer adopted for cross-domain pilots — STABLE.
- **DEC-285:** Same dimensionless horizon ladder inherited; domain-specific `tau_ref` required — STABLE.
- **DEC-286:** `20 deg` and `Delta_Q=0.25` retained as operational preregistered thresholds, not universal constants — STABLE.
- **DEC-287:** Positive signed branch primary; negative extremum remains mandatory reporting — STABLE.
- **DEC-288:** No effect-guided retuning after specification — STABLE.
- **DEC-289:** Success/failure of one application does not condition the scientific validity of the other — STABLE.
- **DEC-290:** Power Grids and Photonics remain protected irrespective of Neuro/Climate outcomes — STABLE.

**STOP.**
