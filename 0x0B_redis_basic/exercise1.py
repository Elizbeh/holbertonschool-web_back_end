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

    def get(self, key: str, fn: Callable=None
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

    @classmethod
    def count_calls(cls, method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = f"{cls.__name__}.{method.__name__}"  # Use the class and method name as the key
            count = cls._method_call_counts.get(key, 0)  # Get the current count (default to 0)
            count += 1  # Increment the count
            cls._method_call_counts[key] = count  # Update the count
            result = method(self, *args, **kwargs)  # Call the original method
            return result
        return wrapper

if __name__ == "__main__":
    cache = Cache()

    @cache.count_calls
    def custom_method():
        return "Custom Method Called"

    custom_method()  # This call will increment the count for the custom_method key
    custom_method()  # Calling it again will further increment the count
    print("Method Call Counts:", cache._method_call_counts)  # Display the method call counts

