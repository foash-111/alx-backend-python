#!/usr/bin/env python3
"""
time module
time.perf.counter() to measure performance
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """run a coroutine and calc how much time does it take"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = (end - start) / n
    return total_time
