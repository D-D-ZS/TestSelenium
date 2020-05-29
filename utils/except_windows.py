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
    """
    意外弹窗处理。
    执行 func 函数，如果正常则重置显示等待并返回，
    如果异常则查找弹窗，首先查找 web 页面的 alert，如果未找到则查找黑名单元素，
    黑名单元素没有找到则抛出 func 的异常，如果找到 alert 或 黑名单元素则处理掉，并进入下一次循环。
    可处理多个弹窗重叠的情况。
    _black_list: 弹窗黑名单
    :param func: 传入的函数
    :return:
    """
    @wraps(func)
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
        # 获取调用 func 的实例对象，BasePage 类型对象
        instance: BasePage = args[0]
        # 调整显示等待时间，提高效率
        instance.driver.implicitly_wait(1)
        while True:
            try:
                # _num 记录找到的弹窗数量，每次循环重置
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
                # 如果没有找到弹窗则抛出func执行的异常
                if _num == 0:
                    raise e1
    return handle_except
