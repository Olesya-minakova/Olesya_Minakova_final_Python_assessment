import requests
from PO.endpoint import links
from PO.authentication import authentication

auth = authentication()
url = links()
BEARER = f"bearer {auth.bearer_id(auth.user_creds)[0]}"


class touristic:
    def __init__(self):
        self.tourist_data = {
            "id": 0,
            "tourist_name": "Tututt",
            "tourist_email": "Tuuust@tut.tu",
            "tourist_location": "Venust",
            "createdat": "2024-01-05T12:10:06.589Z",
        }

    def tourist_creation(self, data):
        headers = {"Authorization": BEARER}
        r = requests.post(url.tour, json=data, headers=headers)
        return r
