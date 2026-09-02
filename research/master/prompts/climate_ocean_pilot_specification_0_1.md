# Climate/Ocean Pilot Specification 0.1 — MASTER Handoff

Execute this instruction in the Climate/Ocean branch. This is a **specification/freeze-preparation task only**.

## Scope

No CORE optimization, no parameter search and no calculation or inspection of

\[
K_E(T),\quad K_{\rm heat}(T),\quad w_E^\star,\quad w_{\rm heat}^\star,\quad \vartheta(T),\quad \Delta_{\rm heat}(T).
\]

Use only the already frozen and numerically qualified two-layer Phillips-QG candidate.

## Frozen physical/numerical inputs

Retain without retuning:

\[
L_x=3.0\times10^7\,\mathrm m,
\quad
L_y=1.0\times10^7\,\mathrm m,
\quad
L_D=10^6\,\mathrm m,
\]

\[
\beta=1.6\times10^{-11}\,\mathrm{m^{-1}s^{-1}},
\quad
U=8\,\mathrm{m\,s^{-1}},
\quad
r=(10\,\mathrm d)^{-1},
\]

and the qualified structure

\[
(A_K,M_K,Q_{{\rm heat},K},B=I,R_{\rm in}=M_K).
\]

Keep the signed convention `positive = northward/poleward heat transport` and the cumulative observable

\[
J_{\rm heat}(T)=\int_0^T x^\dagger Q_{{\rm heat},K}x\,dt.
\]

## Required pilot specification

Freeze before any effect calculation:

1. primary resolution and confirmation/audit resolutions selected only from the already qualified ladder
   \[
   (M_x,N_y)=(4,4),(8,8),(12,12),(16,16),(24,24);
   \]
2. exact state ordering and matrix assembly convention already defined in Numerical Qualification 0.1;
3. the existing time normalization
   \[
   \tau_{\rm ref}=L_D/(\beta L_D^2)=0.7233796296\,\mathrm d;
   \]
4. the inherited fixed horizon ladder
   \[
   T/\tau_{\rm ref}\in\{0.25,0.5,1,2,4,8\};
   \]
5. exact finite-time numerical method for the matrix exponential and cumulative Gramian/integral;
6. Hermiticity, eigenresidual, Rayleigh-quotient and direct trajectory/integration checks;
7. resolution-robustness diagnostics for both objective values and optimizers, with cross-resolution optimizer comparison performed only after projection to a common retained modal subspace or via a physically meaningful modal-weight comparison;
8. a rule for degeneracies using optimal subspaces/projectors rather than arbitrary eigenvectors;
9. the later physical optimizer diagnostics: barotropic/baroclinic energy fractions, zonal/meridional modal weights, layer structure and relative phase information as appropriate;
10. complete verdict classes fixed before execution, including explicit weak/null and numerical-failure outcomes.

## Shared cross-domain reporting protocol to preregister

For Climate, because `B=I` and `R_in=M_K`, the positive objective is the finite-time perturbation-energy gain

\[
K_E(T)=M_K^{-1/2}e^{A_K^\dagger T}M_Ke^{A_KT}M_K^{-1/2},
\]

\[
G_E(T)=\lambda_{\max}(K_E(T)).
\]

The signed cumulative heat-transport operator is

\[
K_{\rm heat}(T)=M_K^{-1/2}
\left[\int_0^T e^{A_K^\dagger t}Q_{{\rm heat},K}e^{A_Kt}\,dt\right]
M_K^{-1/2}.
\]

Report

\[
J_{\rm heat}^{+}(T)=\lambda_{\max}(K_{\rm heat}(T)),
\qquad
J_{\rm heat}^{-}(T)=\lambda_{\min}(K_{\rm heat}(T)).
\]

The positive/poleward branch is primary.

Define the same-K optimizer angle

\[
\vartheta(T)=\arccos\left|{w_E^\star}^\dagger w_{\rm heat}^\star\right|,
\]

and the common dimensionless gap

\[
\Delta_{\rm heat}(T)=
\frac{J_{\rm heat}^{+}(T)-{w_E^\star}^\dagger K_{\rm heat}(T)w_E^\star}
{J_{\rm heat}^{+}(T)},
\]

only when the positive denominator is safely nonzero.

Preregister the inherited operational demonstration thresholds

\[
\vartheta(T)\ge20^\circ,
\qquad
\Delta_{\rm heat}(T)\ge0.25
\]

for at least two neighboring fixed horizons. State explicitly that these are project-level operational thresholds, not universal climate-physics thresholds.

## Anti-bias rules

- Do not change physical parameters, damping, basis, transport sign convention or `B` after seeing a CORE effect.
- Do not add a new resolution rung because an effect appears/disappears.
- Do not redefine heat transport as a positive norm.
- Do not select horizons after inspecting optimizer separation.
- If the later optimizer fails resolution robustness, retain that as the result; do not retune the model.

## Output

Create and commit

`research/climate/climate_ocean_pilot_specification_0_1.md`

and update

`research/climate/STATUS.md`.

The status file must contain a `Next instruction` field. If the specification is complete, set it to `RETURN TO MASTER FOR PILOT FREEZE`; do not self-authorize execution.

Report exact repository paths, commit hash and CI/test status if relevant.

**STOP after specification.**
