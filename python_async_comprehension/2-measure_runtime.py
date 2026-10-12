#!/usr/bin/env python3
"""Measure the runtime of parallel asynchronous comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Run four asynchronous comprehensions and return their runtime."""
    start = time.perf_counter()

    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())

    return time.perf_counter() - start
