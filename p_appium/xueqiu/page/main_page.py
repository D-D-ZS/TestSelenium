#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/22 16:33  
# Author  : DanDan Zhao 
# File    : main_page.py  
#
# import logging
import os

import yaml
from appium.webdriver.common.mobileby import MobileBy

from p_appium.xueqiu.page.market_page import MarketPage
from p_appium.xueqiu.page.search_page import SearchPage
from utils.base import BasePage

# logger = LogHelper().set_logger()


class MainPage(BasePage):

    def go_to_search(self):
        # self.find(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.steps(os.path.join(self.project_path, "p_appium/xueqiu/page/main.yml"))
        self.log.info(f"====android====: 进入搜索页")
        return SearchPage(driver=self.driver)

    def go_to_market(self):
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="行情"]').click()
        # self.wait_for_visible((MobileBy.ID, 'com.xueqiu.android:id/action_search'))
        self.steps(os.path.join(self.project_path, "p_appium/xueqiu/page/main.yml"))
        self.log.info(f"====android====: 进入行情页")
        return MarketPage(driver=self.driver)
