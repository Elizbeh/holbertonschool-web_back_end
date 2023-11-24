#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine called wait_n
    that takes in 2 int arguments
    (in this order): n and max_delay
    Spawn wait_random n times with
    the specified max_delay.wait_n
    return the list of all the delays
    (float values). The list of the
    delays should be in ascending
    order
    """
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
