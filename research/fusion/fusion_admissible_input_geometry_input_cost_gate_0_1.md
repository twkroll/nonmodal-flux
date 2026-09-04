# Fusion F1.2 — Admissible Input Geometry / Input-Cost Gate 0.1

**Date:** 2026-09-04  
**Authority:** MASTER / `research/master/prompts/fusion_admissible_input_geometry_input_cost_gate_0_1.md`  
**Status:** `F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE`

## Scope

This gate determines only the physically admissible initial-condition geometry and the input-cost metric for the already-frozen anisotropic-ZLR four-moment R1 Fusion state/channel.

It does **not** compute any finite-time energy or heat-transport operator, optimizer, principal angle, performance gap, horizon dependence, cumulative transport extremum, parameter scan, stability rescue, FLR/R2 extension, kinetic-electron extension, six-moment GEM model, GENE model, or new channel. It does not alter the frozen free-energy metric `M_k` or ion heat-flux operator `Q_{q_i,k}`.

The gate explicitly distinguishes:

1. **state-space initial-condition admissibility** — which perturbation states of the already-closed tangent model are allowed at `t=0`; and
2. **actuator/preparation realizability** — which subset could be produced by a specified experimental forcing or preparation apparatus.

The present FUSION-F1 question is an initial-condition problem. No experimental actuator or forcing operator is part of the frozen R1 model or the MASTER handoff. Therefore the admissibility decision below is a statement about the closed tangent-state ensemble, not a claim of arbitrary four-channel laboratory actuation.

---

## 1. Frozen state and constraint geometry

The common slab/minimal-curvature R1 state ordering is

\[
\boxed{
z_k=(N,U,P_\parallel,P_\perp)^T
}
\]

with

\[
N=\frac{\widetilde n_i}{n_0},\qquad
U=\frac{\widetilde u_\parallel}{c_s},\qquad
P_\parallel=\frac{\widetilde p_\parallel}{p_0},\qquad
P_\perp=\frac{\widetilde p_\perp}{p_0},
\]

\[
c_s^2=\frac{T_{i0}}{m_i},\qquad p_0=n_0T_{i0}.
\]

All four state components are dimensionless. Their physical meanings are, respectively, normalized ion density perturbation, normalized parallel-flow perturbation, normalized parallel-pressure perturbation, and normalized perpendicular-pressure perturbation.

The corresponding temperature perturbations are

\[
\Theta_\parallel=P_\parallel-N,
\qquad
\Theta_\perp=P_\perp-N.
\]

The electrostatic potential is not an independent dynamical coordinate. In the frozen nonzonal adiabatic-electron sector,

\[
\Phi\equiv\frac{e\widetilde\phi}{T_{i0}}
=\mathcal C_kN,
\qquad
\mathcal C_k=\frac{1}{\tau_i+b_P}>0,
\qquad
b_P=k_\perp^2\rho_i^2,
\qquad
k_y\neq0.
\]

Thus the polarization/electron closure reconstructs `Phi` uniquely from `N`. After this elimination, both the slab and minimal-curvature systems are ordinary four-component linear initial-value problems. There is no remaining algebraic relation among `N`, `U`, `P_parallel`, and `P_perp`.

For a real physical field the Fourier amplitudes obey the usual conjugacy relation

\[
z_{-k}=z_k^*.
\]

This relates the `-k` amplitude to the chosen `+k` amplitude; it does not impose an additional linear constraint inside the complex four-dimensional single-`k` state.

### Tangent-state interpretation

The R1 model is a linear tangent model about a positive equilibrium. Density and pressure positivity are therefore not additional *linear* constraints on a perturbation direction: any finite direction in the retained four-moment tangent space can be assigned a sufficiently small amplitude. F1.2 does not make a finite-amplitude nonlinear realizability claim.

Hence the frozen closure supplies no physical or algebraic reason to remove any of the four retained tangent-state directions from the initial-condition ensemble.

---

## 2. Candidate admissible spaces considered

