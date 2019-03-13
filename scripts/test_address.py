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
        self.page.mine.click_address()

        # 3. 点击新建地址
        self.page.address_list_page.click_new_address()

        # 4. 填写个人信息
        # 4.1 填写联系人
        self.page.address_info_page.input_name("张三")

        # 4.2 填写手机号
        self.page.address_info_page.input_mobile("18888888888")

        # 4.3 填写详细地址
        self.page.address_info_page.input_address("二号楼 三单元 106")

        # 4.4 填写所在地区
        # 4.4.1 选择省、市、区、街道





