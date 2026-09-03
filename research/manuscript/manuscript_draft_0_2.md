# Diagnosing objective nonredundancy in stable linear dynamics: a physics-informed finite-time workflow across plasma, neural and geophysical models

**Draft:** 0.2  
**Status:** STRUCTURAL REVISION — FROZEN-EVIDENCE ONLY  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md` and `research/master/manuscript_draft_review_gate_0_1.md`  
**Scope:** writing and reproducibility exposition only. No new simulation, horizon, parameter, objective, pathway, admissible geometry, or novelty claim is introduced.

## Abstract

Finite-time optimal-perturbation studies often use a positive energy, storage, or state metric as a proxy for the physical quantity of interest. We ask a narrower question: after the dynamics, admissible perturbations, positive metric, and a separately defined signed physical channel have all been fixed, how redundant are the two resulting finite-time optima? We apply the same pre-specified and version-controlled workflow to three stable linear models. In a drift-wave/zonal-flow plasma benchmark, the free-energy-optimal perturbation misses 50.4% of the maximum positive cumulative particle transport at the frozen horizon `T=1`. In a two-source V1/V4 canonical-microcircuit model, terminal synaptic-filter-storage and cumulative V1-SP -> V4-SS pathway objectives select markedly different two-pulse preparations, with performance gaps 0.529 and 0.818 at 112 and 224 ms. In a damped two-layer quasigeostrophic model, however, energy- and poleward-heat-optimal subspaces are orthogonal at the longest frozen horizon while the heat-performance gap is only 0.0412, so the energy optimum retains 95.88% of maximal cumulative poleward heat transport. The nonuniform outcome shows why optimizer geometry and target-performance loss should be reported separately. The contribution is a physics-informed diagnostic workflow and cross-domain physical interpretation, not a new general theory of optimal perturbations.

---

# 1. Introduction

Optimal-perturbation methods ask which admissible disturbance produces the largest response over a prescribed horizon. Positive energy or storage measures are natural objectives because they are stable metrics, often physically interpretable, and mathematically convenient. Yet the scientific target may be a different object: a signed radial particle flux, a meridional heat flux, or the signed contribution of a specified physiological pathway to a storage-rate balance. A positive state metric and a signed channel therefore answer different questions even when both are evaluated on the same linear dynamics.

The mathematical tools needed to compare such questions are established. Transient amplification in stable systems, singular vectors, quadratic finite-time outputs, Gramian and adjoint methods, and norm dependence all have extensive prior art. Stable plasma transient amplification has been studied directly [Landreman2015]; damped baroclinic transient growth is classical [Farrell1985]; atmospheric and oceanic singular vectors depend on the chosen norm or target [KimMorgan2002; Kuang2004]; energy-optimal and mixing-oriented perturbations can differ in fluid mechanics [Foures2014]; and heat-transport-optimal initial perturbations exist in stable ocean models [Sevellec2008]. Neural systems likewise have established literatures on non-normal amplification, transient trajectory design, DCM experimental design, and neural-mass optimal control [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026].

The present contribution is therefore not the generic statement that different objectives can have different optimizers. We instead use one controlled workflow in which the linear generator, positive metric, signed channel, admissible perturbation geometry, input cost, horizon ladder, and numerical gates are specified and frozen before objective-separation results are inspected. We then report both geometric separation and the actual loss in the physical channel incurred by using the conventional positive-objective optimum as a proxy.

Three deliberately different cases test that workflow. A drift-wave/zonal-flow plasma model supplies a strong signed-transport anchor. A two-source canonical-microcircuit model tests a low-dimensional, experimentally interpretable preparation geometry rather than arbitrary full-state actuation. A damped two-layer quasigeostrophic model supplies a weak contrast case in which optimal structures differ sharply while target performance remains almost redundant. The nonuniformity is part of the result: the workflow is intended to diagnose objective nonredundancy, not to maximize it.

Our manuscript-level claim is correspondingly limited: storage/state-optimal and physical-channel-optimal perturbations need not be redundant, but the magnitude and practical consequence of their separation depend on the system, horizon, observable, and admissible perturbation geometry.

---

# 2. Common finite-time framework and study design

## 2.1 Frozen linear problem

Each application is represented by an autonomous stable linear system

\[
\dot x=Ax,
\qquad x(0)=Bu,
\]

with a positive input-cost metric

\[
u^\dagger R_{\rm in}u=1,
\qquad R_{\rm in}=R_{\rm in}^\dagger\succ0.
\]

The matrix `B` is part of the physical specification: it identifies which initial perturbations can actually be prepared. Introducing whitened input coordinates

\[
w=R_{\rm in}^{1/2}u,
\qquad \|w\|_2=1,
\]

places all optimizer comparisons on the same admissible input-cost sphere.

## 2.2 Positive state/storage objective

Let

\[
S_M(x)=\frac12 x^\dagger Mx,
\qquad M=M^\dagger\succ0.
\]

For compactness, the finite-time operator is written for the doubled quadratic form `x^dagger M x=2S_M`:

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2}.
\]

The omitted common factor `1/2` has no effect on optimizer directions, gain ratios, or the channel-performance gaps used below. Whenever a physical storage itself is described, the `1/2` convention is restored explicitly.

The leading eigenspace of `K_M(T)` defines the terminal positive-objective optimum. Its physical meaning is domain specific: free energy in Plasma, synaptic-filter storage in Neuro, and QG perturbation energy in Climate/Ocean.

## 2.3 Signed physical channel

A **physical channel** here means a separately defined signed quadratic transfer, transport, exchange, or pathway-contribution observable. It need not be a conserved flux and the three applications do not share a common physical unit or conservation law. Its instantaneous form is

\[
q_Q(t)=x(t)^\dagger Qx(t),
\qquad Q=Q^\dagger,
\]

and its cumulative value is

\[
J_Q(T)=\int_0^T x(t)^\dagger Qx(t)\,dt.
\]

Defining

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
\]

gives the whitened finite-time channel operator

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger P_Q(T)BR_{\rm in}^{-1/2}.
\]

Its largest and smallest eigenvalues are the maximum and minimum cumulative signed channel values reachable on the frozen admissible perturbation space.

## 2.4 Geometry and performance diagnostics

When the leading eigendirections are nondegenerate, the optimizer angle is

\[
\vartheta(T)=\arccos\!\left|\langle w_M^\star,w_Q^\star\rangle\right|.
\]

When symmetry produces exact degeneracy, as in the QG Fourier representation, we compare the corresponding leading subspaces using conservative principal angles.

Geometric nonidentity is not itself a measure of practical loss. We therefore also evaluate

\[
\Delta_Q(T)=
\frac{J_Q^+(T)-J_Q(T;w_M^\star)}{J_Q^+(T)},
\]

whenever `J_Q^+(T)>0`. Thus `Delta_Q=0` means that the positive-objective optimizer is also channel-optimal, whereas `Delta_Q=0.5` means that it realizes only half of the maximum positive cumulative channel.

## 2.5 Pre-specification, freezing, and operational verdict rules

The model, parameters, `M`, `Q`, `B`, `R_in`, horizon ladders, numerical checks, and verdict rules were prospectively frozen in the version-controlled analysis record before objective-separation effects were inspected. We use this wording rather than implying registration in an external preregistration registry.

For the cross-domain application pilots, a study-specific **strong objective-separation** criterion required both

\[
\vartheta\ge20^\circ,
\qquad
\Delta_Q\ge0.25
\]

on at least two neighboring frozen horizons, together with the domain-specific structural and numerical gates. These thresholds are operational rules for this study, not universal physical constants. The Plasma benchmark also retained its separately frozen `S0-S5` gate structure; the common `vartheta`/`Delta_Q` diagnostics are reported for cross-domain comparison without redefining the original P2-A verdict.

| Diagnostic layer | Operational rule in this study | Interpretation |
|---|---|---|
| Spectral/structural qualification | stable frozen operator; valid `M`, `Q`, `B`, numerical representation | prerequisite, not evidence of objective separation |
| Geometry | `vartheta` or conservative subspace angle | nonidentity of optimal preparations/structures |
| Performance | `Delta_Q` | fraction of maximum positive channel lost by using the positive-objective optimum |
| Strong application separation | `vartheta >= 20 deg` and `Delta_Q >= 0.25` on at least two neighboring horizons | study-specific classification only |
| Robustness | domain-specific residual, trajectory/integral, conditioning, and/or resolution gates | protects against numerical or representation artifacts |

## 2.6 Domain semantics

| Domain | Positive objective | Signed physical channel | Admissible geometry and cost |
|---|---|---|---|
| Plasma/D10-ZF | free energy | radial particle transport | full frozen Galerkin perturbation space; `B=I`, `R_in=M` |
| Neuro/CMC | terminal model-internal synaptic-filter storage | V1-SP -> V4-SS pathway contribution to storage rate | rank-two fixed two-pulse afferent preparation; `R_in=I_2` |
| Climate/Ocean QG | QG perturbation energy | meridional eddy heat transport | balanced QG eddy state space; `B=I`, `R_in=M_K` |

These labels are not interchangeable. In particular, the neural positive metric is not metabolic, thermodynamic, or total physiological brain energy.

---

# 3. Application methods

## 3.1 Plasma: D10-ZF drift-wave/zonal-flow model

For one nonzero poloidal wavenumber `k_y`, the frozen continuous linearization is

\[
\partial_t\Delta_k\hat\varphi
+i k_y U\,\Delta_k\hat\varphi
-i k_y U''\hat\varphi
=C(\hat\varphi-\hat\eta),
\]

\[
\partial_t\hat\eta+i k_y U\hat\eta
=C(\hat\varphi-\hat\eta)-i\kappa k_y\hat\varphi,
\]

with

\[
\Delta_k=\partial_x^2-k_y^2,
\qquad U(x)=\cos x,
\]

and the frozen values

\[
L_x=2\pi,
\quad k_y=1,
\quad C=1,
\quad \kappa=1,
\quad N(x)=0.
\]

The radial Fourier basis is `e_m(x)=L_x^{-1/2}e^{imx}`. At resolution `K`, modes `m=-K,\ldots,K` are retained and the state is ordered

\[
z=(\phi_{-K},\ldots,\phi_K,\eta_{-K},\ldots,\eta_K)^T.
\]

Writing `Delta=diag[-(m^2+k_y^2)]` and `mathsf U` for Galerkin multiplication by `cos x`, the undamped block generator is

\[
A_0=
\begin{pmatrix}
\Delta^{-1}(-ik_y\mathsf U\Delta+ik_y\mathsf U_{xx}+CI) & -C\Delta^{-1}\\
(C-i\kappa k_y)I & -CI-ik_y\mathsf U
\end{pmatrix},
\]

where `mathsf U_xx=-mathsf U`. Pilot 0.2 applies the prospectively selected uniform damping shift

\[
A=A_0-\nu_\perp I,
\qquad \nu_\perp=0.020.
\]

The nondimensional D10-ZF time unit is retained, with `tau_ref=1`; no conversion to dimensional seconds is asserted.

The free-energy quadratic form is

\[
E=\frac12 z^\dagger Mz,
\qquad
M=\begin{pmatrix}-\Delta&0\\0&I\end{pmatrix}\succ0.
\]

The signed outward radial particle flux is

\[
\Gamma=k_y\,\operatorname{Im}(\eta^\dagger\phi)
=z^\dagger Q_\Gamma z,
\]

with

\[
Q_\Gamma=\frac{k_y}{2}
\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}.
\]

The full retained perturbation space is admissible, so

\[
B=I,
\qquad R_{\rm in}=M.
\]

The frozen resolutions are `K=32,64,96` and the horizon ladder is

\[
T\in\{0.25,0.5,1,2,4,8\}.
\]

## 3.2 Neuro: two-source V1/V4 canonical microcircuit

The neural pilot uses two cortical sources, V1 and V4, each with spiny-stellate (`SS`), superficial-pyramidal (`SP`), inhibitory-interneuron (`II`), and deep-pyramidal (`DP`) populations. Each population is represented by a second-order synaptic filter with first-order coordinates `(v_{r,p},z_{r,p})`, where `z=dot v`. The 16-dimensional state is ordered region-major as

\[
(v_{1,SS},z_{1,SS},v_{1,SP},z_{1,SP},v_{1,II},z_{1,II},v_{1,DP},z_{1,DP},
 v_{4,SS},z_{4,SS},v_{4,SP},z_{4,SP},v_{4,II},z_{4,II},v_{4,DP},z_{4,DP})^T.
\]

The frozen autonomous instantaneous-coupling CMC ODE is the linearization of the pinned SPM12 canonical-microcircuit state equation at the exact zero fixed point. Propagation delays are disabled for this first finite-dimensional pilot; this is a scope restriction, not a biological claim of zero conduction delay. The full generator is stable with

\[
\alpha(A)=-33.0964092356\ {\rm s}^{-1}.
\]

For each population with inverse synaptic time constant `kappa_p`, the model-internal filter storage is

\[
S_{r,p}=\frac12\left(z_{r,p}^2+\kappa_p^2v_{r,p}^2\right),
\]

so

\[
S=\frac12x^\dagger Mx,
\]

with `M` diagonal and positive. The frozen time constants are 2 ms (`SS`), 2 ms (`SP`), 16 ms (`II`), and 28 ms (`DP`) in each source. This quantity is a synaptic-filter state storage; no metabolic or thermodynamic interpretation is made.

The primary physiological channel is the prospectively selected forward connection

\[
\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS}.
\]

Decompose the linear generator as

\[
A=A_{\rm rest}+A_{j\to i},
\]

where `A_{j->i}` contains only the Jacobian contribution of this connection. In the frozen state ordering its only nonzero entry is

\[
(A_{j\to i})_{10,3}=16666.6666666667\ {\rm s}^{-1}.
\]

The pathway's signed contribution to the storage-rate balance is represented by

\[
Q_{j\to i}=\frac12\left(A_{j\to i}^\dagger M+MA_{j\to i}\right).
\]

Thus

\[
x^\dagger Q_{j\to i}x
\]

is the instantaneous contribution of that predefined pathway to the rate of the chosen synaptic-filter storage. Positive and negative values mean increasing or decreasing that storage rate through the pathway; they are **not** synonyms for excitatory and inhibitory synaptic signs.

Admissible preparations are not arbitrary hidden-state kicks. A single physiological afferent drive acts on V1-SS with vector

\[
b_{\rm aff,V1}=16000\,e_2.
\]

Two fixed rectangular 1-ms pulses end 2 ms and 16 ms before the autonomous observation window. Their amplitudes are the only optimization coordinates. The corresponding effective initial-state map is

\[
B=[b_1^{\rm eff},b_2^{\rm eff}],
\qquad
b_k^{\rm eff}=\int_{\tau_k}^{\tau_k+\delta}e^{As}b_{\rm aff,V1}\,ds,
\]

with `delta=1 ms`, `tau_1=2 ms`, and `tau_2=16 ms`. The two columns have rank two and pass the prospectively frozen storage-whitened conditioning criterion. Equal-width nonoverlapping pulses define the input-cost metric

\[
R_{\rm in}=I_2
\]

in pulse-amplitude coordinates only.

The reference time is the slowest local synaptic time constant,

\[
\tau_{\rm ref}=28\ {\rm ms},
\]

and the frozen horizons are

\[
T\in\{7,14,28,56,112,224\}\ {\rm ms}.
\]

## 3.3 Climate/Ocean: damped two-layer Phillips QG model

The geophysical pilot uses the linear damped two-layer Phillips quasigeostrophic system

\[
\partial_t q_i'+U_i\partial_xq_i'+\Pi_i\partial_x\psi_i'=-rq_i',
\qquad i=1,2,
\]

with

\[
q_1'=\nabla^2\psi_1'+F(\psi_2'-\psi_1'),
\qquad
q_2'=\nabla^2\psi_2'+F(\psi_1'-\psi_2'),
\]

\[
F=\frac{1}{2L_D^2},
\qquad U_1=+U,
\qquad U_2=-U,
\]

\[
\Pi_1=\beta+\frac{U}{L_D^2},
\qquad
\Pi_2=\beta-\frac{U}{L_D^2}.
\]

The frozen parameters are

\[
L_x=3.0\times10^7\ {\rm m},
\quad L_y=1.0\times10^7\ {\rm m},
\quad L_D=10^6\ {\rm m},
\]

\[
\beta=1.6\times10^{-11}\ {\rm m^{-1}s^{-1}},
\quad U=8\ {\rm m\,s^{-1}},
\quad r=(10\ {\rm d})^{-1}.
\]

The domain is periodic in `x`, with `psi_i'=0` at `y=0,L_y`. The eddy state excludes all zonal-mean modes (`k_x=0`). Introducing barotropic and baroclinic streamfunctions