### Candidate A — full closed R1 tangent state

Allow arbitrary initial perturbations in the already-closed four-moment state, with the electrostatic field reconstructed from `Phi=C_k N`:

\[
\mathcal U_{\rm full}=\mathbb C^4.
\]

This candidate introduces no extra preparation physics and respects exactly the state produced by the R1 reduction.

**Assessment:** physically and structurally justified for an initial-condition optimization problem.

### Candidate B — zero-initial-parallel-flow subspace

One could impose `U(0)=0`, leaving a three-dimensional thermodynamic subspace. Such an ensemble may describe a particular preparation protocol, but neither the R1 closure nor the Fusion question requires zero initial parallel flow. Parallel flow is a retained physical moment and participates in the closed dynamics.

**Assessment:** physically possible as a *special preparation*, but not an intrinsic admissibility restriction. Not selected.

### Candidate C — density/electrostatic-only preparation

One could admit only the density coordinate, with `Phi` following from the closure. This would be rank one.

**Assessment:** this is an actuator-specific restriction not implied by the model. It would also eliminate any nontrivial comparison of distinct initial directions. Not selected.

### Candidate D — thermal-only, fixed-anisotropy, or other moment-locked subspaces

Relations such as `N=0`, `P_parallel=P_perp`, fixed temperature anisotropy, or similar lower-rank moment relations can describe particular preparation ensembles, but none follows from the frozen closure or the stated FUSION-F1 initial-condition question.

**Assessment:** not selected absent an independently specified physical preparation mechanism.

### Candidate E — transport-neutral subspace

A subspace chosen so that

\[
B^\dagger Q_{q_i,k}B=0
\]

would be mathematically constructible.

**Assessment:** rejected as an admissibility principle. The MASTER handoff explicitly forbids imposing transport neutrality merely for mathematical convenience, and the frozen R1 physics supplies no independent preparation argument requiring it.

### Selection

There is therefore one uniquely justified state-space choice for the current question:

\[
\boxed{
\mathcal U_{\rm adm}=\mathbb C^4.
}
\]

Narrower spaces remain possible only after adding a new actuator/preparation hypothesis. They are not competing admissible geometries for the present F1.2 state-space problem.

---

## 3. Selected input map `B`

Use input coordinates

\[
a=(a_N,a_U,a_{P_\parallel},a_{P_\perp})^T
\]

directly in the frozen state ordering. Then

\[
z_k(0)=Ba,
\qquad
\boxed{
B=I_4=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
}
\]

The columns are the coordinate basis of the retained density, parallel-flow, parallel-pressure, and perpendicular-pressure tangent moments. They are a parametrization of admissible *states*, not four asserted laboratory actuators.

Therefore

\[
\boxed{\operatorname{rank}(B)=4.}
\]

This comfortably satisfies the rank-at-least-two requirement for a later comparison of distinct optimal initial directions.

---

## 4. Input-cost metric

The already-frozen perturbation free energy is

\[
W_k(0)=\frac{p_0}{2}z_k(0)^\dagger M_kz_k(0),
\]

with

\[
\boxed{
M_k=
\begin{pmatrix}
\frac52+\mathcal C_k&0&-\frac12&-1\\
0&1&0&0\\
-\frac12&0&\frac12&0\\
-1&0&0&1
\end{pmatrix}.
}
\]

For a general admissible map `B`, the natural fixed-free-energy input budget is

\[
R_{\rm in}=B^\dagger M_kB.
\]

With the selected full-state parametrization `B=I_4`,

\[
\boxed{R_{\rm in}=M_k.}
\]

The corresponding dimensionless quadratic cost is

\[
a^\dagger R_{\rm in}a
=(1+\mathcal C_k)|N|^2+|U|^2
+\frac12|P_\parallel-N|^2
+|P_\perp-N|^2.
\]

Because `C_k>0`, this vanishes only for the zero state. Hence

\[
\boxed{
R_{\rm in}=R_{\rm in}^\dagger\succ0.
}
\]

