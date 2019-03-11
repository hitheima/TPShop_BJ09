from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class MinePage(BaseAction):

    login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"

    @allure.step(title='我的页面 - 点击登录/注册')
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)