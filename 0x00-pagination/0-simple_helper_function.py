#!/usr/bin/env python3
''' takes 2 int args and returns tuple containing start index
and end index corresponding to range of indexes to return in a list'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' func '''
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
