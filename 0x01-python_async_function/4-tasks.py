#!/usr/bin/env python3
""" asynchronous """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ doc """
    lst = []

    for i in range(n):
        lst.append(await wait_random(max_delay))

    return sorted(lst)
