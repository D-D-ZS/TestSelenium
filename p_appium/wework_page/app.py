#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/30 0:12  
# Author  : DanDan Zhao 
# File    : app.py  
# 
# APP 操作类
from p_appium.wework_page.main_page import MainPage
from utils.base import BasePage


class App(BasePage):
    def start_app(self):
        self.app_start_activity(app_package="com.tencent.wework", app_activity=".launch.WwMainActivity")
        return MainPage(driver=self._driver)

    def stop_app(self):
        self.app_close("com.tencent.wework")

    def restart_app(self):
        self.stop_app()
        self.start_app()
