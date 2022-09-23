#!/usr/bin/env python3
""" BasicCache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        """ PUT """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ GET """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
