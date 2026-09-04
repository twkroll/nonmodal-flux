# Physics-informed diagnosis of objective nonredundancy in stable linear dynamics across plasma, neural and geophysical models

**Draft:** 0.4  
**Status:** PRE-SUBMISSION EDITORIAL INTEGRATION — FROZEN-EVIDENCE ONLY  
**Primary target:** Physical Review E — Regular Article  
**Scientific/textual rollback:** `research/manuscript/manuscript_draft_0_3.md`

## Abstract

Finite-time optimal-perturbation studies often use a positive energy, storage, or state metric as a proxy for the physical quantity of interest. We ask a narrower question: after the dynamics, admissible perturbations, positive metric, and a separately defined signed physical channel have all been fixed, how redundant are the two resulting finite-time optima? We apply the same pre-specified and version-controlled workflow to three stable linear models. In a drift-wave/zonal-flow plasma benchmark, the free-energy-optimal perturbation misses 50.4% of the maximum positive cumulative particle transport at the frozen horizon `T=1`. In a two-source V1/V4 canonical-microcircuit model, terminal synaptic-filter-storage and cumulative V1-SP -> V4-SS pathway objectives select markedly different two-pulse preparations, with performance gaps 0.529 and 0.818 at 112 and 224 ms. In a damped two-layer quasigeostrophic model, energy- and poleward-heat-optimal subspaces are orthogonal at the longest frozen horizon while the heat-performance gap is only 0.0412, so the energy optimum retains 95.88% of maximal cumulative poleward heat transport. The nonuniform outcome shows why optimizer geometry and target-performance loss should be reported separately. An additional one-shot geophysical robustness case showed striking fixed-resolution separation but was rejected when the pre-specified refinement criteria failed. The contribution is a physics-informed diagnostic workflow and cross-domain physical interpretation, not a new general theory of optimal perturbations.

# 1. Introduction

Optimal-perturbation methods ask which admissible disturbance produces the largest response over a prescribed horizon. Positive energy or storage measures are natural objectives, but the scientific target may instead be a signed radial particle flux, meridional heat flux, or a specified physiological pathway contribution. A positive state metric and a signed physical channel therefore answer different questions even on the same linear dynamics and admissible perturbation space.

The required mathematical tools are established: transient amplification in stable systems, singular vectors, finite-time quadratic outputs, Gramian/adjoint methods, and norm dependence all have substantial prior art [Landreman2015; Farrell1982; Farrell1985; FarrellIoannou1994; KimMorgan2002; Kuang2004; Foures2014; Sevellec2008]. Neural systems likewise have established literatures on non-normal amplification, transient trajectory design, DCM experimental design, and neural-mass optimal control [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026].

The present contribution is not the generic statement that different objectives can have different optimizers. We use one controlled workflow in which the linear generator, positive metric, signed channel, admissible perturbation geometry, input cost, horizon ladder, and numerical gates are pre-specified and frozen before objective-separation evaluation. We then report both geometric separation and the loss in the selected physical channel incurred by using the conventional positive-objective optimum as a proxy.

Three deliberately different robust cases form the principal evidence sequence: Plasma/D10-ZF (`P2-A`), Neuro/CMC (`NEURO-STRONG`), and Climate-A/Phillips-QG (`CLIM-WEAK`). A separate one-shot Climate-B audit is retained only because the same workflow rejected an attractive fixed-resolution result after mandatory refinement gates failed. The manuscript-level claim is correspondingly limited: storage/state-optimal and physical-channel-optimal perturbations need not be redundant, but the magnitude and practical consequence of their separation depend on system, horizon, observable, admissible geometry, and numerical/representation robustness.

# 2. Common finite-time framework and study design

The shared analysis logic and distinct physical semantics are summarized in **Fig. 1**.

## 2.1 Frozen linear problem

Each application is an autonomous stable linear system

\[
\dot x=Ax,\qquad x(0)=Bu,
\]

with positive input cost

\[
u^\dagger R_{\rm in}u=1,\qquad R_{\rm in}=R_{\rm in}^\dagger\succ0.
\]

With whitened coordinates `w=R_in^{1/2}u`, `||w||_2=1`, optimizer comparisons occur on the same admissible input-cost sphere within each application. The preparation map `B` is part of the physical specification, not a numerical convenience.

