# Diagnosing objective nonredundancy in stable linear dynamics: a physics-informed finite-time workflow across plasma, neural and geophysical models

**Draft:** 0.3  
**Status:** STRUCTURAL REVISION COMPLETE — FROZEN-EVIDENCE ONLY  
**Authority:** `research/master/manuscript_structure_freeze_0_2.md`  
**Scope:** editorial implementation of the frozen manuscript architecture. No new simulation, eigensolve, horizon, parameter, model, objective, channel, admissible geometry, novelty search, or protected-branch work is introduced.

## Abstract

Finite-time optimal-perturbation studies often use a positive energy, storage, or state metric as a proxy for the physical quantity of interest. We ask a narrower question: after the dynamics, admissible perturbations, positive metric, and a separately defined signed physical channel have all been fixed, how redundant are the two resulting finite-time optima? We apply the same pre-specified and version-controlled workflow to three stable linear models. In a drift-wave/zonal-flow plasma benchmark, the free-energy-optimal perturbation misses 50.4% of the maximum positive cumulative particle transport at the frozen horizon `T=1`. In a two-source V1/V4 canonical-microcircuit model, terminal synaptic-filter-storage and cumulative V1-SP -> V4-SS pathway objectives select markedly different two-pulse preparations, with performance gaps 0.529 and 0.818 at 112 and 224 ms. In a damped two-layer quasigeostrophic model, energy- and poleward-heat-optimal subspaces are orthogonal at the longest frozen horizon while the heat-performance gap is only 0.0412, so the energy optimum retains 95.88% of maximal cumulative poleward heat transport. The nonuniform outcome shows why optimizer geometry and target-performance loss should be reported separately. An additional one-shot geophysical robustness case showed striking fixed-resolution separation but was rejected when the pre-specified refinement criteria failed. The contribution is a physics-informed diagnostic workflow and cross-domain physical interpretation, not a new general theory of optimal perturbations.

---

# 1. Introduction

Optimal-perturbation methods ask which admissible disturbance produces the largest response over a prescribed horizon. Positive energy or storage measures are natural objectives because they are stable metrics, often physically interpretable, and mathematically convenient. Yet the scientific target may instead be a signed radial particle flux, a meridional heat flux, or the signed contribution of a specified physiological pathway to a storage-rate balance. A positive state metric and a signed physical channel therefore answer different questions even when both are evaluated on the same linear dynamics and the same admissible perturbation space.

The mathematical tools needed to compare such questions are established. Transient amplification in stable systems, singular vectors, quadratic finite-time outputs, Gramian and adjoint methods, and norm dependence all have substantial prior art. Stable plasma transient amplification has been studied directly [Landreman2015]; damped baroclinic transient growth is classical [Farrell1982; Farrell1985; FarrellIoannou1994]; atmospheric and oceanic singular vectors depend on the chosen norm or target [KimMorgan2002; Kuang2004]; energy-optimal and mixing-oriented perturbations can differ in fluid mechanics [Foures2014]; and heat-transport-optimal initial perturbations exist in stable ocean models [Sevellec2008]. Neural systems likewise have established literatures on non-normal amplification, transient trajectory design, DCM experimental design, and neural-mass optimal control [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026].

The present contribution is therefore not the generic statement that different objectives can have different optimizers. We instead use one controlled workflow in which the linear generator, positive metric, signed channel, admissible perturbation geometry, input cost, horizon ladder, and numerical gates are specified and frozen before objective-separation results are inspected. We then report both geometric separation and the actual loss in the physical channel incurred by using the conventional positive-objective optimum as a proxy.

Three deliberately different robust cases form the principal evidence sequence. A drift-wave/zonal-flow plasma model supplies a strong signed-transport anchor. A two-source canonical-microcircuit model tests a low-dimensional, experimentally interpretable preparation geometry rather than arbitrary full-state actuation. A damped two-layer quasigeostrophic model supplies a robust weak contrast in which optimal structures differ sharply while target performance remains almost redundant. The nonuniformity is part of the result: the workflow is intended to diagnose objective nonredundancy, not to maximize it.

A separate one-shot equivalent-barotropic Climate-B audit is not part of this positive/weak evidence sequence. It is retained because the same workflow rejected an attractive fixed-resolution result after the mandatory refinement gates failed. This negative case makes robustness a distinct evidentiary layer rather than a cosmetic post-processing check.

Our manuscript-level claim is correspondingly limited: storage/state-optimal and physical-channel-optimal perturbations need not be redundant, but the magnitude and practical consequence of their separation depend on the system, horizon, observable, admissible perturbation geometry, and numerical/representation robustness.

---

# 2. Common finite-time framework and study design

## 2.1 Frozen linear problem

Each application is represented by an autonomous stable linear system

\[
\dot x=Ax,
\qquad
x(0)=Bu,
\]

with a positive input-cost metric

\[
u^\dagger R_{\rm in}u=1,
\qquad
R_{\rm in}=R_{\rm in}^\dagger\succ0.
\]

The matrix `B` is part of the physical specification: it identifies which initial perturbations can actually be prepared. Introducing whitened input coordinates

\[
w=R_{\rm in}^{1/2}u,
\qquad
\|w\|_2=1,
\]

places optimizer comparisons on the same admissible input-cost sphere within each application.

## 2.2 Positive state/storage objective

Let

\[
S_M(x)=\frac12x^\dagger Mx,
\qquad
M=M^\dagger\succ0.
\]

For compactness, the finite-time operator is written for the doubled quadratic form `x^\dagger Mx=2S_M`:

\[
K_M(T)
=
R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2}.
\]

The omitted common factor `1/2` has no effect on optimizer directions, gain ratios, or the channel-performance gaps below. Whenever a physical storage itself is described, the `1/2` convention is restored explicitly.

The leading eigenspace of `K_M(T)` defines the terminal positive-objective optimum. Its physical meaning is domain specific: free energy in Plasma, synaptic-filter storage in Neuro, QG perturbation energy in Climate-A, and perturbation kinetic energy in the supplementary Climate-B audit.

