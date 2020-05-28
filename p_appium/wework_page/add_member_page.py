#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 14:25  
# Author  : DanDan Zhao 
# File    : add_member_page.py  
#
from appium.webdriver.common.mobileby import MobileBy

from utils.base import BasePage


class AddMemeberPage(BasePage):
    def go_to_wechat_invite(self):
        pass

    def go_to_add_from_contacts(self):
        pass

    def go_to_manual(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/h3a').click()
        self.wait_for_click((MobileBy.XPATH, '//*[@reourse-id="com.tencent.wework:id/au8" and @text="姓名"]/../[@resource-id="com.tencent.wework:id/au7"]'))
        return True