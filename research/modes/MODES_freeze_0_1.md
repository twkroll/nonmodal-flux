# MODES Mathematical Freeze 0.1 — structural robustness test against CORE 0.1

**Status:** reference / rollback point for the MODES branch.  
**Date:** 2026-09-02  
**Branch:** `explore/modes-core-robustness`  
**Role:** this document does not replace CORE Mathematical Freeze 0.1. It tests which representations and reductions preserve the mathematical mechanism already isolated by CORE.

## 0. Central question

> Which representation, mode basis, or reduced coordinate description preserves the mechanism identified in CORE?

The answer at Freeze 0.1 is not “one preferred modal family.” The structurally correct distinction is:

1. **invertible coordinate changes** are harmless if all CORE tensors/forms are transformed consistently;
2. **dimension reduction** is the dangerous step;
3. a reduction is CORE-faithful only if it preserves the input subspace, signed observable, metric/balance structure, and the relevant short-time transport-generation moments.

The most natural short-time CORE-adapted state space is the dynamical jet / block Krylov space

\[
\mathcal K_J(A,B)=\operatorname{span}\{B,AB,\ldots,A^J B\}.
\]

For a transport-neutral input with generation order \(\nu=1\), the leading mechanism is already contained in

\[
\mathcal K_1(A,B)=\operatorname{span}\{B,AB\}.
\]

This is the main new structural result of the MODES comparison.

---

# 1. CORE objects: coordinate-independent content vs representation

CORE uses

\[
\dot x=Ax,\qquad x(0)=Bu,
\]

with a positive metric \(M\succ0\), an independently derived Hermitian signed transport form \(Q\), admissible-input metric \(R_{\rm in}\succ0\), cumulative operator

\[
P_Q(T)=\int_0^T e^{A^\dagger t}Qe^{At}\,dt,
\]

and generation matrices

\[
G_j=B^\dagger\mathcal L_A^j(Q)B,
\qquad
\mathcal L_A(X)=A^\dagger X+XA.
\]

Whitening gives \(H_j=R_{\rm in}^{-1/2}G_jR_{\rm in}^{-1/2}\).

## 1.1 Exact state-coordinate covariance

Let \(x=T y\) with nonsingular \(T\). Then

\[
A_y=T^{-1}AT,\quad
B_y=T^{-1}B,\quad
M_y=T^\dagger MT,\quad
Q_y=T^\dagger QT.
\]

Consequently

\[
P_{Q_y}(T)=T^\dagger P_Q(T)T,
\]

and

\[
B_y^\dagger P_{Q_y}(T)B_y=B^\dagger P_Q(T)B.
\]

Likewise

\[
B_y^\dagger \mathcal L_{A_y}^j(Q_y)B_y
=B^\dagger \mathcal L_A^j(Q)B.
\]

Therefore the following are invariant under invertible state-coordinate changes:

- physical signed transport values;
- terminal and cumulative generalized gains;
- transport-neutrality \(B^\dagger QB=0\);
- transport-generation order \(\nu\);
- spectra of the whitened generation/gain operators;
- the single- and multi-channel balance identities, provided all forms are transformed by congruence.

The matrices \(A,M,Q,B\) themselves are representation dependent; their physical equivalence class is not.

## 1.2 Input-coordinate covariance

For an invertible reparameterization \(u=Cv\), use

\[
B_v=BC,\qquad R_v=C^\dagger R_{\rm in}C.
\]

The generalized eigenvalues and the zero/nonzero status of the unwhitened generation matrices are unchanged. Individual coordinate vectors change, but the physical optimal initial state does not.

## 1.3 What is genuinely representation-sensitive

The following are not invariants under noninvertible reduction:

- inertia/sign structure retained by the reduced \(Q\);
- neutrality of a projected admissible input unless the input is represented exactly;
- generation order \(\nu\);
- short-time matrices \(H_j\);
- finite-time gains;
- T2/T3 balance structure unless the projection is chosen compatibly with \(M\);
- the T4 relation between energy- and transport-optimal directions.

Thus MODES is fundamentally a **projection/reduction problem**, not a basis-choice problem.

---

# 2. Classical eigenmodes versus the CORE mechanism

