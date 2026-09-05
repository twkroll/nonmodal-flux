# Fusion R1 Structural Redundancy & Fidelity-Breaking Literature Audit 0.1

**Date:** 2026-09-05  
**Authority:** `research/master/prompts/fusion_r1_structural_redundancy_fidelity_breaking_literature_audit_0_1.md`  
**Status:** `EXECUTION COMPLETE — RETURN TO MASTER`  
**Scope:** targeted literature positioning and balance-structure audit only. No finite-time objective calculation, optimizer calculation, parameter/model scan, R1 retuning, FLR/GK execution, new general theory, or Paper-1 modification.

---

## 0. Executive verdict

The frozen R1 structural collapse is strongly supported as an **implicit consequence of standard gyrokinetic/gyrofluid free-energy balance structure**, not as a new free-energy theorem.

For the frozen R1 objects,

\[
\widetilde A^\dagger M_k+M_k\widetilde A
=2\frac{R_0}{L_T}\widehat Q_q,
\qquad B=I_4,
\qquad R_{\rm in}=M_k,
\]

with no positive dissipation term and no independent particle/electron supply channel. Therefore

\[
2\frac{R_0}{L_T}K_q(T)=\mathcal E_M(T)-I
\]

at every finite horizon, so fixed-initial-free-energy cumulative-ion-heat optimization and final-free-energy optimization are affinely equivalent.

The literature establishes all physical ingredients of this collapse very clearly:

1. the local gyrokinetic Helmholtz-free-energy drive is a sum of thermodynamic particle- and heat-flux work terms over species;
2. collisions enter with the entropy-producing sign and provide a free-energy sink;
3. with one kinetic ion species and adiabatic electrons, the density-gradient contribution to the free-energy drive vanishes by quasineutrality, leaving the ion-temperature-gradient drive as the relevant source;
4. pure conservative gyroaveraging/FLR physics changes the free-energy functional and operators but does not by itself create an independent supply channel or positive sink;
5. nonadiabatic electrons introduce an independent electron free-energy drive, while physically valid collisions add a positive entropy/free-energy dissipation channel;
6. collisionless phase mixing is fundamentally a redistribution of free energy to fine velocity-space structure; irreversible removal in a full kinetic balance requires collisions, whereas a finite-dimensional Landau-fluid closure may represent that unresolved transfer as an effective sink only if its balance is constructed consistently.

No `SAME` source was found in the targeted search that explicitly states the **same finite-horizon optimal-objective no-go** in the form “under a one-channel, zero-dissipation free-energy balance and fixed initial free energy, cumulative heat-flux and final-free-energy optimizers are identical at every horizon.” This absence is **not evidence of novelty**. The closest literature contains the balance needed to derive the statement immediately but generally uses it for energetic bounds, turbulence energetics, or mode analysis rather than for a comparison of cumulative-transport and final-energy initial-condition objectives.

### Final positioning

\[
\boxed{\text{R1 structural collapse = physically meaningful control case, but largely an implicit standard-balance consequence.}}
\]

The next physically justified fidelity step should **not** be an FLR-only rescue or an added damping term on R1. The preferred next MASTER gate is a **balance-complete two-species local-gyrokinetic fidelity specification gate** that, before any effect calculation, freezes:

- finite-ion-FLR gyrokinetic dynamics;
- nonadiabatic electron physics (a bounce-averaged trapped-electron model is the cleanest reduced candidate; fully kinetic electrons are the higher-fidelity reference);
- physically separated ion/electron particle- and heat-flux channels;
- an H-theorem-compatible collision operator or an explicitly justified collisionless limit;
- the resulting exact free-energy balance and all signs/normalizations.

This recommendation is based on repairing R1's missing electron channel and missing irreversible sink, not on an expectation of optimizer separation.

---

## 1. Exact search question and frozen scope

The audit asks only:

> How does the exact R1 one-channel/no-dissipation affine redundancy sit relative to established gyrofluid/gyrokinetic free-energy and transport balances, and which physically necessary fidelity additions alter the balance by introducing an independent supply channel and/or a positive dissipation term?

The following R1 facts are frozen and were not modified:

