#!/usr/bin/env python3
"""containing BasicCache module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """defining BasicCache class"""
    def __init__(self):
        """initializing class"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """Return value linked to key"""
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
