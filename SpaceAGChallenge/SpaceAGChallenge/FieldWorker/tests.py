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

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        id = "b64b8cdd-8075-493c-adb4-f80c95f8c1bf"
        data = {"first_name": "LuisPrueba",
                "last_name": "Mundaca", "function": "Harvest"}

        response = self.client.patch("/v1/field_workers/" + id, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        id = "b64b8cdd-8075-493c-adb4-f80c95f8c1bf"
        response = self.client.delete("/v1/field_workers/" + id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)