from rest_framework import status
import requests
# from rest_framework.test import APIClient
import pytest

# class TestCases:
#     def test_get_api(self):
#         response = requests.get('http://127.0.0.1:3000/api/get_student/')
#         assert response.status_code == status.HTTP_200_OK

class TestCases:
    def test_get_api(self):
        response = requests.get('http://127.0.0.1:3000/api/get_student/')
        assert response.status_code == status.HTTP_200_OK

# class TestCases:
#     def test_get_api(self):
#         # response = requests.get('http://127.0.0.1:3000/api/get_student/')
#         assert 5 == 53