#!/usr/bin/env python3
"""
Main file
"""

import csv
import math
from typing import List


class Server:
    """Server Class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Returns a dictionary containing information about the dataset page
        and pagination details.
        """"""
        Returns a dictionary containing information about the dataset page
        and pagination details.
        """

        total_items = 1000
        total_pages = math.ceil(total_items / page_size)
        if page < 1 or page > total_pages:
            return (0, 0)
        start_index = (page - 1) * page_size
        end_index = min(start_index + page_size, total_items)
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a specific page
        from the dataset based on
        the given pagination
        parameters.
        """
        start_index, end_index = self.index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing information about the dataset page
        and pagination details.
        """
        assert isinstance(page,
                          int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size,
                          int) and page_size > 0, "Must be a positive int."

        data_page = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hyper_info = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
        return hyper_info
