"""
This module contains functions for multiplying numbers together.
"""

from typing import Union

# pylint: disable=invalid-name
def multiply(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """Multiplies the two numbers together.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The product of the two numbers.
    """
    if isinstance(x, str) or isinstance(y, str):
        raise TypeError("Both arguments must be numbers.")
    return x * y
