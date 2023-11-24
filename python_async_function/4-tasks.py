#!/usr/bin/env python3
"""Task: Execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    An async routine called task_wait_n
    that takes in 2 int arguments
    (in this order): n and max_delay
    Spawn task_wait_random n times with
    the specified max_delay
    return the list of all the delays
    (float values). The list of the
    delays should be in ascending
    order
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
