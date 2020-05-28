#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 10:03  
# Author  : DanDan Zhao 
# File    : base_page.py  
#
import selenium
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utils.log_helper import LogHelper
from utils.chromedriver_helper import ChromeDriver
import appium
from appium import webdriver as appium_webdriver


class BasePage:
    _base_url = ""
    _driver = None
    log = LogHelper().set_logger()

    def __init__(self, platform="web", driver: WebDriver = None, desired_caps=None):
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

    def wait_for_present(self,  locator, time=10):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def refresh(self):
        self._driver.refresh()

    def app_back(self):
        """
        only for Android
        :return:
        """
        self._driver.keyevent(4)
