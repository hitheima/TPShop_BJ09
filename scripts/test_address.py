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
            # 如果已经登录，此时页面会来到登录页面，直接输入用户名和密码即可
            self.page.login_and_sign_up_page.input_phone("13800138006")
            self.page.login_and_sign_up_page.input_password("123456")
            self.page.login_and_sign_up_page.click_login()
            # 登录成功后会自动的回到，"我的"页面
            assert self.page.login_and_sign_up_page.is_login_success("登录成功")

        # 2. 点击收货地址

        # 3。 xxxxx


