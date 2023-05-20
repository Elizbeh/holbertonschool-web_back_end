#!/usr/bin/env python3
"""Async Comprehensions"""

from typing import List, Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float]:
    """
    The coroutine will collect 10
    random numbers using an async
    comprehensing over
    async_generator, then return
    the 10 random numbers.
    """
    collected_numbers = [i async for i in async_generator()]
    return collected_numbers
