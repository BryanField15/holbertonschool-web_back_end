#!/usr/bin/env python3
"""Module that contains index_range function"""

import csv
import math
from typing import List, Dict, Any


def index_range(page, page_size):
    """Returns a tuple of size two containing a start index and an end index"""
    start_index = ((page - 1) * page_size)
    end_index = (page * page_size)
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the entries from the requested page in the dataset"""
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[int, Any]:
        """Returns a dictionary of hypermedia pagination info"""
        assert (isinstance(page, int) and page > 0)
        assert (isinstance(page_size, int) and page_size > 0)

        data = self.get_page(page, page_size)
        total_items = len(self.dataset())

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if (page * page_size) < total_items else None
        total_pages = (math.ceil(total_items / page_size)
                       if page_size > 0 else 0)

        hype_dict = {
                "page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages,
                }

        return hype_dict
