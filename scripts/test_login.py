import time

from base.base_driver import init_driver


class TestLogin:

    def setup(self):
        self.driver = init_driver()

    def teardown(self):
        time.sleep(1)
        self.driver.quit()

    def test_login(self):
        print("1")