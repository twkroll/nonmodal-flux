# Supplement Table S1 — Operational rules and representative frozen outcomes

The study-specific strong rule is **operational, not a universal physical threshold**: both `theta >= 20 deg` and `Delta_Q >= 0.25` are required on at least two neighboring frozen horizons, together with the domain-specific numerical/structural and robustness gates. The Plasma benchmark retains its separately frozen `S0-S5` gate logic; common `theta`/`Delta_Q` values are listed only for cross-domain comparison.

| Case | Representative frozen horizon(s) | Geometry | Target-performance gap | Robustness / outcome |
|---|---|---|---|---|
| Plasma `P2-A` | `T=1` | `theta=53.396 deg` | `Delta_Gamma=0.504337` | strong primary anchor on tested `K=32,64,96` common resolved subspace |
| Neuro `NEURO-STRONG` | 112 ms; 224 ms | `46.824 deg`; `65.058 deg` | `0.529017`; `0.817841` | strong at neighboring frozen horizons; rank-two two-pulse geometry |
| Climate-A `CLIM-WEAK` | `T/tau_ref=8` | conservative subspace angle `90 deg` | `Delta_heat=0.0411846` | all six frozen horizons resolution robust; weak geometry/performance contrast |
| **Climate-B `CLIM-B-FAIL — resolution robustness`** | all six frozen horizons | large fixed-resolution angles may occur | `Delta_shift=1` at fixed truncation | **0/6 horizons pass full refinement; rejected as robust evidence** |

Climate-B attractive fixed-resolution quantities must never be quoted without the same-context failure qualification.