- anisotropic-ZLR four-moment minimal-curvature branch;
- state `z_k=(N,U,P_parallel,P_perp)^T`;
- adiabatic-electron electrostatic closure;
- physical signed ion radial heat channel `Q_q`;
- collapsed ion particle-flux channel `Q_Gamma_i=0`;
- `B=I_4` and `R_in=M_k`;
- no artificial damping, collisions, Landau-fluid closure, kinetic electrons, FLR/R2 execution, GEM extension, or GENE layer;
- exact single-channel balance
  \[
  \widetilde A^\dagger M_k+M_k\widetilde A
  =2(R_0/L_T)\widehat Q_q;
  \]
- exact affine finite-horizon identity
  \[
  2(R_0/L_T)K_q(T)=\mathcal E_M(T)-I.
  \]

The F1.4 marginal spectrum is retained only as context. No finite-time propagator or objective was calculated in this audit.

---

## 2. Search strategy and source set

### 2.1 Targeted queries

The targeted search used combinations of:

- `gyrokinetic free energy balance heat flux particle flux gradient drive`;
- `adiabatic electrons ITG free energy density gradient particle flux`;
- `gyrofluid free energy conservation finite Larmor radius FLR`;
- `gyrokinetic collisions H theorem free energy dissipation`;
- `bounce averaged electrons free energy balance ion electron drive`;
- `phase mixing Landau damping free energy collision dissipation`;
- `optimal growth gyrokinetic free energy nonmodal`;
- `heat flux optimal perturbation gyrokinetic initial condition`;
- `transport optimal perturbation gyrokinetic`.

### 2.2 Source hierarchy

Priority was given to primary peer-reviewed sources and author/journal copies from:

- *Journal of Plasma Physics* / Cambridge Core;
- *Physics of Plasmas* / AIP and institutional records;
- *Reports on Progress in Physics* / IOP / PubMed;
- arXiv versions when they were the clearest accessible canonical version;
- Princeton/PPPL institutional publication records for older gyrofluid sources.

The search was targeted rather than exhaustive. It does not establish patent-style or theorem-level novelty by absence.

---

## 3. Source-by-source classification

### 3.1 Helander & Plunk (2022) — strongest general-balance overlap

**P. Helander and G. G. Plunk, “Energetic bounds on gyrokinetic instabilities. Part 1. Fundamentals,” Journal of Plasma Physics 88, 905880207 (2022).**  
DOI: `10.1017/S0022377822000277`.

**Relevant structure.** Their key free-energy equation is, schematically,

\[
\frac{d}{dt}\sum_k H(k,t)=2\sum_k[C(k,t)+D(k,t)],
\]

where the collision term has the entropy-producing sign, and the gradient drive is written explicitly as

\[
D(k,t)
=-\sum_a\left[
T_a\Gamma_a\frac{d\ln p_a}{d\psi}
+q_a\frac{d\ln T_a}{d\psi}
\right].
\]

They separately define the radial particle flux `Gamma_a` and radial heat flux `q_a`. Thus the gyrokinetic free-energy supply is already a physically resolved sum of particle- and heat-transport work channels over species.

**Relation to R1:** `CLOSE`.

**Why not SAME:** the paper uses the free-energy budget to derive upper bounds on free-energy growth and does not, in the portions checked, formulate the R1 finite-horizon consequence as an affine equivalence between cumulative heat-work and final-free-energy optimization under a fixed initial free-energy budget.

**Positioning consequence:** the physical balance underlying R1 is standard gyrokinetic free-energy structure. The R1 no-go should not be presented as a new free-energy theorem. Its useful role is the explicit optimization consequence under a deliberately minimal one-channel closure.

---

### 3.2 Plunk & Helander (2023) — closest physical-assumption overlap

**G. G. Plunk and P. Helander, “Energetic bounds on gyrokinetic instabilities. Part 3. Generalized free energy,” Journal of Plasma Physics 89, 905890419 (2023).**  
DOI: `10.1017/S0022377823000739`; arXiv: `2301.00988`.

**Relevant structure.** The principal worked case is a single kinetic ion species with adiabatic electrons. The paper explicitly notes that, under the adiabatic-electron approximation, the density-gradient contribution to the free-energy input vanishes by quasineutrality; the temperature-gradient factor remains. Collisions are neglected in this part of the analysis.

This is physically very close to the R1 restriction: a one-species adiabatic-electron ITG model in which the free-energy source is tied to the ion-temperature-gradient/heat channel rather than an independently accessible density-gradient particle channel.

**Relation to R1:** `CLOSE`.

**Why not SAME:** the paper develops generalized energetic measures and instantaneous optimal growth bounds, including resonance information, rather than the finite-horizon cumulative-heat versus final-free-energy affine identity used by the frozen R1 control.

