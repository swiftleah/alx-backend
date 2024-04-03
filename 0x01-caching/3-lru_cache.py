#!/usr/bin/python3
''' 3-lru '''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' inherits from basecaching & is a caching system '''
    def __init__(self):
        ''' initialization '''
        super().__init__()
        self.accessOrder = []

    def put(self, key, item):
        ''' assigns item value to key in dict '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.accessOrder.remove(key)
        self.accessOrder.append(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lruKey = self.accessOrder.pop(0)
            del self.cache_data[lruKey]
            print(f"DISCARD: {lruKey}")

        self.cache_data[key] = item

    def get(self, key):
        ''' retrieves value linked to key '''
        if key is None or key not in self.cache_data:
            return None
        self.accessOrder.remove(key)
        self.accessOrder.append(key)
        return self.cache_data[key]
