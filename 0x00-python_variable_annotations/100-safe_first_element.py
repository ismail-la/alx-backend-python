#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Duck-typed annotation
    This function returns the first element of a sequence, or None if the
    sequence is empty.

    lst (Sequence): The sequence to process.
    Returns:
    Union[object, None]: The first element of the sequence, or None if the
        sequence is empty."""
    if lst:
        return lst[0]
    else:
        return None
