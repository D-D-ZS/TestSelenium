#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/16 23:48  
# Author  : DanDan Zhao 
# File    : test_handle.py  
# 

from exercise.base import Base


class TestHandle(Base):
    def test_handle(self):
        """
        handle 是浏览器窗口的句柄，当打开新页面时句柄其实还是在之前的页面，因此导致无法定位到新页面的元素。
        因此需要通过切换句柄，使当前控制进入新页面，这样就可以定位新页面的内容
        """
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').click()
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[-1])
        print(self.driver.window_handles)
        self.driver.find_element_by_xpath('//*[@id="channel-shanghai"]/div/ul/li[4]/a').click()