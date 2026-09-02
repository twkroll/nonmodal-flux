# Climate/Ocean Pilot 0.1 Execution Results

**Status:** EXECUTION COMPLETE  
**Frozen verdict:** `CLIM-WEAK`  
**Authority:** `research/master/cross_domain_pilot_freeze_0_1.md` and
`research/master/prompts/climate_ocean_pilot_execution_0_1.md`

This report executes exactly the preregistered Climate/Ocean Pilot Specification 0.1.
No physical parameter, damping, basis, state ordering, signed convention, resolution role,
horizon, tolerance, threshold, or verdict rule was changed after the first CORE-effect
quantity was inspected.

## 1. Frozen pilot

The executed model is the qualified damped two-layer Phillips-QG system with

\[
(A_K,M_K,Q_{{\rm heat},K},B=I,R_{{\rm in}}=M_K),
\]

positive signed transport defined as northward/poleward eddy heat transport, and

\[
J_{{\rm heat}}(T)=\int_0^T x(t)^\dagger Q_{{\rm heat},K}x(t)\,dt.
\]

The frozen time scale and horizon ladder are

\[
\tau_{{\rm ref}}=0.7233796296\,{\rm d},
\qquad
T/\tau_{{\rm ref}}\in\{0.25,0.5,1,2,4,8\}.
\]

The frozen resolution roles are `(12,12)` primary, `(16,16)` confirmation and `(24,24)`
high-resolution audit, with `(8,8)` coarse audit and `(4,4)` qualification-only smoke.

## 2. Conflict check and anti-bias record

The execution prompt, Cross-Domain Pilot Freeze 0.1, Pilot Specification 0.1,
Numerical Qualification 0.1, current Climate `STATUS.md`, and Cross-Domain Integration
Gate 0.1 were checked before calculation. No conflicting frozen object was found. The
earlier Integration Gate's prohibition on execution was explicitly superseded by the later
Cross-Domain Pilot Freeze, which released the already completed specification for execution.

No retuning or search was performed.

## 3. Structural and numerical gates

All mandatory gates pass at the primary, confirmation and high-resolution audit resolutions.

| gate | preregistered requirement | worst observed result | status |
|---|---:|---:|---|
| spectral stability | `alpha(A_K)<0` | -0.0723379629629627 nondim = -0.1 d^-1 | PASS |
| `M_K` | Hermitian positive definite | min eigenvalue 21.3841428690 | PASS |
| `Q_heat,K` | Hermitian and indefinite | both signed eigenvalues at every rung | PASS |
| Hermiticity `K_E` | <= 1e-11 | 9.630e-17 | PASS |
| Hermiticity `K_heat` | <= 1e-11 | 9.365e-16 | PASS |
| symmetrization correction `K_E` | only after Hermiticity pass | <= 4.815e-17 relative | PASS |
| symmetrization correction `K_heat` | only after Hermiticity pass | <= 4.683e-16 relative | PASS |
| extremal eigenresidual | <= 1e-10 | 4.829e-16 | PASS |
| eigenvector normalization | <= 1e-12 | 3.331e-16 | PASS |
| Rayleigh reproduction | <= 1e-11 | 5.762e-16 | PASS |
| PSD `K_E` | min eig >= roundoff bound | min = 0.088147395 | PASS |
| augmented exponential vs Lyapunov tail | numerical agreement | max relative defect 5.688e-14 | PASS |
| direct terminal-energy check | <= 1e-8 | max relative defect 3.981e-16 | PASS |
| direct adaptive heat-integral check | <= 1e-8 | max relative defect 4.339e-16 | PASS |

The cumulative heat integral was computed by the frozen augmented `5 x 5` exponential for
each modal block. The independent stable Lyapunov-tail identity agreed to at worst
`5.688e-14` relative error. The direct Gauss-Kronrod checks used the preregistered
`rtol=1e-10`, `atol=1e-12`; the largest reported quadrature error estimate was
`1.743e-14`.

No matrix was symmetrized before its raw Hermiticity gate passed.

## 4. Primary finite-time results

Because the global matrices are block diagonal and the `+m/-m` partners are exact conjugate
representations of real fields, every leading optimum has an exact two-dimensional
representation eigenspace. The table therefore reports the conservative optimal-subspace
angle and conservative heat gap from the preregistered degeneracy rule.

