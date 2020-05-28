#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/22 17:15  
# Author  : DanDan Zhao 
# File    : search_page.py  
#
from appium.webdriver.common.mobileby import MobileBy

from utils.base import BasePage


class SearchPage(BasePage):

    def SearchStock(self, stock_name):
        """
                搜索框搜索阿里巴巴
                判断是否有阿里巴巴
                点击第一个阿里巴巴
                点击添加自选按钮
                断言，TextView内容变化
                :return:
                """
        self.find('com.xueqiu.android:id/tv_search').click()
        self.find('com.xueqiu.android:id/search_input_text').send_keys(stock_name)
        self.find(MobileBy.XPATH, f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{stock_name}']").click()
        # 加自选
        ele = self.find(MobileBy.XPATH, f"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../../android.widget.LinearLayout[3]/android.widget.TextView")
        before = ele.text
        ele.click()
        self.wait_for_click((MobileBy.XPATH, f"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../../android.widget.LinearLayout[3]/android.widget.TextView"), 10)
        after = ele.text
        return before, after