Assume \(A=V\Lambda V^{-1}\). In full modal coordinates \(y=V^{-1}x\),

\[
Q_{\rm mod}=V^\dagger QV,
\qquad
M_{\rm mod}=V^\dagger MV.
\]

A complete eigenbasis is mathematically exact, even when strongly nonorthogonal. The CORE mechanism is preserved if the transformed \(Q\), \(M\), and input map are retained in full.

The failure occurs when one equates “modal representation” with one of the following approximations:

- retaining only a few eigenvalues/eigenvectors;
- treating nonorthogonal eigenvectors as Euclidean-orthogonal;
- diagonalizing \(A\) and simultaneously discarding off-diagonal entries of \(Q_{\rm mod}\) or \(M_{\rm mod}\);
- ranking modes only by eigenvalue growth/decay rate.

The transport mechanism can live in cross-pairings between modes even when every eigenvalue is stable.

## Counterexample A: nonnormal but spectrally stable

Take

\[
A=\begin{pmatrix}-1&4\\0&-2\end{pmatrix},\quad
Q=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
B=e_2.
\]

Then

\[
B^\dagger QB=0,
\]

while

\[
B^\dagger(A^\dagger Q+QA)B=8.
\]

Hence \(\nu=1\) and cumulative transport begins at order \(T^2\), despite eigenvalues \(-1,-2\). A one-eigenmode truncation cannot simultaneously preserve the admissible initial state and the neutral-to-generated transport mechanism.

## Counterexample B: nonnormality is not necessary

Take the **normal diagonal** system

\[
A=\operatorname{diag}(-1,-2),\quad
Q=\operatorname{diag}(1,-1),\quad
B=\frac1{\sqrt2}(1,1)^T.
\]

Again

\[
B^\dagger QB=0,
\]

but

\[
B^\dagger(A^\dagger Q+QA)B=1\neq0.
\]

Thus the CORE transport-generation mechanism is broader than classical nonnormal transient growth. Here differential decay of positive- and negative-signature components destroys the initial cancellation.

**Freeze statement:** do not identify CORE with nonnormality. Nonnormality can strengthen finite-time effects, but it is neither necessary nor by itself sufficient for signed transport generation.

---

# 3. What is lost in eigenvalue-only / modal truncations

Eigenvalues alone do not encode:

1. the signed observable \(Q\);
2. the metric \(M\);
3. admissibility \(\operatorname{range}(B)\);
4. neutral geometry \(B^\dagger QB=0\);
5. the bilinear pairings
   \[
   (A^rB)^\dagger Q(A^{j-r}B)
   \]
   that build \(H_j\);
6. the distinction between energy-optimal and transport-optimal directions;
7. transient amplification arising from eigenvector nonorthogonality;
8. channel identifiability in the multichannel balance.

A reduction can therefore reproduce the spectrum of \(A\) well and still destroy the CORE mechanism.

---

# 4. Parallel assessment of major mode/reduction families

## 4.1 Nonorthogonal eigenmodes

**Full basis:** SAFE.  
**Truncated basis:** CONDITIONAL.

Nonorthogonality itself is not a defect. A nonunitary basis merely moves geometric information into \(M_{\rm mod}\), \(Q_{\rm mod}\), and the coordinate representation of \(B\). Discarding that geometry is the defect.

For a nonnormal system, left/right eigenvectors or a biorthogonal Petrov--Galerkin construction are usually more informative than a right-eigenvector-only Euclidean projection, but CORE fidelity must still be checked through \(H_j\) and the balance identities.

## 4.2 Optimal perturbation directions / singular vectors

Standard finite-time singular vectors solve an **energy/norm-growth** problem, schematically

\[
\max_u \frac{\|e^{AT}Bu\|_M^2}{\|u\|_{R_{\rm in}}^2}.
\]

They capture nonmodal finite-time growth and are therefore structurally closer to CORE than eigenvalue ranking. But CORE optimizes a different object:

\[
\max_u\frac{u^\dagger B^\dagger P_Q(T)Bu}{u^\dagger R_{\rm in}u}.
\]

For indefinite \(Q\), this is not an ordinary singular-value problem. T4 already predicts that energy and transport optimals can remain separated as \(T\downarrow0\).

