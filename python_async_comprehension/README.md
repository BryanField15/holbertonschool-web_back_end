# Asynchronous Programming in Python

This repository aims to provide practical understanding and implementation of asynchronous programming in Python. It covers topics such as writing an asynchronous generator, using async comprehensions, and type-annotation for generators.

## Table of Contents
1. [Async Generator](#async-generator)
2. [Async Comprehensions](#async-comprehensions)
3. [Run time for four parallel comprehensions](#run-time-for-four-parallel-comprehensions)

---

## Async Generator
- **Filename:** `0-async_generator.py`

- **Description:**
  The script defines a coroutine called `async_generator` that takes no arguments. This coroutine loops 10 times, asynchronously waiting 1 second each loop, then yields a random number between 0 and 10.

---

## Async Comprehensions
- **Filename:** `1-async_comprehension.py`

- **Description:**
  The script imports `async_generator` from the previous task and defines a coroutine called `async_comprehension`. This coroutine collects 10 random numbers using an async comprehension over `async_generator`, and then returns the 10 random numbers.

---

## Run time for four parallel comprehensions
- **Filename:** `2-measure_runtime.py`

- **Description:**
  This script imports `async_comprehension` from the previous task and defines a coroutine named `measure_runtime`. It executes `async_comprehension` four times in parallel using `asyncio.gather`. The coroutine measures the total runtime and returns it.

Please note that the total runtime is roughly 10 seconds. Make sure to understand why this is the case as part of your learning.
