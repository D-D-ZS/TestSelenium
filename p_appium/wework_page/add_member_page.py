#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 14:25  
# Author  : DanDan Zhao 
# File    : add_member_page.py  
#
from appium.webdriver.common.mobileby import MobileBy

from p_appium.wework_page.manual_add_page import ManualAddPage
from utils.base import BasePage


class AddMemberPage(BasePage):
    def go_to_wechat_invite(self):
        pass

    def go_to_add_from_contacts(self):
        pass

    def go_to_manual(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/h3a').click()
        self.wait_for_click((MobileBy.ID, 'com.tencent.wework:id/au7'), 10)
        return ManualAddPage(driver=self._driver)

    def get_toast(self):
        # 抓取toast信息
        status_ele = self.wait_for_present((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'), 10)
        return status_ele.text
