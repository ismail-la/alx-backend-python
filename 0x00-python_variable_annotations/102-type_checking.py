#!/usr/bin/env python3
"""Use mypy to validate the following piece of code
and apply any necessary changes.
This is a module that provides a function for zooming in on a tuple.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Corrected annotations
    This function takes a tuple and a zoom factor, and returns a new list
        with the elements of the tuple repeated according to the zoom factor.

    lst (Tuple): The tuple to zoom in on.
    factor (int): The zoom factor, which determines how many times each
        element of the tuple should be repeated in the output list.

    Returns:
    List: A new list with the elements of the tuple repeated according to
        the zoom factor.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