**Freeze statement:** ordinary singular vectors are useful comparison coordinates, not a canonical CORE reduction basis.

## 4.3 POD

POD is variance/energy optimal for the snapshot ensemble used to construct it. That objective contains no guarantee of preserving a low-energy direction that is essential to a signed cross term or to \(H_1\).

Therefore POD may be excellent for reconstruction while being poor for transport generation. A POD truncation is CORE-faithful only after explicit tests of \(Q\), neutrality, \(H_j\), and balance preservation.

## 4.4 DMD / Koopman-like modal representations

DMD extracts dynamically coherent modes associated with a fitted inter-snapshot linear map. For a truly linear system and a complete representation, it approaches a data-driven eigenmode description. Hence the same distinction applies:

- full-rank invertible DMD coordinates: harmless in principle;
- truncated DMD: no generic guarantee of CORE preservation.

A successful DMD model must be scored against CORE observables, not merely eigenvalue or reconstruction accuracy.

## 4.5 DyCA / Uhl-type dynamic-subspace extraction

DyCA and the earlier Uhl/Hutt/Friedrich line explicitly aim to identify a low-dimensional deterministic/dynamical subspace from multivariate data. This makes them strong **candidate subspace estimators** when \(A\) is not known.

However, their native objective is not preservation of an independently derived signed quadratic transport form. A DyCA subspace can therefore be dynamically accurate and still miss a \(Q\)-critical direction.

Proposed CORE-aware use:

\[
\text{data-driven dynamic subspace}
\quad+\quad
\text{CORE structural tests }(Q,M,B,H_j).
\]

## 4.6 Amplitude reductions

A representation

\[
x\approx V a
\]

is safe only if the physical observable is pulled back as

\[
Q_a=V^\dagger QV,
\qquad
M_a=V^\dagger MV,
\]

and the projected dynamics reproduce the relevant dynamical images of the admissible input.

Keeping only amplitudes while reconstructing neither the slaved variables nor their contribution to \(Q\) can remove the very cross term that transports flux.

## 4.7 Synergetic / slaving-based reduction

Near an instability, a center-manifold/slaving construction has the form

\[
x=V_c a+h(a),
\]

where stable variables are functions of order parameters \(a\). This can preserve CORE-type observables if the **full reconstruction map** is used:

\[
\mathcal Q(a)=x(a)^\dagger Qx(a).
\]

If one drops \(h(a)\) from the observable, a fast/slaved variable that mediates signed transport can disappear from the reduced model.

**Freeze statement:** slaving is a plausible nonlinear extension principle for CORE, but it is not yet a theorem of CORE 0.1.

---

# 5. Natural CORE-adapted reduced basis

## 5.1 Transport-generation jet / block Krylov space

Define

\[
\mathcal K_J(A,B)=\operatorname{span}\{B,AB,\ldots,A^J B\}.
\]

Let \(V\) be any full-rank basis of this space and define

\[
G=V^\dagger MV,
\qquad
W=MVG^{-1},
\qquad W^\dagger V=I.
\]

Use the \(M\)-Galerkin/Petrov--Galerkin reduction

\[
A_r=W^\dagger AV,
\quad
B_r=W^\dagger B,
\quad
M_r=V^\dagger MV=G,
\quad
Q_r=V^\dagger QV.
\]

### Proposition MODES-P1: exact short-time moment preservation

If \(\mathcal K_J(A,B)\subseteq\operatorname{range}(V)\), then for every \(k\le J\),

\[
VA_r^kB_r=A^kB.
\]

Consequently, for every \(j\le J\),

\[
B_r^\dagger\mathcal L_{A_r}^j(Q_r)B_r
=
B^\dagger\mathcal L_A^j(Q)B.
\]

Therefore \(H_0,\ldots,H_J\) are reproduced exactly (using the same input metric), and any generation order \(\nu\le J\) is preserved.

### Corollary: neutral \(\nu=1\) mechanism

If

\[
B^\dagger QB=0,
\qquad H_1\neq0,
\]

then the leading CORE mechanism is exactly represented by

\[
\mathcal K_1(A,B)=\operatorname{span}\{B,AB\}.
\]