## 2.3 Signed physical channel

A **physical channel** here means a separately defined signed quadratic transport, exchange, or pathway-contribution observable. It need not be a conserved flux and the applications do not share a common unit or conservation law. Its instantaneous form is

\[
q_Q(t)=x(t)^\dagger Qx(t),
\qquad
Q=Q^\dagger,
\]

and its cumulative value is

\[
J_Q(T)=\int_0^T x(t)^\dagger Qx(t)\,dt.
\]

Defining

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt
\]

gives the whitened finite-time channel operator

\[
K_Q(T)
=
R_{\rm in}^{-1/2}B^\dagger P_Q(T)BR_{\rm in}^{-1/2}.
\]

Its largest and smallest eigenvalues are the maximum and minimum cumulative signed channel values reachable on the frozen admissible perturbation space.

## 2.4 Geometry and target-performance diagnostics

When the leading eigendirections are nondegenerate, the optimizer angle is

\[
\vartheta(T)=
\arccos\left|\langle w_M^\star,w_Q^\star\rangle\right|.
\]

When symmetry produces an exact leading degeneracy, we compare the full leading eigenspaces using conservative principal-angle diagnostics rather than selecting an arbitrary member of a degenerate subspace.

Geometric nonidentity is not itself a measure of practical loss. Whenever `J_Q^+(T)>0`, we therefore evaluate

\[
\Delta_Q(T)
=
\frac{J_Q^+(T)-J_Q(T;w_M^\star)}{J_Q^+(T)},
\]

or, for a degenerate positive-objective optimum, the conservative version obtained by choosing the member of the positive-objective eigenspace with the best channel performance. Thus `\Delta_Q=0` means that the positive-objective optimum is also channel-optimal, while `\Delta_Q=0.5` means that it realizes only half of the maximum positive cumulative channel.

## 2.5 Pre-specification, freezing, verdict rules, and robustness

The model, parameters, `M`, `Q`, `B`, `R_in`, horizon ladders, numerical checks, and verdict rules were prospectively frozen in the version-controlled analysis record before objective-separation effects were inspected.

For the cross-domain application pilots, a study-specific **strong objective-separation** criterion required both

\[
\vartheta\ge20^\circ,
\qquad
\Delta_Q\ge0.25
\]

on at least two neighboring frozen horizons, together with the domain-specific structural and numerical gates. These thresholds are operational rules for this study, not universal physical constants. The Plasma benchmark retains its separately frozen `S0-S5` gate structure; the common `\vartheta`/`\Delta_Q` diagnostics are reported for comparison without redefining the original `P2-A` verdict.

Robustness is an independent evidentiary layer. A large same-resolution angle or performance gap is insufficient if the pre-specified residual, direct-reproduction, conditioning, or cross-resolution gates fail. The Climate-B audit below is included precisely to document this rejection discipline.

## 2.6 Domain semantics — Main Table 1

| Domain | Defining model | Positive objective | Signed physical channel | Admissible geometry and cost | Frozen role |
|---|---|---|---|---|---|
| Plasma/D10-ZF | stable drift-wave/zonal-flow linearization | free energy | cumulative radial particle transport | full frozen Galerkin perturbation space; `B=I`, `R_in=M` | `P2-A` strong anchor |
| Neuro/CMC | stable two-source V1/V4 CMC | terminal synaptic-filter storage | cumulative V1-SP -> V4-SS pathway contribution to storage rate | rank-two fixed two-pulse afferent preparation; `R_in=I_2` | `NEURO-STRONG` |
| Climate-A/Phillips-QG | stable damped two-layer QG | QG perturbation energy | cumulative poleward eddy heat transport | balanced QG eddy state space; `B=I`, `R_in=M_K` | `CLIM-WEAK` robust contrast |

These labels are not interchangeable. In particular, the neural positive metric is not metabolic, thermodynamic, or total physiological brain energy.

---

# 3. Application methods

## 3.1 Plasma: D10-ZF drift-wave/zonal-flow model

For one nonzero poloidal wavenumber `k_y`, the frozen linearization is

\[
\partial_t\Delta_k\hat\varphi
+ik_yU\Delta_k\hat\varphi
-ik_yU''\hat\varphi
=C(\hat\varphi-\hat\eta),
\]

\[
\partial_t\hat\eta+ik_yU\hat\eta
=C(\hat\varphi-\hat\eta)-i\kappa k_y\hat\varphi,
\qquad
\Delta_k=\partial_x^2-k_y^2.
\]

The frozen point is

\[
U(x)=\cos x,
\quad
L_x=2\pi,
\quad
k_y=C=\kappa=1,
\quad
N(x)=0,
\]

with Pilot-0.2 uniform damping `A=A_0-0.020I`. The nondimensional D10-ZF time unit is retained with `\tau_ref=1`; no dimensional-seconds conversion is asserted.

At resolution `K`, radial Fourier modes `m=-K,\ldots,K` are retained and the state is ordered as all potential coefficients followed by all density coefficients. The free-energy form and signed outward particle-flux form are

\[
E=\frac12z^\dagger Mz,
\qquad
M=\begin{pmatrix}-\Delta&0\\0&I\end{pmatrix}\succ0,
\]

\[
\Gamma
=k_y\operatorname{Im}(\eta^\dagger\phi)
=z^\dagger Q_\Gamma z,
\qquad
Q_\Gamma
=\frac{k_y}{2}
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}.
\]

The full retained perturbation space is admissible, so `B=I` and `R_in=M`. The frozen resolutions are `K=32,64,96` and the horizon ladder is `T={0.25,0.5,1,2,4,8}`. Full block matrices, resolution checks, and numerical tolerances are given in Supplement S2.

## 3.2 Neuro: two-source V1/V4 canonical microcircuit

