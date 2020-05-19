#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 10:21  
# Author  : DanDan Zhao 
# File    : contacts.py  
#
from selenium.webdriver.common.by import By

from page.add_member_page import AddMember
from page.base_page import BasePage


class ContactsPage(BasePage):

    def go_to_add_member(self):
        ele = self.wait_for_click((By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1)>.js_add_member'))
        ele.click()

        def is_visible(x):
            num = len(self.finds(By.ID, 'username'))
            if num > 0:
                return True
            else:
                self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1)>.js_add_member').click()
                return False

        self.wait_for_element(is_visible)
        return AddMember(self._driver)

    def get_member_names(self):
        names = []
        while True:
            self.wait_for_click((By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox'))
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            for element in elements:
                names.append(element.get_attribute("title"))
            current_page, total_page = [int(x) for x in
                                        self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text.split('/')]
            if current_page == total_page:
                return names
            else:
                self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1) .js_next_page').click()

    def get_member(self, username):
        while True:
            # self.wait_for_click((By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox'))
            self.wait_for_click((By.CSS_SELECTOR, '.js_operationBar_footer>.js_add_member'))
            # elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            member_tr = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
            while len(member_tr) <= 0:
                member_tr = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
            for tr in member_tr:
                name = tr.find_element(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
                print(name)
                if username == name.get_attribute("title"):
                    return tr
            try:
                current_page, total_page = [int(x) for x in
                                            self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text.split('/')]
            except Exception as e:
                current_page = 0
                total_page = 0

            if current_page == total_page:
                return None
            else:
                self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1) .js_next_page').click()

    def delete_member(self, username):
        tr = self.get_member(username)
        if tr is not None:
            tr.find_element(By.CSS_SELECTOR, '.member_colRight_memberTable_td_Checkbox').click()

        self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1)>.js_delete').click()
        ele = self.wait_for_click((By.CSS_SELECTOR, '[d_ck=submit]'))
        ele.click()

    def get_name(self, username):
        tr = self.get_member(username)
        if tr is not None:
            name = tr.find_element(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)').get_attribute(
                'title')
            return name
        else:
            return None
