from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class LoginAndSignUpPage(BaseAction):

    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    # 登录按钮
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    # 显示密码按钮
    show_password_button = By.ID, "com.tpshop.malls:id/img_view_pwd"

    @allure.step(title='登录注册 - 输入电话')
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    @allure.step(title='登录注册 - 输入密码')
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    @allure.step(title='登录注册 - 点击登录')
    def click_login(self):
        self.click(self.login_button)

    @allure.step(title='登录注册 - 点击显示密码')
    def click_show_password(self):
        self.click(self.show_password_button)

    def is_login(self, content):
        """
        根据toast的部分内容，判断是否提示登录成功
        :param content:
        :return:
        """
        try:
            self.find_toast(content)
            return True
        except Exception:
            return False

    def is_login_enabled(self):
        """
        判断 登录按钮中的 enabled 属性值 是不是 可用的
        true 表示可用
        false 表示不可用
        :return: 是否可用
        """
        return self.find_element(self.login_button).get_attribute("enabled") == "true"

        # if self.find_element(self.login_button).get_attribute("enabled") == "true":
        #     return True
        # else:
        #     return False

    def is_password_exist(self, password):
        """
        根据传入的密码，判断是否和密码框上的密码一致
        :param password: 传入的密码
        :return: 是否一致
        """
        return self.find_element(self.password_edit_text).text == password

        # try:
        #     self.find_element((By.XPATH, "//*[@text='" + password + "']"))
        #     return True
        # except:
        #     return False


