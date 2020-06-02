#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/6/1 18:02  
# Author  : DanDan Zhao 
# File    : conftest.py  
#
import os
import shlex
import signal
import subprocess
import time

import allure

from utils.common import kill_pid

import pytest


@pytest.fixture(autouse=True)
def record():
    filename = f'{time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))}.mp4'
    cmd = shlex.split(f"scrcpy -r {filename}")
    p = subprocess.Popen(cmd, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # os.system(f"scrcpy -r {filename}.mp4")
    yield
    # with open(filename, "rb") as f:
    #     file = f.read()
    #     allure.attach(file, name="用例录屏", attachment_type=allure.attachment_type.MP4)
    allure.attach.file(filename, name="用例录屏", attachment_type=allure.attachment_type.MP4)
    kill_pid(p.pid)
