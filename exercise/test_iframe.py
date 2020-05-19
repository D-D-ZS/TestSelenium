#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/16 23:41  
# Author  : DanDan Zhao 
# File    : test_iframe.py
# 

"""
有时候会发现不管怎么都定位不到某个元素，这个元素可能是在frame中。
frame 是HTML中的框架，HTML中所谓的框架就是在同一个浏览器显示不止一个页面。
frame 标签有三类，frameset, frame, iframe
frame 中的元素可以使用switch_to方法切换到frame 之后进行定位

以有道邮箱登录页面为例
"""
from exercise.base import Base


class TestIframe(Base):
    def test_iframe(self):
        self.driver.get("https://mail.163.com/index.htm")
        # 由于登录表单在frame中，导致如下直接find无法定位到元素
        # self.driver.find_element_by_name("email").send_keys("username")
        # self.driver.find_element_by_name("password").send_keys("123")
        # 需要先切换到对应frame，之后再定位元素
        # :Usage:
        #   driver.switch_to.frame('frame_name')
        #   driver.switch_to.frame(1)
        #   driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_name("email").send_keys("username")
        self.driver.find_element_by_name("password").send_keys("123")