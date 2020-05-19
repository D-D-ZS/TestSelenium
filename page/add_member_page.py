#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 11:31  
# Author  : DanDan Zhao 
# File    : add_member_page.py
#
from selenium.webdriver.common.by import By

from page.base_page import BasePage


class AddMember(BasePage):
    def add_member(self, username, account, phone):
        self.wait_for_click((By.ID, 'username'), 15).send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(account)
        self.find(By.ID, 'memberAdd_phone').send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_member_editor_form>div:nth-child(1)>a:nth-child(2)').click()