The neural pilot uses V1 and V4 sources, each with spiny-stellate (`SS`), superficial-pyramidal (`SP`), inhibitory-interneuron (`II`), and deep-pyramidal (`DP`) populations represented by second-order synaptic filters. The 16-dimensional autonomous instantaneous-coupling CMC is the linearization of the pinned SPM12 canonical-microcircuit state equation at the exact zero fixed point. Propagation delays are disabled for this finite-dimensional pilot; this is a scope restriction, not a biological claim of zero conduction delay. The frozen generator is stable with

\[
\alpha(A)=-33.0964092356\ {\rm s}^{-1}.
\]

For each population with inverse synaptic time constant `\kappa_p`, the model-internal storage is

\[
S_{r,p}
=\frac12(z_{r,p}^2+\kappa_p^2v_{r,p}^2),
\qquad
S=\frac12x^\dagger Mx,
\]

with frozen time constants 2, 2, 16, and 28 ms for `SS`, `SP`, `II`, and `DP`. The quantity is a synaptic-filter state storage only.

The primary physiological channel is the prospectively selected forward connection

\[
\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS}.
\]

Writing `A=A_rest+A_{j\to i}`, where `A_{j\to i}` contains only that pathway contribution, the signed pathway contribution to the storage-rate balance is

\[
Q_{j\to i}
=\frac12(A_{j\to i}^\dagger M+MA_{j\to i}).
\]

Its sign indicates whether the predefined pathway increases or decreases the chosen storage rate; it is not an excitatory/inhibitory synaptic-sign label.

Admissible preparations are two fixed rectangular 1-ms afferent pulses to V1-SS ending 2 ms and 16 ms before the autonomous observation window. Only their amplitudes vary. Their propagated initial-state columns define

\[
B=[b_1^{\rm eff},b_2^{\rm eff}],
\qquad
b_k^{\rm eff}=
\int_{\tau_k}^{\tau_k+\delta}e^{As}b_{\rm aff,V1}\,ds.
\]

The map has rank two, passes the frozen storage/input-whitened conditioning gate, and uses `R_in=I_2` in pulse-amplitude coordinates. With `\tau_ref=28 ms`, the horizons are 7, 14, 28, 56, 112, and 224 ms. Detailed state ordering, sparse matrices, pulse columns, and numerical checks are in Supplement S3.

## 3.3 Climate-A: damped two-layer Phillips QG model

The robust geophysical application uses

\[
\partial_tq_i'+U_i\partial_xq_i'+\Pi_i\partial_x\psi_i'=-rq_i',
\qquad i=1,2,
\]

with

\[
q_1'=\nabla^2\psi_1'+F(\psi_2'-\psi_1'),
\qquad
q_2'=\nabla^2\psi_2'+F(\psi_1'-\psi_2'),
\]

`F=(2L_D^2)^{-1}`, `U_1=+U`, `U_2=-U`, and the frozen point

\[
L_x=3.0\times10^7\ {m m},
\quad
L_y=1.0\times10^7\ {m m},
\quad
L_D=10^6\ {m m},
\]

\[
\beta=1.6\times10^{-11}\ {m m^{-1}s^{-1}},
\quad
U=8\ {m m\,s^{-1}},
\quad
r=(10\ {m d})^{-1}.
\]

The domain is periodic in `x`, uses `\psi_i'=0` at `y=0,L_y`, and excludes `k_x=0` eddies. In barotropic/baroclinic variables

\[
\psi=\frac{\psi_1'+\psi_2'}2,
\qquad
\tau=\frac{\psi_1'-\psi_2'}2,
\]

the perturbation energy is

\[
E=\frac12\int_\Omega
\left(|\nabla\psi|^2+|\nabla\tau|^2+L_D^{-2}|\tau|^2\right)dA,
\]

and the signed channel is cumulative meridional eddy heat transport,

\[
H_{\rm heat}=C_H\int_\Omega(\partial_x\psi)\tau\,dA,
\qquad C_H>0,
\]

with positive sign northward/poleward. No absolute value or squared heat flux is substituted.

A structure-preserving Fourier/sine basis enforces the boundary conditions and `k_x\ne0` restriction exactly. The balanced eddy state itself is admissible, so `B=I`, `R_in=M_K`. The reference time is `\tau_ref=62500 s=0.7233796296 d`; the frozen horizon ladder is `T/\tau_ref={0.25,0.5,1,2,4,8}`. Primary, confirmation, and high-audit resolutions are `(12,12)`, `(16,16)`, and `(24,24)`. Modal matrices and convergence gates are given in Supplement S4.

---

# 4. Results

## 4.1 Plasma: strong signed-transport anchor

The D10-ZF operators are spectrally stable at all three reported resolutions,

\[
\alpha(A_{32})=-0.0075786,
\quad
\alpha(A_{64})=-0.0133818,
\quad
\alpha(A_{96})=-0.0154924.
\]

Nevertheless, finite-time free-energy amplification exceeds unity at every frozen horizon, while the cumulative particle-transport operator has both positive and negative extrema.

At the representative horizon `T=1`,

\[
G_E=1.8782758,
\qquad
J_\Gamma^+=0.3535169,
\qquad
J_\Gamma^-=-0.1462216,
\]

and the free-energy-optimal perturbation produces

\[
J_\Gamma(w_E^\star)=0.1752252.
\]

Therefore

\[
\Delta_\Gamma=0.5043372,
\qquad
\vartheta=53.396^\circ.
\]

The free-energy optimum misses approximately 50.4% of the maximum positive cumulative particle transport. Scalar objectives and projected optimizer structure are converged across `K=32,64,96` to numerical precision on their common resolved subspace, and the optimizers differ in radial Fourier support, potential/density composition, and relative phase. The least-damped modal trajectory decays while finite-time optimal perturbations transiently amplify.

Thus, locally and without a universality claim,

\[
\text{modal stability}
\neq
\text{finite-time free-energy optimality}
\neq
\text{finite-time particle-transport optimality}.
\]

