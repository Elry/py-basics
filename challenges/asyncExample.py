import asyncio

async def fetch_data(id):
    print(f"Fetching {id}...")
    await asyncio.sleep(2) # non-blocking
    print(f"Received {id}")
    return {"id": id}

async def main():
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    print(results)


if __name__ == "__main__":
    # This runs the main async function and manages the event loop
    asyncio.run(main())
