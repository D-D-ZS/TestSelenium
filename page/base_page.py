#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 10:03  
# Author  : DanDan Zhao 
# File    : base_page.py  
#
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging
from utils.log_helper import LogHelper

LogHelper().set_logger()


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            options = Options()
            options.debugger_address = "127.0.0.1:9999"
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)
            logging.info(f'访问地址：{self._base_url}')

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

    def wait_for_invisible(self, time, locator):
        return WebDriverWait(self._driver, time).until(
            expected_conditions.invisibility_of_element_located(locator)
        )