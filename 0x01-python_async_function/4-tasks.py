#!/usr/bin/env python3
"""This module creates a task by altering another function"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function returns task_wait_random
    """
    list_of_random_num = []
    for i in range(n):
        list_of_random_num.append(await task_wait_random(max_delay))
    return sorted(list_of_random_num)
