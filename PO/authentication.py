import requests


class authentication:
    def __init__(self):
        self.user_data = {
            "name": "tests-user",
            "email": "tests-tests@mail.com",
            "password": "123456",
        }
        self.user_creds = {"email": "tests-tests@mail.com", "password": "123456"}

    def login(self, user_data):
        r = requests.post(
            "http://restapi.adequateshop.com/api/AuthAccount/Login", json=user_data
        )
        return r

    def bearer_id(self, cred):
        r = requests.post(
            "http://restapi.adequateshop.com/api/AuthAccount/Login", json=cred
        )
        bearer = r.json()["data"]["Token"]
        id = r.json()["data"]["Id"]
        return bearer, id
