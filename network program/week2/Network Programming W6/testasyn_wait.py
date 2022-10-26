import asyncio
for coro in as_completed(aws):
    earliest_result = await coro
    # ...