Stable plasma transient amplification itself is established prior art [Landreman2015]. The role of this result is a strong, resolution-robust signed-transport anchor for the common workflow.

## 4.2 Neuro: strong nonredundancy in a constrained two-pulse preparation

The frozen V1/V4 generator is stable and the two-pulse map has rank two with acceptable storage/input-whitened conditioning. The terminal synaptic-filter-storage and cumulative V1-SP -> V4-SS pathway objectives satisfy the study-specific strong criterion at two neighboring long horizons:

\[
T=112\ {m ms}:
\qquad
\vartheta=46.824271^\circ,
\quad
\Delta_Q=0.529017,
\]

\[
T=224\ {m ms}:
\qquad
\vartheta=65.058256^\circ,
\quad
\Delta_Q=0.817841.
\]

In the frozen preparation coordinates the pathway optimum is approximately

\[
w_Q\approx(+0.9924,-0.1230),
\]

whereas the storage optima use same-sign mixtures,

\[
w_M(112\ {m ms})\approx(+0.7687,+0.6396),
\]

\[
w_M(224\ {m ms})\approx(+0.5300,+0.8480).
\]

The pathway optimum therefore combines a dominant recent pulse with a small opposite-sign older component, whereas the long-horizon storage optimum combines the two fixed components with the same sign.

Although the full-state instantaneous pathway matrix is indefinite, the frozen rank-two preparation geometry reaches only positive cumulative channel values over the tested horizon ladder: the minimum eigenvalue of `K_Q(T)` remains positive. The result does **not** demonstrate experimentally reachable negative cumulative pathway transfer. Its narrower claim is strong nonredundancy between terminal synaptic-filter-storage optimality and positive cumulative pathway-contribution optimality on the fixed two-pulse preparation space.

Non-normal neural amplification, transient trajectory design, DCM input design, and neural-mass optimal control are established [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026]. To our knowledge, the targeted literature does not already contain this same stable CMC/DCM comparison over the same fixed rank-two preparation coordinates.

## 4.3 Climate-A: robust weak geometry-versus-performance contrast

The damped two-layer QG operator is spectrally stable throughout the qualified ladder with

\[
\alpha(A_K)=-0.1\ {m d}^{-1}.
\]

At the first five frozen horizons, energy- and poleward-heat-optimal perturbations are nearly redundant: they occupy the same modal support and the heat-performance gap stays below about `0.00317`.

At the longest horizon, `T/\tau_ref=8`, the optimal modal supports switch to

\[
(|m|,n)_E=(3,2),
\qquad
(|m|,n)_{\rm heat}=(4,2).
\]

The optimal subspaces are therefore orthogonal,

\[
\vartheta_{\rm sub}=90^\circ.
\]

Yet

\[
J_{\rm heat}^+=1.54448995,
\qquad
J_{\rm heat|E}^{\rm best}=1.48088082,
\]

so

\[
\Delta_{\rm heat}=0.04118455.
\]

The energy-optimal subspace retains approximately 95.88% of the maximum cumulative poleward heat transport. The heat optimum is more strongly baroclinic and occupies the shorter zonal scale `|m|=4`, but that structural difference has only a small target-performance consequence. All six frozen horizons pass the complete resolution protocol.

This is the central robust weak contrast:

\[
\boxed{\text{large optimizer/subspace separation does not imply a large target-performance gap}.}
\]

Transient baroclinic growth, norm dependence, transient heat flux, and heat-transport-optimal perturbations are established prior art [Farrell1982; Farrell1985; FarrellIoannou1994; KimMorgan2002; Kuang2004; Sevellec2008]. We use this result as a controlled methodological contrast, not as a claim that energy optimization generically fails for climate transport.

---

# 5. Cross-domain synthesis and robustness lessons

## 5.1 Geometry versus target performance

The three robust cases form an evidence hierarchy rather than three replications of one physical effect.

| Domain | Frozen role | Representative robust witness | Interpretation |
|---|---|---|---|
| Plasma/D10-ZF | `P2-A` strong anchor | `T=1`: `\vartheta=53.40 deg`, `\Delta_\Gamma=0.504` | large geometric and target-performance separation |
| Neuro/CMC | `NEURO-STRONG` | 112/224 ms: `\Delta_Q=0.529/0.818` | strong separation in constrained preparation geometry |
| Climate-A/Phillips-QG | `CLIM-WEAK` | `T/\tau_ref=8`: `90 deg`, `\Delta_heat=0.0412` | large geometric separation, small target penalty |

The shared lesson is that **geometric nonidentity and decision relevance are different questions**. `\vartheta` asks whether optimal admissible structures differ. `\Delta_Q` asks how much target performance is lost by using the positive-objective optimum. Climate-A shows that orthogonal optimal subspaces can remain nearly substitutable for the selected channel; Plasma and Neuro show cases in which the proxy choice materially changes the attainable physical target.

Admissible geometry is equally important. Full-state perturbations are acceptable in the already restricted Plasma and QG state spaces, but not in the neural model, where a physically interpretable preparation must be tied to afferent inputs. Nonredundancy is therefore a property of the full frozen tuple `(A,M,Q,B,R_in,T)`, not of `A` or `Q` alone.

The signed semantics also remain domain specific. Plasma and Climate-A realize both signs of their cumulative transport channels on the frozen admissible spaces. Neuro uses a signed pathway operator in full state space but reaches only the positive cumulative branch on its fixed preparation geometry. The commonality is methodological, not a claim that the physical observables are interchangeable.

## 5.2 Robustness rejection: one-shot Climate-B audit

