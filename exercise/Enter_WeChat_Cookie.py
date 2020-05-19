#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/14 21:36  
# Author  : DanDan Zhao 
# File    : Enter_WeChat_Cookie.py  
# 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def get_web_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    print("请扫码登录")
    WebDriverWait(driver, 60, 0.5).until(EC.presence_of_element_located((By.ID, "menu_contacts")))
    cookies = driver.get_cookies()
    print(cookies)
    driver.quit()
    return cookies


class TestCookie:
    def setup_class(self):
        self.cookies = get_web_cookie()

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in self.cookies:
            print(cookie)
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown_method(self):
        self.driver.quit()

    def test_address_book(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # for cookie in self.cookies:
        #     print(cookie)
        #     if "expiry" in cookie:
        #         cookie.pop("expiry")
        #     self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_contacts").click()
        sleep(2)

    def test_menu_apps(self):
        self.driver.find_element_by_id("menu_apps").click()
        sleep(2)





