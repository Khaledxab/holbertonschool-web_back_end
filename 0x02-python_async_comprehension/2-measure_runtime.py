#!/usr/bin/env python3
"""
measure_runtime
"""

from typing import List
from time import perf_counter
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime
    Returns:
        float: [total time]
    """
    start = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = perf_counter()
    return end - start
