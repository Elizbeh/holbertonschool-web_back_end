#!/usr/bin/python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    A class FIFOCache that inherits
    from BaseCaching and is a caching
    system:
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            firstInKey = next(iter(self.cache_data))
            del self.cache_data[firstInKey]
            print("DISCARD:", firstInKey)

        self.cache_data[key] = item
