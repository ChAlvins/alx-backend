#!/usr/bin/env python3
"""containing FIFICache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """defining the lass"""
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
            cache_length = len(self.cache_data)
            base_items = BaseCaching.MAX_ITEMS
            if cache_length >= base_items and key not in self.cache_data:
                oldest_key = self.queue.pop(0)
                self.cache_data.pop(oldest_key)
                print('DISCARD: {}\n'.format(oldest_key))

            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """return value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
