#!/usr/bin/env python3
"""
async_generator
"""

from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """async_generator"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
