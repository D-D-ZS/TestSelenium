#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/17 0:35  
# Author  : DanDan Zhao 
# File    : test_js.py  
# 
"""
selenium 可以执行JavaScript 脚本
execute_script: 执行JS
return： 返回JS的返回结果
execute_script：argument 传参
可以进行时间控件的操作，因为时间控件都是只读属性的。需要定位到时间控件，并将read only属性去掉
"""
from time import sleep

import pytest

from exercise.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_scroll_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("测试")
        ele = self.driver.execute_script('return document.getElementById("su")')
        ele.click()

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("ele=document.getElementById('train_date');ele.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-06-18'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(5)