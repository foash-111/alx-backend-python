import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://jsonplaceholder.typicode.com/todos/1"
        data = await fetch_data(session, url)
        print(data)

asyncio.run(main())






# Explanation: Here, we asynchronously fetch data from an API. 
# This example uses aiohttp for asynchronous HTTP requests, 
# demonstrating how await is used to handle the response once it's ready.
