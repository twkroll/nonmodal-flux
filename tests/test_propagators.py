"""Tests for constant finite-dimensional propagators."""

import jax
import jax.numpy as jnp
import numpy as np
import pytest

from nonmodal_flux.core.propagators import constant_propagator


def test_zero_horizon_returns_identity() -> None:
    A = jnp.array([[-1.0, 2.0], [0.0, -3.0]], dtype=jnp.float64)

    Phi = constant_propagator(A, 0.0)

    np.testing.assert_allclose(np.asarray(Phi), np.eye(2), rtol=0.0, atol=1.0e-14)


def test_diagonal_generator_matches_scalar_exponentials() -> None:
    A = jnp.diag(jnp.array([-1.0, -2.5, 0.25], dtype=jnp.float64))
    T = 0.7

    Phi = constant_propagator(A, T)
    expected = np.diag(np.exp(np.array([-1.0, -2.5, 0.25]) * T))

    np.testing.assert_allclose(np.asarray(Phi), expected, rtol=1.0e-12, atol=1.0e-14)


def test_complex_generator_is_supported() -> None:
    eigenvalues = jnp.array([-1.0 + 2.0j, -0.5 - 0.75j], dtype=jnp.complex128)
    A = jnp.diag(eigenvalues)
    T = 0.4

    Phi = constant_propagator(A, T)
    expected = np.diag(np.exp(np.asarray(eigenvalues) * T))

    np.testing.assert_allclose(np.asarray(Phi), expected, rtol=1.0e-12, atol=1.0e-14)


def test_semigroup_property() -> None:
    A = jnp.array([[-1.0, 4.0], [-0.5, -2.0]], dtype=jnp.float64)
    t = 0.31
    s = 0.47

    lhs = constant_propagator(A, t + s)
    rhs = constant_propagator(A, t) @ constant_propagator(A, s)

    np.testing.assert_allclose(np.asarray(lhs), np.asarray(rhs), rtol=2.0e-12, atol=2.0e-14)


def test_output_preserves_shape_and_inexact_dtype() -> None:
    A = jnp.array([[-1.0, 1.0], [0.0, -2.0]], dtype=jnp.float64)

    Phi = constant_propagator(A, 0.2)

    assert Phi.shape == A.shape
    assert jnp.issubdtype(Phi.dtype, jnp.inexact)
    assert Phi.dtype == jnp.float64


@pytest.mark.parametrize("T", [-1.0e-6, -2.0])
def test_negative_horizon_is_rejected(T: float) -> None:
    A = jnp.eye(2, dtype=jnp.float64)

    with pytest.raises(ValueError, match="T must be non-negative"):
        constant_propagator(A, T)


@pytest.mark.parametrize("T", [np.inf, -np.inf, np.nan])
def test_nonfinite_horizon_is_rejected(T: float) -> None:
    A = jnp.eye(2, dtype=jnp.float64)

    with pytest.raises(ValueError, match="T must be finite"):
        constant_propagator(A, T)


def test_nonreal_horizon_is_rejected() -> None:
    A = jnp.eye(2, dtype=jnp.float64)

    with pytest.raises(TypeError, match="T must be a real scalar"):
        constant_propagator(A, 1.0 + 0.0j)


def test_rank_one_generator_is_rejected() -> None:
    with pytest.raises(ValueError, match="A must be a rank-2 matrix"):
        constant_propagator(jnp.array([1.0, 2.0], dtype=jnp.float64), 0.1)


def test_nonsquare_generator_is_rejected() -> None:
    with pytest.raises(ValueError, match="A must be square"):
        constant_propagator(jnp.ones((2, 3), dtype=jnp.float64), 0.1)


def test_integer_generator_is_rejected() -> None:
    with pytest.raises(TypeError, match="floating-point or complex floating-point dtype"):
        constant_propagator(jnp.eye(2, dtype=jnp.int64), 0.1)


def test_nonfinite_generator_is_rejected() -> None:
    A = jnp.array([[-1.0, jnp.nan], [0.0, -2.0]], dtype=jnp.float64)

    with pytest.raises(ValueError, match="A contains NaN or infinite entries"):
        constant_propagator(A, 0.1)


def test_test_environment_really_has_x64_enabled() -> None:
    assert jax.config.x64_enabled
