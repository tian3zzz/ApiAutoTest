import pytest
from api.user_api.get_personal_information_api import GetPersonalInformationApi


# 获取token
@pytest.mark.usefixtures('get_token')
class TestGetPersonalInformationApi:
    personal_information_api = GetPersonalInformationApi()

    def test_personal_information_api(self, get_token):
        pi_data = {'Token': get_token}
        pi_response = self.personal_information_api.send_post_api(headers=pi_data)

        return pi_response
