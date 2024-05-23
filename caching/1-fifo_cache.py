#!/usr/bin/python3
""" FIFOCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize a FIFOcache dictionary"""
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Assigns the item value given the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            head = next(iter(self.cache_data))
            del(self.cache_data[head])
            print(f"DISCARD: {head}")

    def get(self, key):
        """Return a value given the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