\[
\psi=\frac{\psi_1'+\psi_2'}2,
\qquad
\tau=\frac{\psi_1'-\psi_2'}2,
\]

the perturbation energy is

\[
E=\frac12\int_\Omega\left(|\nabla\psi|^2+|\nabla\tau|^2+L_D^{-2}|\tau|^2\right)dA.
\]

The signed heat channel is the meridional eddy heat transport

\[
H_{\rm heat}=C_H\int_\Omega(\partial_x\psi)\tau\,dA,
\qquad C_H>0,
\]

with positive sign defined as northward/poleward transport. The cumulative objective is

\[
J_{\rm heat}(T)=\int_0^T x(t)^\dagger Q_{{\rm heat},K}x(t)\,dt.
\]

No absolute value or squared heat flux is substituted for this signed quantity.

The structure-preserving basis is

\[
\phi_{mn}(x,y)=
\exp\!\left(i\frac{2\pi m}{L_x}x\right)
\sin\!\left(\frac{\pi n}{L_y}y\right),
\]

with `m!=0` and `n>=1`. Mode-by-mode states are `x_{mn}=(psi_{mn},tau_{mn})^T`; real fields satisfy the exact conjugacy relation `x_{-m,n}=x_{m,n}^*`.

With

\[
L_{\rm ref}=L_D,
\qquad U_{\rm ref}=\beta L_D^2=16\ {\rm m\,s^{-1}},
\]

