import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(6)
    print("Task 2 completed")

async def main():
    task1_handle = asyncio.create_task(task1())
    task2_handle = asyncio.create_task(task2())
    
    # # Optionally wait for both tasks to finish
    # await task1_handle
    # await task2_handle
    i = 0
    while (i < 50):
        print('i')
        i += 1
    
# Run the async main function
asyncio.run(main())
