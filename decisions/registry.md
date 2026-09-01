# Decision Registry

This file records modeling and research decisions. A decision may only be changed by adding a new decision entry that states the reason, alternative, falsification/revision trigger, and escape route.

## D1 — Separate disturbance metric and transport observable

**Status:** Accepted

**Decision:** The positive disturbance-size metric `M` and the signed transport observable `Q` are distinct mathematical and physical objects.

Requirements:

- `M = M† > 0`.
- `Q = Q†` and may be indefinite.
- No implementation may silently replace `Q` by `M` or vice versa.
- Energy/free-energy gain and transport gain are reported separately.

**Reason:** `M` answers “how large is the disturbance?” while `Q` answers “what directed physical effect does it produce?”

**Revision trigger:** Only revise for a model in which the relevant physical energy and transport observable are rigorously identical.

---

## D2 — Hasegawa–Wakatani first-pilot convention

**Status:** Accepted as D2-A

**Decision:** For the first plasma pilot use the non-zonal (`k_y != 0`) linear Hasegawa–Wakatani subsystem with the following fixed orientation and Fourier convention:

- `x` is radial and `y` is poloidal;
- the magnetic field points along `+e_z`;
- normalized `E x B` velocity is `v_E = e_z x grad(phi)`, hence `v_x = -partial_y(phi)`;
- Fourier amplitudes use `exp(i k_x x + i k_y y)`;
- `k^2 = k_x^2 + k_y^2`;
- the state is `z_k = (phi_k, n_k)^T`.

With no added perpendicular dissipation, the frozen linear generator is

```math
L_k=
\begin{pmatrix}
-C/k^2 & C/k^2\\
C-i\kappa k_y & -C
\end{pmatrix}.
```

The physical single-mode energy and signed outward radial particle flux are

```math
E_k=\frac12\left(k^2|\phi_k|^2+|n_k|^2\right)
=\frac12 z_k^\dagger M_k z_k,
```

```math
M_k=\begin{pmatrix}k^2&0\\0&1\end{pmatrix},
```

and

```math
\Gamma_k=k_y\,\operatorname{Im}(n_k^*\phi_k)
=z_k^\dagger Q_{\Gamma,k}z_k,
```

```math
Q_{\Gamma,k}
=\frac{k_y}{2}
\begin{pmatrix}
0&i\\
-i&0
\end{pmatrix}.
```

These objects must continue to be derived from the physical PDE energy and flux, not fitted or reweighted. They satisfy

```math
L_k^\dagger M_k+M_kL_k
=2\kappa Q_{\Gamma,k}-2C
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
```

so that

```math
\frac{dE_k}{dt}=\kappa\Gamma_k-C|\phi_k-n_k|^2.
```

For a single non-zonal linear mode, standard and modified HW have the same subsystem used here. Any perpendicular dissipation introduced later for a spectrally stable pilot must be stated explicitly and retained in the physical balance; it is not part of the base D2-A generator unless a later decision says so.

**Reason:** This convention closes the physical energy/particle-flux balance exactly while preserving the outward-flux sign and the project rule that `M` and `Q` are independently physics-derived.

**Revision trigger:** A source-level inconsistency in the stated orientation/sign convention, failure of the derived balance, or evidence that the two-field pilot cannot represent the intended transport question without a different reduced model.

**Escape route:** Add a new decision entry documenting the alternative convention or reduced drift-fluid model, including the transformation of `L_k`, `M_k`, `Q_{Gamma,k}`, and the outward-flux sign. Do not silently alter D2-A.

---

## D3 — Pilot input spaces

**Status:** Proposed

The plasma pilot should compare at least:

1. the full physically admissible state space;
2. a transport-neutral admissible input space;
3. a physically restricted input space derived from the perturbation mechanism or model constraints.

For a transport-neutral linear input map, the preferred algebraic condition is

`B† Q B = 0`.

**Reason:** This prevents the optimization from becoming trivial by inserting the optimal transport cross-phase already at the initial instant.

**Revision trigger:** Replace the algebraic restriction if the chosen physical model gives a more appropriate notion of initially neutral transport.

---

## D4 — Gate-0 novelty focus

**Status:** Proposed

P1 is provisionally focused on:

> finite-horizon signed transport generated dynamically from physically admissible, transport-neutral initial disturbances, measured against an independent positive energy/input metric and constrained by a physical energy/free-energy balance.

The following are not sufficient standalone novelty claims:

- a quadratic-output Gramian;
- finite-time nonmodal energy growth;
- dependence of an optimal perturbation on the chosen norm/output;
- a restricted input map by itself;
- nonmodal Hasegawa–Wakatani phase dynamics by itself.

**Revision trigger:** A direct prior-art result that already covers the same combination of signed transport, transport-neutral admissible initial conditions, finite-horizon optimization, and comparable structural theorems.

---

## D5 — Physics-derived metrics and transport forms

**Status:** Accepted

**Decision:** Energy/free-energy metrics and transport observables must be derived from the continuous physical expressions before discretization.

In particular:

- transport objectives must not be ad-hoc weighted sums of state amplitudes;
- physical cross terms must be preserved;
- signs and orientation of directed fluxes must be preserved;
- quadrature, mass-matrix, geometric, species, and wavenumber weights produced by the derivation must be preserved;
- distinct physical transport channels remain distinct operators unless a physical balance gives a specific justified combination.

Examples of admissible constructions include particle or heat fluxes whose Fourier representation contains cross-phase terms such as `Im(n* phi)` or `Im(T* phi)` and which are represented by a Hermitian indefinite form `z† Q z`.

`M` is called a metric/norm only when it is positive definite. Indefinite `Q` objects are called **signed transport forms**, **transport observables**, or **transport functionals**, not norms.

**Reason:** The project follows the transport-oriented construction principle exemplified by Lülff: the observable must represent the actual physical transfer quantity, rather than a post-hoc scalar score assembled from state variables.

**Revision trigger:** None without a new explicit decision ID and a physical derivation justifying the change.

---

## D6 — No application sweeps before core validation

**Status:** Accepted

No broad parameter sweep is allowed before the model-independent core passes, in Float64 where applicable:

- analytic benchmark tests;
- Hermiticity checks;
- generalized-eigenproblem residual checks;
- coordinate/scaling invariance checks;
- signed-extremal ordering checks.

**Reason:** Numerical exploration must falsify or support precise theory rather than substitute for it.

---

## D7 — AI applications are a parking-lot idea, not current scope

**Status:** Accepted

**Decision:** Potential applications to recurrent networks, neural ODEs, state-space models, or representation-transfer analysis remain documented as an exploratory idea only. They do not enter P1, the Gate-0 novelty claim, the current implementation milestones, or the plasma model-selection process.

**Reason:** The analogy may be useful later, but adding AI now would broaden the project before the physical transport theory and plasma pilot have passed their gates.

**Revisit trigger:** Reconsider only after the model-independent library is validated and the plasma pilot has produced a robust transport-specific result, or if an independent collaborator/application creates a compelling reason to open a separate AI workstream.

**Escape route:** Keep all AI notes in `research/ai_applications.md`; no AI-specific dependencies or model code are added to the core package during P1.

---

## D8 — First spectrally stable HW single-case pilot

**Status:** Accepted for the first falsification calculation

**Decision:** Use exactly one D2-A Fourier mode with

```text
kx = 0.5
ky = 1.0
C = 1.0
kappa = 1.0
nu_k = 0.15
```

before any parameter sweep. The damping is an explicit single-mode perpendicular damping rate and remains part of the physical sink in the exact energy balance.

The case is spectrally stable, metric-nonnormal, and strictly energy-contractive. For the first transport-neutral diagnostic use the pure-potential input map

```math
B_\phi=(1,0)^T,
```

with the natural input metric `R_in=B_phi^† M B_phi=1.25`. This line has exactly zero initial particle flux but positive first transport-generation coefficient.

**Reason:** The case provides a deliberately strong falsification setting: all eigenvalues are stable and physical energy decreases monotonically, so positive signed particle transport cannot be explained as ordinary transient energy amplification. The pure-potential line tests dynamic cross-phase/flux generation without inserting initial transport.

**Structural warning:** For one complex two-field mode, `Q_Gamma` has signature `(1,1)`. A complex-linear totally `Q_Gamma`-isotropic subspace therefore has dimension at most one. The selected neutral line is suitable for transport-generation diagnostics but cannot support a nontrivial directional comparison between energy-optimal and transport-optimal disturbances within the same neutral subspace.

**Revision trigger:** Failure of the locked diagnostics, evidence that the chosen damping obscures the intended mechanism, or a decision that the headline pilot must contain a multidimensional transport-neutral optimization space rather than using the neutral line only as a generation diagnostic.

**Escape route:** Keep D2-A unchanged and enlarge the pilot state/input space, preferably by a physically justified multi-mode construction or a richer reduced model, so that a multidimensional transport-neutral admissible space can exist.