| T/tau_ref | T [d] | G_E | J_heat+ | J_heat- | Energy mode (|m|,n) | Heat+ mode (|m|,n) | conservative angle | Delta_heat | J_heat at Energy optimum |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.25 | 0.180844907 | 1.056693010 | 0.093877922 | -0.085732393 | (3,1) | (3,1) | 0.018377 | 0.000000197 | 0.093877903 |
| 0.5 | 0.361689815 | 1.115448646 | 0.191889112 | -0.160370231 | (3,1) | (3,1) | 0.073193 | 0.000002996 | 0.191888537 |
| 1 | 0.723379630 | 1.234203809 | 0.395318490 | -0.279425702 | (3,1) | (3,1) | 0.288329 | 0.000043223 | 0.395301403 |
| 2 | 1.446759259 | 1.443047554 | 0.793908822 | -0.423870675 | (4,1) | (4,1) | 0.783966 | 0.000287157 | 0.793680845 |
| 4 | 2.893518518 | 1.698258614 | 1.491899013 | -0.528819904 | (4,1) | (4,1) | 2.772021 | 0.003167930 | 1.487172782 |
| 8 | 5.787037037 | 1.120673800 | 1.544489948 | -0.459892829 | (3,2) | (4,2) | 90.000000 | 0.041184553 | 1.480880819 |

The positive heat denominator is safely nonzero at every horizon under the frozen rule.

The stable system exhibits finite-time perturbation-energy gain above unity throughout the
frozen ladder. The signed heat operator simultaneously has both positive and negative
extrema; the negative/equatorward branch is reported above and is never replaced by an
absolute-value objective.

## 5. Objective dependence

For `T/tau_ref = 0.25, 0.5, 1`, both objectives select the exact modal pair
`(|m|,n)=(3,1)`. At `T/tau_ref = 2,4`, both select `(4,1)`. Their internal
barotropic/baroclinic directions differ only weakly over these five horizons:

- angle grows from `0.0184 deg` at `0.25` to `2.7720 deg` at `4`;
- the conservative heat-performance gap grows only to `0.003168` at `4`.

At the longest frozen horizon,

\[
T/\tau_{{\rm ref}}=8,
\]

the objectives select different exact modal subspaces:

\[
\boxed{{\rm Energy}: (|m|,n)=(3,2)},
\qquad
\boxed{{\rm Heat}: (|m|,n)=(4,2)}.
\]

Because distinct Fourier/Galerkin modal pairs are orthogonal, the conservative principal
angle is exactly

\[
\boxed{\vartheta_{{\rm sub}}=90^\circ}.
\]

However,

\[
J_{{\rm heat}}^+=1.544489947751075,
\qquad
J_{{\rm heat}|E}}^{{\rm best}}=1.480880819059942,
\]

so

\[
\boxed{\Delta_{{\rm heat}}=0.04118455338}.
\]

Thus the energy-optimal subspace still realizes about `95.8815%` of the maximum cumulative
poleward heat transport. The large modal-space angle therefore does **not** correspond to a
large transport-performance penalty in this frozen pilot.

## 6. Resolution robustness

All primary objective values and optimal modal supports are exactly retained under the
nested refinements `(12,12) -> (16,16) -> (24,24)`.

For every frozen horizon:

- `epsilon_G = epsilon_J+ = epsilon_|J-| = 0` to reported floating precision for both
  mandatory refinement pairs;
- captured common-space mass is `mu_c = 1.0` for both Energy and positive-Heat optimal
  subspaces;
- optimal-subspace rank remains `2`;
- the largest numerical principal angle across refinement is below
  `1.5e-6 deg`, far below the frozen `10 deg` limit.

Hence **all six horizons are resolution robust**. The `(8,8)` coarse audit and even the
qualification-only `(4,4)` rung produce the same leading modal pairs and objective values,
but neither is used to rescue or redefine the verdict.

## 7. Physical optimizer diagnostics at the primary resolution

For a real representative, the `+m/-m` conjugate partners are combined with equal norm.
Consequently the modal weights below are projector/subspace invariant: each optimum has
100% of its initial energy in the reported `(|m|,n)` pair.

`f_BT/f_BC` denotes barotropic/baroclinic initial perturbation-energy fractions.
The phase is `arg(tau/psi)` for the positive-m partner. `|layer1|/|layer2|` uses
`psi_1'=psi+tau`, `psi_2'=psi-tau`.

| T/tau_ref | Energy f_BT/f_BC | Heat f_BT/f_BC | Energy phase | Heat phase | Energy layer1/layer2 amp. | Heat layer1/layer2 amp. | Energy flux sign changes | Heat-opt flux sign changes |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.25 | 0.5003/0.4997 | 0.5003/0.4997 | 96.102° | 96.065° | 0.9120 | 0.9125 | 0 | 0 |
| 0.5 | 0.5006/0.4994 | 0.5006/0.4994 | 102.178° | 102.032° | 0.8317 | 0.8336 | 0 | 0 |
| 1 | 0.5011/0.4989 | 0.5011/0.4989 | 114.164° | 113.587° | 0.6913 | 0.6975 | 0 | 0 |
| 2 | 0.4048/0.5952 | 0.4087/0.5913 | 122.516° | 120.988° | 0.5576 | 0.5754 | 0 | 0 |
| 4 | 0.3486/0.6514 | 0.3568/0.6432 | 151.675° | 145.964° | 0.2565 | 0.3110 | 0 | 0 |
| 8 | 0.3373/0.6627 | 0.1762/0.8238 | 179.256° | 159.968° | 0.0363 | 0.2818 | 0 | 1 |

