import os

import pytest

import yaml

if __name__ == '__main__':
    pytest.main([ '/media/tang/工作/pythonProject-tinyshop/test_case/test_data.py','-sv','--alluredir','../report', '--clean-alluredir'])
    # os.system('allure generate ../report -o ../report-allure --clean')
