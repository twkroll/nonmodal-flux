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

## D2 — No frozen Hasegawa–Wakatani convention yet

**Status:** Open

**Decision required:** Select one documented PDE convention and derive the Fourier-space dynamical operator, free-energy metric, and particle-flux form from that convention before implementation.

Requirements before model code is accepted:

1. source convention is cited;
2. signs and normalizations are derived from the PDEs;
3. dissipation and drive terms are explicit;
4. the energy/free-energy balance is verified;
5. the flux matrix reproduces the continuous cross-phase expression.

**Escape route:** If no two-field convention supports the needed physical balance cleanly, use a better documented reduced drift-fluid model rather than forcing the pilot.

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
