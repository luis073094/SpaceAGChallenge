import json
from rest_framework.test import APITestCase
from rest_framework import status


class FieldWorkerAPITestCase(APITestCase):
    def test_list(self):
        response = self.client.get("/v1/field_workers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_registration(self):
        data = {"first_name": "Luis",
                "last_name": "Mundaca", "function": "Harvest"}

        response = self.client.post("/v1/field_workers/", data)
        jsonResponse = json.loads(response.content)
        id = jsonResponse["id"]

        responseGet = self.client.get("/v1/field_workers/" + id + "/")
        jsonResponseGet = json.loads(responseGet.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(jsonResponse), type(data))
        self.assertDictEqual(jsonResponse, jsonResponseGet)

    def test_registration_incomplete(self):
        data = {"last_name": "Mundaca", "function": "Harvest"}
        waited_result = {
            "first_name": [
                "This field is required."
            ]
        }

        response = self.client.post("/v1/field_workers/", data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content), waited_result)


    def test_update(self):
        data = {"first_name": "Luis",
                "last_name": "Mundaca", "function": "Harvest"}
        
        response = self.client.post("/v1/field_workers/", data)
        jsonResponse = json.loads(response.content)
        id = jsonResponse["id"]

        response = self.client.patch("/v1/field_workers/" + id + "/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete(self):
        data = {"first_name": "Luis",
                "last_name": "Mundaca", "function": "Harvest"}
        
        response = self.client.post("/v1/field_workers/", data)
        jsonResponse = json.loads(response.content)
        id = jsonResponse["id"]

        response = self.client.delete("/v1/field_workers/" + id + "/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)