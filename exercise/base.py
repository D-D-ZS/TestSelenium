#!/usr/bin/env python
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/16 23:48  
# Author  : DanDan Zhao 
# File    : base.py  
#
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