the frozen reference time is

\[
\tau_{\rm ref}=\frac{L_D}{U_{\rm ref}}
=62500\ {\rm s}=0.7233796296\ {\rm d}.
\]

In nondimensional coordinates, defining

\[
k_m^*=\frac{2\pi m}{30},
\quad \ell_n^*=\frac{\pi n}{10},
\quad a_{mn}=k_m^{*2}+\ell_n^{*2},
\quad b_{mn}=a_{mn}+1,
\]

gives the exact modal blocks

\[
A_{mn}=\begin{pmatrix}
-r^*+ik_m^*/a_{mn} & -ik_m^*U^*\\
ik_m^*U^*(1-a_{mn})/b_{mn} & -r^*+ik_m^*/b_{mn}
\end{pmatrix},
\]

\[
M_{mn}=S^*\begin{pmatrix}a_{mn}&0\\0&b_{mn}\end{pmatrix},
\qquad
Q_{{\rm heat},mn}=\frac{S^*}{2}
\begin{pmatrix}0&-ik_m^*\\ik_m^*&0\end{pmatrix},
\]

with `S^*=150`, `U^*=1/2`, and `r^*=0.072337962962963`. The global matrices are block diagonal. The balanced eddy state itself is admissible, hence

\[
B=I,
\qquad R_{\rm in}=M_K.
\]

