"""Validated data container for transport-optimal nonmodal problems.

This module deliberately validates *given* physical objects; it never invents or
renormalizes an energy metric or transport observable. In particular, ``M`` and
``Q`` must already have been derived from the underlying physics according to
project decision D5.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

ArrayLike = npt.ArrayLike
NDArray = npt.NDArray[np.floating | np.complexfloating]


class ProblemValidationError(ValueError):
    """Raised when a mathematical invariant of a transport problem is violated."""


def hermiticity_error(matrix: ArrayLike) -> float:
    """Return the relative Frobenius-norm Hermiticity defect.

    The denominator is bounded below by one so that the diagnostic remains
    meaningful for a zero matrix.
    """

    a = np.asarray(matrix)
    if a.ndim != 2:
        raise ProblemValidationError("Hermiticity is defined here only for matrices.")
    defect = np.linalg.norm(a - a.conj().T, ord="fro")
    scale = max(1.0, float(np.linalg.norm(a, ord="fro")))
    return float(defect / scale)


def _as_numeric_matrix(name: str, value: ArrayLike) -> NDArray:
    array = np.asarray(value)
    if array.ndim != 2:
        raise ProblemValidationError(f"{name} must be a rank-2 matrix, got shape {array.shape}.")
    if not np.issubdtype(array.dtype, np.number):
        raise ProblemValidationError(f"{name} must have a numeric dtype, got {array.dtype}.")
    if not np.all(np.isfinite(array)):
        raise ProblemValidationError(f"{name} contains NaN or infinite entries.")
    return array


def _require_hermitian(name: str, matrix: NDArray, *, rtol: float, atol: float) -> None:
    if not np.allclose(matrix, matrix.conj().T, rtol=rtol, atol=atol):
        err = hermiticity_error(matrix)
        raise ProblemValidationError(f"{name} must be Hermitian; relative defect is {err:.3e}.")


def _require_positive_definite(name: str, matrix: NDArray, *, atol: float) -> None:
    # Hermiticity is checked separately, so eigvalsh is the appropriate diagnostic.
    eigenvalues = np.linalg.eigvalsh(matrix)
    minimum = float(np.min(eigenvalues))
    if minimum <= atol:
        raise ProblemValidationError(
            f"{name} must be positive definite; smallest eigenvalue is {minimum:.3e}."
        )


@dataclass(frozen=True, slots=True)
class TransportProblem:
    """Finite-dimensional initial-condition transport optimization problem.

    Parameters
    ----------
    A:
        State generator in ``x_dot = A x``.
    M:
        Positive-definite physical energy/free-energy metric.
    Q:
        Hermitian signed transport form. It may be indefinite.
    B:
        Map from admissible input coordinates ``u`` to ``x(0) = B u``.
    Rin:
        Positive-definite metric/cost on the admissible input coordinates.

    Notes
    -----
    No relation such as ``Rin = B^H M B`` is imposed: that natural-energy choice
    is important in several theorems but is not part of the general formulation.
    Likewise, transport neutrality ``B^H Q B = 0`` is an optional physical input
    restriction, not a universal requirement.
    """

    A: NDArray
    M: NDArray
    Q: NDArray
    B: NDArray
    Rin: NDArray
    rtol: float = 1.0e-10
    atol: float = 1.0e-12

    def __post_init__(self) -> None:
        arrays = {
            name: _as_numeric_matrix(name, value)
            for name, value in {
                "A": self.A,
                "M": self.M,
                "Q": self.Q,
                "B": self.B,
                "Rin": self.Rin,
            }.items()
        }

        a, m, q, b, rin = (arrays[name] for name in ("A", "M", "Q", "B", "Rin"))

        if a.shape[0] != a.shape[1]:
            raise ProblemValidationError(f"A must be square, got shape {a.shape}.")
        n = a.shape[0]
        if n == 0:
            raise ProblemValidationError("The state dimension must be positive.")

        for name, matrix in (("M", m), ("Q", q)):
            if matrix.shape != (n, n):
                raise ProblemValidationError(
                    f"{name} must have state-space shape {(n, n)}, got {matrix.shape}."
                )

        if b.shape[0] != n:
            raise ProblemValidationError(
                f"B must have {n} rows to map into the state space, got {b.shape}."
            )
        input_dim = b.shape[1]
        if input_dim == 0:
            raise ProblemValidationError("The admissible input dimension must be positive.")
        if rin.shape != (input_dim, input_dim):
            raise ProblemValidationError(
                "Rin must act on admissible input coordinates; "
                f"expected {(input_dim, input_dim)}, got {rin.shape}."
            )

        _require_hermitian("M", m, rtol=self.rtol, atol=self.atol)
        _require_hermitian("Q", q, rtol=self.rtol, atol=self.atol)
        _require_hermitian("Rin", rin, rtol=self.rtol, atol=self.atol)
        _require_positive_definite("M", m, atol=self.atol)
        _require_positive_definite("Rin", rin, atol=self.atol)

        # Freeze canonical ndarray views so downstream code receives validated objects.
        for name, array in arrays.items():
            canonical = np.array(array, copy=True)
            canonical.setflags(write=False)
            object.__setattr__(self, name, canonical)

    @property
    def state_dim(self) -> int:
        """Number of dynamical state variables."""

        return int(self.A.shape[0])

    @property
    def input_dim(self) -> int:
        """Number of admissible input coordinates."""

        return int(self.B.shape[1])

    def projected_initial_transport(self) -> NDArray:
        """Return ``B^H Q B`` without modifying or symmetrizing it."""

        return self.B.conj().T @ self.Q @ self.B

    def transport_neutrality_error(self) -> float:
        """Return ``||B^H Q B||_F`` normalized by physical matrix scales."""

        projected = self.projected_initial_transport()
        scale = max(
            1.0,
            float(np.linalg.norm(self.B, ord=2) ** 2 * np.linalg.norm(self.Q, ord=2)),
        )
        return float(np.linalg.norm(projected, ord="fro") / scale)

    def is_transport_neutral(self) -> bool:
        """Test the whole admissible subspace condition ``B^H Q B = 0``."""

        projected = self.projected_initial_transport()
        return bool(np.allclose(projected, 0.0, rtol=self.rtol, atol=self.atol))

    def uses_natural_energy_input_metric(self) -> bool:
        """Test whether ``Rin`` equals the restricted physical energy ``B^H M B``."""

        restricted_energy = self.B.conj().T @ self.M @ self.B
        return bool(np.allclose(self.Rin, restricted_energy, rtol=self.rtol, atol=self.atol))
