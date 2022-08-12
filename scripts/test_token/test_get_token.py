import pytest
from utils import utils
from api.token_api.get_token_api import GetTokinApi


class TestGetTokenApi:
    token_api = GetTokinApi()

    @pytest.mark.parametrize('data', utils.get_yaml_comm('get_token_data/get_token.yaml'))
    def test_get_token_api(self, data):
        test_data = utils.get_yaml_test_data(data)
        response = self.token_api.send_get_token_api(payload=test_data['payload'])

        utils.get_assert_data(data, response)
