"""
This module contains unit tests for the `add` function in the `calculator` package.

"""

from typing import Any, Union
import pytest
from calculator.addition import add


# pylint: disable=invalid-name
@pytest.mark.parametrize(
    "x,y,expected",
    [
        (5, 5, 10),
        (10, 10, 20),
        (25, 5, 30),
        (1000000, 500000, 1500000),
        (-10, -10, -20),
        (-10, 10, 0),
        (10, -10, 0),
        (-1000000, -500000, -1500000),
        (-1000000, 500000, -500000),
        (1000000, -500000, 500000),
        (-50, 40, -10),
        (50, -40, 10),
        (-50, -40, -90),
        (50, 40, 90),
    ],
)
def test_add(
    x: Union[int, float], y: Union[int, float], expected: Union[int, float]
) -> None:
    """
    Fixture that returns a list of good inputs for the `subtract` function.


    Args:
        request (pytest.FixtureRequest)

    Returns:
        Any: A list of good inputs for the `subtract` function. x,y,expected

    """
    assert add(x, y) == expected


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
    Fixture that returns a list of bad inputs for the `addition` function.


    Args:
        request (pytest.FixtureRequest)

    Returns:
        Any: A list of bad inputs for the `subtract` function. x,y,expected

    """
    return request.param


# pylint: disable=redefined-outer-name
def test_addition_bad_inputs(bad_inputs: Any) -> None:
    """Test that the `add` function raises an error when given bad inputs.


    Args:
        bad_inputs (Any): A list of bad inputs for the `subtract` function.

    Returns:
        None

    """
    x, y, expected = bad_inputs
    with pytest.raises(expected):
        add(x, y)
