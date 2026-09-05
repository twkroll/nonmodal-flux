# Fusion F2.4 — Kinetic Admissible Input Geometry / Input-Cost Freeze 0.1

**Date:** 2026-09-05  
**Authority:** MASTER / `research/master/prompts/fusion_f2_4_kinetic_input_geometry_input_cost_freeze_0_1.md`  
**Status:** `F2.4 PASS — KINETIC INPUT GEOMETRY / INPUT COST FROZEN — RETURN TO MASTER`

## Scope

This gate freezes only the **continuous physically admissible initial-condition geometry and initial perturbation cost** for the already-frozen reduced F2-R model

\[
\boxed{
\text{finite-ion-FLR electrostatic local-GK ions}
+\text{collisionless bounce-averaged trapped electrons}
}
\]

at the already-frozen F2.3 single CBC-compatible physical point.

No phase-space discretization, ballooning cutoff, quadrature, discrete quasineutrality operator, discrete `A/M/Q`, spectrum, propagator, Gramian, cumulative objective, optimizer, angle, performance gap or GENE calculation is performed.

The decision is made from initial-value-problem admissibility and the physical Helmholtz free-energy geometry only.

---

## 1. Frozen decision

The full finite-free-energy tangent space of the **already reduced** F2-R model is physically admissible. No additional finite-codimension moment constraint, transport-neutral restriction, parity restriction or effect-motivated subspace is required.

The continuous input pair is therefore frozen as

\[
\boxed{
B=I_{\mathcal H_{F2}},
\qquad
R_{\rm in}=\mathcal M_{F2}.
}
\]

Here `I_HF2` is the identity on the precisely defined reduced kinetic energy space below; it is **not** an identity on an unconstrained larger fully kinetic electron space.

With the F2.1 convention

\[
W[x]=\frac12\langle x,\mathcal M_{F2}x\rangle,
\]

the input quadratic cost is

\[
\boxed{
\langle u,R_{\rm in}u\rangle
=
\langle u,\mathcal M_{F2}u\rangle
=2W[u].
}
\]

Thus fixing the input budget fixes initial Helmholtz free energy, up to the conventional factor of two.

---

## 2. Admissible continuous kinetic Hilbert space

The reduced dynamic state is

\[
x=(g_i,g_e^{\rm tr}),
\]

with

\[
g_i=g_i(\theta,E_i,\mu_i,\sigma),
\qquad
\sigma=\operatorname{sgn}v_\parallel,
\]

and

\[
g_e^{\rm tr}=g_e^{\rm tr}(E_e,\lambda,w).
\]

The electrostatic potential is reconstructed from quasineutrality and is not an independent state coordinate.

Define the physical pre-Hilbert set `D0` as the smooth reduced F2-R perturbations satisfying the already-frozen model/geometry conditions:

1. the single fixed nonzonal Fourier/ballooning sector `k_alpha != 0`;
2. finite ion-FLR gyrokinetic ion phase space on the F2.2 ballooning line;
3. finite weighted ion entropy/free-energy integral;
4. electron nonadiabatic support only on the trapped region fixed by the F2.2/F2.3 magnetic geometry;
5. `g_e^pass = 0` at leading order, as part of the reduced bounce-averaged-electron model itself;
6. bounce-orbit constancy of `g_e^tr`, represented by the invariants `(E_e,lambda,w)` rather than an independent parallel coordinate;
7. ordinary physical single-valuedness/orbit regularity for the ion distribution, including consistent treatment where `v_parallel` changes sign at turning points;
8. the F2.2 ballooning/Fourier conventions and no parity reduction;
9. reconstructed `phi=P_QN x` with finite free-energy contribution.

The admissible Hilbert space is the completion of this physical set in the positive Helmholtz norm,

\[
\boxed{
\mathcal H_{F2}
=\overline{\mathcal D_0}^{\|\cdot\|_{F2}},
\qquad
\|x\|_{F2}^2
\equiv
\langle x,\mathcal M_{F2}x\rangle
=2W[x].
}
\]

