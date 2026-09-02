"""Structural tests for the D10-ZF Fourier-Galerkin discretization design."""

import numpy as np

from nonmodal_flux.models.hasegawa_wakatani import hasegawa_wakatani_matrices


def _multiplication_matrix(
    modes: np.ndarray,
    coefficients: dict[int, complex],
) -> np.ndarray:
    return np.array(
        [
            [coefficients.get(int(m - n), 0.0) for n in modes]
            for m in modes
        ],
        dtype=np.complex128,
    )


def _profile_matrices(
    modes: np.ndarray,
    coefficients: dict[int, complex],
    fundamental_wavenumber: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    u = _multiplication_matrix(modes, coefficients)
    ux = _multiplication_matrix(
        modes,
        {
            q: 1j * fundamental_wavenumber * q * value
            for q, value in coefficients.items()
        },
    )
    uxx = _multiplication_matrix(
        modes,
        {
            q: -(fundamental_wavenumber * q) ** 2 * value
            for q, value in coefficients.items()
        },
    )
    return u, ux, uxx


def _assemble_d10_galerkin(
    *,
    modes: np.ndarray,
    ky: float,
    coupling: float,
    kappa: float,
    profile_coefficients: dict[int, complex],
    fundamental_wavenumber: float = 1.0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    radial_wavenumbers = fundamental_wavenumber * modes.astype(float)
    derivative = np.diag(1j * radial_wavenumbers)
    laplacian = np.diag(-(radial_wavenumbers**2 + ky**2)).astype(
        np.complex128
    )
    identity = np.eye(len(modes), dtype=np.complex128)
    zeros = np.zeros_like(identity)

    u, ux, uxx = _profile_matrices(
        modes,
        profile_coefficients,
        fundamental_wavenumber,
    )

    phi_rhs = -1j * ky * u @ laplacian + 1j * ky * uxx + coupling * identity
    a_phi_phi = np.linalg.solve(laplacian, phi_rhs)
    a_phi_eta = np.linalg.solve(laplacian, -coupling * identity)
    a_eta_phi = (coupling - 1j * kappa * ky) * identity
    a_eta_eta = -coupling * identity - 1j * ky * u
    generator = np.block(
        [[a_phi_phi, a_phi_eta], [a_eta_phi, a_eta_eta]]
    )

    energy_metric = np.block(
        [[-laplacian, zeros], [zeros, identity]]
    )
    particle_flux = 0.5 * ky * np.block(
        [[zeros, 1j * identity], [-1j * identity, zeros]]
    )

    mean_flow_phi = (ky / (2j)) * (
        ux @ derivative - (ux @ derivative).conj().T
    )
    mean_flow_exchange = np.block(
        [[mean_flow_phi, zeros], [zeros, zeros]]
    )

    resistive_sink = 2.0 * coupling * np.block(
        [[identity, -identity], [-identity, identity]]
    )
    return (
        generator,
        energy_metric,
        particle_flux,
        mean_flow_exchange,
        resistive_sink,
    )


def test_projected_profile_matrices_obey_exact_commutator_product_rules() -> None:
    modes = np.arange(-3, 4)
    amplitude = 0.2
    coefficients = {1: amplitude / 2.0, -1: amplitude / 2.0}
    derivative = np.diag(1j * modes.astype(float))
    u, ux, uxx = _profile_matrices(modes, coefficients)

    np.testing.assert_allclose(u.conj().T, u, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(ux.conj().T, ux, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(uxx.conj().T, uxx, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(
        derivative @ u - u @ derivative,
        ux,
        rtol=0.0,
        atol=2.0e-16,
    )
    np.testing.assert_allclose(
        derivative @ ux - ux @ derivative,
        uxx,
        rtol=0.0,
        atol=2.0e-16,
    )


def test_discrete_multichannel_energy_balance_is_exact_for_resolved_zonal_flow() -> None:
    modes = np.arange(-3, 4)
    ky = 1.0
    coupling = 1.0
    kappa = 1.0
    amplitude = 0.2
    coefficients = {1: amplitude / 2.0, -1: amplitude / 2.0}

    generator, metric, q_gamma, q_u, dissipation = _assemble_d10_galerkin(
        modes=modes,
        ky=ky,
        coupling=coupling,
        kappa=kappa,
        profile_coefficients=coefficients,
    )

    np.testing.assert_allclose(metric.conj().T, metric, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(q_gamma.conj().T, q_gamma, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(q_u.conj().T, q_u, rtol=0.0, atol=2.0e-16)
    assert np.linalg.eigvalsh(metric)[0] > 0.0
    assert np.linalg.eigvalsh(dissipation)[0] > -2.0e-14

    balance = generator.conj().T @ metric + metric @ generator
    expected = 2.0 * kappa * q_gamma + 2.0 * q_u - dissipation
    np.testing.assert_allclose(balance, expected, rtol=0.0, atol=5.0e-15)


def test_zero_zonal_flow_reduces_to_independent_d2a_fourier_blocks() -> None:
    modes = np.arange(-2, 3)
    ky = 1.0
    coupling = 1.0
    kappa = 1.0
    generator, metric, q_gamma, q_u, _ = _assemble_d10_galerkin(
        modes=modes,
        ky=ky,
        coupling=coupling,
        kappa=kappa,
        profile_coefficients={},
    )
    count = len(modes)

    np.testing.assert_allclose(q_u, 0.0, rtol=0.0, atol=0.0)

    for index, mode in enumerate(modes):
        block_indices = [index, count + index]
        a_block = generator[np.ix_(block_indices, block_indices)]
        m_block = metric[np.ix_(block_indices, block_indices)]
        q_block = q_gamma[np.ix_(block_indices, block_indices)]
        a_expected, m_expected, q_expected, _ = hasegawa_wakatani_matrices(
            kx=float(mode),
            ky=ky,
            coupling=coupling,
            kappa=kappa,
            damping=0.0,
        )
        np.testing.assert_allclose(a_block, a_expected, rtol=0.0, atol=2.0e-15)
        np.testing.assert_allclose(m_block, m_expected, rtol=0.0, atol=0.0)
        np.testing.assert_allclose(q_block, q_expected, rtol=0.0, atol=0.0)

    off_block = generator.copy()
    for index in range(count):
        block_indices = [index, count + index]
        off_block[np.ix_(block_indices, block_indices)] = 0.0
    np.testing.assert_allclose(off_block, 0.0, rtol=0.0, atol=2.0e-15)


def test_constant_zonal_flow_is_doppler_shift_only() -> None:
    modes = np.arange(-2, 3)
    ky = 1.0
    speed = 0.3
    generator_zero, _, _, _, _ = _assemble_d10_galerkin(
        modes=modes,
        ky=ky,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={},
    )
    generator_flow, _, _, q_u, _ = _assemble_d10_galerkin(
        modes=modes,
        ky=ky,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={0: speed},
    )

    np.testing.assert_allclose(q_u, 0.0, rtol=0.0, atol=0.0)
    np.testing.assert_allclose(
        generator_flow - generator_zero,
        -1j * ky * speed * np.eye(2 * len(modes)),
        rtol=0.0,
        atol=2.0e-15,
    )


def test_sinusoidal_zonal_flow_creates_only_expected_first_sidebands() -> None:
    modes = np.arange(-3, 4)
    amplitude = 0.2
    generator, _, _, q_u, _ = _assemble_d10_galerkin(
        modes=modes,
        ky=1.0,
        coupling=1.0,
        kappa=1.0,
        profile_coefficients={1: amplitude / 2.0, -1: amplitude / 2.0},
    )
    count = len(modes)

    assert np.linalg.norm(q_u) > 0.0

    eta_eta = generator[count:, count:]
    for row, m in enumerate(modes):
        for column, n in enumerate(modes):
            if row == column:
                continue
            if abs(int(m - n)) == 1:
                assert abs(eta_eta[row, column]) > 0.0
            else:
                np.testing.assert_allclose(
                    eta_eta[row, column],
                    0.0,
                    rtol=0.0,
                    atol=0.0,
                )
