from django.test import TestCase

# Create your tests here.
import datetime
import jwt
from django.conf import settings


def generate_access_token(user):
    if user:
    #     access_token_payload = {
    #         'user_id': user,
    #         'token_type': 'access',
    #         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365),
    #         #'iat': datetime.datetime.utcnow(),
    #         'jti': "b932ba39d8024b39a55b3850129cbd10",
    #     }
    # if
        access_token_payload = {
            'user_id': user,
            'token_type': 'access',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            #'iat': datetime.datetime.utcnow(),
            'jti': "b932ba39d8024b39a55b3850129cbd10",
        }
    access_token = jwt.encode(access_token_payload,settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    if user:
    #     refresh_token_payload = {
    #         'user_id': user,
    #         'token_type': 'refresh',
    #         'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365),
    #         'jti': "b932ba39d8024b39a55b3850129cbd10",
    #     }
    # if:
        refresh_token_payload = {
            'user_id': user,
            'token_type': 'refresh',
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'jti': "b932ba39d8024b39a55b3850129cbd10",
        }
    refresh_token = jwt.encode(refresh_token_payload,settings.SECRET_KEY, algorithm='HS256')
    return refresh_token