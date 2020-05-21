#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/6/27 11:11  
# Author  : DanDan Zhao 
# File    : test1.py  
# 
from selenium import webdriver

from utils.chromedriver_helper import ChromeDriver

driver = webdriver.Chrome(executable_path=ChromeDriver().get_driver())
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()