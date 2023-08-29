#!/usr/bin/env python3
import asyncio
import random
from typing import Generator

async def async_generator() -> float:
    for n in range(10):
        yield random.random()
