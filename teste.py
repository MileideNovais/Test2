import requests
import unittest
import json


class TesTAPI(unittest.TestCase):
    def test_create(self):
        url = "http://127.0.0.1:5000/users/create"

        payload = {
            "name": "name",
            "age": "age",
            "address": "address",
        }

        headers ={"Content-Type": "application/json"}

        response = requests.request("POST",url,headers=headers,data=json.dumps(payload))

        data = response.json()[0]

        print(data)

        self.assertEqual(data["name"],payload["name"])
        self.assertEqual(data["age"],payload["age"])
        self.assertEqual(data["address"],payload["address"])

        id = data["id"]

        payload = {
            "name": "name2",
            "age": "age2",
            "address": "address2",
        }

        url = f"http://127.0.0.1:5000/users/update/{id}/edit"

        response = requests.request("PUT",url,headers=headers,data=json.dumps(payload))

        data = response.json()

        print (data)

        self.assertEqual(data["ok"], "Conseguimos modificar o usuário")