**Positioning consequence:** the single-channel character of R1 is not an artificial CORE construction. It reflects a recognized physical consequence of the adiabatic-electron, single-kinetic-species ITG reduction. The optimization-collapse consequence appears to be an unstated corollary rather than a separately established plasma result.

---

### 3.3 Bañón Navarro et al. (2011) — gyrokinetic turbulence balance

**A. Bañón Navarro, P. Morel, M. Albrecht-Marc, D. Carati, F. Merz, T. Görler and F. Jenko, “Free energy balance in gyrokinetic turbulence,” Physics of Plasmas 18, 092303 (2011).**  
DOI: `10.1063/1.3632077`.

**Relevant structure.** The paper derives and analyzes the free-energy evolution for ITG turbulence in the GENE formalism, separating:

- ion-temperature-gradient injection;
- collisional dissipation;
- entropy/electrostatic-energy transfer through curvature and parallel terms;
- nonlinear redistribution across scales.

The important structural point for R1 is that curvature and parallel dynamics redistribute energy within the total free-energy budget, whereas the background gradient supplies and collisions dissipate the total free energy.

**Relation to R1:** `CLOSE`.

**Why not SAME:** it is a turbulence/free-energy-budget study, not a finite-horizon initial-condition optimization no-go. Its kinetic state and dissipative implementation are also higher fidelity than frozen R1.

**Positioning consequence:** R1's distinction between conservative curvature/parallel terms and the sole thermodynamic supply is literature-consistent. A physically valid collisional extension would add a sink rather than merely alter the conservative generator.

---

### 3.4 Abel et al. (2013) — full multiscale transport/free-energy framework

**I. G. Abel, G. G. Plunk, E. Wang, M. Barnes, S. C. Cowley, W. Dorland and A. A. Schekochihin, “Multiscale gyrokinetics for rotating tokamak plasmas: fluctuations, transport and energy flows,” Reports on Progress in Physics 76, 116201 (2013).**  
DOI: `10.1088/0034-4885/76/11/116201`; arXiv: `1209.4782`.

**Relevant structure.** The framework derives gyrokinetic fluctuation free-energy conservation/cascade together with transport equations for mean density, temperature and flow. It links profile relaxation, particle/heat transport, species exchange and entropy production in a systematically ordered gyrokinetic theory.

**Relation to R1:** `ADJACENT`.

**Why:** it establishes the physically richer target framework in which multiple thermodynamic fluxes and species are not collapsed into one R1 heat channel, but it does not state the frozen affine objective relation.

**Positioning consequence:** a credible higher-fidelity extension should move toward a balance structure of this kind rather than patching the four-moment R1 generator with effect-motivated terms.

---

### 3.5 Costello & Plunk (2025) — clean reduced nonadiabatic-electron candidate

**P. J. Costello and G. G. Plunk, “Energetic bounds on gyrokinetic instabilities. Part 4. Bounce-averaged electrons,” Journal of Plasma Physics 91, E12 (2025).**  
DOI: `10.1017/S0022377824000965`; arXiv: `2404.06081`.

**Relevant structure.** The model consists of fully gyrokinetic ions with finite ion-Larmor-radius effects and bounce-averaged trapped electrons. Its Helmholtz free-energy balance has the form

\[
\frac{d}{dt}\sum_k H(k,t)
=2\sum_k\big(D_i(k,t)+D_e^{\rm tr}(k,t)\big),
\]

so the electron contribution is an independent free-energy drive channel in addition to the ion contribution.

**Relation to R1:** `CLOSE` as a fidelity-breaking comparison.

**Why not SAME:** it is a higher-fidelity two-species gyrokinetic model and studies energetic bounds/optimal energy modes, not R1's cumulative heat objective.

**Positioning consequence:** nonadiabatic trapped-electron dynamics are a physically established way to remove the one-channel R1 source structure. This is a particularly clean reduced candidate for a later balance-specification gate because it adds missing electron physics while retaining an analytically controlled gyrokinetic structure.

---

### 3.6 Abel et al. (2008) — positive collisional entropy/free-energy dissipation

**I. G. Abel, M. Barnes, S. C. Cowley, W. Dorland and A. A. Schekochihin, “Linearized model Fokker–Planck collision operators for gyrokinetic simulations. I. Theory,” Physics of Plasmas 15, 122509 (2008).**  
DOI: `10.1063/1.3046067`; arXiv: `0808.1300`.

