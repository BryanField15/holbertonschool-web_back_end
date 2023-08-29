#!/usr/bin/env python3
"""Module that contains a basic asynchronous coroutine"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Async coroutine that measure total execution time for wait_n()"""

    async def measure_time_actual(n: int, max_delay: int) -> float:
        """Actual coroutine to measure time."""
        start_time = time.time()
        await wait_n(n, max_delay)
        end_time = time.time()
        total_time = end_time - start_time
        return (total_time / n)

    return asyncio.run(measure_time_actual(n, max_delay))
