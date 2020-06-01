#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 10:03  
# Author  : DanDan Zhao 
# File    : base_page.py  
#
import inspect
import allure
import selenium
import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.common import Common
from utils.except_windows import except_windows
from utils.log_helper import LogHelper
from utils.chromedriver_helper import ChromeDriver
from appium import webdriver as appium_webdriver
from appium.webdriver.mobilecommand import MobileCommand as Command


class BasePage:
    _base_url = ""
    _driver = None
    log = LogHelper().set_logger()

    def __init__(self, driver: WebDriver = None, platform="web", desired_caps=None):
        """
        实例化时如果传入 driver，直接使用 传入的 driver，如果没有则判断 platform ，并生成对应的driver
        默认生成 selenium webdriver
        暂时只实现了web 和 android 平台
        :param platform: 平台，web android ios
        :param driver:
        :param desired_caps: Android 平台的 desired_capabilities
        """
        self.project_path = Common().parse_path().get("project_path")
        if driver is None:
            if platform == "web":
                webdriver = selenium.webdriver
                options = Options()
                options.debugger_address = "127.0.0.1:9999"
                self._driver = webdriver.Chrome(executable_path=ChromeDriver().get_driver(), options=options)
                self._driver.implicitly_wait(3)
            elif platform == "android":
                webdriver = appium_webdriver
                self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                self._driver.implicitly_wait(10)
            elif platform == "ios":
                pass
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
            self.log.info(f'访问地址：{self._base_url}')

    @except_windows
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_for_element(self, conditions, time=10):
        return WebDriverWait(self._driver, time).until(conditions)

    def wait_for_visible(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_invisible(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def wait_for_present(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def refresh(self):
        self._driver.refresh()

    def back(self):
        self._driver.back()

    def get_package(self) -> str:
        """
        获取当前运行的package
        :return:
        """
        value = self._driver.execute(Command.GET_CURRENT_PACKAGE)
        package = value.get("value")
        return package

    def app_start_activity(self, app_package: str, app_activity: str):
        """
        This is an Android-only method.
        :param app_package:
        :param app_activity:
        :return:
        """
        return self._driver.start_activity(app_package, app_activity)

    def app_current_activity(self) -> str:
        """
        This is an Android-only method.
        :return: str
        """
        current_activity = self._driver.current_activity
        self.log.info(f'===当前activity: {current_activity}')
        return current_activity

    def app_close(self, app_id):
        self._driver.terminate_app(app_id)

    def scroll_to_element(self, by, locator):
        while True:
            try:
                if self.find(by, locator).is_displayed():
                    return self.find(by, locator)
            except Exception as e:
                self.log.info("====: 未找到添加成员元素，滑动屏幕查找")
                size = self._driver.get_window_size()
                x = size.get('width') / 2
                y1 = size.get('height') / 4
                y2 = size.get('height') * 3 / 4
                self._driver.swipe(start_x=x, start_y=y2, end_x=x, end_y=y1)

    @property
    def driver(self):
        return self._driver

    def quit(self):
        self._driver.quit()

    def get_toast_element(self) -> WebElement:
        return self.wait_for_present((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'), 10)

    # 测试步骤的数据驱动
    def steps(self, path):
        name = inspect.stack()[1][3]
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)
        for method in steps:
            print(method.keys())
            if method.get(name):
                for step in method.get(name):
                    print(step)
                    if "by" in step.keys():
                        ele = self.find(step.get("by"), step.get("locator"))
                    if "action" in step.keys():
                        action = step.get("action")
                        if action == "click":
                            ele.click()
                        elif action == "text":
                            ele.text()
                        elif action == "send":
                            ele.send_keys(step.get("value"))

    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def picture_attach_allure(self):
        allure.attach(self._driver.get_screenshot_as_png())
        return