#!/usr/bin/env python3
"""Annotate the below function’s parameters and return
values with the appropriate types.
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """This function takes a list of strings and returns a list of tuples,
    where each tuple contains a string and the length of that string.
    """
    return [(i, len(i)) for i in lst]
