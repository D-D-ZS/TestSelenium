#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 13:59  
# Author  : DanDan Zhao 
# File    : main_page.py  
#
from appium.webdriver.common.mobileby import MobileBy

from utils.base import BasePage


class MainPage(BasePage):

    def go_to_contacts(self):
        self.find(MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/drb and @text="通讯录"]').click()
        self.wait_for_visible((MobileBy.ID, 'com.tencent.wework:id/d94'), 10)
        return True

    def go_to_oa(self):
        self.find(MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/drb and @text="工作台"]').click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/gv4 and @text="工作台"]'), 10)
        return True

    def go_to_mine(self):
        self.find(MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/drb and @text="我"]').click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/gv4 and @text="我"]'), 10)
        return True
