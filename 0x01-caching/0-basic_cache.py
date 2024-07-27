#!/usr/bin/python3
"""Basic Cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Class that implements basic cache

    Attributes:
        MAX_ITEMS: number of items that can be store in the cache
    """
    def put(self, key, item):
        """ Add an item in the cache using the key and item
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
