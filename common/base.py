import os
import time

import allure
import pymysql

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import json
import yaml
# import page.login_page
import conftest


# from conftest import Fixture


class Base():
    # 打开浏览器
    dr = webdriver.Chrome()

    # def __init__(self):
    #     self.dr = webdriver.Chrome()

    def openweb(self, url):
        self.dr.get(url)

    def closeweb(self):
        self.dr.close()

    # 显示等待元素定位
    def base_find(self, ele):
        return WebDriverWait(self.dr, 10, 1).until(lambda x: x.find_element(*ele))

    # 输入
    def base_sendkeys(self, ele, value):
        a = self.base_find(ele)
        a.send_keys(value)

    # 点击
    def base_click(self, ele):
        a = self.base_find(ele)
        a.click()

    # 提取文字
    def base_text(self, ele):
        a = self.base_find(ele)
        return a.text

    # 读取json文件
    def loadjson(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    # 读取yaml文件
    def loadyaml(self, filepath: str):
        with open(filepath, 'r', encoding='utf-8') as file:
            return yaml.load(file, Loader=yaml.FullLoader)



