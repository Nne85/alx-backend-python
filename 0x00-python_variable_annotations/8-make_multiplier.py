#!/usr/bin/env python3
""" this module takes a float multiplier as argument and returns a
function that multiplies a float by multiplier."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use in the returned function.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the product with the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
