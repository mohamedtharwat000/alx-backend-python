#!/usr/bin/env python3
""" asynchronous """
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ doc """
    lst = []

    for _ in range(n):
        lst.append(await task_wait_random(max_delay))

    return sorted(lst)
