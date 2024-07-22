#!/usr/bin/env python3
"""
 Model that defines index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    Args:
        page (int): Current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): Start and end index for the given page
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
