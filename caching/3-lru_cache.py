#!/usr/bin/python3
""" LRUCache module"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize a LRUCache dictionary"""
        super().__init__()
        self.cache_data = {}
        self.lru_order = []

    def put(self, key, item):
        """Assigns the item value given the key and follows LRU policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_order.pop(0)
            del(self.cache_data[lru_key])
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.lru_order.append(key)

    def get(self, key):
        """Retrieve an item by key and update its position in LRU order"""
        if key is None or key not in self.cache_data:
            return None
        self.lru_order.remove(key)
        self.lru_order.append(key)
        return self.cache_data[key]
