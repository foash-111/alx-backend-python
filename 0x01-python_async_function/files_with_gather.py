import asyncio

async def download_file(file_number):
    print(f"Downloading file {file_number}...")
    await asyncio.sleep(2)
    print(f"File {file_number} downloaded!")

async def main():
    await asyncio.gather(
        download_file(1),
        download_file(2),
        download_file(3)
    )

asyncio.run(main())
