import requests


def fetch(url):
    response = requests.get(url)
    return response.json()


car_ids = fetch("https://folkol.com/cars")
print(car_ids)

for c in car_ids:
    print(fetch(f"https://folkol.com/cars/{c}"))
