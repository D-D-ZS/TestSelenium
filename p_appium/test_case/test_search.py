#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/22 17:21  
# Author  : DanDan Zhao 
# File    : test_search.py  
#
import pytest

from p_appium.xueqiu_page.main_page import MainPage


class TestSearch:
    desired_caps = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:7555",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "noReset": True
    }

    def setup(self):
        self.base = MainPage(platform='android', desired_caps=self.desired_caps)

    def teardown(self):
        self.base._driver.quit()
        
    @pytest.mark.parametrize("stock_name", ["阿里巴巴", "小米", "中国平安"])
    def test_search(self, stock_name):
        result = self.base.go_to_search()
        # assert result[0] != result[1]