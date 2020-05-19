#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/7/10 12:04  
# Author  : DanDan Zhao 
# File    : wait_test.py  
# 
# selenium 的三种等待
# 直接等待: 使用 time.sleep(5) 直接等待预期的时间
# 隐式等待：implicitly_wait 通过一定的时长等待页面上某元素加载完成。如果超出设置的时长元素还没有被加载，则抛出NoSuchElementException异常
# 显示等待：等待某个条件成立时继续执行，否则达到最大时长时抛出超时异常

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import *

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


def wait1():
    """
    WebDriverWait 类时由WebDriver 提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常
    expected_conditions 类提供预期结果判断，包括多种方法
    """
    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, "kw")))
    element.send_keys('selenium')
    # 通过 is_displayed() 判断元素是否出现
    el = driver.find_element_by_id("kw")
    for i in range(10):
        try:
            if el.is_displayed():
                break
        except: pass
        sleep(1)
    else:
        print("time out")
    driver.quit()


def wait2():
    """
    implicitly_wait() 方法实现隐式等待，隐式等待是通过一定的时长等待页面上某元素加载完成。如果超出设置的时长元素还没有被加载，则抛出NoSuchElementException异常
    默认为0秒，该方法默认参数的单位为秒，设置值并非固定的等待时间，并不影响脚本的执行速度。
    并不针对页面上的某一个元素进行等待。当脚本执行到某个元素定位时，如果元素可以定位，则继续执行，如果定位不到，则以轮询的当时不断的判断元素是否被定位到。
    全局变量。
    """
    driver.implicitly_wait(20)
    driver.get("http://www.baidu.com")
    try:
        print(ctime())
        driver.find_element_by_id("kw22").send_keys("selenium")
    except Exception as e:
        print(e)
    finally:
        print(ctime())
        driver.quit()


if __name__ == '__main__':
    wait2()