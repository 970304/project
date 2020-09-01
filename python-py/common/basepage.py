from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import dir_location as dl
from common.my_log import MyLog
import logging
import time


class BasePage:

    log = MyLog()

    def __init__(self, driver):
        self.driver = driver

    # 元素可见
    def wait_ele_view(self, locator, times=20, poll_frequency=0.5, doc=''):
        self.log.info("元素{}在{}界面可见".format(locator, doc))
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            self.save_screenshot(doc)
            raise

    def wait_ele_exist(self, locator, times=30, poll_frequency=0.2, doc=''):
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(EC.presence_of_element_located(locator))
            return True
        except:
            self.save_screenshot(doc)
            return False

    # 获取元素
    def get_element(self, locator, doc=''):
        try:
            return self.driver.find_element(*locator)
        except:
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=''):
        ele = self.get_element(locator)
        try:
            ele.send_keys(text)
        except:
            self.save_screenshot(doc)
            raise

    # 点击操作
    def ele_click(self, locator, doc=''):
        ele = self.get_element(locator)
        try:
            ele.click()
        except:
            self.save_screenshot(doc)
            raise

    # 获取元素文本
    def get_ele_text(self, locator, doc=''):
        ele = self.get_element(locator)
        try:
            return ele.text
        except:
            self.save_screenshot(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self, locator, doc=''):
        ele = self.get_element(locator)
        try:
            return ele.get_attribute()
        except:
            self.save_screenshot(doc)
            raise

    # alert操作
    def alert_txt(self):
        time.sleep(0.5)
        alert = self.driver.switch_to.alert
        return alert.text

    def alert_acept(self):
        time.sleep(0.5)
        alert = self.driver.switch_to.alert
        alert.accept()

    # 截图
    def save_screenshot(self, doc=''):
        file_path = dl.scree_dir+'/{}.png'.format(doc)
        try:
            self.driver.save_screenshot(file_path)
        except:
            logging.exception("截图失败")
            raise



