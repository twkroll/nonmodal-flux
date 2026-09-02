# D10-ZF Pilot Interpretation 0.1

**Date:** 2026-09-02  
**Status:** interpretation only; no retuning, no new theory, no new branch

## Scope

This note interprets only the already executed frozen `D10-ZF Pilot 0.1` using the preregistered model point and horizons. It does not modify `A`, `M`, `Q_Gamma`, `B`, `R_in`, the zonal-flow profile, truncation, damping, or time horizons. It does not open a new plasma branch or a new CORE theorem branch.

The source result is `research/d10_zf_pilot_execution_0_1_results.md`.

## 1. Primary preregistered verdict

The pilot fails its intended stable/subcritical benchmark role because

```math
\alpha(A)=0.0803635112>0.
```

Three eigenvalues have positive real part. Therefore the observed finite-time energy growth and transport behavior cannot be interpreted as a clean demonstration occurring inside an asymptotically stable linear system.

The correct primary classification is

```text
PILOT 0.1 PRIMARY VERDICT = FAILURE
```

This failure is specific to the frozen Pilot-0.1 parameter point. It is not, by itself, a failure of the D10-ZF derivation, the structure-preserving Galerkin model, or the branch-independent CORE mathematics.

## 2. What the pilot nevertheless establishes at the frozen point

The following numerical facts remain valid observations of the executed operator:

1. The cumulative particle-flux operator is genuinely signed at every preregistered horizon,

```math
\mathcal G_{\Gamma,-}(T)<0<\mathcal G_{\Gamma,+}(T),
```

for `T in {0.25,0.5,1,2,4,8}`.

2. The terminal free-energy optimizer and positive cumulative-transport optimizer are distinct at every preregistered horizon,

```math
\vartheta(T)>0,
```

with angles approximately

```text
46.22, 41.55, 33.83, 26.05, 23.12, 58.48 degrees.
```

3. The transport-optimal disturbance outperforms the energy-optimal disturbance with respect to cumulative particle transport at every preregistered horizon,

```math
\Delta_\Gamma(T)
=J_\Gamma(T;u_\Gamma^\star)-J_\Gamma(T;u_E^\star)>0.
```

4. The direct trajectory integrations agree with the Gramian/Rayleigh calculations to the documented numerical tolerances.

Thus the coupled D10-ZF operator does exhibit a nontrivial separation between the two optimization objectives. The earlier uncoupled direct-sum explanation is no longer available here because the radial sidebands are physically coupled by the prescribed zonal flow.

## 3. What must not be claimed from Pilot 0.1

The following stronger interpretations are not supported by this pilot:

### 3.1 No stable-nonmodal headline claim

Because `alpha(A)>0`, Pilot 0.1 does not establish that transport-optimal behavior persists in a spectrally stable coupled D10-ZF system. Any statement of the form

```text
strong directed transport despite asymptotic linear stability
```

would be unsupported by this execution.

### 3.2 No attribution of energy growth purely to nonnormal transient amplification

The terminal free-energy gains satisfy `G_E,max(T)>1` on all preregistered horizons, but modal instability is present. Hence the observed energy growth cannot be cleanly separated from exponentially growing eigenmodes at this parameter point.

### 3.3 No transport-generation-from-neutrality claim

Pilot 0.1 uses

```math
B=I_6,
```

and therefore

```math
B^\dagger Q_\Gamma B=Q_\Gamma\neq0.
```

The pilot does not test the transport-neutral initialization mechanism of T1/T4. Positive cumulative transport may include transport already present in the chosen initial condition.

### 3.4 No convergence claim

The pilot uses the minimal `m=(-1,0,1)` Galerkin truncation. No radial-resolution or sideband-convergence study was part of Pilot Execution 0.1. Therefore one cannot yet decide from this run alone whether the unstable eigenvalues and the quantitative optimizer data are converged properties of the continuous D10-ZF problem or are materially influenced by the minimal truncation.

### 3.5 No causal claim about the mean-flow channel

