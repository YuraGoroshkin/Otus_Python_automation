import requests


class DogApiRequest:
    def __init__(self, adres: str = "https://dog.ceo/", path: str = None):
        self.adres = adres
        self.path = path

    def request_one(self):
        requests.get(self.adres, self.path)


DogApiRequest.request_one
