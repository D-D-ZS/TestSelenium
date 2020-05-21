#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 10:21  
# Author  : DanDan Zhao 
# File    : contacts.py  
#
import logging

from selenium.webdriver.common.by import By

from page.add_member_page import AddMember
from page.base_page import BasePage
from utils.log_helper import LogHelper

logger = LogHelper()
logger.set_logger()


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

    def get_name1(self, username):
        while True:
            self.wait_for_click((By.CSS_SELECTOR, '.member_colRight_memberTable_th_Checkbox'))
            elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            print(len(elements))
            for element in elements:
                print(username, element.get_attribute('title'))
                if username == element.get_attribute('title'):
                    print(username, element.get_attribute('title'))
                    return True

            current_page, total_page = self.update_page()
            if current_page == total_page:
                return False
            else:
                self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1) .js_next_page').click()

    def get_member(self, username):
        # current_page, total_page = self.update_page()
        # logging.info(f'delete===:当前页码:{current_page}')
        # if current_page != 1:
        #     self.find(By.ID, 'menu_contacts')
        #     self.wait_for_click((By.CSS_SELECTOR, '.js_operationBar_footer>.js_add_member'))
        #     logging.info('delete===:点击通讯录页标签')

        while True:
            current_page, total_page = self.update_page()
            logging.info(f'delete===:当前页码:{current_page}')
            self.wait_for_click((By.CSS_SELECTOR, '.js_operationBar_footer>.js_add_member'))
            member_tr = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
            logging.info(f'delete===:第一次获取 member 列表，共有成员{len(member_tr)}个')
            while len(member_tr) <= 0:
                member_tr = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
                logging.info(f'delete===:第一次获取失败，再次获取，共有成员{len(member_tr)}个')
            loop = 1
            for member in member_tr:
                logging.debug(f'delete===:读取成员{member}')
                try:
                    self.wait_for_click((By.CSS_SELECTOR, f'.member_colRight_memberTable_tr:nth-child({loop})>.member_colRight_memberTable_td:nth-child(2)'))
                    member_info = member.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td')
                    # name = member.find_element(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)').get_attribute("title")
                    name = member_info[1].get_attribute("title")
                    logging.debug(f'delete===:获取第{loop}个成员名称：{name}')
                    if username == name:
                        logging.info(f'delete===:成员名称{username}在通讯录中（{name}），返回')
                        return member_info
                except Exception as e:
                    logging.error(f'delete===:获取成员名称失败 {e}')
                finally:
                    loop += 1
            current_page, total_page = self.update_page()
            if current_page == total_page:
                logging.info(f'delete===:成员名称{username}不在通讯录中，返回')
                return None
            else:
                self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1) .js_next_page').click()
                logging.info(f'delete===:当前页没有找到成员名称{username}，进入下一页')

    def delete_member(self, username):
        member_info = self.get_member(username)
        if member_info is not None:
            member_info[0].click()
            self.find(By.CSS_SELECTOR, '.js_has_member>.ww_operationBar:nth-child(1)>.js_delete').click()
            ele = self.wait_for_click((By.CSS_SELECTOR, '[d_ck=submit]'))
            ele.click()
        else:
            logging.error(f"delete===:没有用户：{username}")

    def get_name(self, username):
        member_info = self.get_member(username)
        if member_info is not None:
            return True
        else:
            return False
