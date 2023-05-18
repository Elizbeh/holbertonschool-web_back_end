import asyncio
from wait_random import wait_random

async def wait_n(n, max_delay):
    delays = []
    tasks = []
    
    async def gather_result(task):
        result = await task
        delays.append(result)

    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(gather_result)
        tasks.append(task)

    await asyncio.gather(*tasks)

    return sorted(delays)

async def main():
    delays = await wait_n(5, 10)
    print("Delays:", delays)

asyncio.run(main())