**Relevant structure.** The collision operator conserves particles, momentum and energy, obeys Boltzmann's H theorem, vanishes on a Maxwellian and dissipates velocity-space fine structure. It therefore provides a physically controlled entropy-production/free-energy sink rather than arbitrary numerical damping.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** collisions are a physically motivated fidelity addition that changes the R1 balance from

\[
\dot W=gq
\]

to a structure of the form

\[
\dot W=gq-D_{\rm coll},\qquad D_{\rm coll}\ge0.
\]

After integration, cumulative heat is no longer an affine function of final free energy alone because an independent cumulative dissipation operator enters. This removes the exact R1 affine identity in principle without asserting that the resulting optimizers must be widely separated.

---

### 3.7 Scott (2005, 2010) — FLR and gyrofluid free-energy consistency

**B. Scott, “Free-energy conservation in local gyrofluid models,” Physics of Plasmas 12, 102307 (2005).**  
DOI: `10.1063/1.2064968`.

**B. D. Scott, “Derivation via free energy conservation constraints of gyrofluid equations with finite-gyroradius electromagnetic nonlinearities,” Physics of Plasmas 17, 102306 (2010).**  
DOI: `10.1063/1.3484219`; arXiv: `0710.4899`.

**Relevant structure.** Scott derives gyrofluid equations by enforcing the gyrokinetic free-energy structure. In the 2010 construction, finite-gyroradius nonlinearities are part of the conservative gyrofluid derivation; positive-definite dissipation is then added separately to reproduce collisional-fluid limits.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** **FLR by itself is not a justified redundancy-breaking mechanism.** Conservative FLR gyroaveraging can change `A`, `M`, the heat-flux operator and quantitative coefficients, but standard free-energy-consistent derivations do not turn FLR kinematics alone into a new independent supply or positive sink. A later FLR model could break the R1 identity only if the complete higher-fidelity balance also contains an additional source/sink for separate physical reasons.

---

### 3.8 Hammett, Dorland & Perkins (1992); Dorland & Hammett (1993) — Landau-fluid closures and phase mixing

**G. W. Hammett, W. Dorland and F. W. Perkins, “Fluid models of phase mixing, Landau damping, and nonlinear gyrokinetic dynamics,” Physics of Fluids B 4, 2052–2061 (1992).**  
DOI: `10.1063/1.860014`.

**W. Dorland and G. W. Hammett, “Gyrofluid turbulence models with kinetic effects,” Physics of Fluids B 5, 812–835 (1993).**  
DOI: `10.1063/1.860934`.

**Relevant structure.** These works construct moment closures that model collisionless phase mixing/Landau damping and finite-Larmor-radius effects. The 1993 gyrofluid model also contains explicitly dissipative FLR phase-mixing terms that act as a physics-based high-`k_perp` damping mechanism.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** a Landau-fluid term cannot simply be labeled “physical dissipation” without specifying the level of description. In the full collisionless kinetic system, phase mixing is transfer to unresolved velocity-space structure; in a finite moment closure, an effective damping term may represent that transfer as loss from the retained moments. For CORE use, a later finite-dimensional closure must state explicitly whether the lost retained-state free energy appears as a positive `D` term and whether that `D` is balance-consistent.

---

### 3.9 Parker et al. (2016) — phase mixing is reversible transfer before collisional dissipation

**J. T. Parker, E. G. Highcock, A. A. Schekochihin and P. J. Dellar, “Suppression of phase mixing in drift-kinetic plasma turbulence,” Physics of Plasmas 23, 070703 (2016).**  
DOI: `10.1063/1.4958954`; arXiv: `1603.06968`.

**Relevant structure.** The paper separates free energy in fluid and kinetic moments. Parallel streaming transfers free energy between them and is explicitly reversible; collisions remove the fine velocity-space structure. In turbulence, anti-phase-mixing/plasma-echo effects can partly reverse the linear transfer.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** collisionless phase mixing must not automatically be counted as an irreversible positive sink in a full-state balance. It can break a reduced finite-dimensional retained-state identity only when the unresolved kinetic reservoir is represented as an explicit additional subsystem/channel or by a justified coarse-grained dissipative closure.

---

### 3.10 Landreman, Plunk & Dorland (2015) — nonmodal gyrokinetic context

