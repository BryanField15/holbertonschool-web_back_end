#!/usr/bin/env python3
"""Module contains type-annotated function sum_list"""
from typing import List
from typing import Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Function that sums a list of floats"""
    return sum(mxd_list)
