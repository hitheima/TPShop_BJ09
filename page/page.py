from page.home_page import HomePage
from page.login_and_sign_up_page import LoginAndSignUpPage
from page.mine_page import MinePage


class Page:

    def __init__(self, driver):
        self.driver = driver
        print("hehe")

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login_and_sign_up_page(self):
        return LoginAndSignUpPage(self.driver)