**M. Landreman, G. G. Plunk and W. Dorland, “Generalized universal instability: transient linear amplification and subcritical turbulence,” Journal of Plasma Physics 81, 905810501 (2015).**  
DOI: `10.1017/S0022377815000495`; arXiv: `1501.02980`.

**Relevant structure.** The paper demonstrates transient gyrokinetic free-energy amplification in a system with kinetic ions and electrons, weak collisions, a density gradient and no unstable eigenmodes.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** nonmodal gyrokinetic free-energy growth is established prior art. The R1 audit question is narrower: whether a separately defined cumulative transport objective can be independent of free-energy optimality. Landreman et al. do not supply a SAME result for the R1 affine no-go or a free-energy-optimal versus transport-optimal initial-condition comparison.

---

### 3.11 Plunk & Helander (2022) — optimal free-energy modes

**G. G. Plunk and P. Helander, “Energetic bounds on gyrokinetic instabilities. Part 2. Modes of optimal growth,” Journal of Plasma Physics 88, 905880313 (2022).**  
DOI: `10.1017/S0022377822000496`; arXiv: `2201.08707`.

**Relevant structure.** The paper formulates optimal modes that maximize instantaneous growth of gyrokinetic free energy and develops the associated energetic bounds.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** the concept of gyrokinetic optimal perturbations/energy modes is established. In the targeted search, no paper in this series was found that separately optimizes a cumulative particle/heat transport functional over initial conditions and compares its optimizer with the free-energy optimum.

---

### 3.12 Kotschenreuther et al. (2023) — free-energy balance plus independent flux constraint

**M. Kotschenreuther, X. Liu, S. M. Mahajan and D. R. Hatch, “The free energy balance equation applied to gyrokinetic instabilities, the effect of the charge flux constraint, and application to simplified kinetic models,” arXiv:2310.11624 (2023).**

**Relevant structure.** The authors emphasize that the free-energy balance alone does not determine gyrokinetic dynamics and combine it with the charge-flux constraint as an independent physical relation.

**Relation to R1:** `ADJACENT`.

**Positioning consequence:** this reinforces the audit's distinction between a thermodynamic balance and additional physical channel constraints. It also supports avoiding any interpretation of the R1 one-channel balance as a complete statement of higher-fidelity gyrokinetic dynamics.

---

## 4. Positioning of the exact R1 affine collapse

### 4.1 What is explicit in standard literature

The following is explicit prior art:

\[
\boxed{
\dot H
=\sum_{a}\bigl(\text{particle-flux work}_a+\text{heat-flux work}_a\bigr)
-\text{collisional dissipation}
}
\]

up to conventions/signs and factors of two.

It is also explicit that, for the adiabatic-electron single-ion ITG reduction used in the energetic-bound literature, the density-gradient contribution to free-energy input can vanish by quasineutrality while the ion-temperature-gradient source remains.

Therefore the R1 instantaneous balance is not surprising from the gyrokinetic viewpoint; it is a finite-dimensional realization of a recognized limiting balance.

### 4.2 What appears implicit rather than explicit

If the retained model has exactly one physical source channel and no dissipation,

\[
\dot W(t)=gq(t),
\]

then integration gives

\[
g\int_0^T q(t)\,dt=W(T)-W(0).
\]

With `B=I` and the fixed initial free-energy normalization, the frozen operator identity follows immediately. The targeted literature search did not locate a source that promotes this integrated relation to the specific optimal-perturbation statement:

> maximizing cumulative heat work over fixed-free-energy initial conditions is exactly the same problem as maximizing final free energy at every finite horizon.

Accordingly:

- `SAME`: **none found**;
- strongest classification: **CLOSE**;
- novelty inference: **none permitted from absence**.

The scientifically useful R1 contribution is therefore best described as an explicit **structural no-go control** that prevents an unnecessary finite-time optimization experiment once the standard balance has been specialized to the frozen reduced model.

### 4.3 Why the no-go is model-conditional

The affine equivalence depends simultaneously on:

1. one independent supply channel;
2. zero independent positive dissipation;
3. the fixed initial free-energy cost;
4. full retained-state admissibility in the frozen R1 setup;
5. no additional species/channel term hidden by the closure.

It is not a universal gyrokinetic statement. General gyrokinetics has multiple species and, in general, both particle and heat flux work terms plus collisions.

---

## 5. Fidelity-breaking decision support

