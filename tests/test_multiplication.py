"""
This module contains unit tests for the `multiply` function in the `calculator` package.

"""

from typing import Any, Union, Tuple
import pytest
from calculator.multiplication import multiply

# pylint: disable=invalid-name
@pytest.fixture(
    params=[
        (1, 2, 2),
        (3, 4, 12),
        (5, 6, 30),
        (7, 8, 56),
        (9, 10, 90),
        (11, 12, 132),
        (13, 14, 182),
        (15, 16, 240),
        (17, 18, 306),
        (19, 20, 380),
    ],
)
def good_values(request: pytest.FixtureRequest) -> Union[Tuple[int, int, int], Any]:
    """returns 3 values to test the multiply function

    Args:
        request (pytest.FixtureRequest): x,y,expected

    Returns:
        Union[tuple[int, int, int], Any]: returns 3 values to test the multiply function,
        x,y,expected
    """
    return request.param


# pylint: disable=redefined-outer-name
def test_multiply(good_values: Tuple[int, int, int]) -> None:
    """Test multiply function


    Args:
        good_values (tuple[int, int, int]): x,y,expected
    """
    x, y, expected = good_values
    assert multiply(x, y) == expected


@pytest.fixture(
    params=[
        ("5", "5", TypeError),
        (5, "43", TypeError),
        ("43", 765, TypeError),
        ("asdf", "4", TypeError),
        ("764", "dsafa", TypeError),
        ("asdf", "fa", TypeError),
    ]
)
def bad_values(request: pytest.FixtureRequest) -> Union[Tuple[int, int, int], Any]:
    """returns 3 values to test the multiply function

    Args:
        request (pytest.FixtureRequest): x,y,expected

    Returns:
        Union[tuple[int, int, int], Any]: returns 3 values to test the multiply function,
        x,y,expected
    """
    return request.param


def test_multiply_bad_values(bad_values: Any) -> None:
    """Test multiply function with bad values


    Args:
        bad_values (tuple[int, int, int]): x,y,expected
    """
    x, y, exptected_exception = bad_values
    with pytest.raises(exptected_exception):
        multiply(x, y)
