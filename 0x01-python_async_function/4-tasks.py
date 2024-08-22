#!/usr/bin/env python3
"""wait_random n times"""

import asyncio
from typing import Callable
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> Callable:
    """return a list of length n, filled by max_delay range"""
    my_list = [wait_random(max_delay) for x in range(n)]
    result = await asyncio.gather(*my_list)
    return result
