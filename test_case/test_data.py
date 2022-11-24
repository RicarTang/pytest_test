import pytest
import os
from page import PageBaidu
from common import base


# #读取json文件

class TestBaidu(PageBaidu):
    # def teardown(self):
    #     self.closeweb()

    # 用例参数化
    @pytest.mark.parametrize(
        'data',
        base.loadyaml(os.path.join(os.path.dirname(__file__), '../data/baidu.yaml'))
    )
    def test_login(self, data, setup_teardown):
        self.openweb(super().url)
        self.send_text(data['text'])
        self.click_search()