| Candidate addition | R1 deficiency repaired | Balance effect | New positive dissipation? | New independent supply channel? | Sufficient in principle to remove exact R1 affine identity? | Physically required independent of effect size? | Clean canonical source / candidate |
|---|---|---|---|---|---|---|---|
| **H-theorem-compatible collisions** | R1 is exactly collisionless and has no irreversible sink | Adds `-D_coll`, with `D_coll >= 0` in the free-energy balance | **Yes** | No | **Yes**, because cumulative dissipation enters the integrated balance; no guarantee of large optimizer separation | **Yes for a balance-complete weakly collisional model**, but must not be bolted onto frozen R1 as spectral rescue | Abel et al. 2008 collision operator; GENE/GS2-compatible implementation |
| **Nonadiabatic / bounce-averaged electrons** | Adiabatic electrons suppress independent electron response and collapse particle/electron transport structure | Adds electron free-energy drive `D_e` in addition to `D_i`; generally restores electron particle/heat physics | No by itself | **Yes** | **Yes**, when the electron drive is nonzero and independent | **Strongly justified for toroidal ion-scale physics where trapped electrons matter** | Costello & Plunk 2025 reduced two-species bounce-averaged-electron GK |
| **Fully kinetic electrons** | Same as above, plus passing-electron and velocity-space dynamics | General multispecies particle/heat source decomposition | Not without collisions | **Yes** | **Yes in principle** | Highest-fidelity reference; larger step than needed for first gate | Helander & Plunk 2022 general multispecies GK; standard local GK/GENE/GS2 |
| **Additional ion species / impurities** | Single-ion species restriction | Adds species-resolved particle/heat source terms | Not necessarily | **Yes** if gradients/channels are independent | **Yes in principle** | Application dependent, not automatically the next minimal step | General multispecies balance in Helander & Plunk 2022 / Abel et al. 2013 |
| **Pure conservative FLR gyroaveraging / finite-`rho_i` corrections** | ZLR/moment-level loss of finite-gyroradius physics | Changes gyroaverages, metric and conservative/drive operators | **No** | **No, not by itself** | **No structural guarantee**; a single-source zero-`D` balance can remain single-source after FLR | **Yes eventually for quantitative credibility at finite `k_perp rho_i`, but not as a redundancy-breaking rationale** | Scott 2005/2010; finite-ion-FLR GK in Costello & Plunk 2025 |
| **Parallel kinetic phase mixing resolved explicitly** | Four-moment R1 lacks velocity-space cascade/resonance | Adds an internal kinetic reservoir and reversible free-energy transfer | No in the exact collisionless full-state balance | Not necessarily | **Not by itself** if the total resolved free energy still has one external source and zero sink | Physically important for kinetic fidelity | Parker et al. 2016; full drift-/gyrokinetics |
| **Landau-fluid closure** | Finite moment closure lacks kinetic resonance/phase mixing | Can place unresolved phase mixing into closure terms; balance effect depends on construction | **Possibly**, at retained-state level if closure is dissipative and sign-definite | Not necessarily | **Yes only if** the closure introduces a genuine independent positive retained-state sink or extra channel | Plausible reduced route, but requires a separate balance audit | Hammett et al. 1992; Dorland & Hammett 1993 |
| **FLR phase-mixing closure** | Missing perpendicular kinetic phase mixing at high `k_perp` | Adds physics-based hyperviscosity-like retained-state damping | **Yes in the closure** | No | **Yes at the reduced-state level**, due to the closure sink, not due to FLR kinematics alone | Relevant only if the chosen next model requires this closure | Dorland & Hammett 1993 |
| **Balance-complete two-species local GK with finite FLR + nonadiabatic electrons + physical collisions** | Repairs the main R1 closure deficits simultaneously | Multiple independent species/particle/heat supplies plus positive collisional sink | **Yes** | **Yes** | **Yes structurally**; still no claim about effect magnitude | **Strongest credibility basis** | Helander & Plunk 2022 + Costello & Plunk 2025 + Abel et al. 2008; standard local GK implementation later if authorized |

### 5.1 Important distinction: “sufficient to remove identity” is not “guaranteed optimizer separation”

A fidelity addition is marked sufficient in principle when it changes the exact integrated balance so that `K_q(T)` is no longer forced to be an affine function of `E_M(T)` alone. This does **not** imply that the corresponding operators will have different leading eigendirections or a large performance gap. Such an effect may be small, zero by accidental symmetry, or parameter dependent. No effect prediction is made here.

