#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/20 10:33  
# Author  : DanDan Zhao 
# File    : test_fist_appium.py  
#
import json

from appium import webdriver
from selenium.webdriver.common.by import By


def test_start():
    desired_caps = {
      "platformName": "Android",
      "deviceName": "127.0.0.1:7555",
      "appPackage": "com.xueqiu.android",
      "appActivity": ".common.MainActivity",
        "noRest": True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(20)
    els1 = driver.find_elements_by_id("com.xueqiu.android:id/title_text")
    els2 = driver.find_elements_by_id("com.xueqiu.android:id/title_text")
    el1 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
    el1.click()
    el1.click()
    el2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.TextView")
    el2.click()

    driver.quit()

