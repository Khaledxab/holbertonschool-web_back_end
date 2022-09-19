#!/usr/bin/env python3
"""
safely_get_value
"""
from typing import Union, Mapping, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default