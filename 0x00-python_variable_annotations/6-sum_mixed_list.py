#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """This function computes the sum of a list of integers and floats, and
    Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
