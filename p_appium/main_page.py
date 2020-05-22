#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/22 16:33  
# Author  : DanDan Zhao 
# File    : main_page.py  
#
# import logging
from appium.webdriver.common.mobileby import MobileBy

from p_appium.search_page import SearchPage
from utils.base import LogHelper
from utils.base import BasePage

# logger = LogHelper().set_logger()


class MainPage(BasePage):

    def go_to_search(self):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.log.info(f"====android====: 进入搜索页")
        return SearchPage(self._driver)