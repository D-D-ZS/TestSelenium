#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/20 10:33  
# Author  : DanDan Zhao 
# File    : test_fist_appium.py  
#
import json
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAppium:

    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("stock_name", ["阿里巴巴"])
    def test_search(self, stock_name):
        """
        搜索框搜索阿里巴巴
        判断是否有阿里巴巴
        点击第一个阿里巴巴
        点击添加自选按钮
        断言，TextView内容变化
        :return:
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys(stock_name)
        self.driver.find_element(MobileBy.XPATH, f"//*[@resource-id='com.xueqiu.android:id/name' and @text='{stock_name}']").click()
        # 加自选
        ele = self.driver.find_element(MobileBy.XPATH, f"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../../android.widget.LinearLayout[3]/android.widget.TextView")
        before = ele.text
        ele.click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((MobileBy.XPATH, f"//*[@resource-id='com.xueqiu.android:id/stockName' and @text='阿里巴巴']/../../android.widget.LinearLayout[3]/android.widget.TextView")))
        after = ele.text
        print(before, after)
        assert before != after
