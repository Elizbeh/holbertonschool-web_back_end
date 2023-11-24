#!/usr/bin/env python3
"""Tasks with the regular function syntax"""

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    A function that takes an integer
    max_delay and returns a
    asyncio.Task
    """
    task = create_task(wait_random(max_delay))
    return task
