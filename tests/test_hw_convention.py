"""Convention-lock tests for the accepted D2-A Hasegawa-Wakatani pilot.

These tests intentionally encode the frozen PDE/Fourier/sign convention directly,
before the model constructor is implemented.  The later model implementation must
reproduce these identities rather than redefining them.
"""

import numpy as np


def _d2a_matrices(
    *, kx: float, ky: float, coupling: float, kappa: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return the exact matrices implied by the frozen D2-A convention."""

    k2 = kx**2 + ky**2
    assert k2 > 0.0
    assert ky != 0.0
    assert coupling >= 0.0
    assert kappa >= 0.0

    generator = np.array(
        [
            [-coupling / k2, coupling / k2],
            [coupling - 1j * kappa * ky, -coupling],
        ],
        dtype=np.complex128,
    )
    metric = np.diag([k2, 1.0]).astype(np.complex128)
    particle_flux = 0.5 * ky * np.array(
        [[0.0, 1j], [-1j, 0.0]], dtype=np.complex128
    )
    resistive_sink = 2.0 * coupling * np.array(
        [[1.0, -1.0], [-1.0, 1.0]], dtype=np.complex128
    )
    return generator, metric, particle_flux, resistive_sink


def test_d2a_generator_is_equivalent_to_the_frozen_fourier_pdes() -> None:
    kx = 0.6
    ky = 0.9
    coupling = 1.7
    kappa = 0.8
    generator, _, _, _ = _d2a_matrices(
        kx=kx, ky=ky, coupling=coupling, kappa=kappa
    )
    k2 = kx**2 + ky**2

    state = np.array([0.7 - 0.4j, -0.2 + 1.1j], dtype=np.complex128)
    phi, density = state
    phi_dot, density_dot = generator @ state

    np.testing.assert_allclose(
        -k2 * phi_dot,
        coupling * (phi - density),
        rtol=0.0,
        atol=2.0e-14,
    )
    np.testing.assert_allclose(
        density_dot + 1j * kappa * ky * phi,
        coupling * (phi - density),
        rtol=0.0,
        atol=2.0e-14,
    )


def test_d2a_energy_metric_and_particle_flux_form_have_required_structure() -> None:
    _, metric, particle_flux, _ = _d2a_matrices(
        kx=0.4, ky=1.2, coupling=1.5, kappa=0.7
    )

    np.testing.assert_allclose(metric, metric.conj().T, rtol=0.0, atol=0.0)
    assert np.all(np.linalg.eigvalsh(metric) > 0.0)

    np.testing.assert_allclose(
        particle_flux, particle_flux.conj().T, rtol=0.0, atol=0.0
    )
    q_eigenvalues = np.linalg.eigvalsh(particle_flux)
    assert q_eigenvalues[0] < 0.0 < q_eigenvalues[-1]


def test_d2a_quadratic_flux_equals_frozen_cross_phase_expression() -> None:
    for ky in (1.1, -0.7):
        _, _, particle_flux, _ = _d2a_matrices(
            kx=0.5, ky=ky, coupling=1.3, kappa=0.9
        )
        state = np.array([0.8 + 0.3j, -0.4 + 1.2j], dtype=np.complex128)
        phi, density = state

        quadratic_flux = state.conj().T @ particle_flux @ state
        cross_phase_flux = ky * np.imag(np.conj(density) * phi)

        np.testing.assert_allclose(
            np.imag(quadratic_flux), 0.0, rtol=0.0, atol=2.0e-14
        )
        np.testing.assert_allclose(
            np.real(quadratic_flux), cross_phase_flux, rtol=0.0, atol=2.0e-14
        )


def test_d2a_exact_linear_energy_balance_matrix_identity() -> None:
    for kx, ky, coupling, kappa in (
        (0.0, 0.8, 1.4, 0.6),
        (0.5, 1.1, 2.0, 0.9),
        (1.2, -0.7, 0.4, 1.3),
    ):
        generator, metric, particle_flux, resistive_sink = _d2a_matrices(
            kx=kx, ky=ky, coupling=coupling, kappa=kappa
        )

        balance_left = generator.conj().T @ metric + metric @ generator
        balance_right = 2.0 * kappa * particle_flux - resistive_sink

        np.testing.assert_allclose(balance_left, balance_right, rtol=0.0, atol=3.0e-14)
        assert np.min(np.linalg.eigvalsh(resistive_sink)) >= -2.0e-14


def test_d2a_statewise_energy_derivative_matches_flux_minus_resistive_sink() -> None:
    kx = 0.3
    ky = 1.0
    coupling = 1.6
    kappa = 0.75
    generator, metric, particle_flux, _ = _d2a_matrices(
        kx=kx, ky=ky, coupling=coupling, kappa=kappa
    )
    state = np.array([0.9 - 0.2j, 0.1 + 0.7j], dtype=np.complex128)
    phi, density = state

    energy_derivative = np.real(state.conj().T @ metric @ generator @ state)
    particle_transport = np.real(state.conj().T @ particle_flux @ state)
    physical_balance = (
        kappa * particle_transport - coupling * abs(phi - density) ** 2
    )

    np.testing.assert_allclose(
        energy_derivative, physical_balance, rtol=0.0, atol=3.0e-14
    )


def test_uniform_perpendicular_damping_adds_exact_metric_sink() -> None:
    generator, metric, particle_flux, resistive_sink = _d2a_matrices(
        kx=0.7, ky=0.9, coupling=1.2, kappa=0.65
    )
    damping = 0.23
    damped_generator = generator - damping * np.eye(2)

    balance_left = damped_generator.conj().T @ metric + metric @ damped_generator
    balance_right = (
        2.0 * 0.65 * particle_flux
        - resistive_sink
        - 2.0 * damping * metric
    )

    np.testing.assert_allclose(balance_left, balance_right, rtol=0.0, atol=3.0e-14)