## 2.2 Positive objective and signed channel

For a positive storage/state metric

\[
S_M(x)=\frac12x^\dagger Mx,\qquad M=M^\dagger\succ0,
\]

the doubled-form finite-time operator is

\[
K_M(T)=R_{\rm in}^{-1/2}B^\dagger e^{A^\dagger T}Me^{AT}BR_{\rm in}^{-1/2}.
\]

For a separately defined Hermitian signed channel `Q`,

\[
J_Q(T)=\int_0^T x(t)^\dagger Qx(t)\,dt,
\]

\[
K_Q(T)=R_{\rm in}^{-1/2}B^\dagger\left[\int_0^T e^{A^\dagger t}Qe^{At}\,dt\right]BR_{\rm in}^{-1/2}.
\]

The largest and smallest eigenvalues of `K_Q` are the reachable positive and negative cumulative channel extrema on the frozen admissible space.

## 2.3 Geometry, target performance, and robustness

For nondegenerate leading directions,

\[
\vartheta(T)=\arccos|\langle w_M^\star,w_Q^\star\rangle|.
\]

For a degenerate optimum we compare the full leading subspaces using conservative principal-angle diagnostics. Geometric nonidentity is not itself a performance measure, so whenever `J_Q^+(T)>0` we also report

\[
\Delta_Q(T)=\frac{J_Q^+(T)-J_Q(T;w_M^\star)}{J_Q^+(T)},
\]

with the conservative best-in-energy-subspace version when required by degeneracy. Thus geometry and target-performance loss are separate diagnostics.

The model, parameters, `M`, `Q`, `B`, `R_in`, horizons, numerical checks, and verdict rules were **pre-specified and frozen before objective-separation evaluation** in the version-controlled analysis record. The study-specific strong rule requires `\vartheta>=20 deg` and `\Delta_Q>=0.25` on at least two neighboring frozen horizons together with all domain-specific gates. These thresholds are operational rules for this study, not universal physical constants. Supplement S1 records the freeze chronology and protocol; Supplement Table S1 records the operational rule and representative outcomes.

Robustness is an independent evidentiary layer. A large same-resolution angle or gap is insufficient if the pre-specified numerical or cross-resolution gates fail.

## 2.4 Domain semantics — Main Table 1

**Main Table 1** uses the canonical produced table asset.

| Domain | Defining model | Positive metric | Signed physical channel | Admissible geometry / input cost | Time normalization | Frozen role |
|---|---|---|---|---|---|---|
| Plasma/D10-ZF | stable drift-wave/zonal-flow linearization | free energy, `E=1/2 z^dagger M z` | cumulative signed radial particle transport | full frozen Galerkin perturbation space; `B=I`, `R_in=M` | nondimensional D10-ZF time, `tau_ref=1` | `P2-A` strong anchor |
| Neuro/CMC | stable two-source V1/V4 canonical microcircuit | terminal model-internal synaptic-filter storage | cumulative V1-SP -> V4-SS pathway contribution to storage rate | rank-two fixed two-pulse afferent preparation; `R_in=I_2` | `tau_ref=28 ms` | `NEURO-STRONG` |
| Climate-A/Phillips-QG | stable damped two-layer quasigeostrophic model | QG perturbation energy | cumulative signed poleward eddy heat transport | balanced QG eddy state space; `B=I`, `R_in=M_K` | `tau_ref=0.7233796296 d` | `CLIM-WEAK` robust contrast |

The physical meanings are distinct. In particular, the Neuro metric is model-internal synaptic-filter storage, not metabolic, thermodynamic, or total physiological brain energy.

# 3. Application methods

## 3.1 Plasma: D10-ZF

The frozen drift-wave/zonal-flow linearization uses `U(x)=cos x`, `L_x=2pi`, `k_y=C=kappa=1`, `N(x)=0`, and Pilot-0.2 damping `A=A_0-0.020I`. The free-energy metric and signed radial particle-transport form are

\[
M=\begin{pmatrix}-\Delta&0\\0&I\end{pmatrix}\succ0,
\qquad
Q_\Gamma=\frac{k_y}{2}\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}.
\]

The full retained Galerkin space is admissible (`B=I`, `R_in=M`). Frozen resolutions are `K=32,64,96`; horizons are `T={0.25,0.5,1,2,4,8}`. Full equations, ordering, and numerical checks are in Supplement S2.

