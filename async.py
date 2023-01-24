import asyncio
from time import perf_counter


async def main():
    await asyncio.sleep(1)
    print('hello')
    a = input("Enter a sh**t: " )

asyncio.run(main())

