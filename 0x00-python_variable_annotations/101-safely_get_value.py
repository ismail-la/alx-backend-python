#!/usr/bin/env python3
"""Given the parameters and the return values, add type
annotations to the function

Hint: look into TypeVar
def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""


import typing


T = typing.TypeVar('T')


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[T, None] = None) -> \
        typing.Union[typing.Any, T]:
    """annotations of the function
    This function gets the value for a given key in a mapping, or returns
        a default value if the key is not in the mapping.

    dct (Mapping): The mapping to get the value from.
    key (Any): The key to look up in the mapping.
    default (Union[T, None]): The default value to return if the key is not
        in the mapping.

    Returns:
    Union[Any, T]: The value for the key in the mapping, or the default
        value if the key is not in the mapping.
    """
    if key in dct:
        return dct[key]
    else:
        return default