Equivalently, `H_F2` is the finite-free-energy reduced kinetic tangent space after quasineutrality elimination.

For classical solutions, the linear gyrokinetic generator will have a smaller operator domain `D(A_F2) subset H_F2` containing the required parallel derivatives and orbit regularity. That generator-domain distinction is **not** an additional input subspace: finite-energy initial data belong to the physical state Hilbert space and may be interpreted through the usual mild-solution closure, while later numerical qualification must approximate the generator domain consistently.

---

## 3. Quasineutrality reconstructs the field; it does not project the kinetic state

F2.1 froze the `g`-variable quasineutrality relation

\[
\sum_{a=i,e}\frac{e_a^2 n}{T_a}\phi(\theta)
=
\sum_{a=i,e}e_a\int g_a J_{0a}\,d^3v.
\]

For the reduced model,

\[
J_{0e}=1,
\qquad
 g_e=g_e^{\rm tr}\ \text{on the trapped domain},
\qquad
 g_e^{\rm pass}=0.
\]

Therefore, pointwise along the field line,

\[
\boxed{
C_{\rm QN}\,\phi(\theta)
=
e\int g_iJ_{0i}\,d^3v
-e\int_{\rm tr(\theta)}g_e^{\rm tr}\,d^3v,
}
\]

where

\[
C_{\rm QN}
=e^2n\left(\frac1{T_i}+\frac1{T_e}\right)>0.
\]

Hence

\[
\boxed{
\phi=P_{\rm QN}(g_i,g_e^{\rm tr})
}
\]

is uniquely reconstructed for every finite-free-energy kinetic state for which the physical velocity moments exist.

There is no solvability condition of the form

\[
L(g_i,g_e^{\rm tr})=0
\]

that must be imposed before `phi` can be obtained. Quasineutrality is therefore a **closure map**, not a proper-subspace condition on the reduced kinetic state.

This distinction is essential for the later discretization: introducing `phi` as an independent input coordinate would enlarge the physical state incorrectly, while enforcing an artificial moment-nullspace condition would shrink it incorrectly.

---

## 4. Positivity and absence of gauge/null directions

F2.1 froze the positive gyrokinetic Helmholtz form

\[
2W
=
\sum_a\left\langle
T_a\int\frac{|\delta F_a|^2}{F_{a0}}\,d^3v
+
\frac{ne_a^2}{T_a}\left[1-\Gamma_{0a}(b_a)\right]|\phi|^2
\right\rangle,
\]

restricted to the reduced state, with finite ion polarization retained and electron polarization negligible in the `k_perp rho_e << 1` ordering.

On the frozen nonzonal finite-ion-FLR sector,

\[
\boxed{
W[x]>0\quad\text{for every nonzero }x\in\mathcal H_{F2}.
}
\]

Thus

\[
\boxed{\mathcal M_{F2}\succ0}
\]

on `H_F2` and no numerical regularization is needed to define the input cost.

There is also no surviving electrostatic gauge direction:

- `phi` is not an independent coordinate;
- the fixed block has `k_alpha != 0`, so a spatially constant electrostatic gauge mode is outside the represented sector;
- if `x=0`, quasineutrality gives `phi=0` in this block.

Hence neither `B` nor `R_in` needs a gauge-null projection.

---

## 5. Audit of possible physical linear restrictions

### 5.1 Particle number

No additional condition such as

\[
\int g_a\,d^3v=0
\]

is imposed on an individual nonzonal Fourier/ballooning block.

The represented perturbation carries the perpendicular phase factor

\[
e^{i(k_\psi\psi+k_\alpha\alpha)},
\qquad k_\alpha\neq0,
\]

so its flux-surface/binormal average vanishes. Global particle-number constraints belong to the zero-mode sector and do not require each nonzero Fourier component to have zero velocity-space density moment.

### 5.2 Charge

Charge consistency is enforced through quasineutrality, which reconstructs `phi`. It does not require an independent charge-moment null condition on `(g_i,g_e^tr)`.

### 5.3 Parallel momentum

