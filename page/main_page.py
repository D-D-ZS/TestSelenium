#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 10:04  
# Author  : DanDan Zhao 
# File    : main.py  
#
from selenium.webdriver.common.by import By

from page.add_member_page import AddMember
from page.base_page import BasePage
from page.contacts_page import ContactsPage


class Main(BasePage):

    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def got_to_contacts(self):
        self.find(By.ID, "menu_contacts").click()
        return ContactsPage(self._driver)

    # def go_to_apps(self):
    #     self._driver.find_element(By.ID, "menu_apps").click()
    #     return apps()
    def add_member(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt.js_service_list > a:nth-child(1)').click()
        return AddMember(self._driver)
