#!/usr/bin/env python3
"""provide an asynchronous generator of random float numbers"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """get 10 random floats from 0 to 10 async"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
