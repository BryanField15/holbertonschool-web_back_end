#!/usr/bin/env python3
"""Module contains type-annotated function element_lenght"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that returns an elements length"""
    return [(i, len(i)) for i in lst]
