#!/usr/bin/env python3
"""Module contains type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function that returns a function that multiplies a float"""
    def mul_func(n: float) -> float:
        return n * multiplier

    return mul_func