The nested qualified resolution ladder is `(4,4),(8,8),(12,12),(16,16),(24,24)`, with `(12,12)` primary, `(16,16)` confirmation, and `(24,24)` high-resolution audit. The frozen horizons are

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

---

# 4. Results

## 4.1 Plasma: strong signed-transport anchor

The frozen D10-ZF operators are spectrally stable at all three reported resolutions:

\[
\alpha(A_{32})=-0.0075786,
\quad
\alpha(A_{64})=-0.0133818,
\quad
\alpha(A_{96})=-0.0154924.
\]

Nevertheless, finite-time free-energy amplification exceeds unity at every frozen horizon. The cumulative particle-transport operator has both positive and negative extrema over the full admissible state space.

At the representative frozen horizon `T=1`,

\[
G_E=1.8782758,
\qquad
J_\Gamma^+=0.3535169,
\qquad
J_\Gamma^-=-0.1462216.
\]

The free-energy-optimal perturbation yields

\[
J_\Gamma(w_E^\star)=0.1752252,
\]

so

\[
\Delta_\Gamma=0.5043372,
\qquad
\vartheta=53.396^\circ.
\]

Thus the free-energy optimum misses approximately 50.4% of the maximum positive cumulative particle transport at this horizon. The mismatch is not a truncation artifact: scalar objectives and projected optimizer structure are converged across `K=32,64,96` to numerical precision on the common resolved subspace. The two optimizers also differ physically in radial Fourier support, potential/density composition, and relative phase. The least-damped modal trajectory decays while finite-time optimal perturbations transiently amplify.

