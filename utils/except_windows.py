#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/29 15:05  
# Author  : DanDan Zhao 
# File    : except_windows.py  
# 
# 装饰器处理意外弹窗
from functools import wraps

from selenium.webdriver.common.by import By


def except_windows(func):
    def handle_except(*args, **kwargs):
        from utils.base import BasePage
        _black_list = [
            (By.XPATH, '//*[@text="确定"]'),
            (By.XPATH, '//*[@text="好"]'),
            (By.XPATH, '//*[@text="知道了"]'),
            (By.XPATH, '//*[@resource-id="com.xueqiu.android:id/image_cancel"]'),
            (By.XPATH, '//*[@text="无视"]'),
            (By.XPATH, '//*[@text="以后再说"]'),
            (By.XPATH, '//*[@text="关闭"]'),
            (By.XPATH, '//*[@text="以了解"]'),
            (By.XPATH, '//*[@text="允许"]')
        ]
        instance: BasePage = args[0]
        instance.driver.implicitly_wait(1)
        while True:
            try:
                _num = 0
                ele = func(*args, **kwargs)
                instance.driver.implicitly_wait(5)
                return ele
            except Exception as e1:
                try:
                    instance.driver.switch_to.alert.accept()
                    _num += 1
                    instance.log.info(f'===找到 alert ')
                except Exception as e2:
                    instance.log.info(f'===未查找到 alert : {e2}')
                    for locator in _black_list:
                        elements = instance.driver.find_elements(*locator)
                        if len(elements) > 0:
                            for element in elements:
                                instance.log.info(f'===找到弹窗: {element.text}')
                                _num += 1
                                element.click()
                            break
                        else:
                            instance.log.info(f'===未查找到可定位的弹窗 {locator}')
                if _num == 0:
                    raise e1
    return handle_except
