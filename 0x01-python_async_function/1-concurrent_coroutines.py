# /usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays """
    delays = [await wait_random(max_delay) for i in range(n)]
    return sorted(delays)