The dimensional physical budget is `(p_0/2) a^dagger R_in a`. Keeping the common positive prefactor outside `R_in` preserves the already-frozen project convention and changes no physical admissible direction.

This cost is selected because the input budget is perturbation free energy. It is not chosen from any later finite-time heat-transport effect.

---

## 5. Instantaneous restricted heat-channel geometry

The frozen physical ion heat-flux matrix is

\[
Q_{q_i,k}
=p_0\mathcal V_k\mathcal C_k
\begin{pmatrix}
0&0&i/4&i/2\\
0&0&0&0\\
-i/4&0&0&0\\
-i/2&0&0&0
\end{pmatrix},
\qquad
\mathcal V_k=\frac{ck_yT_{i0}}{eB_0}.
\]

Since `B=I_4`, the instantaneous restriction is simply

\[
\boxed{
B^\dagger Q_{q_i,k}B=Q_{q_i,k}.
}
\]

For the admitted nonzonal sector `k_y!=0`, this form is

\[
\boxed{
\operatorname{rank}(B^\dagger Q_{q_i,k}B)=2,
\qquad
\operatorname{signature}(B^\dagger Q_{q_i,k}B)=(1,1,2).
}
\]

It is therefore **indefinite and non-neutral** on the admissible state space. The two-dimensional nullspace includes the parallel-flow direction and the pressure combination with `N=0` and

\[
\frac12P_\parallel+P_\perp=0.
\]

No input geometry was changed to obtain this classification. In particular, F1.2 does not force

\[
B^\dagger Q_{q_i,k}B=0.
\]

Because the selected restriction is already nonzero, no transport-neutral generation-order question is triggered by this gate.

---

## 6. Coordinate/basis consistency

Let `S` be any invertible change of coordinates within the same admissible input space and define

\[
B'=BS.
\]

Writing the same physical initial state as

\[
z_k(0)=Ba=B'a',
\qquad a=Sa',
\]

requires the transformed cost

