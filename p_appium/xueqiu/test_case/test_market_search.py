#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/22 17:21  
# Author  : DanDan Zhao 
# File    : test_search.py  
#
import pytest

from p_appium.xueqiu.page.app import App
from p_appium.xueqiu.page.search_page import SearchPage
from p_appium.xueqiu.test_case.test_base import TestBase


class TestSearch(TestBase):

    # def setup_class(self):
    #     self.base = App().start_app()

    def teardown(self):
        SearchPage(driver=self.base.driver).cancel()

    # def teardown_class(self):
    #     self.base.quit()
        
    @pytest.mark.parametrize("stock_name", ["阿里巴巴", "小米概念", "中国平安"])
    def test_search(self, stock_name):
        result = self.base.go_to_market().go_to_search().search_stock(stock_name).get_toast()
        if "添加成功" or "已从自选删除" in result:
            assert True
        else:
            assert False
