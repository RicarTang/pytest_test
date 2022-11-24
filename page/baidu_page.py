from common.base import Base


class PageBaidu(Base):
    url = 'http://www.baidu.com/'

    input = ('id', 'kw')
    button = ('id', 'su')

    def send_text(self, text):
        self.base_sendkeys(self.input, text)

    def click_search(self):
        self.base_click(self.button)
