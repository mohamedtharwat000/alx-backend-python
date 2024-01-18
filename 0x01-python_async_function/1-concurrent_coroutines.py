#!/usr/bin/env python3
""" asynchronous """
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ doc """
    _list = []

    for _ in range(n):
        _list.append(await wait_random(max_delay))

    return sorted(_list)
