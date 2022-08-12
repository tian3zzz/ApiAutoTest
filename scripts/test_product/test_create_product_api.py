from api.product_api.get_product_list_api import GetProductList
import pytest
from utils import utils


class TestProductListApi:
    send_product_api = GetProductList()

    @pytest.mark.usefixtures('get_token')
    @pytest.mark.parametrize('data', utils.get_yaml_comm('product_data/create_product.yaml'))
    def test_product_list_api(self, get_token, data):
        test_data = utils.get_yaml_test_data(data)
        response = self.send_product_api.send_post_product_api(get_token, test_data['payload'])

        utils.get_assert_data(data, response)