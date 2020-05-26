#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/26 19:48  
# Author  : DanDan Zhao 
# File    : test_browser.py  
#
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from utils.chromedriver_helper import ChromeDriver


class TestBrowser:
    desired_caps = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:7555",
        "browserName": "Browser",
        # "browserName": "Chrome",
        # "appPackage": "com.xueqiu.android",
        # "appActivity": ".view.WelcomeActivityAlias",
        "noReset": True,
        # "chromedriverChromeMappingFile": "C:\\Users\\shaun\\PycharmProjects\\TestSelenium\\config\\chromedriver.json",
        # "chromedriverExecutable": f"{ChromeDriver().get_android_driver(version='2.24')}"
        "chromedriverExecutableDir": "C:\\Users\\shaun\\PycharmProjects\\TestSelenium\\chromedriver"
    }

    def setup(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_xueqiu_webview(self):
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']").click()
        print(self.driver.contexts)
        print(self.driver.current_context)
        # print(self.driver.current_window_handle)
        self.driver.find_element(MobileBy.XPATH, "//*[@content-desc='A股开户']").click()
        sleep(5)
        print(self.driver.contexts)
        # self.driver.switch_to.context()
        # print(self.driver.window_handles)
        # self.driver.find_element(MobileBy.ID, 'phone-number').click()
        # self.driver.find_element(MobileBy.ID, 'phone-number').send_keys('11111111111')

    def test_baidu(self):
        self.driver.get('http://m.baidu.com')
        sleep(5)
