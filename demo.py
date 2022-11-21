import time

import allure
from selenium import webdriver

def save_screenshot():
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get('http://192.168.0.130/TinyShop/index.php?con=admin&act=login')
    t = time.strftime('%Y-%m-%d %H-%M-%S')  # 系统当前时间
    path = r'E:\pythonProject-tinyshop\err_img\{}.png'.format(t)
    dr.save_screenshot(path)
    with open(path, 'rb') as i:
        file = i.read()
        print(file)
    # allure.attach(file, '测试截图', allure.attachment_type.PNG)
save_screenshot()
