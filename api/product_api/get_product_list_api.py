import config
from common import apiRequerts


class GetProductList:
    product_api = config.BASE_URL + '/products'
    get_product_detail_api = config.BASE_URL + '/products/{}'

    def send_get_product_api(self, token):
        headers = {"token": token}
        response = apiRequerts.get(url=self.product_api, headers=headers)
        return response

    def send_post_product_api(self, token, json):
        headers = {"token": token}
        response = apiRequerts.post(url=self.product_api, headers=headers, json=json)
        return response

    def send_get_product_detail_api(self, id, token):
        url = self.get_product_detail_api.format(id)
        headers = {"token": token}
        response = apiRequerts.get(url=url, headers=headers)
        return response
