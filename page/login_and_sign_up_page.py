from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginAndSignUpPage(BaseAction):

    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    def input_password(self, text):
        self.input(self.password_edit_text, text)

    def click_login(self):
        self.click(self.login_button)

    def is_login(self, content):
        try:
            self.find_toast(content)
            return True
        except Exception:
            return False