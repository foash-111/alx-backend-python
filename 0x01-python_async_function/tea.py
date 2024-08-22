import asyncio

async def boil_water():
    print("Boiling water...")
    await asyncio.sleep(2)
    print("Water is ready!")

async def make_tea():
    print("Making tea...")
    await boil_water()
    print("Tea is ready!")

asyncio.run(make_tea())
