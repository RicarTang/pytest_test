import time

import pytest

from selenium import webdriver
from common.base import Base



@pytest.fixture(scope='class')
def openweb():
    base = Base()
    base.dr.maximize_window()
    # base.dr.get('http://192.168.0.130/TinyShop/index.php?con=admin&act=login')
    yield
    time.sleep(3)
    base.dr.quit()
    # dr = webdriver.Chrome()
    # dr.maximize_window()
    # dr.get('http://192.168.0.130/TinyShop/index.php?con=admin&act=login')
    # yield dr
    # time.sleep(3)
    # dr.quit()










