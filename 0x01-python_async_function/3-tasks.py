#!/usr/bin/env python3
"""This module returns a asyncio Task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creats an asyncio.Task that waits for random delay

    Args:
        max_delay: int

    Return:
        asyncio.Task
    """

    task = asyncio.create_task(wait_random(max_delay))
    return task
