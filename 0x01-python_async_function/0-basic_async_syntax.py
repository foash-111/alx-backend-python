#!/usr/bin/env python3

"""
'asyncio'
Imagine you are playing a video game,
but you also have to wait for your favorite cartoon to start.
While you are waiting, you keep playing the game.
When the cartoon starts, you pause the game and start watching.
"Async" is like playing the game while waiting for the cartoon,
and "await" is when you stop the game because the cartoon has started.
"""

import random
import asyncio


# ValueError: a coroutine was expected, got 0.8911870374978059
# def wait_random(max_delay = 10):

async def wait_random(max_delay: int = 10) -> float:
    """using random with await async.sleep()"""
    # delay = await random.uniform(0, max_delay)
    # TypeError: object float can't be used in 'await' expression
    delay = random.uniform(0, max_delay)
    # asyncio.sleep(delay)
    # RuntimeWarning: coroutine 'sleep' was never awaited asyncio.sleep(delay)
    await asyncio.sleep(delay)
    return delay