No physical rule in the frozen local collisionless F2-R model requires the initial ion parallel-momentum moment to vanish. The reduced trapped-electron state is bounce averaged and carries no independently resolved passing-electron parallel flow at leading order, but this is part of the reduced state definition rather than an additional input restriction.

### 5.4 Energy and temperature moments

No zero-energy or zero-temperature-moment constraint is imposed. The system is driven by equilibrium gradients and its perturbation Helmholtz free energy is the positive disturbance norm, not a quantity required to vanish. Finite nonzero density/temperature moments are legitimate perturbation directions.

### 5.5 Gauge

No gauge degree of freedom remains after field elimination in the fixed nonzonal sector, as established above.

### 5.6 Parity

F2.2 explicitly froze **no parity reduction**. Even/odd ballooning or velocity-parity restrictions are therefore forbidden as an input-space simplification.

### 5.7 Ballooning boundary / infinite field line

The F2.2 representation uses the infinite ballooning line. Physical admissibility requires finite free energy and the inherited ballooning/orbit regularity. These are functional-domain conditions, not a finite-dimensional projector selecting a preferred initial subspace.

A later finite `theta` truncation is numerical only and must converge to this continuous space; its boundary condition may not redefine `B`.

### 5.8 Trapped/passing structure

For electrons,

\[
\boxed{g_e^{\rm pass}=0}
\]

is already part of the source-faithful F2-R reduction. The dynamic electron component is the full trapped nonadiabatic space allowed by the frozen `(E_e,lambda,w)` coordinates and bounce-average structure.

For ions, both passing and trapped orbit sectors allowed by the gyrokinetic ion phase space remain present. Turning-point matching/single-valuedness belongs to physical coordinate regularity and the generator domain; it is not an effect-selected moment restriction.

No transport-neutral condition is imposed on either species.

---

## 6. Exact continuous input operator

Let the input space be

\[
\boxed{\mathcal U_{F2}=\mathcal H_{F2}.}
\]

Then the physical initial-value map is simply

\[
\boxed{
B:\mathcal U_{F2}\to\mathcal H_{F2},
\qquad
Bu=u.
}
\]

Therefore

\[
\boxed{B=I_{\mathcal H_{F2}}.}
\]

This is the continuous kinetic analogue of a full-state initial-condition problem. It means every finite-free-energy state of the **reduced physical model** is admissible initial data.

It does not mean:

- that the fully kinetic passing-electron state is admissible in F2-R;
- that `phi` is an independently preparable input;
- that every distribution perturbation is realizable by an independent laboratory actuator;
- that ion and trapped-electron perturbations can be experimentally driven independently with arbitrary precision;
- that transport neutrality is imposed;
- that a later numerical basis may discard directions for convenience.

---

## 7. Exact input cost

The preparation-cost semantics for this project are a fixed amount of initial physical disturbance content, not actuator work. The already-derived positive Helmholtz free energy is the unique frozen positive physical norm for that purpose.

Thus

\[
\boxed{
R_{\rm in}=B^\dagger\mathcal M_{F2}B
=\mathcal M_{F2}.
}
\]

For an input `u`,

\[
J_{\rm in}(u)
=\langle u,R_{\rm in}u\rangle
=2W(0).
\]

A unit CORE input budget may therefore be chosen as

\[
\langle u,\mathcal M_{F2}u\rangle=1,
\]

which corresponds to `W(0)=1/2` in the present normalization. Any alternate overall scalar normalization would be a convention only and would not alter the admissible directions.

No Euclidean `L2` amplitude norm, species-weighted ad hoc norm or numerical coefficient norm is authorized as `R_in`.

---

## 8. Preservation of the F2.1 multichannel physics

Because `B` is the identity on the full reduced kinetic energy space, the admissible initial geometry retains both:

1. ion kinetic perturbation directions that contribute to `Gamma` and `q_i`;
2. trapped-electron nonadiabatic directions that contribute to `Gamma` and `q_e^tr`.

No source-channel direction is removed by construction.

