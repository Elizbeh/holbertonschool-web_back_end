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
        """
        Calls the parent init
        """
        super().__init__()

    def put(self, key, item):
        """
         Assign to the dictionary
         self.cache_data the item
         value for the key key.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            firstInKey = next(iter(self.cache_data))
            del self.cache_data[firstInKey]
            print("DISCARD:", firstInKey)

        self.cache_data[key] = item

    def get(self, key):

        """Return the value
        in self.cache_data linked to
        key."""
        if key is None or key not in self.cache_data:
            return None
