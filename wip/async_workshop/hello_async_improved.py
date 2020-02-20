import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        car_ids = await fetch(session, "https://folkol.com/cars")
        print(car_ids)
        for c in car_ids:
            car = await fetch(session, f"https://folkol.com/cars/{c}")
            print(car)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())  # the two lines above are equivalent to this, but only work for python 3.7+
