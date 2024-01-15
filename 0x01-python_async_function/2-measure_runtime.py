#!/usr/bin/env python3
"""
Module for measuring the time it takes to run a given number of
asynchronous tasks concurrently
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns total execution time"""

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return (total_time/n)
