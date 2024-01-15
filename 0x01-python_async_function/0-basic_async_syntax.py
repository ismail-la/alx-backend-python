#!/usr/bin/env python3
"""Module for asynchronous tasks using asyncio.
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for some time
    Returns the amount of time waited.
    """
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time
