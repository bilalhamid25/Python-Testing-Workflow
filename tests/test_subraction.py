"""
This module contains unit tests for the `subtract` function in the `calculator` package.

"""

from typing import Any
import pytest
from calculator.subtraction import subtract


# pylint: disable=invalid-name
@pytest.fixture(
    params=[
        (5, 3, 2),
        (0, 0, 0),
        (10, 2, 8),
        (-5, -3, -2),
        (-5, 3, -8),
        (5, -3, 8),
        (10, 0, 10),
        (0, 10, -10),
        (10, 10, 0),
        (-10, -10, 0),
        (-10, 10, -20),
        (10, -10, 20),
    ]
)
def good_inputs(request: pytest.FixtureRequest) -> Any:
    """
    Fixture that returns a list of good inputs for the `subtract` function.


    Args:
        request (pytest.FixtureRequest)

    Returns:
        Any: A list of good inputs for the `subtract` function. x,y,expected

    """
    return request.param


# pylint: disable=redefined-outer-name
def test_subtraction(good_inputs: Any) -> None:
    """
    Tests the `subtract` function with different input values.

    Args:
        x: The first number to subtract.
        y: The second number to subtract.
        expected: The expected result of the subtraction.

    """
    x, y, expected = good_inputs
    result = subtract(x, y)
    assert result == expected


@pytest.fixture(
    params=[
        (5, "5", TypeError),
        (5, "5", TypeError),
        (5, "asd", TypeError),
        ("ads", "utre", TypeError),
        ("ads", 5, TypeError),
    ]
)
def bad_inputs(request: pytest.FixtureRequest) -> Any:
    """
    Fixture that returns a list of bad inputs for the `subtract` function.


    Args:
        request (pytest.FixtureRequest)

    Returns:
        Any: A list of bad inputs for the `subtract` function. x,y,expected

    """
    return request.param


def test_subtraction_with_strings(bad_inputs: Any) -> None:
    """
    Tests the `subtract` function with string inputs.

    """
    x, y, expected_exception = bad_inputs
    with pytest.raises(expected_exception):
        subtract(x, y)
