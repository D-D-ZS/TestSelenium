#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/21 10:35  
# Author  : DanDan Zhao 
# File    : common.py  
#
import os
import sys
import zipfile


def kill_pid(pid):
    if sys.platform == 'win32':
        os.system(f"taskkill /pid {pid}")
    else:
        os.system(f"kill {pid}")


class Common:
    def unzip_file(self, zif_filename, unzip_filename):
        if not os.path.exists(zif_filename):
            raise Exception(f'{zif_filename} not found')
        if not zipfile.is_zipfile(zif_filename):
            raise Exception(f'{zif_filename} is not a zip file')
        z = zipfile.ZipFile(zif_filename)
        z.extractall(unzip_filename)

    def parse_path(self) -> dict:
        project_path = os.path.dirname(os.path.dirname(__file__))
        config_path = os.path.join(project_path, 'config')
        data_path = os.path.join(project_path, 'data')
        log_path = os.path.join(project_path, 'logs')
        report_path = os.path.join(project_path, 'report')
        return {"project_path": project_path, "config_path": config_path, "data_path": data_path, "log_path": log_path,
                "report_path": report_path}
