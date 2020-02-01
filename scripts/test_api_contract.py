import requests
import faker

from random import randint

fake = faker.Faker("fr_FR")

URL = "http://127.0.0.1:8000/api/v1/contract/create/"

for _ in range(10):

    DATA = {
        "customer": {
            "name": fake.last_name(),
            "first_name": fake.first_name(),
            "age": randint(18, 70),
        },
        "insurance": "MGEN",
    }

    req = requests.post(URL, json=DATA, timeout=5.0)
    print(req.json())
