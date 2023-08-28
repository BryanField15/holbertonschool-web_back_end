#!/usr/bin/env python3
"""Module contains type-annotated function sum_list"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Function that sums a list of floats"""
    return sum(input_list)
