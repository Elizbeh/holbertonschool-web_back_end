#!/usr/bin/env python3
"""
Writing strings to Redis
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


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

    def get_str(self, key: str) -> str:
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


def count_calls(method: Callable) -> Callable:
    """ Count how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """ Wrapper method """
        self._redis.incr(key)
        return method(self, *args)
    return wrapper

def call_history(method: Callable) -> Callable:
    """ Store history of inputs and outputs into list """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args) -> Any:
        """ Wrapper method """
        input_data = args
        output_data = method(self, *args)
        self._redis.rpush(key + ":inputs", str(input_data))
        self._redis.rpush(key + ":outputs", str(output_data))
        return output_data

    return wrapper
