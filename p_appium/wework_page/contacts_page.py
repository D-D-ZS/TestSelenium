#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 14:18  
# Author  : DanDan Zhao 
# File    : contacts_page.py  
#
from appium.webdriver.common.mobileby import MobileBy

from utils.base import BasePage


class ContactsPage(BasePage):
    def go_to_add_member(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/u').click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/gv4 and @text="添加成员"]'), 10)
        return True

    def go_to_external(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/h1x').click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id=com.tencent.wework:id/gv4 and @text="外部联系人"]'), 10)