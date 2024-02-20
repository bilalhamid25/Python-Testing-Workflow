"""
This module contains functions for dividing numbers together.
"""

from typing import Union

# pylint: disable=invalid-name
def divide(
    x: Union[int, float], y: Union[int, float]
) -> Union[Union[int, float], ZeroDivisionError, TypeError]:
    """Divides the first number by the second.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The quotient of the two numbers.

    Raises:
        ZeroDivisionError: If the second number is zero.
    """
    # check if any of the two given number are string, if yes then raise a type error
    if isinstance(x, str) or isinstance(y, str):
        raise TypeError("Cannot divide a string.")

    if y != 0:
        return x / y
    raise ZeroDivisionError("Cannot divide by zero.")
