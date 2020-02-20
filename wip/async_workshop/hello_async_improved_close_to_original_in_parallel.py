import asyncio
import aiohttp

# on the server part we could use aiohttp web instead of flask
# sth like python server.py to run the server


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    # we need to use the "await". Somebody needs to call "send". The event loop does that for us.
    # the await will suspend execution

    # option1 ensure_future
    # option2 gather

    car_ids = await fetch("https://folkol.com/cars")
    print(car_ids)
    cars = await asyncio.gather(*(fetch(f"https://folkol.com/cars/{c}")
                                  for c in car_ids))
    print(cars)

    # ALTERNATE BELOW; DO STUFF AS SOON AS THEY ARE DONE INSTEAD OF WAITING FOR ALL
    # coros = (fetch(f"https://folkol.com/cars/{c}") for c in car_ids))
    # cars = asyncio.as_completed(coros)
    # does it wait for the fastest? or like gather (which is the slowest?)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())  # the two lines above are equivalent to this, but only work for python 3.7+




