# Evidence & Citation Map 0.2

**Status:** CANONICAL SUPPORT FOR MANUSCRIPT REVISION 0.3  
**Authority:** `research/master/manuscript_structure_freeze_0_2.md`  
**Primary draft:** `research/manuscript/manuscript_draft_0_3.md`  
**Rule:** frozen evidence only. No result may be strengthened by interpolation, a new horizon, resolution, simulation, eigensolve, parameter, model, objective, channel, admissible geometry, or changed physical interpretation.

## 0. Canonical frozen source inventory

### Cross-domain / manuscript governance

- `research/master/cross_domain_result_integration_freeze_0_1.md`
- `research/master/cross_domain_manuscript_positioning_claim_freeze_0_1.md`
- `research/master/manuscript_draft_review_gate_0_1.md`
- `research/master/climate_intra_domain_contrast_result_integration_freeze_0_1.md`
- `research/master/manuscript_structure_freeze_0_2.md`
- `research/manuscript/manuscript_draft_0_2.md` — editorial rollback point
- `research/literature/cross_domain_application_literature_positioning_audit_0_1.md`

### Plasma

- model/specification: `research/d10_zf_pilot_0_1_specification.md`
- frozen execution: `research/d10_zf_pilot_0_2_execution_results.md`
- machine-readable data: `research/d10_zf_pilot_0_2_execution_data.csv`

### Neuro

- specification: `research/neuro/neuro_pilot_specification_0_1.md`
- frozen execution: `research/neuro/neuro_pilot_0_1_execution_results.md`
- machine-readable data: `research/neuro/neuro_pilot_0_1_execution_data.csv`

### Climate-A / Phillips-QG

- numerical/model definition: `research/climate/climate_ocean_numerical_qualification_0_1.md`
- execution specification: `research/climate/climate_ocean_pilot_specification_0_1.md`
- frozen execution: `research/climate/climate_ocean_pilot_0_1_execution_results.md`
- machine-readable data: `research/climate/climate_ocean_pilot_0_1_execution_data.csv`

### Climate-B / Bickley-jet robustness-rejection case

- candidate freeze: `research/climate/climate_intra_domain_contrast_candidate_freeze_0_1.md`
- numerical qualification: `research/climate/climate_intra_domain_contrast_numerical_qualification_0_1.md`
- pilot specification: `research/climate/climate_intra_domain_contrast_pilot_specification_0_1.md`
- frozen execution: `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_results.md`
- machine-readable data: `research/climate/climate_intra_domain_contrast_pilot_0_1_execution_data.csv`
- integrated frozen verdict: `research/master/climate_intra_domain_contrast_result_integration_freeze_0_1.md`

## 1. Cross-domain framework and study-design claims

| Draft 0.3 claim | Frozen source | Allowed wording | Restriction |
|---|---|---|---|
| Common methodological tuple is `(A,M,Q,B,R_in)` | claim freeze; CORE freeze; Draft 0.2 | “common methodological layer” | do not imply common physical semantics |
| Positive objective and signed channel are compared on the same admissible space | claim/structure freezes | “objective-nonredundancy diagnostic” | not a new theorem |
| Physical storage uses `S_M=1/2 x^dagger M x`, while `K_M` is written for doubled form | Draft Review Gate; frozen definitions | common factor omitted from operator; optimizer/gap unaffected | restore `1/2` when naming physical storage |
| `theta` and `Delta_Q` are distinct diagnostics | integrated result freeze; Climate-A result | “geometry and target performance are assessed separately” | angle alone is not practical nonredundancy |
| Robustness is a third evidentiary layer | Structure Freeze 0.2; Climate-B integration freeze | large fixed-resolution separation can be rejected by frozen refinement criteria | do not infer nonrobust physical effect from fixed truncation |
| strong application criterion uses `theta>=20 deg`, `Delta_Q>=0.25` on two neighboring horizons | cross-domain pilot/claim freezes; application specifications | “study-specific operational strong criterion” | never call thresholds universal constants |
| analysis choices were fixed before effect inspection | specifications/freezes/commit chronology | “pre-specified and frozen before objective-separation evaluation” or “prospectively frozen in the version-controlled analysis record before effect inspection” | do not use unqualified `preregistered` |
| “physical channel” covers signed transport/exchange/pathway-contribution observables | claim freeze; review gate | broad methodological definition | do not imply every channel is a conserved flux |

