#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/19 10:09  
# Author  : DanDan Zhao 
# File    : test_delete_member.py  
#

import pytest
import yaml

from page.main_page import Main


class TestDeleteMember:
    def setup(self):
        self.main = Main()
        self._driver = self.main._driver

    def teardown(self):
        self._driver.quit()

    @pytest.mark.parametrize("username",
                             yaml.safe_load(open('C:\\Users\\shaun\\PycharmProjects\\TestSelenium\\data\\user_name_list.yml')))
    def test_delete_member(self, username):
        self.main.got_to_contacts().delete_member(username)
        result = self.main.got_to_contacts().get_name(username)
        assert result is False
