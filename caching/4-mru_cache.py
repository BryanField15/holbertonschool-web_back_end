#!/usr/bin/python3
""" MRUCache module"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize a LRUCache dictionary"""
        super().__init__()
        self.cache_data = {}
        self.mru_order = []

    def put(self, key, item):
        """Assigns the item value given the key and follows LRU policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.mru_order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.mru_order.pop()
            del(self.cache_data[mru_key])
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.mru_order.append(key)

    def get(self, key):
        """Retrieve an item by key and update its position in LRU order"""
        if key is None or key not in self.cache_data:
            return None
        self.mru_order.remove(key)
        self.mru_order.append(key)
        return self.cache_data[key]
