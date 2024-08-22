import asyncio
import aiohttp

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = [
        "https://example.com",
        "https://python.org",
        "https://realpython.com"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        print(*tasks)
        pages = await asyncio.gather(*tasks)
        for i, page in enumerate(pages):
            print(f"Page {i+1}: {page[:60]}...")  # Print first 60 characters of each page

asyncio.run(main())
