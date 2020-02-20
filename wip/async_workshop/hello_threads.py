import requests
from concurrent.futures import ThreadPoolExecutor


def fetch(url):
    response = requests.get(url)
    return response.json()


car_ids = fetch("https://folkol.com/cars")
print(car_ids)

with ThreadPoolExecutor() as executor:
    cars = executor.map(fetch, [f"https://folkol.com/cars/{c}" for c in car_ids])

for c in cars:
    print(c)
