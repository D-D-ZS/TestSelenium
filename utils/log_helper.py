#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/19 20:26  
# Author  : DanDan Zhao 
# File    : logging.py  
#
import logging
import os

import yaml


class LogHelper():

    def set_logger(self):
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/config.yml')
        config = yaml.safe_load(open(path)).get('logging')
        filename = config.get('path')
        level = config.get('level')
        if level == 'info':
            level = logging.INFO
        elif level == 'debug':
            level = logging.DEBUG
        elif level == 'warn':
            level = logging.WARN
        elif level == 'error':
            level = logging.ERROR
        else:
            logging.error('日志等级配置出错')
        log_format = config.get('format')
        encode = config.get('encode')
        h = logging.FileHandler(filename=filename, encoding=encode)
        logging.basicConfig(level=level, format=log_format, handlers=[h])
        return logging
