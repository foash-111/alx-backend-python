#!/usr/bin/env python3
"""implement method that create a coroutine and return it"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create task and return it"""
    return asyncio.create_task(wait_random(max_delay))