---

## 6. Specific audit questions answered

### 6.1 Is the R1 affine equivalence explicit in the literature?

**Balance ingredients: explicit. Optimal-objective consequence: apparently implicit in the targeted source set.**

Helander & Plunk (2022) give the general free-energy budget in particle-/heat-flux form. Plunk & Helander (2023) explicitly identify the adiabatic-electron single-ion limit in which the density-gradient contribution to free-energy input vanishes. Integrating a one-channel/no-dissipation specialization immediately yields the R1 identity, but no `SAME` finite-horizon optimizer statement was located.

### 6.2 Do collisions break the identity?

**Yes in principle, physically and structurally.** A valid collision operator contributes an entropy-producing/free-energy sink. The integrated balance then contains a cumulative dissipation operator in addition to final free energy. This removes the exact two-operator affine identity, without guaranteeing a nonzero optimizer angle.

### 6.3 Do kinetic/nonadiabatic electrons break the identity?

**Yes in principle when their thermodynamic drive is nonzero and independent.** A two-species balance contains separate ion and electron drive contributions, which in general decompose further into particle- and heat-flux work terms.

### 6.4 Does FLR alone break the identity?

**No as a structural rule.** Free-energy-consistent FLR physics can remain entirely inside the conservative/metric/gyroaveraged drive structure. If the higher-fidelity model still has exactly one external thermodynamic source and no dissipation, the same kind of integrated one-channel identity can survive with modified operators. FLR should be included for physical fidelity when warranted, not because it is expected to generate objective separation.

### 6.5 Is collisionless Landau damping a positive sink?

**Not in the exact full kinetic free-energy balance.** Collisionless phase mixing transfers free energy into fine velocity-space structure and can be reversed by plasma-echo/anti-phase-mixing dynamics. True entropy production requires collisions. A finite-dimensional Landau-fluid model may represent unresolved phase mixing as an effective retained-state sink, but the closure must be audited for sign and free-energy consistency before it can play the `D >= 0` role in CORE.

### 6.6 Is there prior work comparing free-energy-optimal and transport-optimal gyrokinetic initial conditions?

The targeted search located established work on:

- transient/nonmodal free-energy amplification (Landreman et al. 2015);
- instantaneous optimal free-energy modes and energetic bounds (Plunk & Helander 2022 and later papers).

It did **not** locate a `SAME` study that optimizes a cumulative physical particle/heat flux over initial conditions and directly compares that optimizer with a free-energy-optimal initial condition under the R1 assumptions. This is not a novelty proof and should be stated only as “no such comparison was identified in the targeted search.”

---

## 7. Ranked recommendation for the next physically justified fidelity gate

### Rank 1 — Balance-complete two-species local-GK specification gate

**Recommended MASTER action:** open a **specification/qualification gate only**, not an effect calculation, for a two-species local electrostatic gyrokinetic model that retains finite ion FLR, introduces a nonadiabatic electron response, and specifies a physical H-theorem-compatible collision operator or a deliberately justified collisionless limit.

A practical reduced first candidate is the **fully gyrokinetic-ion + bounce-averaged trapped-electron** system of Costello & Plunk (2025), augmented only through a canonical collision model if MASTER decides a collisional balance is required. A fully kinetic-electron local-GK implementation is the higher-fidelity reference, not necessarily the first execution target.

The gate should freeze before any finite-time inspection:

1. species and equilibrium-gradient set;
2. exact Helmholtz/free-energy metric;
3. separate `Gamma_i`, `q_i`, `Gamma_e`, `q_e` channel definitions and signs;
4. exact collision contribution and proof/sign check for entropy production;
5. FLR gyroaveraging convention;
6. electron approximation (bounce-averaged or fully kinetic);
7. state/input geometry and cost;
8. exact finite-dimensional/discretized balance identity after structure-preserving discretization.

**Reason for rank 1:** this repairs both scientifically important R1 deficiencies — adiabatic-electron channel collapse and missing irreversible sink — in a standard gyrokinetic framework. It does not rely on an anticipated optimizer gap.

### Rank 2 — Collision-consistent reduced gyrofluid/Landau-fluid gate

If MASTER prioritizes a low-dimensional analytic bridge before local GK, use a published free-energy-consistent gyrofluid/Landau-fluid hierarchy and require an explicit audit of which closure terms are conservative transfers and which are positive retained-state sinks.

