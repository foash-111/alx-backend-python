#!/usr/bin/env python3
"""wait_random n times"""

import asyncio
from typing import List
from time import perf_counter
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of length n, filled by max_delay range"""
    # start = perf_counter()
    my_list = [task_wait_random(max_delay) for x in range(n)]
    result = await asyncio.gather(*my_list)
    # end = perf_counter()
    # print(end - start)
    return result
