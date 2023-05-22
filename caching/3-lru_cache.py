#!/usr/bin/python3
"""LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A class LRUCache that inherits
    from BaseCaching
     """
    def __init__(self):
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        if key is None or item is None:
            return

        if key in self.cache_data:
            """ Update usage order if
            key already exists"""
            self.usage_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            """ Discard the least
            recently used ite"""
            least_used = self.usage_order.pop(0)
            del self.cache_data[least_used]
            print("DISCARD: {}".format(least_used))

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        """ Update usage order when
        key is accessed"""
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
