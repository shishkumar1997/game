from rest_framework import status
import requests


class TestCases:
    def test_get_api(self):
        response = requests.get('http://127.0.0.1:3000/api/get_student/3')
        assert response.status_code == status.HTTP_200_OK