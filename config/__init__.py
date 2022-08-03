import os

__all__ = ['BASE_DIR', 'LOG_PATH', 'TEST_CASE_DATA']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_PATH = BASE_DIR + '/outputs/log/'

TEST_CASE_DATA = BASE_DIR + '/case_data/'

BASE_URL = 'http://localhost/zentaopms/www/api.php/v1'

