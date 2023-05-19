#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
from typing import List
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure_time: function
    args: n and max_delay "int"
    wait-n(n, mas_delay): total
    execution time measurement.
    Returns: total_time / n "float"
    """
    start_time = perf_counter()
    asyncio.run(wait_n(n, max_delay)
)
    end_time = perf_counter()
    total_time = end_time - start_time
    return total_time / n