## 2. Plasma evidence map

| Claim | Frozen source | Exact support / quantity | Required positioning | Forbidden extension |
|---|---|---|---|---|
| D10-ZF PDE and Galerkin state | `research/d10_zf_pilot_0_1_specification.md` | frozen continuous model and Fourier ordering | model definition only | no new plasma model |
| `U=cos x`, `Lx=2pi`, `ky=C=kappa=1`, `N=0` | same | canonical point | frozen pre-effect point | no retuning |
| Pilot-0.2 damping `A=A0-0.020I` | execution result | scope lock | prospectively selected stability axis | no post-effect damping change |
| free-energy metric `M=diag(-Delta,I)` | specification | physical free energy | call it Plasma free energy | not generic state norm in physical captions |
| particle channel `Q_Gamma=(ky/2)[[0,iI],[-iI,0]]` | specification | signed radial particle flux | retain sign | no absolute transport replacement |
| `B=I`, `R_in=M` | specification | full retained Galerkin space | physical admissibility | no transport-neutral claim |
| spectral stability at `K=32,64,96` | execution result | `alpha=-0.0075786,-0.0133818,-0.0154924` | stable controlled benchmark | no continuum-limit theorem |
| `G_E>1` at all frozen horizons | execution result | six-horizon table | transient free-energy amplification | not first plasma transient growth |
| signed cumulative transport has both signs | execution result | `J_Gamma^-<0<J_Gamma^+` | signed-channel evidence | no unsigned substitute |
| `T=1`: `G_E=1.8782758`, `J_Gamma+=0.3535169`, `J_Gamma-=-0.1462216` | execution result | representative row | frozen witness | no alternative effect-enhancing witness |
| `T=1`: `J_Gamma(w_E)=0.1752252`, `Delta_Gamma=0.5043372`, `theta=53.396 deg` | execution result | representative row | strong anchor | not generic to plasma |
| resolution-robust optimizer structure | execution result | common-subspace overlap one to floating precision; unresolved energy ~`2e-15` | tested ladder only | no continuum proof |

Literature positioning remains prior-art-first: stable plasma transient amplification is established [Landreman2015]; adjacent objective-dependent optimizer precedent includes [Foures2014; Sevellec2008].

## 3. Neuro evidence map

