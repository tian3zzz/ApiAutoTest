import config
from common import apiRequerts


class GetPersonalInformationApi:
    post_personal_information_url = config.BASE_URL + '/user'

    def send_post_api(self, headers):
        response = apiRequerts.get(url=self.post_personal_information_url, headers=headers)
        return response