This benchmark therefore supports, locally and without a universality claim,

\[
\text{modal stability}\neq\text{finite-time free-energy optimality}\neq\text{finite-time particle-transport optimality}.
\]

Stable plasma transient amplification itself is established prior art [Landreman2015], and objective-dependent optimizers are known in adjacent fluid and ocean settings [Foures2014; Sevellec2008]. The role of the Plasma result here is to provide a strong, resolution-robust signed-transport anchor for the common workflow.

## 4.2 Neuro: strong nonredundancy in a constrained two-pulse preparation

The frozen V1/V4 CMC generator is stable and the two-pulse preparation map has rank two with acceptable storage-whitened conditioning. The terminal synaptic-filter-storage optimum and the cumulative V1-SP -> V4-SS pathway-contribution optimum satisfy the study-specific strong criterion at two neighboring long horizons:

\[
T=112\ {\rm ms}:
\qquad
\vartheta=46.824271^\circ,
\quad
\Delta_Q=0.529017,
\]

\[
T=224\ {\rm ms}:
\qquad
\vartheta=65.058256^\circ,
\quad
\Delta_Q=0.817841.
\]

The result is directly interpretable in the admissible preparation coordinates. At long horizons the pathway-optimal unit-cost mixture is approximately

\[
w_Q\approx(+0.9924,-0.1230),
\]

whereas the terminal-storage optimum uses same-sign pulse mixtures,

\[
w_M(112\,\mathrm{ms})\approx(+0.7687,+0.6396),
\]

\[
w_M(224\,\mathrm{ms})\approx(+0.5300,+0.8480).
\]

Thus the pathway optimum combines a dominant recent pulse with a small opposite-sign older component, whereas the long-horizon storage optimum combines the two fixed pulse components with the same sign.

The full-state instantaneous pathway matrix is indefinite, but the frozen two-dimensional admissible preparation geometry reaches only positive cumulative channel values over the tested horizon ladder: the minimum eigenvalue of `K_Q(T)` remains positive. The result therefore does **not** demonstrate experimentally reachable negative cumulative pathway transfer. Its narrower claim is strong nonredundancy between terminal synaptic-filter-storage optimality and positive cumulative pathway-contribution optimality on a physically motivated two-pulse preparation space.

Non-normal neural amplification, transient trajectory design, DCM input design, and neural-mass optimal control are established [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026]. To our knowledge, the targeted literature does not already contain this same stable CMC/DCM problem in which terminal synaptic-filter storage and the cumulative contribution of a predefined V1-SP -> V4-SS pathway are separately optimized over the same fixed rank-two two-pulse preparation coordinates.

## 4.3 Climate/Ocean: a robust weak contrast

The damped two-layer QG operator is spectrally stable throughout the qualified resolution ladder, with

\[
\alpha(A_K)=-0.1\ {\rm d}^{-1}.
\]

At the first five frozen horizons, the energy- and poleward-heat-optimal perturbations are nearly redundant: they occupy the same modal support, the conservative optimizer/subspace angle remains small, and the heat-performance gap stays below about `0.00317`.

At the longest horizon,

\[
T/\tau_{\rm ref}=8,
\]

the optimal modal supports switch to

\[
(|m|,n)_E=(3,2),
\qquad
(|m|,n)_{\rm heat}=(4,2).
\]

The corresponding optimal subspaces are orthogonal,

\[
\vartheta_{\rm sub}=90^\circ.
\]

Yet the maximum cumulative poleward heat transport is

\[
J_{\rm heat}^+=1.54448995,
\]

while the best heat transport available within the energy-optimal subspace is

\[
J_{\rm heat|E}^{\rm best}=1.48088082.
\]

Hence

\[
\Delta_{\rm heat}=0.04118455,
\]

