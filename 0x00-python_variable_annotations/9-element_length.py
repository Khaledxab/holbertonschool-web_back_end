#!/usr/bin/env python3
"""Let's duck type an iterable object"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length"""
    return [(i, len(i)) for i in lst]