This gives a natural interpretation:

> the initial layer is transport neutral; the first dynamical image \(AB\) supplies the state direction whose \(Q\)-pairing with the initial layer generates transport.

An \(M\)-orthogonal block-Arnoldi basis makes this layered mechanism explicit.

## 5.2 Proposition MODES-P2: projected balance preservation

For the same \(M\)-Galerkin reduction,

\[
A_r^\dagger M_r+M_rA_r
=V^\dagger(A^\dagger M+MA)V.
\]

Hence, if CORE has

\[
A^\dagger M+MA
=\sum_\alpha g_\alpha Q_\alpha-D,
\qquad D\succeq0,
\]

then the reduced system obeys exactly

\[
A_r^\dagger M_r+M_rA_r
=\sum_\alpha g_\alpha Q_{\alpha,r}-D_r,
\]

with

\[
Q_{\alpha,r}=V^\dagger Q_\alpha V,
\qquad D_r=V^\dagger DV\succeq0.
\]

Thus the same projection can preserve both the short-time generation hierarchy and the T2/T3 balance structure.

## 5.3 Limitation

The block Krylov basis guarantees **local/short-time** matching through the chosen order. It does not generally reproduce the full finite-time operator \(P_Q(T)\) exactly. Exact global reproduction requires the relevant state orbit to remain in the reduced subspace (e.g. an appropriate \(A\)-invariant subspace) or a separate finite-horizon input/output approximation.

---

# 6. Haken, Hutt, Uhl, Friedrich: actual connection

## 6.1 Haken

Haken's synergetics develops order parameters and the slaving principle near instabilities. This is a principled route from many degrees of freedom to a small set of collective variables.

**Classification for CORE 0.1:** STRUCTURALLY ANALOGOUS.  
**Can become mathematically direct:** if a center/invariant manifold is derived and \(M,Q\) are pulled back through the full slaving map.

It is not currently correct to call the CORE transport-optimal vector an order parameter in Haken's technical sense.

## 6.2 Uhl + Friedrich + Haken (1995)

Uhl, Friedrich and Haken explicitly developed a procedure to identify spatial modes and corresponding order-parameter equations from spatiotemporal signals near instabilities.

**Classification:** MATHEMATICALLY DIRECT as a mode-identification/reduced-dynamics methodology; only STRUCTURALLY ANALOGOUS to CORE's signed-transport preservation criterion.

## 6.3 Hutt + Uhl + Friedrich (1999)

Their perturbative signal-analysis method targets spatial modes, a criterion for the number of interacting modes, and filtering of nonorthogonal noise.

**Classification:** MATHEMATICALLY DIRECT to the MODES question of nonorthogonal mode extraction and mode count. It does not by itself preserve CORE's \(Q\), \(H_j\), or balance laws.

This paper is the strongest historical bridge among the four names for the current MODES task.

## 6.4 Uhl et al. (2024), DyCA

DyCA separates a deterministic ODE-driven subspace from stochastic components of multivariate data.

**Classification:** MATHEMATICALLY DIRECT as a candidate dynamic-subspace estimator; CORE preservation remains an additional constraint.

## 6.5 Hutt's stochastic center-manifold / neural-field work

Hutt and collaborators use mode reductions, stability analysis, stochastic center-manifold methods, and neural-field dynamics near instabilities.

**Classification:** STRUCTURALLY ANALOGOUS to a future nonlinear/stochastic CORE reduction; model-specific parts can become mathematically direct when the same hypotheses hold.

## 6.6 Friedrich--Peinke stochastic cascades

The Markov-in-scale / Kramers--Moyal program concerns probability evolution across scale, not the deterministic finite-time signed transport operator of CORE 0.1.

**Classification:** HEURISTIC/PARALLEL at this stage. It should not be presented as a derivation of CORE or vice versa.

---

# 7. General reduction principle emerging from MODES

A candidate general principle is:

> **Reduce by preserving the mechanism-defining forms and dynamical moments, not by preserving state variance or eigenvalues alone.**

For CORE this means a reduced model should be scored by a hierarchy of structural residuals, e.g.

