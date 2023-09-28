#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Function returns a tuple of start
    and end indexes for pagination.

    Args:
    page (int): The current page
    number.

    page_size (int): Number of items
    per page.

    Returns:
    tuple: A tuple containing the
    start and end indexes.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
