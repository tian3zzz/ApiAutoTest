import requests
import config
from common import apiRequerts

class GetTokinApi:

    post_token_url = config.BASE_URL + '/tokens'

    def send_get_token_api(self, payload):
        response = apiRequerts.post(url=self.post_token_url, json=payload, headers={'Content-Type': 'application/json'})
        return response
