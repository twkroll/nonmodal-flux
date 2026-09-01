"""Tests for the T3.1 multichannel balance nonidentifiability result."""

import numpy as np

from nonmodal_flux.core.gramians import (
    accumulated_signed_extrema,
    accumulated_transport_operator,
)
from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator


def _multichannel_witness() -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    float,
    float,
    np.ndarray,
]:
    """Return two different channel decompositions with the same total balance."""

    a = np.array([[-1.0, 0.7], [0.0, -1.6]])
    m = np.eye(2)
    dissipation = np.diag([2.6, 3.8])
    g1 = 1.2
    g2 = 0.8

    total_transport = a.conj().T @ m + m @ a + dissipation
    q1 = np.array([[0.4, 0.5], [0.5, -0.2]])
    q2 = (total_transport - g1 * q1) / g2

    shift = np.array([[0.3, -0.4], [-0.4, 0.1]])
    q1_shifted = q1 + g2 * shift
    q2_shifted = q2 - g1 * shift

    return a, m, dissipation, q1, g1, g2, np.stack([q2, q1_shifted, q2_shifted])


def _problem(a: np.ndarray, m: np.ndarray, q: np.ndarray) -> TransportProblem:
    return TransportProblem(
        A=a,
        M=m,
        Q=q,
        B=np.eye(a.shape[0]),
        Rin=np.eye(a.shape[0]),
    )


def test_channel_shift_preserves_the_total_physical_balance() -> None:
    a, m, dissipation, q1, g1, g2, packed = _multichannel_witness()
    q2, q1_shifted, q2_shifted = packed

    balance_left = a.conj().T @ m + m @ a
    total_original = g1 * q1 + g2 * q2
    total_shifted = g1 * q1_shifted + g2 * q2_shifted

    np.testing.assert_allclose(total_original, total_shifted, rtol=0.0, atol=2.0e-14)
    np.testing.assert_allclose(
        total_original - dissipation,
        balance_left,
        rtol=0.0,
        atol=2.0e-14,
    )
    assert not np.allclose(q1, q1_shifted)
    assert not np.allclose(q2, q2_shifted)


def test_weighted_finite_horizon_gramian_sum_is_unchanged() -> None:
    a, m, dissipation, q1, g1, g2, packed = _multichannel_witness()
    q2, q1_shifted, q2_shifted = packed

    p1_problem = _problem(a, m, q1)
    p2_problem = _problem(a, m, q2)
    p1_shifted_problem = _problem(a, m, q1_shifted)
    p2_shifted_problem = _problem(a, m, q2_shifted)
    dissipation_problem = _problem(a, m, dissipation)

    for horizon in (0.2, 0.7, 1.3):
        p1 = np.asarray(accumulated_transport_operator(p1_problem, horizon))
        p2 = np.asarray(accumulated_transport_operator(p2_problem, horizon))
        p1_shifted = np.asarray(
            accumulated_transport_operator(p1_shifted_problem, horizon)
        )
        p2_shifted = np.asarray(
            accumulated_transport_operator(p2_shifted_problem, horizon)
        )

        weighted_original = g1 * p1 + g2 * p2
        weighted_shifted = g1 * p1_shifted + g2 * p2_shifted
        np.testing.assert_allclose(
            weighted_original,
            weighted_shifted,
            rtol=2.0e-11,
            atol=3.0e-12,
        )

        p_d = np.asarray(accumulated_transport_operator(dissipation_problem, horizon))
        phi = np.asarray(constant_propagator(a, horizon))
        delta_m = phi.conj().T @ m @ phi - m
        np.testing.assert_allclose(
            weighted_original,
            delta_m + p_d,
            rtol=2.0e-11,
            atol=3.0e-12,
        )


def test_individual_channel_gramians_and_signed_gains_are_not_identified_by_balance() -> None:
    a, m, _, q1, _, _, packed = _multichannel_witness()
    q2, q1_shifted, q2_shifted = packed
    horizon = 0.7

    channel1 = _problem(a, m, q1)
    channel2 = _problem(a, m, q2)
    channel1_shifted = _problem(a, m, q1_shifted)
    channel2_shifted = _problem(a, m, q2_shifted)

    p1 = np.asarray(accumulated_transport_operator(channel1, horizon))
    p1_shifted = np.asarray(accumulated_transport_operator(channel1_shifted, horizon))
    p2 = np.asarray(accumulated_transport_operator(channel2, horizon))
    p2_shifted = np.asarray(accumulated_transport_operator(channel2_shifted, horizon))

    assert np.linalg.norm(p1_shifted - p1) > 5.0e-2
    assert np.linalg.norm(p2_shifted - p2) > 5.0e-2

    gains1 = np.asarray(accumulated_signed_extrema(channel1, horizon))
    gains1_shifted = np.asarray(accumulated_signed_extrema(channel1_shifted, horizon))
    gains2 = np.asarray(accumulated_signed_extrema(channel2, horizon))
    gains2_shifted = np.asarray(accumulated_signed_extrema(channel2_shifted, horizon))

    assert np.linalg.norm(gains1_shifted - gains1) > 5.0e-2
    assert np.linalg.norm(gains2_shifted - gains2) > 5.0e-2
