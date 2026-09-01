"""Signed finite-horizon output operators.

This module keeps the physical transport observable separate from the positive
input/energy metrics.  It currently implements only the terminal signed-output
operator for constant linear dynamics; whitening and eigenvalue optimization
belong to later steps.
"""

from __future__ import annotations

from numbers import Real

import jax
import jax.numpy as jnp

from nonmodal_flux.core.problem import TransportProblem
from nonmodal_flux.core.propagators import constant_propagator

Array = jax.Array


def terminal_signed_output_operator(problem: TransportProblem, T: Real) -> Array:
    """Return the admissible-input terminal transport operator.

    For ``x_dot = A x`` and ``x(0) = B u``, the terminal signed transport is

    ``q(T; u) = u^H K_Q^term(T) u``

    with

    ``K_Q^term(T) = B^H Phi(T)^H Q Phi(T) B``.

    Parameters
    ----------
    problem:
        Validated transport problem containing ``A``, ``Q``, and ``B``.
    T:
        Finite, non-negative terminal horizon. Validation is delegated to the
        constant propagator.

    Returns
    -------
    jax.Array
        The raw Hermitian input-space operator before any ``Rin`` whitening.

    Notes
    -----
    The result is *not* explicitly symmetrized.  Hermiticity should follow from
    the validated Hermiticity of ``Q`` and the algebra itself; later tests will
    measure any numerical defect rather than hiding it.
    """

    phi = constant_propagator(problem.A, T)
    q = jnp.asarray(problem.Q)
    b = jnp.asarray(problem.B)
    propagated_inputs = phi @ b
    return propagated_inputs.conj().T @ q @ propagated_inputs
