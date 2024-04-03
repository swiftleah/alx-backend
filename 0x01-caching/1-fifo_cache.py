#!/usr/bin/python3
''' inherits from BaseCaching '''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' class caching system '''
    def __init__(self):
        '''initialization '''
        super().__init__()

    def put(self, key, item):
        ''' assigns item value for key to dict '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD:", first_key)
        self.cache_data[key] = item

    def get(self, key):
        ''' retrieves value linked to key '''
        return self.cache_data.get(key, None)
