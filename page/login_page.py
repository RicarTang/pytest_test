
from common.base import Base


class Page_login(Base):
    # url1 = 'http://127.0.0.1/TinyShop/index.php?con=admin&act=login'

    # 定位器

    login_user = ('xpath', "//input[@name='name']")  # 用户名
    login_pwd = ('xpath', "//input[@name='password']")  # 密码
    login_vcode = ('xpath', "//input[@name='verifyCode']")  # 验证码
    login_btn = ('xpath', "//input[@value='登 录']")  # 登录按钮

    # 获取元素对象
    def send_user(self, name):
        self.base_sendkeys(self.login_user, name)

    def send_pwd(self, pwd):
        self.base_sendkeys(self.login_pwd, pwd)

    def send_vcode(self, code):
        self.base_sendkeys(self.login_vcode, code)

    def click_btn(self):
        self.base_click(self.login_btn)


# if __name__ == '__main__':
#     a = Page_login()
#     a.base_openurl('http://192.168.36.130/TinyShop/index.php?con=admin&act=login')
#     a.send_user('admin')
