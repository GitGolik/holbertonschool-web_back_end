#!/usr/bin/env python3
"""execute multiple random delays"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return random delays in ASC order"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