## 3.2 Neuro: two-source V1/V4 canonical microcircuit

The 16-state stable V1/V4 CMC uses populations `(SS,SP,II,DP)` with second-order synaptic filters and no propagation-delay module in this finite-dimensional pilot. The generator has `alpha(A)=-33.0964092356 s^-1`. The positive quantity is model-internal synaptic-filter storage. The frozen signed pathway is

\[
\mathrm{V1\,SP}\rightarrow\mathrm{V4\,SS},
\qquad
Q_{j\to i}=\frac12(A_{j\to i}^\dagger M+MA_{j\to i}).
\]

Admissible preparations are two fixed 1-ms afferent pulses to V1-SS ending 2 ms and 16 ms before observation; only their amplitudes vary. Their propagated columns define a rank-two `B` with `R_in=I_2`. With `tau_ref=28 ms`, horizons are 7, 14, 28, 56, 112, and 224 ms. Full state ordering, pulse columns, and numerical checks are in Supplement S3.

## 3.3 Climate-A: damped two-layer Phillips QG

The frozen model is a damped two-layer Phillips-QG channel with `L_x=3.0e7 m`, `L_y=1.0e7 m`, `L_D=1.0e6 m`, `beta=1.6e-11 m^-1 s^-1`, `U=8 m s^-1`, and `r=(10 d)^-1`. A structure-preserving Fourier/sine basis enforces periodic `x`, wall boundary conditions, and `k_x!=0`. The positive metric is QG perturbation energy and the signed channel is poleward eddy heat transport. The balanced eddy state is admissible (`B=I`, `R_in=M_K`), `tau_ref=62500 s=0.7233796296 d`, and `T/tau_ref={0.25,0.5,1,2,4,8}`. The primary/confirmation/high resolutions are `(12,12)/(16,16)/(24,24)`. Full modal matrices and refinement checks are in Supplement S4.

# 4. Results

## 4.1 Plasma: strong signed-transport anchor

The D10-ZF operators are spectrally stable at all three reported resolutions, while finite-time free-energy amplification exceeds unity at every frozen horizon and the cumulative particle-transport operator has both positive and negative extrema. At `T=1`,

\[
G_E=1.8782758,\quad J_\Gamma^+=0.3535169,\quad J_\Gamma^-=-0.1462216,
\]

\[
J_\Gamma(w_E^\star)=0.1752252,\quad \Delta_\Gamma=0.5043372,\quad \vartheta=53.396^\circ.
\]

Thus the free-energy optimum misses approximately 50.4% of maximum positive cumulative particle transport. The reported objective-separation quantities are resolution robust on the tested common resolved subspace. **Figure 2** summarizes the frozen six-horizon diagnostics and the `T=1` witness. This is a controlled stable benchmark, not a claim of first plasma transient growth, nonlinear turbulence, experiment, or universality.

## 4.2 Neuro: strong nonredundancy on a constrained two-pulse space

The stable frozen V1/V4 model satisfies the study-specific strong criterion at two neighboring long horizons:

\[
T=112\,\mathrm{ms}:\quad \vartheta=46.824271^\circ,\quad \Delta_Q=0.529017,
\]

\[
T=224\,\mathrm{ms}:\quad \vartheta=65.058256^\circ,\quad \Delta_Q=0.817841.
\]

The pathway optimum is approximately `(+0.9924,-0.1230)`, whereas the storage optima are approximately `(+0.7687,+0.6396)` at 112 ms and `(+0.5300,+0.8480)` at 224 ms. Although the full-state instantaneous pathway matrix is indefinite, the frozen rank-two admissible geometry reaches only positive cumulative pathway values over the tested horizon ladder. Therefore the result does **not** demonstrate an experimentally reachable negative cumulative pathway branch. **Figure 3** shows the six-horizon geometry/performance diagnostics and the signed two-pulse preparation coordinates.

## 4.3 Climate-A: robust weak geometry-versus-performance contrast

The qualified QG generator is stable with `alpha(A_K)=-0.1 d^-1`. The first five horizons are nearly redundant. At the longest frozen horizon, `T/tau_ref=8`, the energy-optimal and heat-optimal supports are

\[
(|m|,n)_E=(3,2),\qquad (|m|,n)_{\rm heat}=(4,2),
\]

