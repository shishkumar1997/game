# from rest_framework.test import APIClient
# import pytest

# @pytest.fixture(autouse=True)
# def use_dummy_cache_backend(settings):
#     settings.CACHES = {
#         "default": {
#             "BACKEND": "django.core.cache.backends.dummy.DummyCache",
#         }
#     }
#     settings.DEBUG = True

# @pytest.fixture
# def api_client():
#     return APIClient()