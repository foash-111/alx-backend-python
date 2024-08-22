import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")
    return "Result from task 1"

async def task2():
    print("Task 2 started")
    await asyncio.sleep(6)
    print("Task 2 completed")
    return "Result from task 2"

async def main():
    # Create and await both tasks concurrently
    results = await asyncio.gather(task1(), task2())
    
    print("All tasks completed")
    print(f"Results: {results}")

# Run the async main function
asyncio.run(main())
