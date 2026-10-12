#!/usr/bin/env python3
"""create an asyncio task of random delay"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create and return a task wait_random in run"""
    return asyncio.create_task(wait_random(max_delay))
