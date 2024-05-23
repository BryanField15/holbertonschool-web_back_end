#!/usr/bin/python3
""" LIFOCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize a FIFOcache dictionary"""
        super().__init__()
        self.cache_data = {}
        self.keys = []

    def put(self, key, item):
        """Assigns the item value given the key"""
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.keys.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.keys.pop()
            del(self.cache_data[last_key])
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """Return a value given the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
