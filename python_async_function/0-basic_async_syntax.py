#!/usr/bin/env python3
"""module for simple delay"""


import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """create a delay based on 0 to max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
