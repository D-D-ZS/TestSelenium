#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/20 22:15  
# Author  : DanDan Zhao 
# File    : chromedriver_helper.py  
#
import os
import re
import sys

import requests

from utils.common import Common
import wget

common = Common()


class ChromeDriver:
    _chrome_data = "C:\\Users\shaun\\AppData\\Local\\Google\\Chrome\\User Data\\Last Version"
    _driver_path = 'C:\\Users\\shaun\\PycharmProjects\\TestSelenium\\chromedriver'
    _mirror = 'http://npm.taobao.org/mirrors/chromedriver/'

    def get_driver(self, chrome_data=_chrome_data, driver_path=_driver_path, mirror=_mirror):
        if sys.platform == 'win32':
            zip_driver = "chromedriver_win32.zip"
        elif sys.platform == 'linux':
            zip_driver = 'chromedriver_linux64.zip'
        elif sys.platform == 'darwin':
            zip_driver = 'chromedriver_mac64.zip'
        else:
            raise Exception(f'不支持当前系统：{sys.platform}')
        with open(chrome_data) as f:
            version = f.readline()
        version_path = os.path.join(driver_path, version)
        # print(driver_path, version_path)

        def get_file(version):
            url = mirror + '/' + version + '/' + zip_driver
            try:
                wget.download(url, version_path)
            except Exception as e:
                response = requests.get(mirror)
                version1 = version.split('.')[0:3]
                # print(version1)
                # print(response.text)
                pattern = f'>({version1[0]}.{version1[1]}.{version1[2]}\.\d+)'
                pattern = re.compile(pattern)
                html = response.text
                last_v = []
                final_v = ''
                for line in html.split('\n'):
                    if re.search(pattern, line):
                        v = re.findall(pattern, line)[0]
                        last_v.append(v.split('.')[-1])
                        if len(last_v) == 2:
                            if int(last_v[1]) - int(last_v[0]) > 0:
                                final_v = last_v[1]
                            else:
                                final_v = last_v[0]
                version = f'{version1[0]}.{version1[1]}.{version1[2]}.{final_v}'
                url = mirror + '/' + version + '/' + zip_driver
                # print(url)
                wget.download(url, version_path)
            finally:
                common.unzip_file(os.path.join(version_path, zip_driver), version_path)

        if not os.path.exists(version_path):
            os.makedirs(version_path)
            get_file(version)
            return os.path.join(version_path, "chromedriver.exe")
        elif not os.path.exists(os.path.join(version_path, "chromedriver.exe")):
            # get到对应版本的文件
            get_file(version)
            return os.path.join(version_path, "chromedriver.exe")
        else:
            return os.path.join(version_path, "chromedriver.exe")
