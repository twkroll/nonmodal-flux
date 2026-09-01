"""Propagators for finite-dimensional linear dynamics.

The first implementation deliberately covers only the constant-generator case

    x_dot = A x,

for which the exact finite-time propagator is Phi(T) = exp(A T).

This module does not construct metrics or observables; it only advances the
state dynamics supplied by a validated problem definition.
"""

from __future__ import annotations

from numbers import Real

import jax
import jax.numpy as jnp
import jax.scipy.linalg as jsp_linalg

Array = jax.Array


def _validate_time(T: Real) -> float:
    """Validate and return a finite, non-negative propagation horizon."""

    if not isinstance(T, Real):
        raise TypeError(f"T must be a real scalar, got {type(T).__name__}.")
    value = float(T)
    if not jnp.isfinite(value):
        raise ValueError("T must be finite.")
    if value < 0.0:
        raise ValueError(f"T must be non-negative, got {value}.")
    return value


def constant_propagator(A: Array, T: Real) -> Array:
    """Return the exact propagator ``Phi(T) = exp(A T)`` for constant ``A``.

    Parameters
    ----------
    A:
        Square state generator. Real and complex floating-point arrays are
        supported.
    T:
        Finite, non-negative propagation horizon.

    Returns
    -------
    jax.Array
        Matrix exponential ``exp(A*T)`` with the same matrix shape as ``A``.

    Notes
    -----
    The project requires JAX x64 mode for numerical work. The function checks
    this explicitly rather than silently accepting reduced precision.
    """

    if not jax.config.x64_enabled:
        raise RuntimeError(
            "nonmodal-flux requires JAX x64 mode. Set JAX_ENABLE_X64=true "
            "before importing JAX or enable jax_enable_x64 explicitly."
        )

    a = jnp.asarray(A)
    if a.ndim != 2:
        raise ValueError(f"A must be a rank-2 matrix, got shape {a.shape}.")
    if a.shape[0] != a.shape[1]:
        raise ValueError(f"A must be square, got shape {a.shape}.")
    if a.shape[0] == 0:
        raise ValueError("A must have positive dimension.")
    if not jnp.issubdtype(a.dtype, jnp.inexact):
        raise TypeError(
            "A must have a floating-point or complex floating-point dtype; "
            f"got {a.dtype}."
        )
    if not bool(jnp.all(jnp.isfinite(a))):
        raise ValueError("A contains NaN or infinite entries.")

    horizon = _validate_time(T)
    return jsp_linalg.expm(a * horizon)