The D10-ZF balance contains both `Q_Gamma` and the separate mean-flow exchange channel `Q_U`. Pilot Execution 0.1 optimized only `Q_Gamma`. The present numbers do not by themselves identify how much of the observed free-energy growth is supplied by the density-gradient channel versus mean-flow exchange along each optimizer trajectory.

## 4. Interpretation of the positive secondary diagnostics

The secondary diagnostics are scientifically informative but should be classified below the primary gate.

The robust qualitative statement supported by the frozen calculation is:

> In the physically coupled six-state D10-ZF Galerkin operator, maximizing terminal perturbation free energy and maximizing cumulative radial particle transport are different finite-horizon optimization problems and select different initial disturbances over all preregistered horizons.

This statement survives the pilot failure because it is a direct property of the frozen operator and does not require spectral stability.

However, its value for the intended nonmodal-stability narrative is limited until the same separation is demonstrated in an admissible stable/subcritical coupled case.

## 5. Meaning of the instability

The instability should be interpreted conservatively.

At least three possibilities remain logically open:

1. the chosen prescribed zonal-flow amplitude/profile together with `C=kappa=1` is genuinely linearly unstable in the underlying D10-ZF model;
2. the minimal three-radial-mode truncation shifts or creates unstable eigenvalues that would change under resolution refinement;
3. both effects contribute.

Pilot 0.1 did not contain the calculations needed to distinguish these possibilities. Therefore the failure must not be diagnosed post hoc as either a physical instability or a truncation artifact.

## 6. Consequence for D10-ZF and CORE

### D10-ZF

D10-ZF remains structurally alive. The pilot does not invalidate:

```math
A_U^\dagger M+MA_U
=2\kappa Q_\Gamma+2Q_U-D_C,
```

nor the physically derived sideband coupling, metric, or particle-flux form. It only shows that the first preregistered numerical point is unsuitable for the intended stable/subcritical benchmark.

### CORE

The branch-independent CORE statements are not falsified. In particular, the execution does not contradict the mathematical distinction between positive `M` and signed `Q`, finite-horizon signed transport optimization, or energy-versus-transport optimizer separation.

It also does not validate the strongest T1/T4 transport-neutral mechanism because `B=I_6` is not transport-neutral.

## 7. Preregistered-criteria reading

The pilot should therefore be recorded in three layers:

```text
PRIMARY BENCHMARK GATE:       FAIL
Reason: alpha(A) > 0.

SECONDARY OBJECTIVE SEPARATION: OBSERVED
Reason: theta(T) > 0 and Delta_Gamma(T) > 0 at all six horizons.

STABLE-NONMODAL CORE DEMONSTRATION: NOT ESTABLISHED
Reason: modal instability contaminates the intended benchmark interpretation.
```

This is not a mixed or ambiguous primary outcome: the preregistered benchmark fails. The positive secondary diagnostics are retained as observations, not used to rescue the failed gate.

## 8. What follows — and what does not follow

Pilot Interpretation 0.1 does not authorize retuning of Pilot 0.1. The frozen run remains a failed preregistered pilot.

If MASTER later authorizes a successor pilot, it must be preregistered separately. The minimum unresolved prerequisites before interpreting a successor as a stable coupled benchmark are:

- establish whether spectral stability is robust to radial-resolution refinement;
- choose any new parameter point without optimizing for a large CORE effect;
- preserve the physically derived `M` and `Q_Gamma` and document any change in `B` independently;
- repeat the same fixed-horizon diagnostics without post-hoc retuning.

Those steps are outside this interpretation note.

## 9. Final interpretation

The frozen D10-ZF Pilot 0.1 is a **failed stable/subcritical benchmark but an informative coupled-objective witness**.

The most important positive observation is not the magnitude of the transport gain, but the persistence of energy-versus-particle-transport optimizer separation after replacing the earlier uncoupled modal direct sum by a physically coupled zonal-flow operator.

The most important negative observation is decisive: the selected point is already modally unstable, so it cannot support the intended claim that the separation is a genuinely finite-time/nonmodal phenomenon within a stable coupled system.

No retuning is performed here.
