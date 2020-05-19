#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/6/28 15:07  
# Author  : DanDan Zhao 
# File    : control_browser_test.py  
# 
# 控制浏览器操作

from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
# 设定窗口大小，默认设置当前窗口
driver.set_window_size(500, 300)
sleep(2)
# 放大窗口
driver.maximize_window()
sleep(2)
# 控制浏览器前进后退
driver.get("http://www.baidu.com")
print("first url: http://www.baidu.com")
driver.get("http://news.baidu.com")
print("second url: http://news.baidu.com")
# 后退到百度首页
driver.back()
print("back to: ", driver.current_url)
# 前进到新闻页
driver.forward()
print("forward to: ", driver.current_url)
sleep(2)
# 模拟浏览器刷新
driver.refresh()
sleep(2)
driver.quit()