The physically clearest objective dependence occurs at `T/tau_ref=8`:

- Energy optimum: `(3,2)`, `f_BT=0.337279`, `f_BC=0.662721`,
  `arg(tau/psi)=179.256 deg`.
- Heat optimum: `(4,2)`, `f_BT=0.176190`, `f_BC=0.823810`,
  `arg(tau/psi)=159.968 deg`.

The heat-optimal initial condition is therefore more strongly baroclinic and uses a shorter
zonal scale (`|m|=4` rather than `3`). For positive `m`, the instantaneous signed modal heat
flux is proportional to `k Im(psi* tau)`, so the relative phase directly controls its sign
and magnitude.

The reconstructed layer-amplitude ratios at the longest horizon are

\[
|\psi_1'|/|\psi_2'|=0.03627
\quad\text{(Energy)},
\qquad
0.28185
\quad\text{(Heat)}.
\]

Both are layer-2 dominated in this modal representation, but the Energy optimum is much
closer to layer cancellation in `psi_1'`.

## 8. Signed heat-flux histories

For `T/tau_ref <= 4`, the instantaneous heat flux along both the Energy-optimal and
Heat-optimal direct trajectories remains positive/poleward for the entire frozen interval.

At `T/tau_ref=8`:

- Energy optimum: instantaneous flux remains positive, from `0.00324333` initially to
  `0.00363471` finally, with maximum `0.29844877`; no sign change.
- Heat optimum: instantaneous flux starts at `0.07210171`, reaches maximum `0.32952020`,
  and changes sign once at
  `t/tau_ref = 7.38606370` (`t = 5.34292802 d`), ending at `-0.03998843`.

For the Heat optimum at `T/tau_ref=8`, the positive and negative time-integrated
contributions are approximately `+1.55720334` and `-0.01271373`, respectively, giving the
net signed optimum `1.54448995`. This is consistent with the frozen cumulative signed
objective: a late equatorward interval is allowed if the preceding poleward transport
produces the largest positive net integral.

## 9. Frozen verdict

The verdict precedence is applied exactly as preregistered:

1. no numerical gate fails -> not `CLIM-NUMERICAL-FAIL`;
2. all horizons satisfy the complete resolution-robustness gate -> not
   `CLIM-RESOLUTION-FAIL`;
3. `J_heat+` is safely positive at every horizon -> not `CLIM-TRANSPORT-NULL`;
4. no neighboring horizon pair satisfies **both**
   `angle >= 20 deg` and `Delta_heat >= 0.25` -> not `CLIM-STRONG`;
5. the robust `T/tau_ref=8` horizon has a clearly resolvable objective dependence because
   `angle = 90 deg >= 5 deg` -> `CLIM-WEAK`.

Therefore

\[
\boxed{\text{Climate/Ocean Pilot 0.1 verdict: CLIM-WEAK}}.
\]

## 10. Allowed interpretation

This frozen idealized QG pilot supports the limited statement that the perturbation-energy
and cumulative signed eddy-heat objectives are **not geometrically identical** over the
entire fixed horizon ladder. At the longest frozen horizon they select different robust
zonal modal supports and different barotropic/baroclinic structure.

The result does **not** support the stronger claim that the energy-optimal perturbation
substantially fails to transport heat: its cumulative poleward heat performance at the
longest horizon is only `4.12%` below the heat optimum, and all shorter-horizon gaps are
smaller.

## 11. Forbidden interpretation

This result must not be presented as:

- a universal climate or ocean theorem;
- evidence that singular-vector or optimal-perturbation methods are new;
- a strong Climate-domain replication of the Plasma/Pilot-0.2 performance gap;
- a statement about blocking, AMOC, Primitive-Equation dynamics, or realistic forecast skill;
- justification for retuning `U`, `r`, `L_D`, beta, the domain, horizons or resolutions.

The correct frozen outcome is the preregistered weak result.

## 12. Reproducibility outputs

Machine-readable results:

`research/climate/climate_ocean_pilot_0_1_execution_data.csv`

Frozen numerical regression tests:

`tests/test_climate_ocean_pilot_0_1.py`

The committed test suite for this pilot contains structural/stability, augmented-integral
versus Lyapunov-tail, resolution-support and direct-quadrature/verdict checks. A local
execution before commit returned:

`4 passed`.

No scientific setting was changed to obtain that test result.

**STOP.**