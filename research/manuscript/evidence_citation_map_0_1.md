# Evidence & Citation Map 0.1

**Status:** CANONICAL SUPPORT FOR MANUSCRIPT REVISION 0.2  
**Authority:** `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md` and `research/master/manuscript_draft_review_gate_0_1.md`  
**Primary draft:** `research/manuscript/manuscript_draft_0_2.md`

## 0. Evidence discipline

Every quantitative or model-defining statement in Draft 0.2 must trace to a frozen source. No result may be strengthened by interpolation, a new horizon, a new resolution, a new simulation, or a changed physical interpretation.

Canonical frozen evidence and specification sources:

- Plasma model definition: `research/d10_zf_pilot_0_1_specification.md`
- Plasma frozen execution: `research/d10_zf_pilot_0_2_execution_results.md`
- Plasma machine-readable data: `research/d10_zf_pilot_0_2_execution_data.csv`
- Neuro specification: `research/neuro/neuro_pilot_specification_0_1.md`
- Neuro execution: `research/neuro/neuro_pilot_0_1_execution_results.md`
- Neuro machine-readable data: `research/neuro/neuro_pilot_0_1_execution_data.csv`
- Climate numerical/model definition: `research/climate/climate_ocean_numerical_qualification_0_1.md`
- Climate execution specification: `research/climate/climate_ocean_pilot_specification_0_1.md`
- Climate execution: `research/climate/climate_ocean_pilot_0_1_execution_results.md`
- Climate machine-readable data: `research/climate/climate_ocean_pilot_0_1_execution_data.csv`
- Integrated result freeze: `research/master/cross_domain_result_integration_freeze_0_1.md`
- Claim freeze: `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`
- Draft review: `research/master/manuscript_draft_review_gate_0_1.md`
- Neuro/Climate literature audit: `research/literature/cross_domain_application_literature_positioning_audit_0_1.md`

## 1. Cross-domain framework and study-design claims

| Draft 0.2 claim | Frozen source | Allowed wording | Restriction |
|---|---|---|---|
| Common methodological tuple is `(A,M,Q,B,R_in)` | claim freeze; CORE freeze | “common methodological layer” | do not imply common physical semantics |
| Positive objective and signed channel are compared on the same admissible space | claim freeze | “objective-nonredundancy diagnostic” | not a new theorem |
| `S_M=1/2 x^dagger M x`, while `K_M` is written for `x^dagger M x` | Draft Review Gate; frozen definitions | “common factor 1/2 omitted from the operator; optimizer/gap unaffected” | restore factor when calling the quantity physical storage |
| `theta` and `Delta_Q` are distinct diagnostics | result freeze; Climate result | “geometry and performance are assessed separately” | angle alone is not practical nonredundancy |
| strong application criterion uses `theta>=20 deg`, `Delta_Q>=0.25` on two neighboring horizons | Cross-Domain Pilot/Claim freezes | “study-specific operational strong criterion” | never call thresholds universal constants |
| analysis choices were fixed before effect inspection | specifications/freezes/commit chronology | “pre-specified and frozen before objective-separation evaluation” | default wording is not “preregistered” unless external registration chronology is documented |
| “physical channel” covers signed transport/exchange/pathway-contribution objectives | claim freeze + review gate | broad methodological definition | do not imply every channel is a conserved flux |

## 2. Plasma model and result map

| Claim | Source | Exact support / quantity | Required positioning | Forbidden extension |
|---|---|---|---|---|
| D10-ZF linear PDE and Galerkin state | `research/d10_zf_pilot_0_1_specification.md` | Secs. 1–4 | model definition only | no new plasma model |
| `U=cos x`, `Lx=2pi`, `ky=C=kappa=1`, `N=0` | same | Secs. 1–2 | frozen point | no retuning |
| state at resolution `K`: all `phi_m`, then all `eta_m`, `m=-K...K` | same + execution dimensions | Fourier ordering generalized from frozen Galerkin convention | presentational generalization only | do not change basis |
| free-energy metric `M=diag(-Delta,I)` | same | Sec. 5 | Plasma free energy | not generic “state norm” in captions |
| particle channel `Q_Gamma=(ky/2)[[0,iI],[-iI,0]]` | same | Sec. 6 | signed radial particle transport | do not replace by absolute transport |
| Pilot 0.2 damping `A=A0-0.020I` | execution result | scope lock | prospectively selected stability axis | no post-effect damping change |
| spectral stability at `K=32,64,96` | execution result | `alpha=-0.0075786,-0.0133818,-0.0154924` | Landreman2015 context | no universal stability claim |
| `G_E>1` over all frozen horizons | execution result | Sec. 2 | transient free-energy amplification | not first plasma transient growth |
| signed cumulative transport has both signs | execution result | `J_Gamma^-<0<J_Gamma^+` | signed channel | no absolute-value replacement |
| `T=1`: `Delta_Gamma=0.504337`, `theta=53.396 deg` | execution result | `T=1` row | Foures2014; Sevellec2008 as adjacent objective-dependence precedents | not generic to plasma |
| resolution-robust optimizer structure | execution result | Secs. 3–5 | tested ladder only | no continuum-limit claim |

