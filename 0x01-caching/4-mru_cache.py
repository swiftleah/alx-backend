#!/usr/bin/env python3
''' class that inherits from basecaching '''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mruKey = self.accessOrder.pop()
            del self.cache_data[mruKey]
            print(f"DISCARD: {mruKey}")
        self.accessOrder.append(key)

        self.cache_data[key] = item

    def get(self, key):
        ''' retrieves value linked to key '''
        if key is None or key not in self.cache_data:
            return None
        self.accessOrder.remove(key)
        self.accessOrder.append(key)
        return self.cache_data[key]
