#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/30 21:23  
# Author  : DanDan Zhao 
# File    : market.py  
#
from appium.webdriver.common.mobileby import MobileBy

from p_appium.xueqiu_page.search_page import SearchPage
from utils.base import BasePage


class MarketPage(BasePage):
    def go_to_search(self):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/action_search').click()
        self.wait_for_visible((MobileBy.ID, 'com.xueqiu.android:id/search_input_text'))
        return SearchPage(driver=self.driver)