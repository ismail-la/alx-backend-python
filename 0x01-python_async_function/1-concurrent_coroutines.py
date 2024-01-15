#!/usr/bin/env python3
"""Module for asynchronous tasks using asyncio.
"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times
    Returns a list of the wait times, sorted in ascending order.
    """
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay_times)
