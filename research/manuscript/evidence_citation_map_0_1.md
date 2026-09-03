# Evidence & Citation Map 0.1

**Status:** CANONICAL DRAFT SUPPORT  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`  
**Purpose:** map manuscript claims to frozen evidence, required prior art, and claim restrictions.

## 0. Evidence discipline

Every quantitative statement in `research/manuscript/manuscript_draft_0_1.md` must trace to one of the frozen result files below. No result may be strengthened by interpolation, a new horizon, a new resolution, or a new simulation.

Canonical frozen evidence:

- Plasma: `research/d10_zf_pilot_0_2_execution_results.md`
- Plasma machine-readable data: `research/d10_zf_pilot_0_2_execution_data.csv`
- Neuro: `research/neuro/neuro_pilot_0_1_execution_results.md`
- Neuro machine-readable data: `research/neuro/neuro_pilot_0_1_execution_data.csv`
- Climate/Ocean: `research/climate/climate_ocean_pilot_0_1_execution_results.md`
- Climate/Ocean machine-readable data: `research/climate/climate_ocean_pilot_0_1_execution_data.csv`
- Integrated result freeze: `research/master/cross_domain_result_integration_freeze_0_1.md`
- Manuscript claim freeze: `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`
- Neuro/Climate literature audit: `research/literature/cross_domain_application_literature_positioning_audit_0_1.md`

## 1. Cross-domain framework claims

| Manuscript claim | Frozen evidence | Quantity / section | Allowed wording | Required citation context | Restriction |
|---|---|---|---|---|---|
| Common transferable tuple is `C=(A,M,Q,B,R_in)` | claim freeze; result integration freeze | framework sections | “common methodological layer” | none required for project definition; cite established optimal-perturbation literature in Introduction | do not imply common physical semantics |
| Positive objective and signed channel should be compared on same admissible space | claim freeze | canonical manuscript claim | “physics-informed objective-nonredundancy diagnostic” | Foures2014; Sevellec2008 as adjacent objective-dependent precedents | not a new theorem |
| Optimizer angle and channel-performance loss are distinct diagnostics | Climate execution + result freeze | longest QG horizon | “geometry and performance must be assessed separately” | prior-art discussion may mention norm dependence | do not infer practical nonredundancy from angle alone |
| Preregistration/anti-retuning is part of workflow | all pilot specification/result freezes | no-retuning records | “frozen before effect inspection” / “no retuning” | none required beyond methods | do not call threshold values universal constants |

## 2. Plasma claim map

| Claim | Source file | Exact source quantity | Allowed wording | Required prior art | Forbidden wording |
|---|---|---|---|---|---|
| Frozen D10-ZF resolutions are spectrally stable | `research/d10_zf_pilot_0_2_execution_results.md` | Sec. 1; `alpha(A_K)` = -0.0075786, -0.0133818, -0.0154924 | “spectrally stable at all three frozen resolutions” | Landreman2015 for stable plasma transient amplification context | no universal stability claim |
| Finite-time free-energy amplification exceeds unity at every horizon | same | Sec. 2; `G_E` = 1.1747 … 39.7632 | “finite-time free-energy amplification despite modal stability” | Landreman2015 | not first plasma transient growth |
| Cumulative particle transport has positive and negative extrema | same | Sec. 2; `G_Gamma,-<0<G_Gamma,+` | “signed cumulative particle-transport operator has both signs” | none beyond plasma context | do not replace by absolute transport |
| At `T=1`, energy optimum misses ~50.4% of max positive particle transport | same | row `T=1`; `Delta_Gamma=0.5043371669` | “misses approximately 50%” / “realizes about one half” | Foures2014; Sevellec2008 as adjacent objective-dependence precedents | not generic to plasma |
| At `T=1`, optimizer angle is 53.396° | same | row `T=1` | report only paired with `Delta_Gamma` | none | angle alone is not enough |
| Plasma optimizer difference is resolution robust | same | Sec. 3 | “resolution robust across K=32,64,96” | none | no claim beyond tested ladder |
| Plasma optimizers differ structurally in Fourier support and phase | same | Secs. 4–5 | “physically distinct within frozen representation” | none | do not infer nonlinear turbulence behavior |
| Direct modal trajectory decays while finite-time optimals grow | same | Sec. 6 | “least-damped modal trajectory decays while finite-time optimal perturbations amplify” | Landreman2015 | not proof of nonlinear subcritical turbulence |

### Plasma required citations

- Landreman, Plunk & Dorland (2015), DOI `10.1017/S0022377815000495`.
- Foures, Caulfield & Schmid (2014), DOI `10.1017/jfm.2014.182`.
- Sévellec et al. (2008), DOI `10.1175/2008JPO3875.1`.

## 3. Neuro claim map

| Claim | Source file | Exact source quantity | Allowed wording | Required prior art | Forbidden wording |
|---|---|---|---|---|---|
| Frozen model is stable two-source V1/V4 CMC/DCM | `research/neuro/neuro_pilot_0_1_execution_results.md` | scope + structural gates; `alpha(A)=-33.096409 s^-1` | “stable two-source V1/V4 CMC/DCM tangent model” | Friston2003 for DCM background | no in-vivo validation claim |
| Positive metric is synaptic-filter storage | same + claim freeze | scope / semantic guardrail | “model-internal synaptic-filter storage” | none | never “brain energy”, “metabolic energy”, “thermodynamic energy” |
| Primary physiological channel is V1-SP -> V4-SS pathway contribution | same | frozen tuple | “predefined pathway contribution to storage-rate balance” | Friston2003 for effective-connectivity context | not generic causal efficacy |
| Admissible preparation is rank-two two-pulse geometry | same | scope; rank(B)=2; pulse delays 2 and 16 ms | “fixed rank-two two-pulse afferent preparation” | Basu2018 / DCM input-design context if desired | no hidden-state actuation claim |
| `NEURO-STRONG` thresholds met at neighboring 112 and 224 ms | same | Sec. 3; 112 ms and 224 ms rows | exact values allowed | none | do not change thresholds post hoc |
| 112 ms: angle 46.824°, gap 0.529 | same | Sec. 3 | exact numerical report | none | pair geometry with gap |
| 224 ms: angle 65.058°, gap 0.818 | same | Sec. 3 | exact numerical report | none | pair geometry with gap |
| Pathway optimum ~(+0.9924,-0.1230) | same | Sec. 4 | “dominant recent pulse plus small opposite-sign older pulse” | none | not a stimulation recommendation |
| Storage optimum at 224 ms ~(+0.5300,+0.8480) | same | Sec. 4 | “same-sign mixture, older pulse dominant” | none | not experimentally validated efficacy |
| Negative cumulative pathway extremum is not reachable on frozen `B` space | same | Sec. 3 + result integration freeze | “cumulative minimum remains positive on frozen rank-two preparation space” | none | do not claim reachable bidirectional cumulative transfer |
| Narrow application-specific novelty survives | literature audit | Neuro sections 2.4–2.5 | use exact “to our knowledge” formulation only | Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026 | no broad optimal-stimulation novelty |

### Neuro required citations

- Hennequin, Vogels & Gerstner (2012), Phys. Rev. E 86, 011909.
- Bondanelli & Ostojic (2020), PLoS Comput. Biol. 16, e1007655.
- Friston, Harrison & Penny (2003), NeuroImage 19, 1273–1302.
- Daunizeau et al. (2011), PLoS Comput. Biol. 7, e1002280.
- Salfenmoser & Obermayer (2022), Front. Comput. Neurosci. 16, 931121.
- Ogino et al. (2026), eLife reviewed preprint 110030.

## 4. Climate/Ocean claim map

| Claim | Source file | Exact source quantity | Allowed wording | Required prior art | Forbidden wording |
|---|---|---|---|---|---|
| Frozen Phillips-QG pilot is spectrally stable | `research/climate/climate_ocean_pilot_0_1_execution_results.md` | structural gates; `alpha=-0.1 d^-1` | “stable damped two-layer Phillips-QG pilot” | Farrell1985 | not new stable baroclinic transient growth |
| All primary/confirmation/audit numerical gates pass | same | Secs. 3 and 6 | “resolution robust over frozen nested ladder” | none | no extrapolation beyond tested ladder |
| Positive metric is QG perturbation energy; channel is signed meridional eddy heat transport | same | frozen pilot | exact domain-specific wording | FarrellIoannou1994; Sevellec2008 context | no generic heat-transport novelty |
| First five horizons show near redundancy | same | Secs. 4–5 | “same modal support; small angle and gap” | KimMorgan2002; Kuang2004 | do not hide this weak result |
| Longest horizon energy support `(3,2)`, heat support `(4,2)` | same | Sec. 5 | exact modal-support statement | none | no claim of general modal switch |
| Longest-horizon optimal subspaces are orthogonal | same | Sec. 5; `theta_sub=90°` | exact geometry | norm-dependence prior art | angle must be paired with gap |
| Longest-horizon heat gap is 0.04118455338 | same | Sec. 5 | “only 4.12%” | none | not a strong replication |
| Energy optimum retains about 95.88% of max poleward heat transport | same | Sec. 5 | exact interpretation | none | do not say energy optimum fails to transport heat |
| Heat optimum is more baroclinic / shorter zonal scale at longest horizon | same | Sec. 7 | physical structure statement | none | no forecast-skill extrapolation |
| Heat-opt flux changes sign once late at longest horizon | same | Sec. 8 | “late sign reversal while net signed integral remains maximal” | none | do not replace signed integral with absolute flux |
| Narrow same-system novelty wording survives only cautiously | literature audit | Climate sections 3.4–3.5 | exact “to our knowledge” formulation only | Farrell1982; Farrell1985; FarrellIoannou1994; KimMorgan2002; Kuang2004; Sevellec2008 | no broad QG/singular-vector novelty |

### Climate/Ocean required citations

- Farrell (1982), J. Atmos. Sci. 39, 1663–1686.
- Farrell (1985), J. Atmos. Sci. 42, 2718–2727.
- Farrell & Ioannou (1994), J. Atmos. Sci. 51, 2685–2698.
- Kim & Morgan (2002), J. Atmos. Sci. 59, 3099–3116.
- Kuang (2004), J. Atmos. Sci. 61, 2943–2949.
- Sévellec et al. (2008), DOI `10.1175/2008JPO3875.1`.

## 5. Abstract-level quantitative witnesses

The abstract may use at most one compact witness per domain, all traceable to frozen tables:

- Plasma: `T=1`, `Delta_Gamma=0.504337`, optionally `theta=53.396°`.
- Neuro: adjacent 112/224 ms pair; `Delta_Q=0.529/0.818`, angles `46.824°/65.058°`.
- Climate: longest horizon `theta_sub=90°`, `Delta_heat=0.0411846`, energy optimum retains ~95.88%.

Do not replace the weak Climate witness with an effect-enhancing alternative.

## 6. Section-level wording guardrails

### Abstract
Allowed: common workflow, nonuniform outcomes, representative quantitative witnesses, angle-vs-performance lesson.

Forbidden: “new theory”, “universal”, “first transient growth”, “first optimal perturbation”, “brain energy”, or language implying `CLIM-WEAK` is strong.

### Introduction
Allowed: proxy-objective problem; established prior art; methodological integration gap.

Forbidden: novelty by absence; statements that objective-dependent optimizers were previously unknown.

### Results
Allowed: exact frozen verdicts and numbers.

Forbidden: omission or reframing of `CLIM-WEAK`; optimizer angle without matching performance gap where interpretation depends on nonredundancy.

### Discussion
Allowed: system dependence, role of `B`, signed vs positive objectives, limitations, protected future directions.

Forbidden: nonlinear, experimental, forecast-skill, universal, or cross-domain physical-equivalence claims.

## 7. Bibliographic placeholders requiring later normalization only

Bibliographic cleanup may correct punctuation, issue numbers, page ranges, DOI presentation, and citation style. It may not change the prior-art classification or expand novelty claims without a new literature gate.

**STOP — evidence map contains no new scientific result.**