A separate equivalent-barotropic Bickley-jet audit was frozen before effect inspection as a single additional Climate attempt. All local algebraic and direct physical-reproduction gates passed at the mandatory primary `(16,32)`, confirmation `(20,40)`, and high-audit `(24,48)` resolutions. At each individual truncation, Energy-vs-Shift separation appeared very large: the target-performance gap was `\Delta_shift=1` to roundoff and large angles followed from a parity mechanism in which the energy optimum remains in one preserved parity sector while the signed jet-translation channel couples opposite parity sectors. **These fixed-resolution observations failed the pre-specified refinement protocol and are not robust Climate evidence.** Zero of the six frozen horizons passed the complete cross-resolution criteria: signed objective values remained outside the frozen 2% convergence rule, common-space optimizer/subspace mass fell below `\mu_c=0.95`, and the optimizing scales migrated as resolution increased. The branch is therefore frozen as `CLIM-B-FAIL — resolution robustness failure`, not as a fourth positive application result. Full model, gate, and failure ledgers are given in Supplement S5.

The methodological lesson is distinct from Climate-A: a large same-resolution angle or performance gap can be rejected when its numerical/representation support does not survive the prospectively frozen refinement tests.

---

# 6. Discussion and limitations

## 6.1 Contribution and novelty level

The strongest defensible contribution is methodological integration plus physical insight (`N2+N3` in the project classification), with narrower application-level contributions. The workflow combines physical predefinition of `M`, `Q`, `B`, and `R_in`; common finite-time positive and signed-channel operators; signed extrema; optimizer/subspace and target-performance diagnostics; direct physical reconstruction; numerical robustness gates; prospective freezing; and explicit anti-retuning rules.

No mathematical novelty is claimed for transient growth, singular vectors, quadratic-output optimization, Gramian/Lyapunov methods, or the generic fact that different objectives can select different optimizers. Those ingredients are established. The contribution is the controlled physical question and the nonuniform evidence obtained when it is asked across different systems without selecting parameters to enlarge the effect.

## 6.2 Domain-specific semantics and physical admissibility

The physical meanings of `M`, `Q`, and `B` differ across domains and should remain explicit. Plasma free energy, neural synaptic-filter storage, Climate-A QG perturbation energy, and Climate-B barotropic kinetic energy are not one common physical quantity. Likewise, radial particle transport, pathway contribution, eddy heat transport, and jet-translation forcing have distinct semantics.

The matrix `B` is not a numerical convenience. It encodes the physically or experimentally admissible preparation space. In Neuro, a rank-one single afferent direction could not support a nontrivial optimizer-direction comparison, whereas the frozen two-pulse protocol supplies a rank-two reachable initial-state geometry without arbitrary latent-state kicks or time-dependent optimal control. In Plasma and the QG cases, full-state perturbations are admissible only because the represented state spaces have already been physically restricted.

## 6.3 Geometry, performance, and robustness are separate evidentiary layers

A distinct optimizer can be scientifically interesting without being practically consequential. Climate-A provides the clearest example: a 90-degree subspace separation coexists with only a 4.12% heat-performance gap. Conversely, the Plasma and Neuro examples show that moderate-to-large geometric differences can coincide with substantial target loss.

Climate-B adds a third layer. Even an apparently maximal fixed-resolution performance gap cannot support a physical demonstration when the prescribed refinement checks fail. The audit is therefore evidence for rejection discipline, not for a strong atmospheric objective-nonredundancy effect.

## 6.4 Limitations and protected future work

All demonstrations use linear tangent dynamics. They do not establish nonlinear saturation, turbulence-level transport prediction, in-vivo neural causal efficacy, realized nonlinear jet displacement, climate-change prediction, or operational forecast skill. The neural model omits propagation delays and uses a deliberately low-dimensional preparation geometry that does not reach a negative cumulative pathway branch. Climate-A is an idealized two-layer QG system. Climate-B is a failed one-shot refinement case and cannot be promoted by its fixed-resolution structure.

The study-specific 20-degree and 0.25 thresholds are operational classification rules rather than universal constants. The targeted literature audits support cautious `to our knowledge` formulations but do not prove novelty by absence. Bibliographic metadata cleanup, including final publication-status verification for Ogino et al. (2026), remains an editorial task.

Protected future directions include delayed or pathway-expanded neural models, higher-fidelity geophysical models, realistic fusion applications, Power-Grid and Photonics/Waves applications, and MODES/CONT/CASCADE extensions. None is required to support the present manuscript, and none is executed or implied by this revision.

---

# 7. Conclusion

A positive energy, storage, or state objective is not automatically equivalent to a separately defined signed physical channel. The practically relevant question is not only whether the corresponding optimizers differ geometrically, but whether substituting the conventional positive-objective optimum causes a meaningful loss in the channel of interest and whether that conclusion survives the required robustness checks.

Across the three frozen robust case studies, the answer is deliberately nonuniform. The Plasma benchmark shows a large particle-transport penalty for the free-energy optimum. The constrained Neuro preparation problem shows a large pathway-performance penalty for the terminal-storage optimum. Climate-A shows that orthogonal optimal subspaces can nevertheless differ by only about 4.12% in cumulative poleward heat-transport performance. The separate Climate-B audit adds a negative methodological lesson: large fixed-resolution separation is not sufficient when refinement fails.

The manuscript therefore advances a physics-informed, prospectively frozen diagnostic workflow and a cross-domain evidence base, not a universal theorem of optimal perturbations. The magnitude and practical consequence of objective nonredundancy remain system-, horizon-, observable-, admissible-geometry-, and robustness-dependent.

---

# Supplement

## S1. Analysis freeze chronology and reproducibility protocol

The analysis record uses a version-controlled sequence of model/candidate freezes, numerical qualifications, execution specifications, execution releases, frozen execution results, literature-positioning audits, result-integration freezes, manuscript claim freezes, and the present structure freeze. The manuscript-facing terminology is **pre-specified and frozen before objective-separation evaluation** or **prospectively frozen in the version-controlled analysis record before effect inspection**.

Across applications, execution used fixed horizon ladders and prospectively defined structural/numerical gates. The common factor-of-two convention is: physical storage is `S_M=1/2 x^\dagger Mx`, whereas the finite-time terminal operator is written for `x^\dagger Mx`; this does not alter optimizer directions or normalized performance gaps.

