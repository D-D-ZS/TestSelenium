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

    def update_page(self):
        try:
            current_page, total_page = [int(x) for x in
                                        self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text.split('/')]
        except Exception as e:
            current_page = total_page = 1
        return current_page, total_page

    # def get_name(self, username):
    #     while True:
    #         self.wait_for_click((By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox'))
    #         elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
    #         print(len(elements))
    #         for element in elements:
    #             print(username, element.get_attribute('title'))
    #             if username == element.get_attribute('title'):
    #                 print(username, element.get_attribute('title'))
    #                 return True
    #
    #         current_page, total_page = self.update_page()
    #         if current_page == total_page:
    #             return False
    #         else:
    #             self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1) .js_next_page').click()

    def get_member(self, username):
        while True:
            self.wait_for_click((By.CSS_SELECTOR, '.js_operationBar_footer>.js_add_member'))

            current_page, total_page = self.update_page()
            if current_page != 1:
                self.find(By.ID, 'menu_contacts')
                self.wait_for_click((By.CSS_SELECTOR, '.js_operationBar_footer>.js_add_member'))

            member_tr = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
            while len(member_tr) <= 0:
                member_tr = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')

            for tr in member_tr:
                member = tr
                name = member.find_element(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)').get_attribute("title")
                print(username, name)
                if username == name:
                    print(username, name)
                    return member
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
        else:
            print(f"没有用户：{username}")

    def get_name(self, username):
        member = self.get_member(username)
        if member is not None:
            return True
        else:
            return False