| Claim | Frozen source | Exact support / quantity | Required positioning | Forbidden extension |
|---|---|---|---|---|
| two-source V1/V4 CMC with SS/SP/II/DP | `research/neuro/neuro_pilot_specification_0_1.md` | frozen source identities and architecture | CMC/DCM context | no in-vivo validation claim |
| autonomous instantaneous-coupling pilot | same | propagation-delay module disabled | scope restriction | never biological zero-delay claim |
| 16-state `(v,z)` region-major ordering | same | Sec. state ordering | model definition | no hidden-state reinterpretation |
| stable generator | specification/execution | `alpha(A)=-33.0964092356 s^-1` | numerical qualification | no generic CMC stability claim |
| synaptic-filter storage | same | `1/2(z^2+kappa^2v^2)` and diagonal `M` | “model-internal synaptic-filter storage” | never brain/metabolic/thermodynamic energy |
| primary path V1-SP -> V4-SS | same | predefined connection | physiological pathway label | no generic causal efficacy claim |
| `Q_j->i=1/2(A_j->i^dagger M+M A_j->i)` | same | pathway contribution to storage-rate balance | sign = storage-rate contribution | sign is not excitatory/inhibitory sign |
| two fixed 1-ms afferent pulses ending 2 and 16 ms before observation | same | preparation protocol | fixed rank-two preparation geometry | not time-dependent optimal control |
| `rank(B)=2`, whitened condition number `34.294<100` | same | qualification | pre-effect geometry gate | no retuned pulse times |
| `R_in=I_2` | same | pulse-dose coordinates only | input-cost metric | not `B=I` in neural state space |
| `tau_ref=28 ms`; horizons 7–224 ms | same | frozen time ladder | model-native scale | no new horizon |
| `NEURO-STRONG` at 112/224 ms | execution result | `theta=46.824/65.058 deg`, `Delta=0.529017/0.817841` | strong application result | no threshold change |
| pathway optimum ~`(+0.9924,-0.1230)` versus same-sign storage optima | execution result | frozen optimizer table | direct two-pulse interpretation | not stimulation recommendation |
| cumulative negative pathway branch not reachable on frozen `B` space | execution + integration freeze | minimum eigenvalue `K_Q(T)` positive | keep restriction prominent | no bidirectional cumulative-transfer claim |
| narrow absence statement | literature audit | approved Neuro positioning | use “to our knowledge” only | no mathematical novelty claim |

Approved positioning sources: [Hennequin2012; Bondanelli2020; Friston2003; Daunizeau2011; Salfenmoser2022; Ogino2026]. `Ogino2026` final publication status remains metadata verification only.

## 4. Climate-A evidence map

| Claim | Frozen source | Exact support / quantity | Required positioning | Forbidden extension |
|---|---|---|---|---|
| damped two-layer Phillips-QG equations | `research/climate/climate_ocean_numerical_qualification_0_1.md` | frozen physical model | idealized QG model | no Primitive-Equation extrapolation |
| periodic `x`, Dirichlet walls, `kx!=0` eddy restriction | same | structure-preserving basis | physical state restriction | no zonal-mean mode |
| BT/BC variables and QG energy | same | modal energy matrix | Climate-A QG energy | do not conflate with Plasma free energy |
| signed poleward heat transport and `Q_heat` | same | direct signed-flux reproduction | positive = northward/poleward | no absolute/squared heat objective |
| `B=I`, `R_in=M_K`, `tau_ref=0.7233796296 d` | climate specification | frozen admissible geometry/time | fixed normalization | no changed cost/time scale |
| primary/confirmation/high resolutions `(12,12)/(16,16)/(24,24)` | specification | frozen roles | mandatory refinement | no extra rung |
| stable `alpha=-0.1 d^-1` | qualification/execution | all qualified rungs | Farrell1985 context | not new stability result |
| first five horizons nearly redundant | execution result | gap <= about `0.00317` | report weak finding | do not hide |
| longest support switches `(3,2)` vs `(4,2)` | execution result | exact modal supports | structural contrast | no generic modal-switch claim |
| `theta_sub=90 deg`, `J_heat+=1.54448995`, `J_heat|E=1.48088082` | execution result | `T/tau_ref=8` | representative robust witness | do not call strong replication |
| `Delta_heat=0.04118455`, retained performance ~95.88% | execution result | longest horizon | canonical geometry/performance contrast | no generic failure of energy optimization |
| all six horizons resolution robust | execution result | value invariance, `mu_c=1`, rank 2, angles <`1.5e-6 deg` | robustness support | tested ladder only |
| narrow same-system absence statement | literature audit | approved Climate positioning | “to our knowledge” only | no broad novelty claim |

Approved positioning sources: [Farrell1982; Farrell1985; FarrellIoannou1994; KimMorgan2002; Kuang2004; Sevellec2008].

## 5. Climate-B robustness-rejection evidence map

