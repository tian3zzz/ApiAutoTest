from api.product_api.get_product_list_api import GetProductList
import pytest


class TestProductListApi:
    send_product_api = GetProductList()

    @pytest.mark.usefixtures('get_token')
    def test_product_list_api(self, get_token):
        self.send_product_api.send_get_product_api(get_token)
