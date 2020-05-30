#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 14:18  
# Author  : DanDan Zhao 
# File    : contacts_page.py  
#
from appium.webdriver.common.mobileby import MobileBy

from p_appium.wework.page.add_member_page import AddMemberPage
from p_appium.wework.page.external_page import ExternalPage
from utils.base import BasePage


class ContactsPage(BasePage):
    def go_to_add_member(self):
        ele = self.scroll_to_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/h1x"]/*[@text="添加成员"]')
        # ele2 = self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/h1x"]/*[@text="添加成员"]')
        ele.click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gv4" and @text="添加成员"]'), 10)
        self.log.info("to_page===: 进入添加成员页面")
        return AddMemberPage(driver=self._driver)

    def go_to_external(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/h1x"]/[@text="外部联系人"]').click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/gv4" and @text="外部联系人"]'), 10)
        self.log.info("to_page===: 进入外部联系人页面")
        return ExternalPage(driver=self._driver)
