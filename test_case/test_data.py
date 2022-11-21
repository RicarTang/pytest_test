import os
import time

import allure
import pytest

from page.login_page import Page_login
from common.base import Base

# #读取json文件
base = Base()
json_data = base.loadjson('/media/tang/工作/pythonProject-tinyshop/data/login.json')
# 读取yaml文件
yaml_data = base.loadyaml('/media/tang/工作/pythonProject-tinyshop/data/login.yaml')

class Test_login(Page_login):

    # def setup(self):
    #     self.base_openurl('http://192.168.36.130/TinyShop/index.php?con=admin&act=login')
    # def teardown(self):
    #     self.base_quiturl()
    # 用例参数化
    @pytest.mark.parametrize('data', yaml_data)
    def test_login(self, data,openweb):
        self.dr.get('http://www.baidu.com/')
        self.send_user(data['name'])
        self.send_pwd(data['pwd'])
        self.send_vcode(1234)
        self.click_btn()

        if pytest.assume(False) is False:
            base.save_screenshot()
        # with allure.step('错误截图'):
        #     with open('','rb',encoding='utf-8') as f:
        #         img = f.read()
        #     allure.attach(img,'错误截图')



