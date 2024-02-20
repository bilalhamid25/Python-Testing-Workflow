"""
This module contains functions for adding numbers together.
"""

from typing import Union


# pylint: disable=invalid-name
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Adds two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of the two numbers.
    """
    if isinstance(x, str) or isinstance(y, str):
        raise TypeError("Both arguments must be numbers.")
    return x + y
