import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("phone", "password", "expect"), analyze_file("login_data", "test_login"))
    def test_login(self, phone, password, expect):
        self.page.home.click_mine()
        self.page.mine.click_login_and_sign_up()
        self.page.login_and_sign_up_page.input_phone(phone)
        self.page.login_and_sign_up_page.input_password(password)
        self.page.login_and_sign_up_page.click_login()
        assert self.page.login_and_sign_up_page.is_login(expect)

    def test_login4(self):
        print(4)
