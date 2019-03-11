import time

from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_add_address(self):
        # 1. 判断是否登录
        # 1.1 首页 点击 我的
        self.page.home.click_mine()
        # 1.2 我的 点击 齿轮
        self.page.mine.click_setting()

        # 1.3 判断是否登录
        if not self.page.mine.is_login():
            print("没有登录。准备登录")
        else:
            print("已经登录")

        # 2. 点击收货地址

        # 3。 xxxxx


