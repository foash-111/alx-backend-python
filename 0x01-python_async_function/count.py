import asyncio

async def count_up():
    for i in range(1, 4):
        print(f"Counting up: {i}")
        await asyncio.sleep(1)

async def count_down():
    for i in range(3, 0, -1):
        print(f"Counting down: {i}")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(count_up(), count_down())

asyncio.run(main())
