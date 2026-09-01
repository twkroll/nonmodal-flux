"""Tests for the validated finite-dimensional transport problem container."""

import numpy as np
import pytest

from nonmodal_flux.core.problem import ProblemValidationError, TransportProblem, hermiticity_error


def _base_problem() -> dict[str, np.ndarray]:
    """Return a small valid problem with a genuinely indefinite transport form."""

    return {
        "A": np.array([[-1.0, 2.0], [0.0, -3.0]]),
        "M": np.array([[2.0, 0.25], [0.25, 1.0]]),
        "Q": np.array([[0.0, 1.0], [1.0, 0.0]]),
        "B": np.eye(2),
        "Rin": np.array([[2.0, 0.25], [0.25, 1.0]]),
    }


def test_valid_problem_accepts_indefinite_signed_q() -> None:
    problem = TransportProblem(**_base_problem())

    assert problem.state_dim == 2
    assert problem.input_dim == 2
    np.testing.assert_allclose(np.linalg.eigvalsh(problem.Q), [-1.0, 1.0])


def test_q_is_not_required_to_be_positive_definite() -> None:
    data = _base_problem()
    data["Q"] = np.array([[0.0, 1.0j], [-1.0j, 0.0]])

    problem = TransportProblem(**data)

    assert np.min(np.linalg.eigvalsh(problem.Q)) < 0.0
    assert np.max(np.linalg.eigvalsh(problem.Q)) > 0.0


def test_nonhermitian_q_is_rejected() -> None:
    data = _base_problem()
    data["Q"] = np.array([[0.0, 1.0], [0.0, 0.0]])

    with pytest.raises(ProblemValidationError, match="Q must be Hermitian"):
        TransportProblem(**data)


def test_nonhermitian_m_is_rejected() -> None:
    data = _base_problem()
    data["M"] = np.array([[1.0, 1.0], [0.0, 1.0]])

    with pytest.raises(ProblemValidationError, match="M must be Hermitian"):
        TransportProblem(**data)


def test_non_positive_definite_m_is_rejected() -> None:
    data = _base_problem()
    data["M"] = np.diag([1.0, 0.0])

    with pytest.raises(ProblemValidationError, match="M must be positive definite"):
        TransportProblem(**data)


def test_non_positive_definite_rin_is_rejected() -> None:
    data = _base_problem()
    data["Rin"] = np.diag([1.0, -0.5])

    with pytest.raises(ProblemValidationError, match="Rin must be positive definite"):
        TransportProblem(**data)


@pytest.mark.parametrize(
    ("name", "replacement", "message"),
    [
        ("A", np.zeros((2, 3)), "A must be square"),
        ("M", np.eye(3), "M must have state-space shape"),
        ("Q", np.eye(3), "Q must have state-space shape"),
        ("B", np.ones((3, 1)), "B must have 2 rows"),
        ("Rin", np.eye(3), "Rin must act on admissible input coordinates"),
    ],
)
def test_dimension_mismatches_are_rejected(
    name: str, replacement: np.ndarray, message: str
) -> None:
    data = _base_problem()
    data[name] = replacement

    with pytest.raises(ProblemValidationError, match=message):
        TransportProblem(**data)


def test_nan_or_infinite_entries_are_rejected() -> None:
    data = _base_problem()
    data["A"] = data["A"].copy()
    data["A"][0, 0] = np.nan

    with pytest.raises(ProblemValidationError, match="A contains NaN or infinite entries"):
        TransportProblem(**data)


def test_transport_neutrality_is_a_whole_subspace_condition() -> None:
    data = {
        "A": np.diag([-1.0, -2.0]),
        "M": np.eye(2),
        "Q": np.array([[0.0, 0.5], [0.5, 0.0]]),
        "B": np.array([[1.0], [0.0]]),
        "Rin": np.array([[1.0]]),
    }

    problem = TransportProblem(**data)

    np.testing.assert_allclose(problem.projected_initial_transport(), [[0.0]])
    assert problem.is_transport_neutral()
    assert problem.transport_neutrality_error() == pytest.approx(0.0)


def test_non_neutral_input_space_is_detected_but_not_rejected() -> None:
    problem = TransportProblem(**_base_problem())

    assert not problem.is_transport_neutral()
    assert problem.transport_neutrality_error() > 0.0


def test_natural_energy_input_metric_is_detected() -> None:
    data = _base_problem()
    data["B"] = np.array([[1.0], [2.0]])
    data["Rin"] = data["B"].T @ data["M"] @ data["B"]

    problem = TransportProblem(**data)

    assert problem.uses_natural_energy_input_metric()


def test_general_positive_input_metric_is_allowed() -> None:
    data = _base_problem()
    data["Rin"] = 3.0 * np.eye(2)

    problem = TransportProblem(**data)

    assert not problem.uses_natural_energy_input_metric()


def test_validated_arrays_are_copied_and_read_only() -> None:
    data = _base_problem()
    original_a = data["A"]
    problem = TransportProblem(**data)

    original_a[0, 0] = 99.0
    assert problem.A[0, 0] == pytest.approx(-1.0)
    with pytest.raises(ValueError):
        problem.A[0, 0] = 0.0


def test_hermiticity_error_is_zero_for_hermitian_matrix() -> None:
    matrix = np.array([[1.0, 2.0j], [-2.0j, 3.0]])

    assert hermiticity_error(matrix) == pytest.approx(0.0)
