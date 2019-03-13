from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class AddressInfoPage(BaseAction):
    # 收货人 输入框
    name_edit_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"

    # 手机号 输入框
    mobile_edit_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"

    # 详细地址 输入框
    address_edit_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"

    # 所在地区 按钮
    region_button = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    @allure.step(title='收货地址 - 输入收货人')
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    @allure.step(title='收货地址 - 输入手机号')
    def input_mobile(self, text):
        self.input(self.mobile_edit_text, text)

    @allure.step(title='收货地址 - 输入详细地址')
    def input_address(self, text):
        self.input(self.address_edit_text, text)

    @allure.step(title='收货地址 - 点击所在地区')
    def click_region(self):
        self.click(self.region_button)