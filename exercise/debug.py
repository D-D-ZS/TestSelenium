#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 19:00  
# Author  : DanDan Zhao 
# File    : debug.py  
#
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.mobilecommand import MobileCommand as Command
from appium import webdriver

from utils.base import BasePage

desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    # "appPackage": "com.tencent.wework",
    # "appActivity": ".launch.WwMainActivity",
    # "noReset": True
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias"
}


class TestAsert(BasePage):
    pass


if __name__ == '__main__':
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    sleep(5)
    k_v = driver.activate_app("com.tencent.wework")
    print(k_v)
    driver.terminate_app("com.tencent.wework")
    # t = TestAsert(driver=driver)
    # # print(t._driver)
    # sleep(15)
    # t.find(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()

# package = driver.execute(Command.GET_CURRENT_PACKAGE)
# print(type(package.get("value")))
# aa = driver.start_activity("com.tencent.wework", ".launch.WwMainActivity")
# driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/drb" and @text="通讯录"]').click()
# print(driver.current_activity)
# size = driver.get_window_size()
# x = size.get('width')/2
# y1 = size.get('height')/4
# y2 = size.get('height')*3/4
# av = driver.swipe(start_x=x, start_y=y2, end_x=x, end_y=y1)
# # print(av)

# 通讯录添加成员 activity .friends.controller.MemberInviteMenuActivity