\[
\boxed{
R_{\rm in}'=S^\dagger R_{\rm in}S
=(B')^\dagger M_kB'.
}
\]

Then

\[
(a')^\dagger R_{\rm in}'a'=a^\dagger R_{\rm in}a,
\]

so the physical free-energy budget is basis independent. The restricted instantaneous channel transforms covariantly,

\[
\boxed{
(B')^\dagger Q_{q_i,k}B'
=S^\dagger(B^\dagger Q_{q_i,k}B)S.
}
\]

Thus Hermiticity, positive definiteness of the input cost, rank of the admissible space, and the inertia of the restricted Hermitian channel are unchanged by an invertible basis change.

A useful explicit example is the thermodynamic-coordinate basis

\[
y=(N,U,\Theta_\parallel,\Theta_\perp)^T,
\qquad
z=Ty,
\]

with

\[
T=
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
1&0&1&0\\
1&0&0&1
\end{pmatrix}.
\]

Using `B'=T` spans exactly the same physical four-dimensional state space. In this basis,

\[
T^\dagger M_kT
=\operatorname{diag}\!\left(1+\mathcal C_k,1,\frac12,1\right)\succ0,
\]

while the physical heat-flux form is the same density/thermal cross-phase written in temperature coordinates. The pressure-coordinate cross terms in `M_k` therefore do not signal a different input geometry.

By contrast, a noninvertible map that removes directions changes `range(B)` itself. That is a physical restriction, not a coordinate change, and requires an independent preparation argument.

---

## 7. Slab versus minimal-curvature applicability

The same admissible-input interpretation applies to both already-derived R1 generators:

\[
\boxed{
B^{\rm slab}=B^{\rm curv}=I_4,
\qquad
R_{\rm in}^{\rm slab}=R_{\rm in}^{\rm curv}=M_k.
}
\]

Reason:

- both generators use the same four retained state moments in the same normalization;
- both use the same algebraic electrostatic closure `Phi=C_k N`;
- B5.4 established the same positive free-energy metric `M_k` for slab and curvature;
- B5.5 established the same instantaneous physical heat-flux operator `Q_{q_i,k}` for both branches.

Curvature changes `A_k`, but not the state admissibility, input free-energy budget, or instantaneous channel definition. F1.2 therefore supplies no pre-effect reason to choose different `B,R_in` pairs between slab and minimal curvature.

---

## 8. PASS / HOLD / FAIL assessment

The required PASS conditions are satisfied:

- one physically justified state-space admissible perturbation space is selected: the full closed R1 tangent state;
- `B=I_4` is explicit in the frozen ordering `(N,U,P_parallel,P_perp)`;
- `R_in=M_k` is explicit, Hermitian, and strictly positive definite;
- `rank(B)=4>=2`;
- the eliminated electrostatic field constraint is exactly respected through `Phi=C_k N`;
- there is no additional linear closure constraint on the four retained state coordinates;
- no choice used optimizer separation, finite-time performance, horizons, parameter scans, or effect size;
- the same interpretation applies to slab and minimal-curvature R1;
- the instantaneous restricted channel was diagnosed only after selecting the physical state space and remains rank-2 indefinite rather than being forced neutral.

Therefore

\[
\boxed{
\text{F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE}
}
\]

---

## 9. Allowed interpretations

The F1.2 result supports the following statements:

- `B=I_4` means that the later R1 initial-condition problem may range over all perturbation directions of the already-closed four-moment tangent state.
- `R_in=M_k` means that admissible input amplitude is measured by the already-derived perturbation free energy.
- The full admissible space is not instantaneously heat-transport neutral; signed positive and negative instantaneous heat-flux directions exist structurally.
- The same pre-effect input geometry/cost applies to slab and minimal-curvature R1.
- Any invertible reparametrization of the same four-dimensional state space is physically equivalent if `R_in` and the restricted channel are transformed covariantly.

## 10. Forbidden interpretations

The F1.2 result does **not** establish that:

- an experiment can independently actuate all four moments;
- a particular antenna, heating source, fueling source, flow drive, or boundary actuator realizes `B=I_4`;
- arbitrary finite-amplitude moment states are nonlinearly realizable;
- the full-state choice is preferable because it produces a larger finite-time heat-transport/free-energy separation;
- transport neutrality should be imposed before a later finite-time calculation;
- the same `B,R_in` automatically survives FLR/R2, kinetic-electron, six-moment, or gyrokinetic fidelity upgrades.

Those would require separate physical gates.

---

## 11. Exact open issues after F1.2

No scientifically consequential ambiguity remains **within the present R1 state-space initial-condition question**.

The following issues are explicitly deferred rather than solved here:

1. MASTER must decide and freeze the next Fusion candidate/convention package; F1.2 does not self-authorize F1.3.
2. If the scientific question is later changed from arbitrary initial conditions to a specified experimental preparation/forcing mechanism, a new actuator-specific `B` and corresponding cost must be derived; `B=I_4` must not be cited as an actuator claim.
3. Any later fidelity upgrade that changes the state, closure, or physical free-energy functional requires rechecking admissibility and input cost.
4. Finite-amplitude nonlinear realizability is outside the tangent-state scope.

None of these issues requires a HOLD for the current F1.2 gate.

---

## Final verdict and STOP

\[
\boxed{
\text{F1.2 PASS — RETURN TO MASTER FOR FUSION CANDIDATE/CONVENTION FREEZE}
}
\]

Canonical selection:

\[
\boxed{
B=I_4,
\qquad
R_{\rm in}=M_k,
\qquad
\operatorname{rank}(B)=4,
\qquad
B^\dagger Q_{q_i,k}B=Q_{q_i,k}\ \text{indefinite of rank 2}.
}
\]

**STOP — F1.2 COMPLETE; RETURN TO MASTER. NO FINITE-TIME EFFECT INSPECTION AND NO BRANCH-SIDE NEXT GATE.**