**Reason for rank 2:** computationally/analytically compact, but closure semantics introduce extra ambiguity about whether phase mixing is represented as true dissipation or unresolved-state transfer.

### Rank 3 — FLR-only R2 gate

Do **not** promote an FLR-only model as the next redundancy-breaking test. It may be a valuable physical fidelity check, especially at finite `k_perp rho_i`, but the literature does not support treating conservative FLR alone as a new independent balance channel or sink.

**Reason for rank 3:** useful fidelity improvement but weak decision value for the exact R1 structural no-go.

---

## 8. Allowed claims

The following are supported by the audit:

1. **R1 is a legitimate structural no-go control.** Under its frozen adiabatic-electron, one-ion-heat-channel, zero-dissipation balance and fixed initial free-energy cost, cumulative ion-heat work is affinely fixed by the final free-energy change.
2. **The underlying physical balance is standard rather than novel.** General gyrokinetic free-energy theorems explicitly resolve gradient-driven free-energy input into species particle- and heat-flux work and collisional entropy production.
3. **The R1 single-channel restriction has a clear physical origin.** In the single-kinetic-ion/adiabatic-electron ITG limit, the density-gradient contribution to free-energy drive is removed by quasineutrality, leaving the temperature-gradient drive.
4. **FLR alone is not a justified structural escape route.** Conservative FLR corrections may alter operators and metrics without adding an independent source or sink.
5. **Nonadiabatic electrons and physical collisions are literature-supported fidelity additions that alter the balance in genuinely independent ways.** They may remove the exact R1 affine identity, without any claim about the eventual optimizer-separation magnitude.

---

## 9. Forbidden claims

Do not claim:

- that the R1 balance identity or its integrated form is a new gyrokinetic free-energy theorem;
- that absence of a `SAME` optimizer paper proves novelty;
- that FLR automatically produces free-energy/heat-objective separation;
- that collisionless phase mixing is automatically irreversible dissipation in a fully resolved kinetic system;
- that adding arbitrary damping to frozen R1 is physically equivalent to adding a valid collision operator;
- that nonadiabatic electrons, collisions, or any other fidelity addition guarantee a large optimizer angle or performance gap;
- that the marginal R1 point should be spectrally rescued or retuned;
- that this audit authorizes GENE, FLR/R2, kinetic-electron, collision, or finite-time execution.

---

## 10. Uncertainties and open literature items

1. The search was targeted, not exhaustive across all older gyrofluid dissertations, conference proceedings and code documentation. An older source may state the one-channel integrated equivalence more explicitly.
2. “Adiabatic electrons imply vanishing particle flux” depends on the precise local model, flux-surface averaging and closure conventions. The robust statement used here is narrower: in the cited single-ion adiabatic-electron energetic-bound formulation, the density-gradient contribution to the free-energy input vanishes by quasineutrality; the frozen R1 branch independently has `Q_Gamma_i=0`.
3. A particular finite-dimensional Landau-fluid closure may or may not supply a positive-semidefinite `D` in the exact metric used for CORE. That must be checked model by model rather than inferred from the phrase “Landau damping.”
4. A two-species model can still have a vanishing electron free-energy source at special gradients/geometries. The future gate must freeze physical gradients before any objective inspection and verify actual channel independence algebraically.
5. Even when the exact affine identity is removed, accidental commutation or symmetry can keep energy- and transport-optimal directions identical. No literature-based effect prediction should substitute for a later preregistered calculation.

---

## 11. Final verdict and return instruction

### Literature classification

No targeted `SAME` source was found for the exact finite-horizon R1 optimizer no-go. The strongest sources are `CLOSE` because they provide essentially all of the gyrokinetic free-energy balance ingredients from which the frozen result follows under R1's restrictive assumptions.

### Structural verdict

\[
\boxed{
\text{R1 affine redundancy is best positioned as an explicit optimal-control consequence of a standard one-channel gyrokinetic free-energy balance limit.}
}
\]

### Fidelity verdict

\[
\boxed{
\text{Do not use FLR-only or ad-hoc damping as a redundancy-breaking rescue.}
}
\]

The strongest physics-first next gate is a **balance-complete two-species local-gyrokinetic specification gate** with nonadiabatic electrons, finite ion FLR and a physically defined collision treatment, with all particle/heat/species channels frozen before any finite-time objective calculation.

No new Fusion execution is authorized by this report.

**EXECUTION COMPLETE — STOP / RETURN TO MASTER.**