The common study-specific strong application rule is `\vartheta>=20 deg` and `\Delta_Q>=0.25` on at least two neighboring frozen horizons, subject to all application-specific gates. Climate-A and Climate-B additionally use explicit cross-resolution objective-value and common-subspace tests. Failure of a frozen gate is retained as the result; no parameter, horizon, resolution, objective, or admissible geometry is changed to repair it.

## S2. Plasma detailed specification and numerical checks

The frozen D10-ZF point is `U(x)=cos x`, `L_x=2pi`, `k_y=C=kappa=1`, `N(x)=0`, with Pilot-0.2 damping `A=A_0-0.020I`. At resolution `K`, modes `m=-K,...,K` are retained and the state is ordered as all `phi_m` followed by all `eta_m`. With `Delta=diag[-(m^2+k_y^2)]`,

\[
M=
\begin{pmatrix}-\Delta&0\\0&I\end{pmatrix},
\qquad
Q_\Gamma=
\frac{k_y}{2}
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}.
\]

The input geometry is `B=I`, `R_in=M`. The frozen resolutions `K=32,64,96` have state dimensions 130, 258, and 386; the horizon ladder is `T={0.25,0.5,1,2,4,8}`.

All `S0-S5` gates pass. Maximum reported numerical defects include raw Hermiticity defects below about `3.7e-13`, optimizer-normalization error `1.4e-15`, transport eigen-residual `3.2e-14`, direct terminal-energy error `7.2e-14`, and direct cumulative-flux integration error `7.1e-8`. Projecting `K=96` optimizers onto the common `|m|<=32` subspace gives overlap one to floating-point precision and unresolved energy below about `2e-15`. The full horizon ledger is stored in `research/d10_zf_pilot_0_2_execution_data.csv`.

## S3. Neuro detailed specification and numerical checks

The frozen state is ordered region-major in `(v,z)` coordinates for V1 and V4 populations `(SS,SP,II,DP)`. The operating point is `x*=0`; synaptic time constants are `(2,2,16,28)` ms. The positive matrix is

\[
M={\rm diag}(
250000,1,250000,1,3906.25,1,1275.51020408163,1,
250000,1,250000,1,3906.25,1,1275.51020408163,1).
\]

For the frozen V1-SP -> V4-SS pathway,

\[
(A_{j\to i})_{10,3}=16666.6666666667\ {\rm s}^{-1},
\]

and

\[
(Q_{j\to i})_{10,3}=(Q_{j\to i})_{3,10}=8333.33333333333.
\]

The afferent vector is `b_aff,V1=16000e_2`. Two fixed unit-height 1-ms pulses occupy `[-3,-2]` ms and `[-17,-16]` ms relative to observation onset. Their effective propagated columns define `B`; `rank(B)=2`, the storage/input-whitened condition number is `34.294<100`, and `R_in=I_2`.

All frozen structural and numerical gates pass. The maximum semigroup error is `6.636e-14`; maximum primary/adaptive cumulative-operator disagreement is `2.291e-12`; raw finite-time Hermiticity residuals are below `1.361e-13`; direct trajectory reproduction errors are below `5e-10`. The full ledger is stored in `research/neuro/neuro_pilot_0_1_execution_data.csv` and `research/neuro/neuro_pilot_0_1_execution_results.md`.

## S4. Climate-A detailed specification and numerical checks

Climate-A uses the basis

\[
\phi_{mn}(x,y)
=
\exp\left(i\frac{2\pi m}{L_x}x\right)
\sin\left(\frac{\pi n}{L_y}y\right),
\qquad m\ne0,\ n\ge1,
\]

with mode state `x_mn=(psi_mn,tau_mn)^T` and exact real-field conjugacy. With `L_ref=L_D`, `U_ref=beta L_D^2=16 m s^-1`, `tau_ref=62500 s`, define

\[
k_m^*=\frac{2\pi m}{30},
\quad
\ell_n^*=\frac{\pi n}{10},
\quad
a_{mn}=k_m^{*2}+\ell_n^{*2},
\quad
b_{mn}=a_{mn}+1.
\]

The frozen modal blocks are

\[
A_{mn}=
\begin{pmatrix}
-r^*+ik_m^*/a_{mn}&-ik_m^*U^*\\
ik_m^*U^*(1-a_{mn})/b_{mn}&-r^*+ik_m^*/b_{mn}
\end{pmatrix},
\]

\[
M_{mn}=150
\begin{pmatrix}a_{mn}&0\\0&b_{mn}\end{pmatrix},
\qquad
Q_{{\rm heat},mn}=75
\begin{pmatrix}0&-ik_m^*\\ik_m^*&0\end{pmatrix},
\]

with `U^*=1/2` and `r^*=0.072337962962963`.

All mandatory algebraic, augmented-exponential/Lyapunov-tail, eigenpair, terminal-energy, direct heat-integral, and resolution gates pass. For all six horizons the objective values are invariant to reported precision under `(12,12)->(16,16)->(24,24)`, common-space captured mass is one, optimal-subspace rank remains two, and cross-resolution principal angles remain below `1.5e-6 deg`. The full ledger is stored in `research/climate/climate_ocean_pilot_0_1_execution_data.csv`.

## S5. Climate-B one-shot robustness-rejection case

### S5.1 Frozen model, metric, and signed channel

Climate-B is the single authorized equivalent-barotropic Bickley-jet candidate,

\[
\partial_t\zeta'
+U(y)\partial_x\zeta'
+[\beta-U''(y)]\partial_x\psi'
=-r\zeta',
\qquad
\zeta'=\nabla^2\psi',
\]

\[
U(y)=U_0\operatorname{sech}^2(y/L),
\]

at the fixed point

\[
\beta=1.6\times10^{-11}\ {\rm m^{-1}s^{-1}},
\quad U_0=20\ {\rm m\,s^{-1}},
\quad L=1000\ {\rm km},
\quad r=(10\ {\rm d})^{-1},
\]

