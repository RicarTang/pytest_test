import os

import pytest



if __name__ == '__main__':
    pytest.main(['test_case/test_data.py', '--alluredir', './report/report-pytest', '--clean-alluredir'])
    os.system('allure generate ./report/report-pytest -o ./report/report-allure --clean')
