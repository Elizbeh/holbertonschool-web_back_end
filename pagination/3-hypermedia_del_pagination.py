#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert isinstance(index,
                          int) and index >= 0,
        "Index must be a non-negative integer."
        assert isinstance(page_size,
                          int) and page_size > 0,
        "Page size must be a positive integer."

        indexed_dataset = self.indexed_dataset()

        # Verify that the requested index is in a valid range
        assert index < len(indexed_dataset), "Index is out of range."

        # Get the data for the requested page
        data_page = [indexed_dataset[i] for i in range(index,
                     index + page_size) if i in indexed_dataset]

        # Find the next index by iterating over the dataset
        next_index = None
        for i in range(index + page_size, len(indexed_dataset)):
            if i in indexed_dataset:
                next_index = i
                break

        # Update next_index if the current page has deletions
        while next_index is not None and next_index not in indexed_dataset:
            next_index += 1

        hyper_info = {
            'index': index,
            'page_size': len(data_page),
            'data': data_page,
            'next_index': next_index,
        }

        return hyper_info²²
