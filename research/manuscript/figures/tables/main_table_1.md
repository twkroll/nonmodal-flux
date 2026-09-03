# Main Table 1 — Model/objective/admissible-geometry definitions

| Domain | Defining model | Positive metric | Signed physical channel | Admissible geometry / input cost | Time normalization | Frozen role |
|---|---|---|---|---|---|---|
| Plasma/D10-ZF | stable drift-wave/zonal-flow linearization | free energy, `E=1/2 z^dagger M z` | cumulative signed radial particle transport | full frozen Galerkin perturbation space; `B=I`, `R_in=M` | nondimensional D10-ZF time, `tau_ref=1` | `P2-A` strong anchor |
| Neuro/CMC | stable two-source V1/V4 canonical microcircuit | terminal model-internal synaptic-filter storage | cumulative V1-SP -> V4-SS pathway contribution to storage rate | rank-two fixed two-pulse afferent preparation; `R_in=I_2` | `tau_ref=28 ms` | `NEURO-STRONG` |
| Climate-A/Phillips-QG | stable damped two-layer quasigeostrophic model | QG perturbation energy | cumulative signed poleward eddy heat transport | balanced QG eddy state space; `B=I`, `R_in=M_K` | `tau_ref=0.7233796296 d` | `CLIM-WEAK` robust contrast |

**Semantic guardrail:** the three positive metrics and three signed channels are physically distinct. In particular, the Neuro metric is synaptic-filter state storage, not metabolic, thermodynamic, or total physiological brain energy.