and the energy-optimal subspace retains approximately 95.88% of the maximum cumulative poleward heat transport. The heat optimum is more strongly baroclinic and occupies the shorter zonal scale `|m|=4`, but that clear structural difference has only a small target-performance consequence.

This is the central weak contrast of the study:

\[
\boxed{\text{large optimizer/subspace separation does not imply a large objective-performance gap}.}
\]

Transient growth in damped baroclinic systems, QG singular vectors, norm dependence, transient heat flux, and heat-transport-optimal perturbations all have substantial prior art [Farrell1982; Farrell1985; FarrellIoannou1994; KimMorgan2002; Kuang2004; Sevellec2008]. To our knowledge, the targeted literature does not report the exact same-system comparison of QG perturbation-energy optimality with signed cumulative eddy-heat-transport optimality in this stable damped two-layer Phillips-QG tangent model. We use the result as a controlled methodological contrast, not as a strong novelty claim.

---

# 5. Cross-domain synthesis

The three frozen cases form an evidence hierarchy rather than three replications of one physical effect.

| Domain | Positive objective | Signed channel | Frozen role | Representative result |
|---|---|---|---|---|
| Plasma/D10-ZF | free energy | cumulative radial particle transport | `P2-A`, strong anchor | `T=1`: `vartheta=53.40 deg`, `Delta_Gamma=0.504` |
| Neuro/CMC | terminal synaptic-filter storage per pulse cost | cumulative V1-SP -> V4-SS pathway contribution | `NEURO-STRONG` | 112/224 ms: `Delta_Q=0.529/0.818` |
| Climate/Ocean QG | QG perturbation energy | cumulative poleward eddy heat transport | `CLIM-WEAK`, contrast | `T/tau_ref=8`: `90 deg`, `Delta_heat=0.0412` |

The shared diagnostic lesson is that **geometric nonidentity and decision relevance are different questions**. `vartheta` asks whether the optimal admissible structures differ. `Delta_Q` asks whether that difference matters for the physical target. The Climate case shows that two orthogonal optimal subspaces can still be practically substitutable for a given channel, whereas Plasma and Neuro show cases in which using the positive-objective optimum produces a substantial loss in the channel of interest.

Admissible geometry is equally important. Full-state perturbations are acceptable in the already restricted Plasma and QG state spaces, but not in the neural model, where a physically interpretable preparation must be tied to afferent inputs. Consequently, nonredundancy is a property of `(A,M,Q,B,R_in,T)`, not of `A` or `Q` alone.

The signed semantics also remain domain dependent. Plasma and Climate/Ocean realize both signs of their cumulative transport channels on the frozen admissible spaces. Neuro uses a signed pathway operator in full state space but reaches only the positive cumulative branch on its frozen preparation geometry. The commonality is therefore methodological rather than a claim that all three observables are the same kind of flux.

---

# 6. Discussion

## 6.1 Contribution and novelty level

The strongest defensible contribution is methodological integration plus physical insight (`N2+N3` in the project classification), with narrower application-level contributions. The workflow combines physical predefinition of `M`, `Q`, `B`, and `R_in`; common finite-time positive and signed-channel operators; signed extrema; optimizer/subspace and performance-gap diagnostics; direct physical reconstruction; numerical robustness gates; prospective freezing; and explicit anti-retuning rules.

No mathematical novelty is claimed for transient growth, singular vectors, quadratic-output optimization, Gramian/Lyapunov methods, or the generic fact that different objectives can select different optimizers. Those ingredients are established. The contribution is the disciplined physical question and the nonuniform evidence obtained when it is asked under one controlled workflow.

## 6.2 Geometric identifiability versus practical relevance

A distinct optimizer can be scientifically interesting without being decision relevant. If the target objective has a broad maximum, two orthogonal structures may deliver nearly the same channel value. Conversely, a moderate geometric separation can correspond to a large performance loss. This distinction matters whenever an energy or storage optimum is used as a practical proxy for transport, transfer, or pathway contribution.

The Climate/Ocean result is therefore not a failed replication but a necessary contrast. It shows that the workflow can conclude that the conventional energy optimum remains a good proxy in the tested setting even after detecting a sharp structural switch. Plasma and Neuro show the opposite regime, where the proxy choice materially changes the attainable physical target.

## 6.3 Role of physical admissibility

The matrix `B` should not be treated as a numerical convenience. It encodes the physically or experimentally realizable preparation space. The Neuro example is particularly instructive: a rank-one single afferent direction could not support a nontrivial optimizer-direction comparison, whereas the frozen two-pulse preparation creates a rank-two reachable initial-state geometry without invoking arbitrary latent-state kicks or time-dependent optimal control. In Plasma and Climate/Ocean, by contrast, full-state perturbations are admissible only because the represented state spaces have already been physically restricted.

## 6.4 Limitations

