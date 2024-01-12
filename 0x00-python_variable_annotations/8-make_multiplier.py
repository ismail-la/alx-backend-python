#!/usr/bin/env python3
""" a type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """This function takes a float as an argument and
    Returns a function that multiplies a float by multiplier
    """
    def float_multiply(x: float) -> float:
        """
        This function multiplies a float by the multiplier.

        n (float): The float to multiply by the multiplier.

        Returns:
        float: The result of multiplying n by the multiplier.
        """
        return multiplier * x
    return float_multiply