Climate-B is **robustness-rejection evidence only**. It is not robust positive Climate application evidence and may not be added to the Plasma/Neuro/Climate-A positive/weak evidence sequence.

| Claim | Frozen source | Exact support / quantity | Allowed wording | Forbidden wording/extension |
|---|---|---|---|---|
| equivalent-barotropic Bickley jet | candidate freeze | `U=U0 sech^2(y/L)` with fixed physical point | “one-shot Bickley-jet robustness audit” | no alternative jet/parameter point |
| fixed physical point | candidate freeze | `beta=1.6e-11`, `U0=20 m/s`, `L=1000 km`, `r=(10d)^-1`, `Lx=20000 km`, `Ly=10000 km` | frozen pre-effect point | no retuning |
| positive metric | candidate freeze | perturbation kinetic energy | barotropic perturbation kinetic energy | do not call it Climate-A QG energy |
| signed shift channel | candidate freeze | `g=-U'`; Reynolds-stress convergence projected onto translation tangent | cumulative eddy forcing/impulse of infinitesimal translation coordinate | never realized nonlinear jet displacement/climate-change prediction |
| `B=I`, `R_in=M_K` | candidate freeze | complete retained eddy state | fixed admissible geometry | no masks/EOF/localization |
| parity structure | candidate/numerical qualification | `A_K` preserves parity; `Q_shift,K` couples opposite parity | mechanism for fixed-truncation observation | every manuscript mention must carry resolution-failure qualification in same paragraph/caption |
| pre-effect numerical qualification | numerical qualification | quadrature audit worst `2.92e-14`; signed witness reproduced; stable `alpha=-0.1 d^-1` | local/structural qualification passed | not evidence of finite-time robustness |
| frozen horizons | pilot specification | `T/tau_ref={0.25,0.5,1,2,4,8}` | all six executed | no added/interpolated horizon |
| mandatory resolutions | pilot specification | primary `(16,32)`, confirmation `(20,40)`, high `(24,48)` | frozen refinement ladder | no extra repair rung |
| objective-value convergence rule | pilot specification | `epsilon_Y<=0.02` for `G_M,J_shift+,|J_shift-|` | pre-specified refinement criterion | no relaxed threshold |
| common-space rule | pilot specification | `mu_c>=0.95`, equal rank, max principal angle <=10 deg | pre-specified subspace criterion | no raw padded-vector comparison |
| local finite-time gates all passed | execution result | worst Hermiticity `5.49e-15`; Lyap/block exp `1.06e-12`; direct shift error `9.68e-14`; etc. | “failure is not algebraic/direct-reproduction failure” | do not imply refinement passed |
| fixed-truncation `Delta_shift=1` and large angles | execution result | all mandatory same-resolution rows | may be described only as a striking fixed-resolution observation **rejected by refinement** | never quote without same-context resolution-failure qualification; never put in Abstract |
| zero of six horizons robust | execution result + integration freeze | complete refinement table | “0/6 frozen horizons passed the full refinement protocol” | no subset cherry-picking |
| short-horizon cutoff migration | execution result | e.g. `m=16->20->24`, `mu_c=0` at `T/tau=.25` | example of small-scale sensitivity | no repair interpretation |
| longest-horizon failure persists | execution result | `mu_M=.7281/.7808`, `mu_shift=.7513/.8337`; `eps_J+=.0835/.0360` | concrete robustness-failure witness | do not call near-converged strong result |
| frozen verdict | execution/integration freezes | `CLIM-B-FAIL — resolution robustness failure` | exact manuscript label | never `CLIM-B-STRONG` or robust strong Climate-B |
| no repair before first manuscript | integration/structure freezes | no hyperdiffusion, scale-selective damping, extra resolution, changed channel/geometry, third candidate | “no repair proposal is part of this paper” | no rescue plan framed as manuscript result |

### Required main-text rule

