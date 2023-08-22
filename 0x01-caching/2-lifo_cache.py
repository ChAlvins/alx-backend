#!/usr/bin/env python3
"""containing LIFOCache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """defining the class"""
    def __init__(self):
        """initializing class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                newest_key = self.queue.pop()
                self.cache_data.pop(newest_key)
                print('DISCARD: {}\n'.format(newest_key))

            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
