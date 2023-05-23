#!/usr/bin/python3
"""MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    A class MRUCache that inherits
    from BaseCaching
    """
    def __init__(self):
        """Calls the parent init"""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """Update usage order if
        exist and discard the most
        recentely used item"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_data = self.usage_order.pop()
            del self.cache_data[mru_data]
            print("DISCARD: {}".format(mru_data))

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """Update usage order when
        key is accesed"""
        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
