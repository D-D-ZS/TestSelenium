#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/19 10:09  
# Author  : DanDan Zhao 
# File    : test_delete_member.py  
#
from time import sleep

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
                             yaml.safe_load(open('C:\\Users\\shaun\\PycharmProjects\\TestSelenium\\data\\user.yml')))
    def test_delete_member(self, username):
        self.main.got_to_contacts().delete_member(username[0])
        sleep(1)
        re = self.main.got_to_contacts().get_name(username[0])
        assert re is None
