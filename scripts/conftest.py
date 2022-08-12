import pytest
from api.get_token_api import GetTokinApi


@pytest.fixture(scope='class')
def get_token():
    token_api = GetTokinApi()
    token_api_payload = {'account': 'root',
                         'password': 'tian159.'}
    token_response = token_api.send_get_token_api(token_api_payload)
    token = token_response.json().get('token')
    return token
