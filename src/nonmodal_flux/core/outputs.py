"""Signed finite-horizon output operators.

This module keeps the physical transport observable separate from the positive
input/energy metrics. It implements the terminal signed-output operator for
constant linear dynamics, its positive-input-metric whitening, and signed
terminal extrema and extremal modes. Reconstruction in physical input
coordinates belongs to a later step.
"""

from __future__ import annotations

from numbers import Real

import jax
import jax.numpy as jnp
import jax.scipy.linalg as jsp_linalg

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
    The result is *not* explicitly symmetrized. Hermiticity should follow from
    the validated Hermiticity of ``Q`` and the algebra itself; tests measure any
    numerical defect rather than hiding it.
    """

    phi = constant_propagator(problem.A, T)
    q = jnp.asarray(problem.Q)
    b = jnp.asarray(problem.B)
    propagated_inputs = phi @ b
    return propagated_inputs.conj().T @ q @ propagated_inputs


def whitened_terminal_signed_output_operator(problem: TransportProblem, T: Real) -> Array:
    """Return the terminal transport operator in unit input-metric coordinates.

    Let

    ``K = B^H Phi(T)^H Q Phi(T) B``

    and factor the positive input metric as ``Rin = L L^H`` with a lower
    Cholesky factor ``L``. The change of variables ``v = L^H u`` turns the
    denominator ``u^H Rin u`` into ``v^H v``. The corresponding Hermitian
    operator is

    ``H = L^{-1} K L^{-H}``.

    The implementation uses triangular solves on both sides and never forms
    ``Rin^{-1}`` or ``L^{-1}`` explicitly.
    """

    operator = terminal_signed_output_operator(problem, T)
    rin = jnp.asarray(problem.Rin)
    lower = jnp.linalg.cholesky(rin)

    left_whitened = jsp_linalg.solve_triangular(lower, operator, lower=True)
    return jsp_linalg.solve_triangular(
        lower,
        left_whitened.conj().T,
        lower=True,
    ).conj().T


def terminal_signed_extrema(problem: TransportProblem, T: Real) -> tuple[Array, Array]:
    """Return the minimum and maximum normalized terminal signed transport.

    The generalized Rayleigh quotient

    ``u^H K_Q^term(T) u / (u^H Rin u)``

    is equivalent, after Cholesky whitening, to the ordinary Rayleigh quotient
    of ``H_Q^term(T)``. Since this matrix is Hermitian, its smallest and largest
    eigenvalues are respectively the most negative and most positive terminal
    signed outputs under unit input cost.

    Returns
    -------
    (jax.Array, jax.Array)
        ``(lambda_min, lambda_max)`` of the whitened terminal operator.

    Notes
    -----
    No eigenvector is returned here, and no optimizer is transformed back to
    physical input coordinates. The operator is also not explicitly
    symmetrized before calling ``eigvalsh``; any loss of Hermiticity should be
    exposed by validation tests rather than silently hidden.
    """

    operator = whitened_terminal_signed_output_operator(problem, T)
    eigenvalues = jnp.linalg.eigvalsh(operator)
    return eigenvalues[0], eigenvalues[-1]


def terminal_signed_extremal_modes(
    problem: TransportProblem,
    T: Real,
) -> tuple[Array, Array, Array, Array]:
    """Return signed terminal extrema and their whitened extremal modes.

    If ``H_Q^term(T)`` denotes the Cholesky-whitened terminal operator, this
    function solves the Hermitian eigenproblem

    ``H_Q^term(T) v = lambda v``

    and returns the modes associated with its smallest and largest eigenvalues.
    The eigenvectors are represented in the Euclidean, whitened coordinates
    ``v = L^H u`` and therefore have unit Euclidean norm.

    Returns
    -------
    (jax.Array, jax.Array, jax.Array, jax.Array)
        ``(lambda_min, v_min, lambda_max, v_max)``. The vectors ``v_min`` and
        ``v_max`` are normalized eigenvectors in whitened input coordinates.

    Notes
    -----
    Eigenvector phase is arbitrary. If an extremal eigenvalue is degenerate,
    the returned vector is one orthonormal representative of the corresponding
    eigenspace and should not be interpreted as a unique optimizer. No
    transformation back to physical input coordinates is performed here.
    """

    operator = whitened_terminal_signed_output_operator(problem, T)
    eigenvalues, eigenvectors = jnp.linalg.eigh(operator)
    return (
        eigenvalues[0],
        eigenvectors[:, 0],
        eigenvalues[-1],
        eigenvectors[:, -1],
    )
