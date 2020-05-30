#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/30 23:30  
# Author  : DanDan Zhao 
# File    : test_base.py  
#
from p_appium.xueqiu.page.app import App


class TestBase:
    def setup_class(self):
        self.base = App().start_app()

    def teardown_class(self):
        self.base.quit()