## 3. Neuro model and result map

| Claim | Source | Exact support / quantity | Required positioning | Forbidden extension |
|---|---|---|---|---|
| two-source V1/V4 CMC with SS/SP/II/DP populations | `research/neuro/neuro_pilot_specification_0_1.md` | Sec. 1 | Friston2003 / CMC context | no in-vivo validation claim |
| 16-state `(v,z)` region-major ordering | same | Sec. 3 | model definition | no hidden-state reinterpretation |
| synaptic-filter storage `1/2(z^2+kappa^2 v^2)` and diagonal `M` | same | Sec. 6 | “model-internal synaptic-filter storage” | never “brain energy” or “metabolic energy” |
| `A=A_rest+A_j->i`; primary channel V1-SP -> V4-SS | same | Sec. 7 | predefined physiological connection | no claim of generic causal efficacy |
| `Q_j->i=1/2(A_j->i^dagger M+M A_j->i)` | same | Sec. 7 | pathway contribution to storage-rate balance | sign is not excitatory/inhibitory sign |
| two fixed 1-ms pulses ending 2 and 16 ms before observation generate `B` | same | Secs. 8–10 | fixed preparation geometry | not time-dependent optimal control |
| `rank(B)=2`, whitened condition number `34.294<100` | same | Sec. 11 | pre-effect geometry qualification | no retuned pulse times |
| `R_in=I_2` in pulse-amplitude coordinates | same | Sec. 10 | input-cost metric only | not `B=I` in neural state space |
| `tau_ref=28 ms`; horizons 7–224 ms | same | Sec. 12 | model-native time scale | no added horizon |
| `NEURO-STRONG` at 112/224 ms | execution result | `theta=46.824/65.058 deg`, `Delta=0.529/0.818` | narrow application claim | no threshold change |
| pathway optimum `~(+0.9924,-0.1230)` vs same-sign storage optimum | execution result | optimizer table/section | direct preparation-coordinate interpretation | not a stimulation recommendation |
| cumulative negative pathway extremum not reachable on frozen `B` space | execution result + result freeze | minimum eigenvalue remains positive | keep restriction prominent | no bidirectional cumulative-transfer claim |
| narrow absence claim survives | literature audit | Neuro positioning | Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026 | use only “to our knowledge” wording |

## 4. Climate/Ocean model and result map

| Claim | Source | Exact support / quantity | Required positioning | Forbidden extension |
|---|---|---|---|---|
| damped two-layer Phillips-QG PV equations | `research/climate/climate_ocean_numerical_qualification_0_1.md` | Sec. 1 | model definition | no Primitive-Equation extrapolation |
| periodic `x`, Dirichlet streamfunction walls, `kx!=0` eddy restriction | same | Sec. 3 | physical state restriction | no zonal-mean mode added |
| BT/BC variables and QG perturbation energy | same | Secs. 2, 6 | Climate QG energy | do not conflate with Plasma free energy |
| signed poleward heat transport and `Q_heat` | same | Secs. 7–8 | positive = northward/poleward | no absolute/squared heat flux |
| `B=I`, `R_in=M_K`, `tau_ref=0.7233796296 d` | climate specification | Secs. 1–4 | frozen admissible geometry/time | no changed normalization |
| resolution roles `(12,12)/(16,16)/(24,24)` | climate specification | Sec. 3 | primary/confirmation/high audit | no extra rung |
| stable `alpha=-0.1 d^-1` | numerical qualification/execution | qualification table | Farrell1985 context | not new damped baroclinic stability result |
| first five horizons near redundant | execution result | horizon results | report weak finding | do not hide it |
| longest horizon supports `(3,2)` vs `(4,2)` | execution result | modal-support diagnostics | exact result | no generic modal-switch claim |
| `theta_sub=90 deg`, `Delta_heat=0.0411846`, retained performance `95.88%` | execution result | longest-horizon row | canonical geometry/performance contrast | never call this strong replication |
| narrow same-system absence claim survives | literature audit | Climate positioning | Farrell1982; Farrell1985; FarrellIoannou1994; KimMorgan2002; Kuang2004; Sevellec2008 | “to our knowledge” only |

## 5. Abstract witnesses

Revision 0.2 uses one compact witness per domain:

- Plasma: `T=1`, energy optimum misses about 50.4% of maximum positive cumulative particle transport.
- Neuro: 112/224 ms, pathway-performance gaps `0.529/0.818`.
- Climate: longest horizon, `90 deg` subspace angle with only `0.0412` heat gap and `95.88%` retained heat performance.

These are frozen representative witnesses and may not be replaced by effect-enhancing alternatives.

## 6. Bibliographic status

Bibliographic metadata in Draft 0.2 are taken only from already approved literature-positioning sources. `Ogino2026` remains explicitly marked for manual verification of final publication status before submission. Metadata cleanup is permitted; novelty reclassification is not.

## 7. Figure and supplement discipline

Figures may read only frozen CSV/result files and use presentational transformations. Supplement-level model equations, parameter tables, sparse matrices, and chronology may be copied from frozen specification files. No plotting or supplement script may instantiate a model to create new scientific values.

**STOP — this map introduces no new scientific result.**