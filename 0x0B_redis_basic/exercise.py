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
            key (str): The key under which the data is
            stored in Redis.

        Returns:
            str: The retrieved data as a string.
        """
        return self.get(fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer from Redis using the
        provided key.

        Args:
            key (str): The key under which the data is
            stored in Redis.

        Returns:
            int: The retrieved data as an integer.
        """
        return self.get(fn)


def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts how many times
    a method of the Cache class is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__name__
        count_key = f"call_count:{key}"
        self._redis.incr(count_key)
        return method(self, *args, **kwargs)

    return wrapper


Cache.store = count_calls(Cache.store)


def call_history(method: Callable) -> Callable:
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, result)
        return result
    return wrapper


Cache.store = call_history(Cache.store)


def replay(method: Callable):
    """
    Display the history of calls for a particular function.

    Args:
        method (Callable): The function for which
        to display the history.
    """

    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    # Retrieve input and output lists from Redis
    inputs = cache._redis.lrange(input_key, 0, -1)
    outputs = cache._redis.lrange(output_key, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)}
          times: ")


replay(cache.store)
