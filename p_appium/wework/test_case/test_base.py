#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/30 23:22  
# Author  : DanDan Zhao 
# File    : test_base.py  
#
from p_appium.wework.page.main_page import MainPage


class TestBase:
    def setup(self):
        self.main_page = MainPage(platform="android", desired_caps=self.desired_caps)
