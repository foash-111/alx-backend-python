#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
"""wait_random n times"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of length n, filled by max_delay range"""
    my_list = [wait_random(max_delay) for x in range(n)]
    result = await asyncio.gather(*my_list)
    return result
