#!/usr/bin/python3
""" Basic dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def put(self, key, item):
        """
         A class BasicCache that
         inherits from BaseCaching
         and is a caching system
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
