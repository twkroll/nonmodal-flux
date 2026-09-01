"""Frozen D2-A non-zonal linear Hasegawa-Wakatani mode.

The matrices in this module are not fitted or chosen for numerical convenience.
They implement the convention frozen in decision D2-A:

* ``x`` radial and ``y`` poloidal;
* ``v_E = e_z x grad(phi)`` so ``v_x = -partial_y phi``;
* Fourier amplitudes proportional to ``exp(i k dot x)``;
* state ``z_k = (phi_k, n_k)^T``;
* physical energy ``E_k = (k^2 |phi_k|^2 + |n_k|^2)/2``;
* signed radial particle flux ``Gamma_k = k_y Im(n_k^* phi_k)``.

For uniform perpendicular damping ``nu_k >= 0`` the exact balance is

``A^H M + M A = 2 kappa Q_Gamma - D``

with ``D = 2 C S + 2 nu_k M`` and
``S = [[1, -1], [-1, 1]]``.
"""

from __future__ import annotations

from numbers import Real

import numpy as np
import numpy.typing as npt

from nonmodal_flux.core.problem import ArrayLike, TransportProblem

NDArray = npt.NDArray[np.complex128]


def _finite_real(name: str, value: Real) -> float:
    if not isinstance(value, Real):
        raise TypeError(f"{name} must be a real scalar, got {type(value).__name__}.")
    result = float(value)
    if not np.isfinite(result):
        raise ValueError(f"{name} must be finite, got {result}.")
    return result


def hasegawa_wakatani_matrices(
    *,
    kx: Real,
    ky: Real,
    coupling: Real,
    kappa: Real,
    damping: Real = 0.0,
) -> tuple[NDArray, NDArray, NDArray, NDArray]:
    """Return ``(A, M, Q_Gamma, D)`` for one frozen D2-A Fourier mode.

    Parameters
    ----------
    kx, ky:
        Radial and poloidal wavenumbers.  The first pilot is explicitly
        non-zonal, so ``ky`` must be nonzero.
    coupling:
        Resistive HW coupling ``C >= 0``.
    kappa:
        Background density-gradient drive ``kappa >= 0``.
    damping:
        Optional uniform perpendicular damping rate ``nu_k >= 0`` acting as
        ``A -> A - nu_k I``.  No value is inserted automatically.

    Returns
    -------
    A:
        The complex 2x2 generator in ``z_dot = A z``.
    M:
        Positive physical energy metric ``diag(k^2, 1)``.
    Q_Gamma:
        Hermitian signed particle-flux form satisfying
        ``z^H Q_Gamma z = ky Im(n^* phi)``.
    D:
        Positive-semidefinite sink in
        ``A^H M + M A = 2 kappa Q_Gamma - D``.
    """

    kx_value = _finite_real("kx", kx)
    ky_value = _finite_real("ky", ky)
    coupling_value = _finite_real("coupling", coupling)
    kappa_value = _finite_real("kappa", kappa)
    damping_value = _finite_real("damping", damping)

    k2 = kx_value**2 + ky_value**2
    if k2 <= 0.0:
        raise ValueError("k^2 = kx^2 + ky^2 must be positive.")
    if ky_value == 0.0:
        raise ValueError("D2-A first-pilot modes must be non-zonal: ky != 0.")
    if coupling_value < 0.0:
        raise ValueError("coupling C must be nonnegative.")
    if kappa_value < 0.0:
        raise ValueError("kappa must be nonnegative.")
    if damping_value < 0.0:
        raise ValueError("damping nu_k must be nonnegative.")

    generator = np.array(
        [
            [-coupling_value / k2, coupling_value / k2],
            [coupling_value - 1j * kappa_value * ky_value, -coupling_value],
        ],
        dtype=np.complex128,
    )
    if damping_value != 0.0:
        generator = generator - damping_value * np.eye(2, dtype=np.complex128)

    metric = np.diag([k2, 1.0]).astype(np.complex128)
    particle_flux = 0.5 * ky_value * np.array(
        [[0.0, 1j], [-1j, 0.0]], dtype=np.complex128
    )
    resistive_sink = 2.0 * coupling_value * np.array(
        [[1.0, -1.0], [-1.0, 1.0]], dtype=np.complex128
    )
    sink = resistive_sink + 2.0 * damping_value * metric

    return generator, metric, particle_flux, sink


def make_hasegawa_wakatani_problem(
    *,
    kx: Real,
    ky: Real,
    coupling: Real,
    kappa: Real,
    damping: Real = 0.0,
    B: ArrayLike | None = None,
    Rin: ArrayLike | None = None,
) -> TransportProblem:
    """Construct a validated transport problem for one D2-A HW mode.

    If ``B`` is omitted, the full two-component state is admissible.  If
    ``Rin`` is omitted, the input cost is the physical initial energy restricted
    to the chosen input map, ``B^H M B``.  These defaults do not alter the
    physical metric or flux observable and can be replaced explicitly for the
    transport-neutral and physically restricted input spaces studied later.
    """

    generator, metric, particle_flux, _ = hasegawa_wakatani_matrices(
        kx=kx,
        ky=ky,
        coupling=coupling,
        kappa=kappa,
        damping=damping,
    )

    input_map = np.eye(2, dtype=np.complex128) if B is None else np.asarray(B)
    input_metric = (
        input_map.conj().T @ metric @ input_map if Rin is None else np.asarray(Rin)
    )

    return TransportProblem(
        A=generator,
        M=metric,
        Q=particle_flux,
        B=input_map,
        Rin=input_metric,
    )