with conservative subspace angle

\[
\vartheta_{\rm sub}=90^\circ.
\]

Yet

\[
J_{\rm heat}^+=1.54448995,\qquad J_{\rm heat|E}^{\rm best}=1.48088082,
\]

\[
\Delta_{\rm heat}=0.04118455.
\]

The energy-optimal subspace therefore retains about 95.88% of maximum cumulative poleward heat transport. All six frozen horizons pass the prescribed refinement protocol. **Figure 4** deliberately shows the `90 deg` geometry together with the small `Delta_heat≈0.0412` performance loss. The frozen verdict remains `CLIM-WEAK`.

# 5. Cross-domain synthesis and robustness lessons

## 5.1 Geometry versus target performance

The three robust cases form an evidence hierarchy rather than replications of one physical effect. **Figure 5** is a non-inferential paired summary of geometry and target-performance diagnostics for Plasma, Neuro, and Climate-A only. It contains no trend line, fit, regression, decision region, universal threshold, common physical-objective scale, or Climate-B fixed-resolution point.

Plasma and Neuro show substantial target loss when the conventional positive-objective optimum is used as a proxy. Climate-A shows the complementary case: orthogonal optimal subspaces can coexist with only a 4.12% target-performance loss. The shared lesson is that optimizer geometry and decision-relevant performance are different questions. Admissible geometry is equally important: full-state perturbations are acceptable in the already physically restricted Plasma and QG spaces, whereas the neural comparison is tied to a fixed rank-two afferent preparation.

## 5.2 Robustness rejection: one-shot Climate-B audit

The separate equivalent-barotropic Bickley-jet audit passed local algebraic and direct-reproduction gates and displayed striking same-resolution separation, including `Delta_shift=1` to roundoff and large optimizer angles. **Those fixed-resolution observations failed the pre-specified refinement protocol and are not robust Climate evidence.** Zero of six frozen horizons passed the full cross-resolution criteria. The frozen verdict is

\[
\boxed{\text{CLIM-B-FAIL — resolution robustness failure}}.
\]

The full model, resolution-failure ledger, and stop rule are in Supplement S5. **Supplement Fig. S5** separates local PASS gates from cross-resolution FAIL gates and states `0/6` frozen horizons robust. No repair, retuning, extra resolution, alternative channel, or third Climate candidate is part of this manuscript.

# 6. Discussion and limitations

The strongest defensible contribution is methodological integration plus physical interpretation, with narrower application-level contributions. No mathematical novelty is claimed for transient growth, singular vectors, quadratic-output optimization, Gramian/Lyapunov methods, or the generic fact that different objectives can select different optimizers.

The physical meanings of `M`, `Q`, and `B` remain domain specific. Plasma free energy, neural synaptic-filter storage, QG perturbation energy, and the supplementary barotropic kinetic-energy metric are not one common physical quantity. Likewise, particle transport, pathway contribution, heat transport, and jet-translation forcing have distinct semantics.

The results identify three evidentiary layers: optimizer/subspace geometry, target-performance loss, and numerical/representation robustness. Climate-A makes the first distinction explicit; Climate-B makes the third unavoidable.

All demonstrations use linear tangent dynamics. They do not establish nonlinear saturation, turbulence-level transport prediction, in-vivo neural causal efficacy, realized nonlinear jet displacement, climate-change prediction, or operational forecast skill. The neural model omits propagation delays; Climate-A is an idealized two-layer QG system; Climate-B is a failed one-shot refinement case. The study-specific 20-degree and 0.25 thresholds are operational rules, not universal constants.

Supplement S6 records the frozen machine-readable source paths and remaining bibliography metadata notes. Protected future directions are not part of Revision 0.4.

# 7. Conclusion

A positive energy, storage, or state objective is not automatically equivalent to a separately defined signed physical channel. The practically relevant questions are whether the optimizers differ, how much target performance is lost by substituting the positive-objective optimum, and whether the conclusion survives the required robustness checks.

Across the three robust frozen cases the answer is deliberately nonuniform: Plasma shows a large particle-transport penalty, Neuro shows a large pathway-performance penalty on a constrained two-pulse space, and Climate-A shows that orthogonal optimal subspaces can nevertheless differ by only about 4.12% in cumulative poleward heat-transport performance. Climate-B adds the negative methodological lesson that large fixed-resolution separation is insufficient when refinement fails.

