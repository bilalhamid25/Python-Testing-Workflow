"""
This module contains functions for subtracting numbers together.
"""

from typing import Union


# pylint: disable=invalid-name
def subtract(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Subtracts the second number from the first.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The difference between the two numbers.
    """
    if isinstance(x, str) or isinstance(y, str):
        raise TypeError("Both arguments must be numbers.")
    return x - y
