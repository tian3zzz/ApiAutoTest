import pytest
from utils import utils
from config import log_config
import logging
from api.get_token_api import GetTokinApi
from jsonpath import jsonpath


class TestGetTokenApi:
    token_api = GetTokinApi()

    @pytest.mark.parametrize('data', utils.get_yaml_comm('get_token.yaml'))
    def test_get_token_api(self, data):
        test_data = utils.get_yaml_test_data(data)
        response = self.token_api.send_get_token_api(payload=test_data['payload'])

        utils.get_assert_data(data, response)