\[
L_x=20000\ {\rm km},
\qquad L_y=10000\ {\rm km},
\qquad
\tau_{\rm ref}=L/U_0=50000\ {\rm s}.
\]

The positive metric is perturbation kinetic energy. The poleward jet-translation tangent is `g(y)=-U'(y)`, and the signed channel is

\[
q_{\rm shift}(t)
=
\frac{\int g(y)[-\partial_y\overline{u'v'}]dy}
{\int g(y)^2dy}.
\]

Positive sign denotes forcing in the poleward-translation direction. The cumulative `J_shift` is only cumulative eddy forcing/impulse of the infinitesimal translation coordinate under frozen tangent dynamics; it is not realized nonlinear jet displacement.

The positive-zonal-Fourier / centered-sine Galerkin representation retains `k_x!=0` eddies, exact real-field conjugacy, Dirichlet walls, and both meridional parity sectors. `A_K` preserves parity whereas `Q_shift,K` couples opposite parity. The retained eddy state is admissible, so `B=I`, `R_in=M_K`.

### S5.2 Frozen protocol and pre-effect qualification

The nested ladder is

| role | `(M_x,N_y)` | complex dimension |
|---|---:|---:|
| structural smoke | `(8,16)` | 128 |
| coarse audit | `(12,24)` | 288 |
| primary | `(16,32)` | 512 |
| confirmation | `(20,40)` | 800 |
| high-resolution audit | `(24,48)` | 1152 |

The executed horizon ladder is `T/tau_ref={0.25,0.5,1,2,4,8}`.

Before finite-time execution, the 512-versus-1024 Gauss-Legendre assembly audit passed with worst relative discrepancy `2.92e-14`; `M_K` was positive definite; `Q_shift,K` was Hermitian and indefinite; parity-forbidden residuals were at roundoff; the predeclared `c_11=1,c_12=+/-i` sign witness reproduced the channel directly to about `1e-14` relative; and every frozen resolution was spectrally stable with `alpha(A_K)=-0.1 d^-1`.

### S5.3 Local finite-time gates passed

At primary, confirmation, and high audit, all local finite-time gates passed. Across the mandatory runs:

- worst raw Hermiticity residual: `5.49e-15`;
- worst Lyapunov-tail / independent block-exponential discrepancy: `1.06e-12`;
- worst extremal eigenpair residual: `2.57e-15`;
- worst normalization error: `8.89e-16`;
- worst Rayleigh residual: `2.28e-15`;
- worst direct terminal-energy reproduction error: `2.28e-15`;
- worst direct reconstructed Reynolds-stress cumulative-shift error: `9.68e-14`;
- minimum finite-time energy-operator eigenvalue: `1.0498e-2`.

Thus the eventual failure is not an algebraic, integration, eigensolver, PSD, or direct physical-reproduction failure.

### S5.4 Fixed-resolution observation, with required failure qualification

At every individual frozen truncation the same-resolution target-performance gap is `Delta_shift=1` to roundoff and optimizer angles are large. At several primary-resolution horizons the angle is 90 degrees; at the two shortest horizons it is approximately 78.34 and 77.45 degrees. This behavior has a clean parity explanation: the energy optimum remains in one preserved parity sector and hence has zero cumulative signed shift forcing, whereas the shift optimum mixes opposite parity sectors. **These are qualified fixed-truncation observations only and are rejected as robust Climate evidence because the mandatory refinement gates fail.**

The pre-specified cross-resolution protocol required, for both primary-to-confirmation and confirmation-to-high refinement,

\[
\epsilon_Y\le0.02,
\qquad
Y\in\{G_M,J_{\rm shift}^+,|J_{\rm shift}^-|\},
\]

together with common-space captured mass `mu_c>=0.95` and largest common-space principal angle no greater than 10 degrees for both objective optima.

### S5.5 Complete resolution failure

Zero of the six frozen horizons passes the full resolution protocol.

At `T/tau_ref=0.25`, the positive-shift objective changes by approximately 7.08% from primary to confirmation and 4.62% from confirmation to high audit, exceeding the 2% rule. Both optima also migrate from zonal mode `m=16` to `20` to `24`, producing zero captured common-space mass in the lower zonal subspace.

At `T/tau_ref=8`, where the optima are no longer pinned directly to the immediate cutoff, the failure persists. Primary-to-confirmation captured masses are `0.7281` for energy and `0.7513` for shift; confirmation-to-high masses are `0.7808` and `0.8337`. The positive signed objective changes by approximately 8.35% and 3.60% over the two refinement steps, again outside the 2% rule, and the common-space angle gates also fail.

| `T/tau_ref` | robust? | principal frozen failure features |
|---:|---|---|
| 0.25 | FAIL | signed-objective nonconvergence; zero captured mass from cutoff migration |
| 0.5 | FAIL | signed-objective nonconvergence; zero captured mass from cutoff migration |
| 1 | FAIL | objective-value failures and cutoff migration |
| 2 | FAIL | objective-value plus common-space mass/angle failures |
| 4 | FAIL | signed-objective plus common-space mass/angle failures |
| 8 | FAIL | objective nonconvergence; `mu_c<0.95`; principal-angle failures |

Hence

\[
\boxed{\text{0 of 6 frozen horizons resolution robust}}
\]

and the required two neighboring robust horizons do not exist.

### S5.6 Frozen verdict and stop rule

The exact frozen verdict is

\[
\boxed{\text{CLIM-B-FAIL — resolution robustness failure}}.
\]

The large fixed-resolution angles, `Delta_shift=1`, and parity mechanism are retained only with this resolution-failure qualification. They may not be presented as a robust strong Climate result.

No Climate-B repair is part of this paper. The one-shot protocol forbids post-effect hyperdiffusion, scale-selective damping, extra resolution rungs, alternative `g=-U'`, masks, EOF restrictions, localization, changed horizons, or a third Climate candidate. Machine-readable frozen results are in `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`.

