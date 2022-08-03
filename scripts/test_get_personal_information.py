import pytest
from utils import utils
from config import log_config
import logging
from api.get_personal_information_api import GetPersonalInformationApi
from api.get_token_api import GetTokinApi
from jsonpath import jsonpath


class TestGetPersonalInformationApi:
    personal_information_api = GetPersonalInformationApi()
    token_api = GetTokinApi()

    def test_personal_information_api(self):
        # 引用前面的登录接口的token
        token_api_payload = {'account': 'root',
                             'password': 'tian159.'}
        token_response = self.token_api.send_get_token_api(token_api_payload)
        token = token_response.json().get('token')

        # 获取个人信息
        pi_data = {'Token': token}
        pi_response = self.personal_information_api.send_post_api(headers=pi_data)

        return pi_response
