#!/usr/bin/python3
''' class BasicCache that inherits from BaseCaching '''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' inherits from BaseCaching '''
    def put(self, key, item):
        ''' assigns item value for key to dictionary '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' retrieves value linked to key '''
        return self.cache_data.get(key, None)