## S6. Additional frozen-data tables and citation metadata notes

### S6.1 Operational study rules and representative outcomes

This is the supplement placement of the former Main Table 2.

| Case | Operational rule | Representative frozen outcome | Robustness status |
|---|---|---|---|
| Plasma `P2-A` | original `S0-S5`; common `theta,Delta` reported for comparison | `T=1`: `theta=53.40 deg`, `Delta_Gamma=0.504` | converged across `K=32,64,96` |
| Neuro `NEURO-STRONG` | `theta>=20 deg`, `Delta_Q>=0.25` on neighboring horizons | 112/224 ms: `Delta_Q=0.529/0.818` | all frozen structural/direct gates pass |
| Climate-A `CLIM-WEAK` | same strong thresholds plus full refinement protocol | `T/tau_ref=8`: `90 deg`, `Delta_heat=0.0412` | all six horizons robust |
| Climate-B | same strong thresholds plus full refinement protocol | striking fixed-resolution separation only | `CLIM-B-FAIL — resolution robustness` |

### S6.2 Frozen machine-readable sources

- Plasma: `research/d10_zf_pilot_0_2_execution_data.csv`
- Neuro: `research/neuro/neuro_pilot_0_1_execution_data.csv`
- Climate-A: `research/climate/climate_ocean_pilot_0_1_execution_data.csv`
- Climate-B: `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`

No figure or table may instantiate model generators, solve new eigensystems, add horizons, interpolate or smooth scientific values, or rerun trajectories. If a desired display is unsupported by frozen stored values, it must be simplified or omitted.

### S6.3 Bibliography normalization status

Bibliographic metadata remain restricted to already approved positioning sources. `Ogino2026` remains an editorial metadata-verification item before submission; this does not authorize a new novelty search.

- **[Landreman2015]** Landreman, M., Plunk, G. G. & Dorland, W. (2015). “Generalized universal instability: transient linear amplification and subcritical turbulence.” *Journal of Plasma Physics* **81**, 905810501. DOI: `10.1017/S0022377815000495`.
- **[Foures2014]** Foures, D. P. G., Caulfield, C. P. & Schmid, P. J. (2014). “Optimal mixing in two-dimensional plane Poiseuille flow at finite Péclet number.” *Journal of Fluid Mechanics* **748**, 241–277. DOI: `10.1017/jfm.2014.182`.
- **[Hennequin2012]** Hennequin, G., Vogels, T. P. & Gerstner, W. (2012). “Non-normal amplification in random balanced neuronal networks.” *Physical Review E* **86**, 011909. DOI: `10.1103/PhysRevE.86.011909`.
- **[Bondanelli2020]** Bondanelli, G. & Ostojic, S. (2020). “Coding with transient trajectories in recurrent neural networks.” *PLoS Computational Biology* **16**(2), e1007655. DOI: `10.1371/journal.pcbi.1007655`.
- **[Friston2003]** Friston, K. J., Harrison, L. & Penny, W. (2003). “Dynamic causal modelling.” *NeuroImage* **19**(4), 1273–1302. DOI: `10.1016/S1053-8119(03)00202-7`.
- **[Daunizeau2011]** Daunizeau, J., Preuschoff, K., Friston, K. & Stephan, K. E. (2011). “Optimizing Experimental Design for Comparing Models of Brain Function.” *PLoS Computational Biology* **7**(11), e1002280. DOI: `10.1371/journal.pcbi.1002280`.
- **[Salfenmoser2022]** Salfenmoser, L. & Obermayer, K. (2022). “Nonlinear optimal control of a mean-field model of neural population dynamics.” *Frontiers in Computational Neuroscience* **16**, 931121. DOI: `10.3389/fncom.2022.931121`.
- **[Ogino2026]** Ogino, M. et al. (2026). “Designing optimal perturbation inputs for system identification in neuroscience.” *eLife reviewed preprint* 110030; reviewed-preprint v1 DOI `10.7554/eLife.110030.1`. **VERIFY FINAL PUBLICATION STATUS BEFORE SUBMISSION.**
- **[Farrell1982]** Farrell, B. F. (1982). “The Initial Growth of Disturbances in a Baroclinic Flow.” *Journal of the Atmospheric Sciences* **39**, 1663–1686.
- **[Farrell1985]** Farrell, B. F. (1985). “Transient Growth of Damped Baroclinic Waves.” *Journal of the Atmospheric Sciences* **42**, 2718–2727.
- **[FarrellIoannou1994]** Farrell, B. F. & Ioannou, P. J. (1994). “A Theory for the Statistical Equilibrium Energy Spectrum and Heat Flux Produced by Transient Baroclinic Waves.” *Journal of the Atmospheric Sciences* **51**(19), 2685–2698.
- **[KimMorgan2002]** Kim, H. M. & Morgan, M. C. (2002). “Dependence of Singular Vector Structure and Evolution on the Choice of Norm.” *Journal of the Atmospheric Sciences* **59**, 3099–3116.
- **[Kuang2004]** Kuang, Z. (2004). “The Norm Dependence of Singular Vectors.” *Journal of the Atmospheric Sciences* **61**, 2943–2949.
- **[Sevellec2008]** Sévellec, F., Huck, T., Ben Jelloul, M., Vialard, J. & Fedorov, A. V. (2008). “Optimal Surface Salinity Perturbations of the Meridional Overturning and Heat Transport in a Global Ocean General Circulation Model.” *Journal of Physical Oceanography* **38**(12). DOI: `10.1175/2008JPO3875.1`.

---

**Revision boundary:** every equation, parameter, numerical result, classification, literature-positioning statement, and robustness interpretation in Draft 0.3 is copied, condensed, or reorganized from already frozen repository sources. Revision 0.3 introduces no new scientific result, figure production, journal targeting, submission preparation, novelty search, or protected-branch work.
