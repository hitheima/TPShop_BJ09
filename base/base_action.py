from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    # 因为这个类中的其他对象方法需要使用driver对象
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        """
        根据元素的从特征（元组），定位对应的元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        :return: 找到元素本身
        """
        # by = feature[0]
        # value = feature[1]
        # by, value = feature
        # element = self.driver.find_element(by, value)
        by, value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))
        return element

    def find_elements(self, feature, timeout=10.0, poll=1.0):
        """
        根据元素的从特征（元组），定位符合特征条件的多个元素
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        :return: 列表，符合条件的元素
        """
        by, value = feature
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))
        return element

    def click(self, feature, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且点击
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, text, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且输入文字
        :param feature: 特征
        :param text: 要输入的文字
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).send_keys(text)

    def clear(self, feature, timeout=10.0, poll=1.0):
        """
        根据传进来的特征，去找对应的元素，并且清空
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).clear()

    def find_toast(self, content):
        """
        根据部分toast内容，获取全部的toast内容
        :param content: 部分内容
        :return: 全部内容
        """
        feature = By.XPATH, "//*[contains(@text,'" + content + "')]"
        return self.find_element(feature, 5, 0.1).text

    def scroll_page_one_time(self, dir="down"):
        """
        滑动 半屏 从 4/3 到 4/1
        :param dir: 反向
            up: 从上往下
            down: 从下往上
            left: 从左往右
            right: 从右往左
        """
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        top_x = width * 0.5
        top_y = height * 0.25
        bottom_x = top_x
        bottom_y = width * 0.75
        left_x = width * 0.25
        left_y = height * 0.5
        right_x = width * 0.75
        right_y = left_y

        if dir == "down":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif dir == "up":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif dir == "left":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        elif dir == "right":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        else:
            raise Exception("请传入正确的参数 up/down/left/right")

    def scroll_find_element(self, feature, dir="down"):
        """
        边滑边找，如果找到则返回，如果没有找到则抛异常
        :param feature: 元素的特征
        :return: 元素
        """
        while True:

            source = self.driver.page_source
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_page_one_time(dir)
                if source == self.driver.page_source:
                    # 到底了
                    raise Exception("滑动到底")
