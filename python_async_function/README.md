## Asynchronous Programming in Python

This project aims to explore asynchronous programming in Python using the `asyncio` library. By the end of this project, I have gained a solid understanding of the `async` and `await` syntax, learned how to execute asynchronous programs using `asyncio`, discovered how to run concurrent coroutines, and became adept at creating `asyncio` tasks. Additionally, I explored using the `random` module to introduce time delays in asynchronous functions.

---

### What I Learned

I've learned how to:

- Use `async` and `await` syntax to write asynchronous code.
- Execute an asynchronous program using `asyncio.run()`.
- Run concurrent coroutines using `asyncio.gather()` or `asyncio.create_task()`.
- Create `asyncio` tasks and manage their execution.
- Utilize the `random` module to simulate real-world delays in asynchronous operations.

---

### Task 0 - The Basics of Async
- **Filename:** `0-basic_async_syntax.py`

- **Description:**
The task involves writing an asynchronous coroutine that accepts an integer argument (`max_delay` with a default value of 10). The function, named `wait_random`, waits for a random delay between 0 and `max_delay` seconds and returns the delay. The `random` module is used for generating the random delay.

---

### Task 1 - Execute Multiple Coroutines Concurrently
- **Filename:** `1-concurrent_coroutines.py`

- **Description:**
This task focuses on executing multiple coroutines concurrently. The `wait_n` asynchronous routine is written, which takes two integer arguments `n` and `max_delay`. The function spawns `wait_random` (from the previous task) `n` times with the specified `max_delay`. `wait_n` returns a list of all the delays (float values), sorted in ascending order without using the `sort()` method due to concurrency considerations.

---

### Task 2 - Measure the Runtime
- **Filename:** `2-measure_runtime.py`

- **Description:**
In this task, we measure the total execution time for the `wait_n(n, max_delay)` coroutine from the previous task. The function `measure_time` is created, taking integers `n` and `max_delay` as arguments. It measures the total execution time for `wait_n(n, max_delay)` and returns the average time taken by calculating `total_time / n`. The time module is used to approximate the elapsed time.

---

### Task 3 - Tasks
- **Filename:** `3-tasks.py`

- **Description:**
This task is about creating a function called `task_wait_random` that takes an integer `max_delay` as its argument. Unlike the previous tasks, this is not an async function but a regular Python function. It returns an `asyncio.Task` object, wrapping the `wait_random` coroutine from Task 0. This allows the coroutine to be scheduled and run as a task in the event loop.

---

### Task 4 - Tasks Continued
- **Filename:** `4-tasks.py`

- **Description:**
This task is an extension of the previous task. It involves modifying the `wait_n` function to create a new function named `task_wait_n`. The main difference is that this new function uses `task_wait_random` to schedule the coroutines as tasks. The function still takes two integer arguments, `n` and `max_delay`, and returns a list of float values representing the delays, sorted in ascending order.
