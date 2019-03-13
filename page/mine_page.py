from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class MinePage(BaseAction):

    # 登录/注册
    login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"

    # 齿轮设置按钮
    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"

    # 导航栏的特征
    title_bar = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    # 收货地址
    address_button = By.XPATH, "//*[@text='收货地址']"

    @allure.step(title='我的页面 - 点击登录/注册')
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)

    @allure.step(title='我的页面 - 点击设置')
    def click_setting(self):
        self.click(self.setting_button)

    @allure.step(title='我的页面 - 点击收货地址')
    def click_address(self):
        # 找收货地址，如果没有就滑动
        self.scroll_find_element(self.address_button).click()

    # 只要调用，返回title bar的标题
    def get_title_bar_text(self):
        return self.find_element(self.title_bar).text

    def is_login(self):
        """
        目前是否已经登录
        :return: 是否已经登录
        """
        return self.get_title_bar_text() == "设置"
