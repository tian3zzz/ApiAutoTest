import yaml
import config
from utils.assert_utils import *
from jsonpath import jsonpath


def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        yaml_content = yaml.safe_load(f)
    return yaml_content


def get_yaml_comm(file):
    test_data = load_yaml(config.TEST_CASE_DATA + file)
    return test_data


# 获取测试数据
def get_yaml_test_data(test_cases):
    test_data = {}
    for key, value in test_cases['testCases'].items():
        test_data[key] = value
    return test_data


# # 获取参数
# def get_yaml_payload(testCases):
#     test_data = get_yaml_test_data(testCases)
#     return test_data['payload']


# 获取断言值并返回字典
def get_yaml_assert(test_cases):
    test_data = get_yaml_test_data(test_cases)
    assert_data_dict = {}
    for key, value in test_data['assert'].items():
        assert_data_dict[key] = value
    return assert_data_dict


# 获取断言数据后进行断言
def get_assert_data(test_cases, response):
    assert_data = get_yaml_assert(test_cases)
    for key, value in assert_data.items():
        actual = jsonpath(response.json(), key)[0]
        if value['compart'] == 'equals':
            equals(actual, value['expect'])
        elif value['compart'] == 'not_equals':
            not_equals(actual, value['expect'])
        elif value['compart'] == 'greater_than':
            greater_than(actual, value['expect'])
        elif value['compart'] == 'greater_than_or_equals':
            greater_than_or_equals(actual, value['expect'])
        elif value['compart'] == 'less_than':
            less_than(actual, value['expect'])
        elif value['compart'] == 'less_than_or_equals':
            less_than_or_equals(actual, value['expect'])
        elif value['compart'] == 'is_null':
            is_null(actual)
        elif value['compart'] == 'is_not_null':
            is_not_null(actual)
        elif value['compart'] == 'status_code':
            equals(response.status_code, value['expect'])
        else:
            print('暂不支持该断言方法...')
