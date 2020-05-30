#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/30 17:27  
# Author  : DanDan Zhao 
# File    : app.py  
#
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from p_appium.xueqiu_page.main_page import MainPage
from utils.base import BasePage


class App(BasePage):
    def __init__(self, driver: WebDriver = None):
        desired_caps = dict()
        desired_caps["platformName"] = "Android"
        desired_caps["deviceName"] = "127.0.0.1:7555"
        desired_caps["noReset"] = True
        super().__init__(platform="android", driver=driver, desired_caps=desired_caps)

    def start_app(self):
        self.app_start_activity(app_package="com.xueqiu.android", app_activity=".view.WelcomeActivityAlias")
        return MainPage(driver=self._driver)

    def stop_app(self):
        self.app_close("com.xueqiu.android")
        return self

    def restart_app(self):
        self.stop_app().start_app()