import requests
import asyncio
import aiohttp


def fetch(url):
    response = requests.get(url)
    return response.json()


async def main():
    car_ids = fetch("https://folkol.com/cars")
    print(car_ids)
    for c in car_ids:
        car = fetch(f"https://folkol.com/cars/{c}")
        print(car)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())  # the two lines above are equivalent to this, but only work for python 3.7+
