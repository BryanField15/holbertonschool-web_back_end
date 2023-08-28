#!/usr/bin/env python3
"""Module contains type-annotated function to_kv"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function that makes tuple from a string and a float"""
    new_tuple: Tuple[str, float] = (k, v ** 2)
    return new_tuple
