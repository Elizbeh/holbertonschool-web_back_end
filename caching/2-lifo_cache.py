#!/usr/bin/python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class LIFOCache that inherits
    from BaseCaching and is a
    caching system:
    """
    def __init__(self):
        """calls the parent init"""
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """ Adds an item to the"""

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            """Discard the last item
            put in cache
            """
            last_key = self.insertion_order[-1]
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]
            self.insertion_order.pop()

        self.cache_data[key] = item
        self.insertion_order.append(key)

    def get(self, key):
        """Get an item in the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
