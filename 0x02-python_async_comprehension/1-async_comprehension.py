#!/usr/bin/env python3
"""[async_comprehension]
"""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension
    Returns:
        List[float]: [list of 10 random numbers]
    """
    return [i async for i in async_generator()]