\[
\varepsilon_j
=
\left\|
B^\dagger\mathcal L_A^j(Q)B
-
B_r^\dagger\mathcal L_{A_r}^j(Q_r)B_r
\right\|,
\]

plus neutrality and balance errors

\[
\varepsilon_Q=\|B_r^\dagger Q_rB_r-B^\dagger QB\|,
\]

\[
\varepsilon_{\rm bal}
=
\left\|
A_r^\dagger M_r+M_rA_r
-\sum_\alpha g_\alpha Q_{\alpha,r}+D_r
\right\|.
\]

Finite-time extensions should additionally compare \(B^\dagger P_Q(T)B\), not merely state reconstruction.

This defines a **CORE-aware model reduction** problem.

---

# 8. Branch points

## BP-M1 — primary reduced basis

### M1-A: eigenmode truncation
Parked as default. Useful only with explicit CORE validation.

### M1-B: POD/DMD/DyCA learned basis
Active as data-driven candidate when \(A\) is unavailable. Must be followed by CORE structural scoring.

### M1-C: finite-time optimal/singular-vector basis
Active as comparison branch for nonmodal finite-time dynamics. Standard energy singular vectors are not transport-specific.

### M1-D: CORE transport-generation Krylov/jet basis
**Current preferred theoretical branch for short-time mechanism preservation.**

Rollback condition: abandon as primary basis if it fails numerically at moderate horizon or if a smaller structure-preserving subspace is derived.

## BP-M2 — local versus global reduction

### M2-A: local moment/generation matching
Current stable result: \(\mathcal K_J(A,B)\) with \(M\)-projection.

### M2-B: global finite-horizon reduction
Open. Candidates include finite-horizon input/output balancing or quadratic-output moment matching, but the indefinite signed \(Q\) structure must be preserved rather than replaced by a positive output norm.

## BP-M3 — nonlinear extension

### M3-A: center-manifold/slaving reduction
Open, physically attractive near instability.

### M3-B: generic learned amplitude model
Open, but must pull back the signed observable and pass structural tests.

No choice required yet; both should be tested on the same benchmark before selection.

---

# 9. What would justify CORE 0.2?

MODES would justify a CORE 0.2 change if one or more of the following is accepted/proved in the canonical CORE line:

1. **Coordinate-covariance theorem/remark:** explicitly state that CORE quantities are invariant under full invertible state reparameterization when forms are transformed by congruence.
2. **Nonnormality caveat:** explicitly state and demonstrate that transport generation does not require nonnormal \(A\).
3. **Structure-preserving reduction proposition:** add the block-Krylov/dynamical-jet result preserving \(H_j\) through order \(J\).
4. **Balance-preserving projection proposition:** record that \(M\)-Galerkin projection preserves the projected T2/T3 balance exactly.
5. **Reduction criterion:** distinguish state reconstruction/spectral accuracy from preservation of \(Q\), neutrality, generation order and finite-time signed gain.
6. **Data-driven interface:** define how POD/DMD/DyCA candidate subspaces are accepted or rejected by CORE structural residuals.

Items 1--4 are already mathematically strong enough to propose to CORE; novelty relative to the model-reduction literature must still be assessed before manuscript-level claims.

---

# 10. Statements not yet justified

Do **not** claim that:

- CORE is fundamentally a theory of nonnormality;
- eigenmodes are intrinsically wrong;
- POD, DMD or DyCA preserve transport because they reconstruct the state well;
- standard singular vectors solve the signed transport problem;
- the transport-generation Krylov basis is novel model-reduction theory (quadratic-output Krylov/moment-matching literature exists);
- Haken's slaving principle has already been derived from CORE;
- CORE optimal disturbances are Haken order parameters;
- Friedrich--Peinke scale dynamics is a consequence of CORE 0.1;
- a universal low-dimensional modal basis exists independent of \(Q\), \(B\), horizon and physical channel;
- an indefinite signed observable can be safely replaced by a positive output norm for balancing/reduction.

---

# 11. MODES Freeze 0.1 — stable / branch / open classification

## STABLE