This is a physical-admissibility statement only. It does **not** establish that the later discretized Hermitian channel operators are linearly independent, that their optimal directions differ, or that any finite-time objective separation is nonzero.

---

## 9. Later discretization requirements inherited from F2.4

A later structure-preserving discretization must preserve the following continuous geometry.

### 9.1 State-space conformity

The discrete space `H_F2,K` must approximate `H_F2`, including:

- ion ballooning/velocity directions;
- trapped-electron energy/pitch/well directions;
- both ion orbit-sign branches where physically present;
- no parity reduction;
- no artificial moment-null constraints;
- no transport-neutral projection.

### 9.2 Quasineutrality

The discrete potential must be reconstructed from the discrete kinetic state through a consistent quasineutrality solve. If `phi` is retained as an auxiliary numerical unknown, the algebraic quasineutrality constraint must be enforced exactly enough that `phi` does not become an extra independent input direction.

### 9.3 Positivity

The discrete Helmholtz form must satisfy

\[
M_K=M_K^\dagger\succ0
\]

on the discrete physical state after elimination of any algebraic field variable and spurious null directions.

No diagonal loading or numerical regularization may be used to manufacture positivity if the discretization has introduced an unphysical nullspace.

### 9.4 Discrete input pair

For a conforming coefficient representation of the full discrete state,

\[
\boxed{
B_K=I_{\mathcal H_{F2,K}},
\qquad
R_{{\rm in},K}=M_K.
}
\]

If a nontrivial basis/inclusion map is used, the coordinate representation must instead satisfy the congruent physical relation

\[
R_{{\rm in},K}=B_K^\dagger M_K B_K
\]

and converge to the same continuous identity embedding. A numerical basis is not allowed to alter admissibility.

### 9.5 Orbit/separatrix and ballooning convergence

Later quadrature must treat trapped/passing separatrices, bounce weights, ion turning points and the ballooning-line truncation so that the discrete free-energy norm and reconstructed field converge to the continuous forms. Cutoff/boundary choices remain a later numerical gate.

### 9.6 Channel preservation

The discrete physical particle and heat channels must be reconstructed from the F2.1 flux integrals on the same discrete state space. They may not be used to define or prune `B_K`.

---

## 10. Source and provenance check

The decision is consistent with the already-frozen source lineage:

- Costello & Plunk, *Journal of Plasma Physics* **91**, E12 (2025), derive the reduced system of fully gyrokinetic finite-FLR ions plus bounce-averaged electrons in the slow-electron-transit ordering and construct its Helmholtz free-energy balance. Their reduced dynamical variables are distribution functions, while quasineutrality supplies the electrostatic field.
- Helander & Plunk, *Journal of Plasma Physics* **88**, 905880207 (2022), formulate local gyrokinetic free energy as the physical disturbance measure for general multispecies flux-tube gyrokinetics.
- F2.1 already established for this project that, after quasineutrality elimination on the nonzonal finite-ion-FLR sector, the Helmholtz functional is strictly positive and defines `M_F2 > 0`.

The present gate adds no new kinetic closure or physics. It only classifies the physical initial-value geometry implied by those frozen equations.

---

## 11. F2.4 verdict

The candidate

\[
B=I_{\mathcal H_{F2}},
\qquad
R_{\rm in}=\mathcal M_{F2}
\]

is physically valid **provided the identity is understood on the reduced finite-free-energy Hilbert space defined above**.

Quasineutrality uniquely reconstructs `phi` and does not force a kinetic-state projection. Global invariant constraints do not impose zero moments on the fixed nonzonal block. No gauge, parity, transport-neutral or effect-motivated restriction is required. The source-faithful passing-electron removal and bounce/orbit regularity are already part of the reduced model/function-space definition.

Therefore

\[
\boxed{
\text{F2.4 PASS — KINETIC INPUT GEOMETRY / INPUT COST FROZEN — RETURN TO MASTER}
}
\]

No phase-space discretization or later numerical gate is self-authorized here.

**STOP / RETURN TO MASTER.**