The manuscript therefore advances a physics-informed, pre-specified and version-controlled diagnostic workflow and a cross-domain evidence base, not a universal theorem of optimal perturbations.

# Reproducibility and analysis record

Model definitions, admissible geometries, objective definitions, horizon ladders, numerical gates, and verdict rules were **pre-specified and frozen before objective-separation evaluation**. Failed frozen gates are retained rather than repaired by post-effect retuning. Supplement S1 documents the chronology and protocol. The frozen figure package uses stored data/definitions only; its manifest, validation record, captions, and presentation-only scripts are version controlled under `research/manuscript/figures/`.

# Data Availability

The machine-readable frozen execution data supporting the reported numerical values and figures are available in the public version-controlled repository `twkroll/nonmodal-flux` (`https://github.com/twkroll/nonmodal-flux`). The primary data paths are listed in Supplement S6 and `research/manuscript/pre_submission_asset_map_0_1.md`. The current project record does not document an archival DOI or other permanent archival repository identifier. Archival deposition and/or assignment of a persistent identifier remains a submission-readiness item and is not fabricated in this revision.

# Code Availability

The presentation-only figure-generation and validation scripts used for the frozen figure package are available in the same public repository under `research/manuscript/figures/src/`. The repository also contains the frozen specifications, execution-result records, machine-readable data files, and manuscript evidence/source maps supporting the manuscript. Revision 0.4 does not assert a software license, archival DOI, or institutional preservation commitment not documented in the frozen record.

# References

Bibliographic content is unchanged from Draft 0.3 and restricted to the already approved positioning sources: [Landreman2015], [Foures2014], [Hennequin2012], [Bondanelli2020], [Friston2003], [Daunizeau2011], [Salfenmoser2022], [Ogino2026], [Farrell1982], [Farrell1985], [FarrellIoannou1994], [KimMorgan2002], [Kuang2004], and [Sevellec2008]. Full frozen metadata are retained in `research/manuscript/manuscript_supplement_0_1.md`, Sec. S6.3. Final publication-status verification for `Ogino2026` remains a submission-readiness metadata item and does not authorize a new novelty search.

# Figure captions

**Figure 1. Common frozen-data workflow.** The shared methodological layer freezes `A`, `M`, `Q`, `B`, and `R_in` before objective-separation evaluation; geometry, target-performance loss, and robustness are distinct evidentiary layers. Plasma, Neuro, and Climate-A retain distinct physical semantics. Climate-B is the Supplement S5 robustness-rejection case, not a fourth robust application.

**Figure 2. Plasma strong anchor (`P2-A`).** Frozen six-horizon D10-ZF diagnostics retain both signs of cumulative particle transport. At `T=1`, `G_E=1.8783`, `vartheta=53.40 deg`, and `Delta_Gamma=0.5043`, so the free-energy optimum misses about 50.4% of maximum positive cumulative particle transport.

**Figure 3. Neuro constrained two-pulse result (`NEURO-STRONG`).** The six-horizon geometry/performance comparison and 112/224-ms unit-cost pulse-coordinate directions preserve the negative second coordinate of the pathway optimum. The pulses are fixed preparations, not a time-dependent control waveform, and no reachable negative cumulative pathway branch is depicted.

**Figure 4. Climate-A robust weak contrast (`CLIM-WEAK`).** At `T/tau_ref=8`, the energy and heat optimal supports are `(3,2)` and `(4,2)` with conservative subspace angle `90 deg`, while `Delta_heat=0.0411846`; the energy-optimal subspace retains about 95.88% of maximum cumulative poleward heat transport.

**Figure 5. Non-inferential cross-domain geometry/performance summary.** Representative robust-domain witnesses are aligned on separate geometry and target-performance axes. No trend, fit, regression, phase diagram, universal boundary, correlation claim, or common physical-objective scale is implied; Climate-B fixed-resolution points are excluded.

**Revision boundary:** Revision 0.4 changes title, manuscript/asset integration, availability wording, figure/table callouts, supplement packaging, and editorial compression only. Scientific equations/semantics, parameters, frozen numerical values, classifications, evidence ordering, and robustness interpretations are unchanged from the Draft-0.3 evidence base.
