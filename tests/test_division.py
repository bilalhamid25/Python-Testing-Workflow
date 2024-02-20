"""
This module contains unit tests for the `divide` function in the `calculator` package.

"""

from typing import Any
import pytest
from calculator.division import divide

# pylint: disable=invalid-name
@pytest.fixture(
    params=[
        (5, 5, 1),
        (10, 10, 1),
        (25, 5, 5),
        (20, 25, 4 / 5),
    ]
)
def good_inputs(request: pytest.FixtureRequest) -> Any:
    """Returns tuple of values to be tested that will fail. x,y,expected

    Args:
        request (pytest.FixtureRequest): Get values from the fixtures written above

    Returns:
        Any: returns tuples containing 3 values, gets that values from the fixture above
    """
    return request.param


# pylint: disable=redefined-outer-name
def test_division(good_inputs: Any) -> None:
    """
    Tests the `divide` function with different input values.

    Args:
        x: The first number to divide.
        y: The second number to divide.
        expected: The expected result of the division.

    """
    x, y, expected = good_inputs
    result = divide(x, y)
    assert result == expected


@pytest.fixture(
    params=[
        ("hello", 2, TypeError),
        (10, "world", TypeError),
        ("ten", "two", TypeError),
        (10, 0, ZeroDivisionError),
    ]
)
def bad_inputs(request: pytest.FixtureRequest) -> Any:
    """Returns tuple of values to be tested that will fail. x,y,expected

    Args:
        request (pytest.FixtureRequest): Get values from the fixtures written above

    Returns:
        Any: returns tuples containing 3 values, gets that values from the fixture above
    """
    return request.param


def test_division_by_zero(bad_inputs: Any) -> None:
    """
    Tests the `divide` function when the second number is zero.

    """
    x, y, expected_exception = bad_inputs
    with pytest.raises(expected_exception):
        divide(x, y)


@pytest.fixture(
    params=[
        ("345", "24", TypeError),
        ("sdaf", "asf", TypeError),
        ("5", 5, TypeError),
        (5, "433", TypeError),
    ]
)
def bad_input_divide_with_strings(request: pytest.FixtureRequest) -> Any:
    """Returns tuple of mixed values strings or ints to be tested that will fail. x,y,expected

    Args:
        request (pytest.FixtureRequest): Get values from the fixtures written above

    Returns:
        Any: returns tuples containing 3 values, gets that values from the fixture above
    """
    return request.param


def test_division_with_strings(bad_input_divide_with_strings: Any) -> None:
    """
    Tests the `divide` function with string inputs.

    """
    x, y, expected_exception = bad_input_divide_with_strings
    with pytest.raises(expected_exception):
        divide(x, y)
