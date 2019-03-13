from page.address_info_page import AddressInfoPage
from page.address_list_page import AddressListPage
from page.home_page import HomePage
from page.login_and_sign_up_page import LoginAndSignUpPage
from page.mine_page import MinePage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login_and_sign_up_page(self):
        return LoginAndSignUpPage(self.driver)

    @property
    def address_info_page(self):
        return AddressInfoPage(self.driver)

    @property
    def address_list_page(self):
        return AddressListPage(self.driver)