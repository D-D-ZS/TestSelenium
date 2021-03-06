#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/18 11:05  
# Author  : DanDan Zhao 
# File    : test_add_member.py  
#

import pytest
import yaml
import os

from web.page.main_page import Main
from utils.log_helper import LogHelper
from utils.common import Common

LogHelper().set_logger()


class TestAddMember:
    data_path = Common().parse_path().get("data_path")

    def setup(self):
        self.main = Main()
        self._driver = self.main._driver

    def teardown(self):
        self._driver.quit()

    # @pytest.mark.skip
    @pytest.mark.parametrize("username, account, phone",
                             yaml.safe_load(open(os.path.join(data_path, "user.yml"))))
    def test_add_member(self, username, account, phone):
        self.main.got_to_contacts().go_to_add_member().add_member(username, account, phone)
        result = self.main.got_to_contacts().get_name(username)
        assert result
