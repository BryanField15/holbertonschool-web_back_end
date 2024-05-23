#!/usr/bin/python3
""" BaseCache module"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize cache dictionary"""
        self.cache_data = {}

    def put(self, key, item):
        """Assigns the item value given the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
    
    def get(self, key):
        """Return a value given the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]