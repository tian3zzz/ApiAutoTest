from api.product_api.get_product_list_api import GetProductList
import pytest
from utils import utils


class TestGetProductDetail:
    send_product_detail_api = GetProductList()

    @pytest.mark.usefixtures('get_token')
    @pytest.mark.parametrize('data', utils.get_yaml_comm('product_data/product_detail.yaml'))
    def test_product_detail_api(self, get_token, data):
        test_data = utils.get_yaml_test_data(data)
        response = self.send_product_detail_api.send_get_product_detail_api(test_data['id'], get_token)
        utils.get_assert_data(data, response)

