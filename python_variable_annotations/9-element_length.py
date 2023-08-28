#!/usr/bin/env python3
"""Module contains type-annotated function make_multiplier"""
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns a function that multiplies a float"""
    return [(i, len(i)) for i in lst]