Climate-B may appear only as the brief Sec. 5.2 robustness-rejection case. If `Delta_shift=1`, a near-90-degree/90-degree angle, or the parity mechanism is mentioned, the same paragraph must state that **zero of six horizons passed the full cross-resolution robustness protocol** and that the result is rejected as robust Climate evidence.

### Required Supplement S5 rule

Supplement S5 may contain the full frozen model/protocol/result ledger. It must clearly separate:

1. passed candidate/numerical/local finite-time gates;
2. attractive same-resolution separation;
3. failed cross-resolution objective/subspace gates;
4. exact verdict `CLIM-B-FAIL — resolution robustness failure`;
5. no repair proposal as part of this paper.

## 6. Abstract witness freeze

Draft 0.3 uses exactly the three robust representative witnesses already frozen in Draft 0.2 and Structure Freeze 0.2:

- Plasma: `T=1`, energy optimum misses about 50.4% of maximum positive cumulative particle transport.
- Neuro: 112/224 ms, pathway-performance gaps `0.529/0.818`.
- Climate-A: longest horizon, `90 deg` subspace separation with only `0.0412` heat gap and `95.88%` retained heat performance.

Climate-B may receive at most one qualitative Abstract sentence stating that an additional one-shot geophysical fixed-resolution result was rejected by the pre-specified refinement criteria. Do not quote `Delta_shift=1` in the Abstract.

These witnesses may not be replaced by effect-enhancing alternatives.

## 7. Surviving and forbidden manuscript-level claims

### Allowed

- A physics-informed finite-time workflow can test whether a positive storage/state objective is redundant with a separately defined signed physical channel on the same admissible space.
- In the frozen robust evidence, objective nonredundancy is strong in Plasma and Neuro and weak in Climate-A.
- Optimizer geometry and target-performance loss must be evaluated separately.
- Large fixed-resolution separation can fail pre-specified refinement and must not be promoted without robustness.
- The contribution is a controlled cross-domain diagnostic workflow and physical interpretation, not new generic quadratic-output mathematics.

### Forbidden

- new general quadratic-output, Gramian, singular-vector, or optimal-perturbation mathematics;
- universal nonredundancy of energy/storage and transport/channel objectives;
- first plasma transient growth or first neural optimal stimulation;
- robust strong Climate-B evidence;
- a demonstrated strong-versus-weak intra-domain Climate pair;
- claims that Climate-B `Delta_shift=1` or near-orthogonal optimizers survive refinement;
- interpreting `J_shift` as realized nonlinear jet displacement or climate-change prediction;
- generic failure of energy optimization for climate transport;
- universal interpretation of the 20-degree / 0.25 study thresholds;
- flattening Plasma free energy, Neuro storage, Climate-A QG energy, and Climate-B kinetic energy into one physical quantity.

## 8. Bibliographic status

Bibliographic metadata in Draft 0.3 are inherited only from approved positioning sources in Draft 0.2 and the frozen literature audits. `Ogino2026` remains marked for final publication-status verification before submission. Metadata cleanup is editorial; it does not authorize a new novelty search or reclassification.

## 9. Figure, table, and supplement evidence discipline

Figures and tables may read only the frozen CSV/result files and frozen analytical definitions listed above. Presentational transformations are allowed; scientific transformations are not. No plotting or supplement script may instantiate models, solve new matrix exponentials/eigensystems, create new horizon values, rerun trajectories, interpolate, smooth, or fit scientific data.

Main Fig. 5 uses only robust Plasma/Neuro/Climate-A diagnostics and must be a non-inferential geometry/performance summary, not a phase diagram. Climate-B fixed-resolution effect points are excluded from this robust-domain summary and belong only in the clearly labeled Supplement S5 robustness-rejection display.

Former Main Table 2 is supplementary. Any Climate-B row must read `CLIM-B-FAIL — resolution robustness` or equivalent unambiguous failure wording.

**STOP — Evidence & Citation Map 0.2 introduces no new scientific result.**
