#!/usr/bin/env python3
"""Module contains coroutine called async_generator that takes no arguments"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10x, asynchronously wait 1sec,  yield random number"""
    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
