import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    # we need to use the "await". Somebody needs to call "send". The event loop does that for us.
    # the await will suspend execution
    car_ids = await fetch("https://folkol.com/cars")
    print(car_ids)
    for c in car_ids:
        car = await fetch(f"https://folkol.com/cars/{c}")
        print(car)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())  # the two lines above are equivalent to this, but only work for python 3.7+
