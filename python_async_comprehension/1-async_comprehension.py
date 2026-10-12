#!/usr/bin/env python3
"""collect random numbers with async comprehension"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return ten random floats collected in async"""
    return [number async for number in async_generator()]
