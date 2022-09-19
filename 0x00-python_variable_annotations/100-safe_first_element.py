#!/usr/bin/env python3
"""sage first element"""
from typing import Sequence, Any, Union


def safe_first_element(lst):
    """safe_first_element"""
    if lst:
        return lst[0]
    else:
        return None
