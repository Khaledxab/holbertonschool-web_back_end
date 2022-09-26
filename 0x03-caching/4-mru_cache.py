#!/usr/bin/env python3
"""
MRUCashe
"""
from base_caching import BaseCaching


class MRUCashe(BaseCaching):
    """
    MRUCashe
    Args:
        BaseCaching ([class]): [BaseCaching module]
    """

    def __init__(self):
        """Constructor
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add an item
         in the cache
         """
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(0)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """Get an item by key"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key) or None
