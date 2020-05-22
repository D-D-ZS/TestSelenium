#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/21 10:35  
# Author  : DanDan Zhao 
# File    : common.py  
#
import os
import zipfile


class Common:
    def unzip_file(self, zif_filename, unzip_filename):
        if not os.path.exists(zif_filename):
            raise Exception(f'{zif_filename} not found')
        if not zipfile.is_zipfile(zif_filename):
            raise Exception(f'{zif_filename} is not a zip file')
        z = zipfile.ZipFile(zif_filename)
        z.extractall(unzip_filename)
