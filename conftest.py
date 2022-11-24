import time

import pytest


from common import base



@pytest.fixture(scope='class')
def setup_teardown():

    base.dr.maximize_window()

    yield
    time.sleep(3)
    base.dr.quit()











