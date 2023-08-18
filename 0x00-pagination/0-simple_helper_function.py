#!/usr/bin/env python3
"""module with index_rangefunction"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function returning atuple of  size two"""
    if page < 1 or page_size <= 0:
        pass

    start_index = (page - 1) * page_size
    end_index = (page * page_size)

    return (start_index, end_index)
