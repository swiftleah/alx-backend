#!/usr/bin/python3
''' inherits from BaseCaching '''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' class caching system '''
    def __init__(self):
        '''initialization '''
        super().__init__()

    def put(self, key, item):
        ''' assigns item value for key to dict
        and discards LIFO key '''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print("DISCARD:", last_key)
        self.cache_data[key] = item

    def get(self, key):
        ''' retrieves value linked to key '''
        return self.cache_data.get(key, None)
