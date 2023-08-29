#!/usr/bin/env python3
"""Module that contains a basic asynchronous coroutine"""
import asyncio
from typing import List


async def wait_n(n: int , max_delay: int) -> List[float]:
    """Async coroutine spawns wait_random n times with specified max_delay."""
    list_of_all_delays = []
    wait_random = __import__('0-basic_async_syntax').wait_random
    for count in range(n):
        delay = await wait_random(max_delay)
        list_of_all_delays.append(delay)
    return sorted(list_of_all_delays)