- Full invertible coordinate changes preserve the CORE mechanism when \(M,Q,A,B\) are transformed consistently.
- Dimension reduction, not nonorthogonal coordinates themselves, is the main structural risk.
- Full eigenmode representations are valid; eigenvalue-only or mode-truncated descriptions can destroy CORE.
- Nonnormality is not necessary for neutral-to-generated signed transport.
- For short-time order \(J\), a block Krylov space containing \(B,AB,\ldots,A^JB\) preserves the generation matrices through order \(J\) under the stated projection.
- An \(M\)-Galerkin projection preserves the projected energy/transport balance.
- POD/DMD/DyCA require an explicit CORE structural acceptance test.

## BRANCH

- CORE-Krylov/jet basis is the preferred theoretical short-time branch.
- Data-driven dynamic modes remain the preferred empirical subspace-discovery branch when governing operators are not known.
- Finite-horizon balanced/quadratic-output reduction remains a parallel branch for long-time accuracy.

## CONJECTURE

- A hybrid basis combining the early transport-generation jet with finite-horizon transport observability may provide a compact basis that is accurate both locally and globally.
- In nonlinear systems, a slaving/center-manifold reduction with the full pullback of \(Q\) may provide the appropriate CORE-compatible amplitude theory.

## OPEN

- Minimal dimension required to preserve a prescribed set of \(H_j\) beyond the simple sufficient Krylov construction.
- Best indefinite-output analogue of balanced truncation for the signed CORE observable.
- Error bounds connecting \(\varepsilon_j\) to finite-horizon signed gain errors.
- Whether a learned DyCA/DMD subspace can recover the CORE-Krylov jet from data without access to \(A\).
- How the D10-ZF/other active CORE branches modify the preferred long-horizon reduction after their assumptions are fixed.

---

# 12. Return package to CORE

## Robust findings

1. CORE is coordinate covariant; basis choice is not physics.
2. Reduction must preserve \(Q\), \(M\), \(B\), neutrality and the generation moments, not merely eigenvalues or energy.
3. The short-time mechanism has a natural state-space carrier: the dynamical jet \(\{B,AB,\ldots\}\).
4. For \(\nu=1\), \(\operatorname{span}(B,AB)\) is sufficient to preserve the leading neutral-to-generated transport term.
5. \(M\)-weighted projection preserves the projected T2/T3 balance structure.
6. Nonnormality is optional, not defining.

## Counterexamples returned to CORE

- stable nonnormal \(2\times2\) system with \(H_0=0\), \(H_1=8\): eigenvalues alone miss the mechanism;
- normal diagonal \(2\times2\) system with \(H_0=0\), \(H_1=1\): mechanism exists without nonnormality;
- generic POD/eigenmode truncation can lose a low-energy \(Q\)-partner and thereby alter neutrality or generation order.

## Requested CORE changes/extensions

Propose for CORE 0.2:

- coordinate-covariance remark/proposition;
- explicit nonnormality caveat;
- transport-generation Krylov/jet preservation proposition;
- balance-preserving \(M\)-projection proposition;
- structural reduction diagnostics.

## Questions CORE must answer before a global MODES choice

- Which active branch quantities beyond T1--T4 must a reduced model preserve exactly?
- Is the target reduction primarily short-time/asymptotic, or must it reproduce \(P_Q(T)\) on a finite horizon interval?
- For multichannel transport, must all \(Q_\alpha\) be preserved simultaneously or can one channel be privileged?

---

# References / orientation

- C. Uhl, R. Friedrich, H. Haken, *Analysis of spatiotemporal signals of complex systems*, Phys. Rev. E 51, 3890 (1995).
- A. Hutt, C. Uhl, R. Friedrich, *Analysis of spatiotemporal signals: a method based on perturbation theory*, Phys. Rev. E 60, 1350 (1999).
- C. Uhl et al., *Disentangling dynamic and stochastic modes in multivariate time series*, Front. Appl. Math. Stat. 10 (2024).
- H. Haken, synergetics / order-parameter and slaving-principle literature.
- P. J. Schmid, *Dynamic mode decomposition of numerical and experimental data*, J. Fluid Mech. 656 (2010).
- Literature on balanced/POD reduction for nonnormal systems and recent Krylov/moment-matching methods for linear systems with quadratic outputs must be treated as prior art when assessing novelty of the CORE-aware reduction result.
