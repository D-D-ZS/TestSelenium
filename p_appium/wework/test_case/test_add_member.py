#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 13:51  
# Author  : DanDan Zhao 
# File    : test_add_member.py  
#
import os

import yaml

from p_appium.wework.page.main_page import MainPage
from utils.chromedriver_helper import ChromeDriver
from utils.base import BasePage
import pytest

from utils.common import Common


class TestAddMember:
    desired_caps = {
        "platformName": "Android",
        "deviceName": "127.0.0.1:7555",
        "appPackage": "com.tencent.wework",
        "appActivity": ".launch.WwMainActivity",
        "noReset": True
    }
    data_path = Common().parse_path().get("data_path")

    def setup_class(self):
        self.main_page = MainPage(platform="android", desired_caps=self.desired_caps)

    def teardown_class(self):
        self.main_page.quit()

    def teardown(self):
        self.main_page.back()

    @pytest.mark.parametrize("username, address, mobile_phone",
                             yaml.safe_load(open(os.path.join(data_path, 'user.yml'))))
    def test_add_member(self, username, address, mobile_phone):
        page = self.main_page.go_to_contacts().go_to_add_member().go_to_manual().add_member(username=username,
                                                                                            address=address,
                                                                                            mobile_phone=mobile_phone)
        result = page.get_toast()
        assert "成功" in result