All three demonstrations use linear tangent dynamics. They do not establish nonlinear saturation, turbulence-level transport prediction, in-vivo neural causal efficacy, or operational forecast skill. The three `M`, `Q`, and `B` objects have different physical meanings and should not be collapsed into one cross-domain physical quantity. The neural model omits propagation delays and uses a deliberately low-dimensional preparation geometry that does not reach a negative cumulative pathway branch. The Climate/Ocean model is an idealized two-layer QG system and its weak result cannot be extrapolated to Primitive-Equation models, AMOC dynamics, atmospheric blocking, or forecast systems. Finally, the targeted literature audits support cautious `to our knowledge` formulations but do not prove novelty by absence.

## 6.5 Future work

Protected future directions include delayed or pathway-expanded neural models, higher-fidelity geophysical models, realistic fusion applications, Power-Grid and Photonics/Waves applications, and MODES/CONT/CASCADE extensions. None is required to support the present manuscript claims, and none was opened during this revision.

---

# 7. Conclusion

A positive energy, storage, or state objective is not automatically equivalent to a separately defined signed physical channel. The practically relevant question is not only whether the two optimizers differ geometrically, but whether substituting the conventional positive-objective optimum causes a meaningful loss in the channel of interest.

Across three frozen stable linear case studies, the answer is deliberately nonuniform. The Plasma benchmark shows a large particle-transport penalty for the free-energy optimum. The constrained Neuro preparation problem shows a large pathway-performance penalty for the terminal-storage optimum. The QG case shows that orthogonal optimal subspaces can nevertheless differ by only about 4.12% in cumulative poleward heat-transport performance. Together these results support a simple reporting principle: optimizer geometry and target-performance loss should be evaluated separately, within a physically defined admissible perturbation space.

The manuscript therefore advances a physics-informed, prospectively frozen diagnostic workflow and a cross-domain evidence base, not a new theorem of optimal perturbations.

---

# Methods Appendix / Supplement-level reproducibility material

The following material is retained in the manuscript package so that a journal-specific version can move it to Supplement without changing the science.

## A. Plasma reproducibility details

The Fourier state at resolution `K` contains `2(2K+1)` complex coefficients ordered as all `phi_m` followed by all `eta_m`, `m=-K,...,K`. The Laplacian block is `Delta_mm=-(m^2+k_y^2)`. Multiplication by `U=cos x` couples only nearest radial neighbors. The frozen uniform damping is a generator shift `-0.020 I`; it was selected by a blind stability qualification before any objective-separation calculation. The reported resolutions are `K=32,64,96`, with dimensions 130, 258, and 386. Numerical checks include Hermiticity residuals, optimizer normalization, transport eigen-residuals, Rayleigh reproduction, direct terminal-energy reproduction, direct cumulative-flux integration, modal decay, and common-subspace optimizer comparison across resolutions. No parameter was retuned after objective inspection.

## B. Neuro reproducibility details

The pinned CMC fixed point is `x*=0`, with baseline-subtracted sigmoid slope `S'(0)=1/6`. Synaptic time constants are `(2,2,16,28) ms` for `(SS,SP,II,DP)` in both regions. The storage metric is

\[
M=\operatorname{diag}(
250000,1,
250000,1,
3906.25,1,
1275.51020408163,1,
250000,1,
250000,1,
3906.25,1,
1275.51020408163,1).
\]

The primary V1-SP -> V4-SS pathway block has only `(A_{j->i})_{10,3}=16666.6666666667`, so the corresponding symmetric channel matrix has only

\[
(Q_{j\to i})_{10,3}=(Q_{j\to i})_{3,10}=8333.33333333333
\]

nonzero. The afferent input is `b_aff,V1=16000 e_2`. The two 1-ms preparation pulses occupy `[-3,-2] ms` and `[-17,-16] ms` relative to observation onset. Their effective columns are obtained from the frozen matrix-exponential integral

\[
b_k^{\rm eff}=A^{-1}\left(e^{A(\tau_k+\delta)}-e^{A\tau_k}\right)b_{\rm aff,V1}.
\]

The resulting map has `rank(B)=2`; the storage/input-whitened condition number is `34.294<100`. The pulse-dose metric is `R_in=I_2`. Full sparse generator entries and all effective-column components remain available in the frozen pilot specification and should be supplied in machine-readable/Supplement form for submission.

## C. Climate/Ocean reproducibility details

The Fourier/Galerkin basis enforces exactly zonal periodicity, `psi_i'=0` at the meridional walls, and exclusion of `m=0`. For each mode, `x_{mn}=(psi_{mn},tau_{mn})`. With `S^*=150`, the analytic blocks are those given in Sec. 3.3; hence `M_K` is Hermitian positive definite and `Q_heat,K` is Hermitian indefinite at every admissible resolution. The primary/confirmation/high-audit resolutions are `(12,12)`, `(16,16)`, and `(24,24)`, with dimensions 576, 1024, and 2304. The finite-time heat integral is evaluated by a frozen augmented-exponential formulation and independently checked by a Lyapunov-tail identity and direct adaptive trajectory quadrature. Objective values must agree within the pre-specified residual and resolution tolerances; no additional resolution rung or horizon is introduced after effect inspection.

## D. Analysis-freeze chronology and terminology

