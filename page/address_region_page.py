import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class AddressRegionPage(BaseAction):

    # 选择城市的特征
    city_feature = By.ID, "com.tpshop.malls:id/tv_city"

    # 确定 按钮
    commit_button = By.ID, "com.tpshop.malls:id/btn_right"

    @allure.step(title='收货人地址区域 - 选择区域')
    def click_cities(self):
        for _ in range(4):
            # 获取当前屏幕范围内的所有的城市
            cities_button = self.find_elements(self.city_feature)
            # 获取所有城市的个数
            cities_count = len(cities_button)
            # 根据个数，生成随机的下标
            random_index = random.randint(0, cities_count - 1)
            # 通过随机的下标，取一个随机的城市，并点击
            cities_button[random_index].click()

            time.sleep(3)

    @allure.step(title='收货人地址区域 - 点击确定')
    def click_commit(self):
        self.click(self.commit_button)
