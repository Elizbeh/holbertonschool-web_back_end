#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    Cache class for storing data in Redis with random keys.
    """
    def __init__(self):
        """
        Initializes the Cache and connects to Redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis with a random key.

        Args:
            data (Union[str, bytes, int, float]):
            The data to be stored in Redis.

        Returns:
            str: The randomly generated key under
            which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, float]:
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(elf, key: str) -> str:
        """
        Retrieves a string from Redis using the provided key.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            str: The retrieved data as a string.
        """"""
        Retrieves a string from Redis using the provided key.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            str: The retrieved data as a string.
        """
        return self.get(fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer from Redis using the provided key.

        Args:
            key (str): The key under which the data is stored in Redis.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(fn)


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
