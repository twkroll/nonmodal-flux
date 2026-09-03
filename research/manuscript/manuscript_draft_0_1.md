# Diagnosing objective nonredundancy in stable linear dynamics: a physics-informed finite-time workflow across plasma, neural and geophysical models

**Draft:** 0.1  
**Status:** INTEGRATED DRAFT — FROZEN-EVIDENCE ONLY  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`  
**Scope:** manuscript drafting only. No new simulations, parameters, horizons, objectives, pathways, admissible geometries, or novelty claims are introduced here.

## Abstract

### Background
Finite-time optimal-perturbation analyses often optimize a positive storage, norm, or state-amplification quantity. Such objectives are physically useful, but they need not answer the same question as a separately defined signed physical channel such as particle transport, heat transport, or a directed pathway contribution. Transient growth, singular vectors, quadratic-output optimization, norm dependence, and optimal stimulation are established methodologies; the issue addressed here is therefore not whether such optimization is possible, but whether a conventional positive objective is actually redundant with the physical channel of interest on the same admissible perturbation space.

### Methods
We use a preregistered physics-informed finite-time workflow built from the domain-specific tuple

\[
\mathfrak C=(A,M,Q,B,R_{\rm in}),
\]

where `A` is the frozen linear generator, `M\succ0` is a positive storage/state metric, `Q=Q^\dagger` is a separately defined signed physical channel, `x(0)=Bu` defines admissible perturbations, and `R_in\succ0` fixes input cost. In whitened coordinates, the terminal positive objective and cumulative signed-channel operator are

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2},
\]

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger\left[\int_0^T e^{A^\dagger t}Qe^{At}\,dt\right]BR_{\rm in}^{-1/2}.
\]

We compare their optimal directions or optimal subspaces, signed channel extrema, physical structure, and the dimensionless channel-performance gap

\[
\Delta_Q(T)=\frac{J_Q^+(T)-J_Q(T;w_M^\star)}{J_Q^+(T)},
\]

using frozen horizon ladders, numerical checks, and anti-retuning rules.

### Results
The three preregistered applications produce deliberately nonuniform outcomes. In a spectrally stable drift-wave/zonal-flow plasma benchmark, finite-time free-energy amplification coexists with a signed cumulative particle-transport operator; at `T=1`, the energy-optimal perturbation misses approximately 50.4% of the maximum attainable positive cumulative particle transport. In a stable two-source V1/V4 canonical-microcircuit model, terminal synaptic-filter-storage and cumulative V1-SP -> V4-SS pathway objectives select distinct pulse preparations; at 112 and 224 ms the optimizer angles are 46.82° and 65.06°, with channel-performance gaps 0.529 and 0.818. By contrast, in a stable damped two-layer Phillips-QG model, energy- and poleward-heat-optimal subspaces become orthogonal at the longest frozen horizon, yet the heat-performance gap is only 0.0412, so the energy optimum retains approximately 95.88% of maximal cumulative poleward heat transport.

### Conclusions
Storage/state-optimal and physical-channel-optimal perturbations need not be redundant, but the magnitude and practical consequence of their separation are system-, horizon-, observable-, and admissible-geometry-dependent. Optimizer geometry and target-performance loss should therefore be reported separately. The contribution is methodological integration and physical interpretation across frozen applications, not a new general theory of quadratic-output optimization.

---

# 1. Introduction

Optimal-perturbation methods ask which admissible disturbance produces the largest response over a specified horizon. In fluid mechanics, plasma physics, atmospheric and oceanic dynamics, and control-oriented models, a common choice is a positive norm or storage quantity because it provides a stable metric for comparing perturbations and often has a direct physical interpretation. Yet the quantity that matters scientifically may instead be a signed channel: radial particle transport, meridional eddy heat transport, or the contribution of a specified connection to a storage-rate balance.

These two classes of objective need not be interchangeable. A positive storage metric asks how large a state becomes according to a chosen quadratic measure. A signed channel asks how much directed physical transfer is accumulated. The corresponding optimizers can differ even when they are computed from the same linearized dynamics and the same admissible perturbation space. The central practical question is therefore not merely whether two optimizers have a nonzero angle, but whether replacing a channel-specific optimum by a conventional storage/state optimum causes a meaningful loss in the channel quantity itself.

The mathematical ingredients underlying this question are established. Transient amplification in stable and non-normal systems has a long history, including stable plasma dynamics and damped baroclinic waves [Landreman2015; Farrell1985]. Singular vectors and optimal perturbations are standard tools in fluid, atmospheric, and oceanic dynamics, and their dependence on norm or objective is well known [KimMorgan2002; Kuang2004]. Energy-optimal and mixing- or scalar-optimal perturbations can differ in fluid mechanics [Foures2014], while observable-dependent optimal perturbations, including heat-transport objectives, have been studied in ocean models [Sevellec2008]. Neural systems likewise have established literatures on non-normal transient amplification, transient trajectory design, DCM experimental design, and neural-mass optimal control [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026].

Our contribution is therefore not a claim that these individual techniques are new. Instead, we use a common preregistered workflow in which the positive metric `M`, signed channel `Q`, admissible geometry `B`, and input cost `R_in` are fixed from the physics or experimental interpretation before objective separation is inspected. We then compare storage/state-optimal and channel-optimal perturbations using both geometric diagnostics and direct channel-performance loss, together with explicit robustness and no-retuning rules.

We test this workflow in three deliberately different settings. First, a spectrally stable drift-wave/zonal-flow plasma benchmark provides a strong signed-transport anchor. Second, a stable canonical-microcircuit model tests whether the same workflow remains informative when the admissible perturbation space is an experimentally interpretable rank-two pulse-preparation geometry rather than the full state space. Third, a stable two-layer quasigeostrophic model provides a contrast case in which the optimal subspaces become geometrically distinct while the actual heat-transport penalty remains small. This nonuniform outcome is central to the paper: the workflow is intended to diagnose objective nonredundancy, not to maximize its apparent size.

The manuscript-level claim is correspondingly limited. A preregistered physics-informed finite-time workflow can test whether a conventional positive storage/state objective is redundant with an independently defined signed physical channel on the same admissible perturbation space. Across the three frozen models considered here, that nonredundancy is strong in the plasma and neural pilots but weak in the climate/ocean pilot, showing that optimizer geometry and practical channel-performance loss must be assessed separately.

---

# 2. Common framework and preregistration logic

## 2.1 Linear dynamics and admissible perturbations

Each application is represented by an autonomous frozen linear system

\[
\dot x=Ax,
\]

with admissible initial conditions

\[
x(0)=Bu.
\]

The matrix `B` is part of the physical specification. It is not chosen after seeing an optimizer. In Plasma and Climate/Ocean, `B=I` is admissible on already restricted physical state spaces. In Neuro, `B` is a rank-two preparation map generated from two fixed afferent pulses through the same physiological input pathway. The input cost is

\[
u^\dagger R_{\rm in}u=1,
\qquad R_{\rm in}\succ0.
\]

Introducing whitened coordinates `w=R_in^{1/2}u` gives `\|w\|_2=1`.

## 2.2 Positive objective and signed channel

The positive quadratic storage/state metric is

\[
S(x)=\frac12x^\dagger Mx,
\qquad M=M^\dagger\succ0.
\]

Its terminal finite-time operator is

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2}.
\]

The corresponding optimal direction maximizes `w^\dagger K_M(T)w` over `\|w\|=1`.

Separately, the instantaneous signed physical channel is

\[
q(t)=x(t)^\dagger Qx(t),
\qquad Q=Q^\dagger,
\]

and the cumulative channel is

\[
J_Q(T)=\int_0^T x(t)^\dagger Qx(t)\,dt.
\]

Define

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
\]

and

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger P_Q(T)BR_{\rm in}^{-1/2}.
\]

The extremal eigenvalues of `K_Q(T)` give the maximum and minimum cumulative signed channel attainable on the frozen admissible space.

## 2.3 Geometry and performance are distinct diagnostics

Let `w_M^\star` denote an optimizer of the positive objective and `w_Q^\star` an optimizer of the positive cumulative channel. When leading eigenspaces are non-degenerate, their angle is

\[
\vartheta(T)=\arccos|\langle w_M^\star,w_Q^\star\rangle|.
\]

When symmetry creates exact degeneracy, as in the QG Fourier blocks, we compare optimal subspaces by conservative principal angles.

Geometric separation alone is not enough. We also compute

\[
\Delta_Q(T)=
\frac{J_Q^+(T)-J_Q(T;w_M^\star)}{J_Q^+(T)},
\]

provided the positive optimum is safely nonzero. `\Delta_Q=0` means the positive-objective optimizer is channel-optimal; `\Delta_Q=0.5` means it realizes only half of the maximum positive channel.

## 2.4 Domain semantics are not interchangeable

The common operator form does not imply common physical meaning.

| Domain | `M` | `Q` | `B, R_in` |
|---|---|---|---|
| Plasma/D10-ZF | free-energy metric | signed radial particle transport | full frozen perturbation state space, `B=I`, `R_in=M` |
| Neuro/CMC | model-internal synaptic-filter storage | V1-SP -> V4-SS contribution to the storage-rate balance | fixed rank-two two-pulse preparation, `R_in=I_2` |
| Climate/Ocean QG | QG perturbation energy | signed meridional eddy heat transport | balanced QG eddy state space, `B=I`, `R_in=M_K` |

In particular, the neural storage metric is not metabolic or thermodynamic brain energy. Its reported positive objective is terminal synaptic-filter storage per frozen pulse-cost metric.

## 2.5 Anti-retuning and robustness protocol

For each pilot, the model, channel, positive metric, admissible geometry, input cost, horizon ladder, numerical resolution roles, and verdict rules were frozen before inspecting the corresponding objective-separation results. A weak or null result was retained rather than repaired by changing parameters. Numerical checks include Hermiticity, positive definiteness or PSD where required, eigensystem residuals, direct trajectory reproduction, finite-time integral checks, and resolution comparison. These controls are part of the methodological contribution because they distinguish a diagnostic workflow from effect-guided parameter selection.

---

# 3. Plasma: strong signed-transport anchor

## 3.1 Frozen benchmark

The plasma pilot uses the D10-ZF branch at

\[
U(x)=\cos x,\quad L_x=2\pi,\quad k_y=1,
\]

with `C=\kappa=1`, `N=0`, and frozen perpendicular damping `\nu_\perp=0.020`. The physical state metric is free energy, the signed channel is radial particle transport, `B=I`, and `R_in=M`. Resolutions `K=32,64,96` and horizons

\[
T\in\{0.25,0.5,1,2,4,8\}
\]

were fixed before effect evaluation.

The system is spectrally stable at all three resolutions, with

\[
\alpha(A_{32})=-0.0075786,
\quad
\alpha(A_{64})=-0.0133818,
\quad
\alpha(A_{96})=-0.0154924.
\]

Despite modal stability, finite-time free-energy amplification satisfies `G_E(T)>1` at every frozen horizon.

## 3.2 Signed transport and objective separation

The cumulative particle-transport operator has both positive and negative extrema over the full admissible state space for every horizon. At `T=1`,

\[
G_E=1.8782758,
\qquad
J_\Gamma^+=0.3535169,
\qquad
J_\Gamma^-=-0.1462216.
\]

The energy-optimal perturbation produces only

\[
J_\Gamma(w_E^\star)=0.1752252,
\]

so

\[
\Delta_\Gamma=0.5043372.
\]

Thus the energy optimum misses approximately 50.4% of the maximum attainable positive cumulative particle transport at this frozen horizon. The optimizer angle is

\[
\vartheta=53.396^\circ.
\]

The effect is not confined to one horizon: the optimizer angle remains at least about 28° and the transport gap remains positive over the complete frozen ladder.

## 3.3 Structural distinction and robustness

The separation is resolution-robust. Scalar objective values agree to near roundoff across `K=32,64,96`, and projected high-resolution optimizers coincide with the corresponding lower-resolution directions on the common resolved subspace. The optimizer structures are also physically different. At `T=1`, the energy optimum is concentrated around radial Fourier modes `m=\pm2,\pm1,\pm3`, whereas the transport optimum is dominated by `m=0` and then `m=\pm1`. The two families also differ in their potential/density composition and relative phase.

Direct trajectories reinforce the distinction. The least-damped modal trajectory decays, while finite-time optimal perturbations exhibit transient free-energy amplification. The transport-optimal direct trajectory reproduces the cumulative Gramian optimum within the frozen numerical tolerance.

## 3.4 Interpretation

This pilot supports the benchmark-level hierarchy

\[
\text{modal stability}\neq\text{finite-time free-energy optimality}\neq\text{finite-time particle-transport optimality}.
\]

The claim is intentionally local to the controlled linear benchmark. Transient amplification in stable plasma systems is established prior art [Landreman2015], and the broader fact that different physical objectives can select different optimal perturbations is also established in adjacent fluid and ocean literature [Foures2014; Sevellec2008]. The role of this result is therefore to anchor the common workflow with a strong, resolution-robust signed-transport example rather than to claim new quadratic-output mathematics.

---

# 4. Neuro: strong objective nonredundancy on a constrained preparation space

## 4.1 Frozen CMC/DCM preparation problem

The neural pilot uses a stable two-source macaque canonical-microcircuit model with V1 as source `j` and V4 as source `i`. The pre-defined physiological channel is

\[
\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS},
\]

with channel matrix

\[
Q_{j\to i}^{\rm CORE}
=
\frac12(A_{j\to i}^\dagger M+MA_{j\to i}).
\]

Here `M` is model-internal synaptic-filter storage. It is not metabolic brain energy. The admissible perturbations are generated by two fixed 1-ms afferent pulses through the same V1-SS input pathway, ending 2 ms and 16 ms before the observation time. Their amplitudes define the rank-two preparation coordinate `w=(h_1,h_2)` with `R_in=I_2`.

The full linear generator is stable,

\[
\alpha(A)=-33.096409\ \mathrm{s}^{-1},
\]

and the frozen reference time is `\tau_ref=28 ms`, giving horizons 7, 14, 28, 56, 112, and 224 ms.

## 4.2 Strong neighboring-horizon separation

All frozen structural and numerical gates pass. At the two neighboring long horizons required by the preregistered strong-verdict rule,

\[
T=112\ \mathrm{ms}:
\quad
\vartheta=46.824271^\circ,
\quad
\Delta_Q=0.529017,
\]

and

\[
T=224\ \mathrm{ms}:
\quad
\vartheta=65.058256^\circ,
\quad
\Delta_Q=0.817841.
\]

The same workflow also detects a separated point at 28 ms (`\vartheta\approx30.89°`, `\Delta_Q\approx0.262`), but the frozen `NEURO-STRONG` verdict is supported by the adjacent 112/224-ms pair.

The channel optimum is approximately horizon-independent at long times,

\[
w_Q\approx(+0.9924,-0.1230),
\]

whereas the terminal-storage optimum uses a same-sign mixture at the two long horizons,

\[
w_M(112\,\mathrm{ms})\approx(+0.7687,+0.6396),
\]

\[
w_M(224\,\mathrm{ms})\approx(+0.5300,+0.8480).
\]

Thus the separation has a direct preparation-space interpretation: the pathway optimum combines a dominant recent pulse with a small opposite-sign older pulse, whereas the long-horizon storage optimum combines the two pulses with the same sign and shifts weight toward the older pulse.

## 4.3 Admissible-geometry restriction

The full-state instantaneous channel matrix is indefinite, but the frozen two-dimensional preparation geometry does not realize a negative cumulative channel extremum on the reported horizon ladder: the minimum eigenvalue of `K_Q(T)` remains positive. The neural result therefore does not establish experimentally reachable positive and negative cumulative pathway transfer. Its claim is narrower: terminal synaptic-filter-storage optimality and positive cumulative pathway-contribution optimality are strongly nonredundant on a physically motivated two-pulse preparation space.

This distinction matters methodologically because `B` is part of the physical problem. A rank-one single-pulse preparation would make nontrivial optimizer-direction comparison impossible; the frozen rank-two map instead comes from two independently dosable afferent pulse components propagated through the same CMC dynamics, not from arbitrary hidden-state actuation.

## 4.4 Literature positioning

Non-normal neural amplification, transient trajectory design, DCM input/experimental-design optimization, neural-mass optimal control, and recent control-theoretic perturbation design are all established [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026]. Accordingly, we do not claim novelty for optimal stimulation, transient neural amplification, or directed connectivity.

To our knowledge, the targeted literature does not already contain the same stable CMC/DCM preparation problem in which terminal quadratic synaptic-filter storage and the cumulative contribution of a predefined physiological pathway are separately optimized over the same fixed rank-two two-pulse preparation coordinates. The present contribution is therefore an application/methodological comparison with direct preparation-coordinate meaning, not a new general neural-control theory.

---

# 5. Climate/Ocean: a robust weak contrast case

## 5.1 Frozen two-layer QG pilot

The geophysical pilot uses a damped two-layer Phillips quasigeostrophic model on the balanced eddy state space. The positive metric is classical QG perturbation energy, the signed physical channel is cumulative meridional eddy heat transport, positive northward/poleward, and `B=I`, `R_in=M_K` on the restricted physical state space. The numerical qualification fixes

\[
\tau_{\rm ref}=0.7233796296\ \mathrm{d},
\qquad
\alpha(A_K)=-0.1\ \mathrm{d}^{-1}<0,
\]

with the horizon ladder

\[
T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\}.
\]

Primary, confirmation, and high-resolution roles are `(12,12)`, `(16,16)`, and `(24,24)`. All structural, trajectory, finite-time-integral, eigensystem, and resolution-robustness gates pass.

## 5.2 Near redundancy at short and intermediate horizons

At the first five horizons, energy- and poleward-heat-optimal perturbations select the same modal support and differ only weakly internally. The conservative optimizer/subspace angle grows from approximately 0.018° at `T/\tau_ref=0.25` to only 2.772° at `T/\tau_ref=4`, while the heat-performance gap remains at or below about 0.00317.

This is already informative: the common workflow is capable of reporting near redundancy rather than forcing a large effect.

## 5.3 Orthogonal subspaces with a small performance penalty

At the longest frozen horizon,

\[
T/\tau_{\rm ref}=8,
\]

the objectives select different exact modal subspaces,

\[
(|m|,n)_E=(3,2),
\qquad
(|m|,n)_{\rm heat}=(4,2).
\]

Because the modal pairs are orthogonal,

\[
\vartheta_{\rm sub}=90^\circ.
\]

Yet

\[
J_{\rm heat}^+=1.54448995,
\qquad
J_{\rm heat|E}^{\rm best}=1.48088082,
\]

which gives

\[
\Delta_{\rm heat}=0.04118455.
\]

The energy-optimal subspace therefore still realizes about 95.88% of maximal cumulative poleward heat transport. The geometry is strongly different, but the target performance is only weakly different.

The physical structures are nevertheless distinguishable. At this horizon the heat optimum is more strongly baroclinic and occupies the shorter zonal scale `|m|=4` rather than `|m|=3`. The signed heat-flux history of the heat optimum changes sign once late in the interval, but its net cumulative heat transport remains maximal and positive, illustrating why the cumulative signed objective cannot be replaced by an absolute-value flux criterion.

## 5.4 Interpretation and prior art

Transient growth in damped baroclinic systems is classical [Farrell1985], as are QG singular vectors and norm/objective dependence [Farrell1982; KimMorgan2002; Kuang2004]. Transient baroclinic heat flux has long been linked to non-normal dynamics [FarrellIoannou1994], and heat-transport-optimal initial perturbations exist in stable ocean-model literature [Sevellec2008].

To our knowledge, the targeted literature does not report the same direct energy-optimal versus signed cumulative eddy-heat-transport-optimal comparison in a stable damped two-layer Phillips-QG tangent system. The value of the present pilot is therefore not a headline novelty claim or a strong replication of the plasma gap. It is a controlled contrast demonstrating the methodological lesson

\[
\boxed{\text{large optimizer/subspace angle does not imply a large objective-performance gap}.}
\]

---

# 6. Cross-domain synthesis

## 6.1 Nonuniform outcomes under one workflow

The three frozen results form an evidence hierarchy rather than three interchangeable replications.

| Domain | Conventional positive objective | Physical channel | Frozen outcome | Representative witness |
|---|---|---|---|---|
| Plasma/D10-ZF | free energy | signed cumulative radial particle transport | `P2-A` strong anchor | `T=1`: `\vartheta=53.40°`, `\Delta_\Gamma=0.504` |
| Neuro/CMC | terminal synaptic-filter storage per pulse cost | cumulative V1-SP -> V4-SS pathway contribution | `NEURO-STRONG` | 112/224 ms: `\Delta_Q=0.529/0.818` |
| Climate/Ocean QG | QG perturbation energy | signed cumulative poleward eddy heat transport | `CLIM-WEAK` contrast | `T/\tau_ref=8`: `90°`, but `\Delta_{heat}=0.0412` |

The shared lesson is not that positive objectives are poor proxies in every model. Rather, proxy quality must be tested. The same diagnostic layer identifies a strong transport mismatch in Plasma, a strong preparation-objective mismatch in Neuro, and only a weak practical heat-transport mismatch in Climate/Ocean.

## 6.2 Why both angle and performance gap are needed

The plasma and neural cases might tempt an interpretation based primarily on optimizer angle. The QG case shows why that would be incomplete. Two optimal subspaces can be orthogonal yet produce almost the same target performance if the target objective landscape is broad near its maximum or if different structures have similar channel values. Conversely, a moderate optimizer angle can accompany a substantial performance penalty. Reporting `\vartheta` and `\Delta_Q` together therefore distinguishes geometric nonidentity from practical nonredundancy.

## 6.3 Admissible geometry is part of the physics

The three cases also illustrate different meanings of `B`. Full-state perturbations are physically acceptable in the restricted plasma and QG state spaces, whereas a neural preparation must be tied to experimentally meaningful afferent inputs. This distinction is essential: optimizer comparisons are made within `range(B)`, not in an arbitrary full-state space. The framework therefore treats admissibility and cost on the same footing as the dynamics and channel definition.

## 6.4 Signed channels should remain signed

Plasma and Climate/Ocean explicitly retain positive and negative cumulative channel branches rather than replacing them by magnitudes or squares. In Neuro, the full-state instantaneous pathway operator is indefinite even though the frozen admissible preparation geometry reaches only positive cumulative values. These differences again reinforce that the commonality is methodological; the physical semantics and reachable signed geometry are domain specific.

---

# 7. Discussion

## 7.1 What is contributed

The strongest defensible novelty level is methodological integration plus physical insight (`N2+N3`), with narrower application contributions (`N1`). The method package is the disciplined combination of physical predefinition of `M`, `Q`, `B`, and `R_in`; common finite-time operators; signed extrema; optimizer/subspace and performance-gap diagnostics; direct physical reconstruction; robustness checks; preregistered verdict rules; and anti-retuning freezes.

The physical insight is correspondingly conditional. In some admissible geometries, a conventional positive objective is a poor proxy for a separately defined physical channel. In others it remains a good proxy even when the optimizer geometry changes visibly. Therefore objective nonredundancy is a property to diagnose, not an effect to presume.

## 7.2 Relation to established optimal-perturbation literature

The present workflow sits within mature literatures rather than replacing them. Plasma transient amplification without unstable eigenmodes is established [Landreman2015]. Fluid-mechanical work has already shown that energy-optimal and mixing-oriented objectives can differ [Foures2014]. Atmospheric and oceanic singular vectors are known to depend on norm and final metric [KimMorgan2002; Kuang2004], and heat-transport objectives have been optimized in stable ocean systems [Sevellec2008]. Neural transient amplification and optimized perturbations or controls likewise have substantial precedents [Hennequin2012; Bondanelli2020; Daunizeau2011; Salfenmoser2022; Ogino2026].

The cross-domain contribution is therefore the consistent physics-informed question asked across all three cases: after fixing the physically admissible perturbations and independently defining both the positive metric and signed channel, how redundant are their finite-time optima in geometry and in achieved target performance?

## 7.3 Limitations

First, all three demonstrations use frozen linear tangent dynamics. They do not establish nonlinear saturation behavior, turbulence-level transport prediction, in-vivo neural causality, or realistic forecast skill. Second, the physical meanings of `M`, `Q`, and `B` differ across domains, so the results should not be collapsed into a single universal physical interpretation. Third, the neural preparation geometry is deliberately low-dimensional and does not reach a negative cumulative pathway extremum. Fourth, the climate model is an idealized two-layer QG system, and its weak result should not be extrapolated to Primitive-Equation models, AMOC dynamics, blocking, or operational forecasting. Fifth, the targeted literature audits support cautious `to our knowledge` formulations but are not proofs of novelty by absence.

## 7.4 Why the weak QG result is important

The QG case acts as a built-in check against effect-maximizing interpretation. It passed the same predefinition, numerical qualification, and robustness discipline as the strong cases but returned only a 4.12% target-performance gap at the point of maximal geometric separation. Retaining this result strengthens the methodological message: the workflow can conclude that a conventional energy optimum remains an adequate heat-transport proxy in the tested setting, even while it diagnoses nonidentical optimal structure.

## 7.5 Future work

Several extensions are intentionally outside the first paper. These include delayed or pathway-expanded neural models, higher-fidelity geophysical models, realistic fusion applications, Power-Grid and Photonics/Waves applications, and MODES/CONT/CASCADE extensions. They remain protected future branches rather than missing pieces required to support the present claims.

---

# 8. Conclusion

A positive storage or state objective is not automatically equivalent to a separately defined signed physical channel, even when both are optimized over the same stable linear dynamics. The relevant question is quantitative: do the objectives select meaningfully different admissible perturbations, and does that geometric difference translate into a meaningful loss of the physical channel when the conventional objective is used as a proxy?

Across three frozen case studies, the answer is deliberately nonuniform. The plasma benchmark shows a strong particle-transport penalty for the energy optimum; the constrained neural preparation problem shows a strong pathway-performance penalty for the terminal-storage optimum; and the QG heat-transport case shows that orthogonal optimal subspaces can still differ by only about 4.12% in target performance. This contrast motivates a simple reporting principle: optimizer geometry and physical-channel performance should be evaluated separately.

The manuscript therefore advances a physics-informed, preregistered diagnostic workflow and a cross-domain evidence base, not a new theorem of optimal perturbations. Within that scope, the results support the conclusion that storage/state-optimal and physical-channel-optimal perturbations need not be redundant, while the practical importance of their separation remains system-, horizon-, observable-, and admissible-geometry-dependent.

---

# Placeholder bibliography

The entries below are mandatory positioning anchors from the frozen claim package. Bibliographic formatting will be normalized later without changing scientific claims.

- **[Landreman2015]** Landreman, M., Plunk, G. G. & Dorland, W. (2015). *Generalized universal instability: transient linear amplification and subcritical turbulence*. Journal of Plasma Physics 81, 905810501. DOI: 10.1017/S0022377815000495.
- **[Foures2014]** Foures, D. P. G., Caulfield, C. P. & Schmid, P. J. (2014). *Optimal mixing in two-dimensional plane Poiseuille flow at finite Péclet number*. Journal of Fluid Mechanics 748, 241–277. DOI: 10.1017/jfm.2014.182.
- **[Hennequin2012]** Hennequin, G., Vogels, T. P. & Gerstner, W. (2012). *Non-normal amplification in random balanced neuronal networks*. Physical Review E 86, 011909.
- **[Bondanelli2020]** Bondanelli, G. & Ostojic, S. (2020). *Coding with transient trajectories in recurrent neural networks*. PLoS Computational Biology 16, e1007655.
- **[Friston2003]** Friston, K. J., Harrison, L. & Penny, W. (2003). *Dynamic causal modelling*. NeuroImage 19, 1273–1302.
- **[Daunizeau2011]** Daunizeau, J., Preuschoff, K., Friston, K. & Stephan, K. E. (2011). *Optimizing Experimental Design for Comparing Models of Brain Function*. PLoS Computational Biology 7, e1002280.
- **[Salfenmoser2022]** Salfenmoser, L. & Obermayer, K. (2022). *Nonlinear optimal control of a mean-field model of neural population dynamics*. Frontiers in Computational Neuroscience 16, 931121.
- **[Ogino2026]** Ogino, M. et al. (2026). *Designing optimal perturbation inputs for system identification in neuroscience*. eLife reviewed preprint 110030.
- **[Farrell1982]** Farrell, B. F. (1982). *The Initial Growth of Disturbances in a Baroclinic Flow*. Journal of the Atmospheric Sciences 39, 1663–1686.
- **[Farrell1985]** Farrell, B. F. (1985). *Transient Growth of Damped Baroclinic Waves*. Journal of the Atmospheric Sciences 42, 2718–2727.
- **[FarrellIoannou1994]** Farrell, B. F. & Ioannou, P. J. (1994). *A Theory for the Statistical Equilibrium Energy Spectrum and Heat Flux Produced by Transient Baroclinic Waves*. Journal of the Atmospheric Sciences 51, 2685–2698.
- **[KimMorgan2002]** Kim, H. M. & Morgan, M. C. (2002). *Dependence of Singular Vector Structure and Evolution on the Choice of Norm*. Journal of the Atmospheric Sciences 59, 3099–3116.
- **[Kuang2004]** Kuang, Z. (2004). *The Norm Dependence of Singular Vectors*. Journal of the Atmospheric Sciences 61, 2943–2949.
- **[Sevellec2008]** Sévellec, F., Huck, T., Ben Jelloul, M., Vialard, J. & Fedorov, A. V. (2008). *Optimal Surface Salinity Perturbations of the Meridional Overturning and Heat Transport in a Global Ocean General Circulation Model*. Journal of Physical Oceanography 38. DOI: 10.1175/2008JPO3875.1.

---

**Draft boundary:** all quantitative results above are copied or paraphrased from frozen canonical result files. This draft does not authorize any new calculation, literature claim, journal targeting, or protected-branch work.
