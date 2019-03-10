from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    # 因为这个类中的其他对象方法需要使用driver对象
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
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

    def find_elements(self, feature, timeout=10, poll=1):
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

    def click(self, feature, timeout=10, poll=1):
        """
        根据传进来的特征，去找对应的元素，并且点击
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).click()

    def input(self, feature, text, timeout=10, poll=1):
        """
        根据传进来的特征，去找对应的元素，并且输入文字
        :param feature: 特征
        :param text: 要输入的文字
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).send_keys(text)

    def clear(self, feature, timeout=10, poll=1):
        """
        根据传进来的特征，去找对应的元素，并且清空
        :param feature: 特征
        :param timeout: 超时时间
        :param poll: 每多久照一次
        """
        self.find_element(feature, timeout, poll).clear()

    # def xxxx(self):
    #     self.driver.find_element_by_xxx("xxx")
    #     WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element_by_xxx("xxx"))
