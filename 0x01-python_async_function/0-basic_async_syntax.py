#!/usr/bin/env python3
""" This module displays an  asynchronous coroutine """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This function runs an asynchronomous corountine
    Arg:
       integer argument (max_delay, with a default value of 10)
       waits for a random delay between 0 and max_delay
    Return:
        max_delay(float)
    """

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