The study uses a version-controlled sequence of model freezes, numerical qualifications, execution specifications, execution results, literature-positioning audits, and manuscript claim freezes. In external text we describe this as **pre-specified and frozen before objective-separation evaluation** or **prospectively frozen in the version-controlled analysis record before effect inspection**. We do not rely on the stronger conventional meaning of external preregistration unless the final Methods/Data Availability section explicitly documents and justifies that terminology.

## E. Bibliography normalization status

Bibliographic metadata below are restricted to already approved positioning sources. Entries marked `VERIFY FINAL STATUS` require a final manual bibliographic check before submission; this is metadata verification only, not a new novelty search.

- **[Landreman2015]** Landreman, M., Plunk, G. G. & Dorland, W. (2015). “Generalized universal instability: transient linear amplification and subcritical turbulence.” *Journal of Plasma Physics* **81**, 905810501. DOI: `10.1017/S0022377815000495`.
- **[Foures2014]** Foures, D. P. G., Caulfield, C. P. & Schmid, P. J. (2014). “Optimal mixing in two-dimensional plane Poiseuille flow at finite Péclet number.” *Journal of Fluid Mechanics* **748**, 241–277. DOI: `10.1017/jfm.2014.182`.
- **[Hennequin2012]** Hennequin, G., Vogels, T. P. & Gerstner, W. (2012). “Non-normal amplification in random balanced neuronal networks.” *Physical Review E* **86**, 011909. DOI: `10.1103/PhysRevE.86.011909`.
- **[Bondanelli2020]** Bondanelli, G. & Ostojic, S. (2020). “Coding with transient trajectories in recurrent neural networks.” *PLoS Computational Biology* **16**(2), e1007655. DOI: `10.1371/journal.pcbi.1007655`.
- **[Friston2003]** Friston, K. J., Harrison, L. & Penny, W. (2003). “Dynamic causal modelling.” *NeuroImage* **19**(4), 1273–1302. DOI: `10.1016/S1053-8119(03)00202-7`.
- **[Daunizeau2011]** Daunizeau, J., Preuschoff, K., Friston, K. & Stephan, K. E. (2011). “Optimizing Experimental Design for Comparing Models of Brain Function.” *PLoS Computational Biology* **7**(11), e1002280. DOI: `10.1371/journal.pcbi.1002280`.
- **[Salfenmoser2022]** Salfenmoser, L. & Obermayer, K. (2022). “Nonlinear optimal control of a mean-field model of neural population dynamics.” *Frontiers in Computational Neuroscience* **16**, 931121. DOI: `10.3389/fncom.2022.931121`.
- **[Ogino2026]** Ogino, M. et al. (2026). “Designing optimal perturbation inputs for system identification in neuroscience.” *eLife reviewed preprint* 110030; reviewed-preprint v1 DOI `10.7554/eLife.110030.1`. **VERIFY FINAL PUBLICATION STATUS BEFORE SUBMISSION.**
- **[Farrell1982]** Farrell, B. F. (1982). “The Initial Growth of Disturbances in a Baroclinic Flow.” *Journal of the Atmospheric Sciences* **39**, 1663–1686. DOI: `10.1175/1520-0469(1982)039<1663:TIGODI>2.0.CO;2`.
- **[Farrell1985]** Farrell, B. F. (1985). “Transient Growth of Damped Baroclinic Waves.” *Journal of the Atmospheric Sciences* **42**, 2718–2727. DOI: `10.1175/1520-0469(1985)042<2718:TGODBW>2.0.CO;2`.
- **[FarrellIoannou1994]** Farrell, B. F. & Ioannou, P. J. (1994). “A Theory for the Statistical Equilibrium Energy Spectrum and Heat Flux Produced by Transient Baroclinic Waves.” *Journal of the Atmospheric Sciences* **51**(19), 2685–2698. DOI: `10.1175/1520-0469(1994)051<2685:ATFTSE>2.0.CO;2`.
- **[KimMorgan2002]** Kim, H. M. & Morgan, M. C. (2002). “Dependence of Singular Vector Structure and Evolution on the Choice of Norm.” *Journal of the Atmospheric Sciences* **59**, 3099–3116. DOI: `10.1175/1520-0469(2002)059<3099:DOSVSA>2.0.CO;2`.
- **[Kuang2004]** Kuang, Z. (2004). “The Norm Dependence of Singular Vectors.” *Journal of the Atmospheric Sciences* **61**, 2943–2949. DOI: `10.1175/JAS-3308.1`.
- **[Sevellec2008]** Sévellec, F., Huck, T., Ben Jelloul, M., Vialard, J. & Fedorov, A. V. (2008). “Optimal Surface Salinity Perturbations of the Meridional Overturning and Heat Transport in a Global Ocean General Circulation Model.” *Journal of Physical Oceanography* **38**(12). DOI: `10.1175/2008JPO3875.1`.

---

**Revision boundary:** all equations, parameter values, numerical results, and literature-positioning statements above are copied, condensed, or reorganized from already frozen repository sources. Revision 0.2 introduces no new scientific result and authorizes no journal targeting or protected-branch work.