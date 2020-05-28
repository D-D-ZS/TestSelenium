#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2020/5/28 14:39  
# Author  : DanDan Zhao 
# File    : manual_add.py  
#
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from utils.base import BasePage


class ManualAddPage(BasePage):
    def add_member(self, username, account="", alias="", gender="", mobile_phone="", phone="", mail="", address="", position="", department="", identity=""):
        """
        username 必填
        phone 和 mail 至少填写一个
        （模拟器上还要填写一下地址才能保存）
        :param identity: 身份
        :param account: 账号
        :param alias: 别名
        :param mobile_phone: 手机号码 和 邮箱必须填其一
        :param username: 用户名 必填
        :param phone: 座机号码
        :param mail: 邮箱地址 和 手机号码必须填其一
        :param gender: 性别
        :param address: 地址
        :param department: 部门
        :param position: 职位
        :return: True 添加成功
        """
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/av1" and @text="更多选项"]').click()
        self.wait_for_visible((MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/au8" and @text="帐号　"]'), 10)
        input_elements = self.finds(MobileBy.ID, 'com.tencent.wework:id/au8')
        for element in input_elements:
            field = element.text
            content = ""
            if '姓名' in field :
                content = username
            elif "帐号" in field:
                content = account
            elif '别名' in field:
                content = alias
            elif '手机' in field:
                content = mobile_phone
            elif '座机' in field:
                content = phone
            elif '邮箱' in field:
                content = mail
            elif '职务' in field:
                content = position
            else:
                self.log.info(f'===: 有新增字段au8：{field}')

            if content == "":
                continue
            else:
                locator = f'//*[@resource-id="com.tencent.wework:id/au8" and @text="{field}"]/..//*[@class="android.widget.EditText"]'
                self.find(MobileBy.XPATH, locator).send_keys(content)
                self.log.info(f"===: 输入成员{element.text}: {content}")

        au_elements = self.finds(MobileBy.ID, 'com.tencent.wework:id/au_')
        for element in au_elements:
            content = ""
            field = element.text
            if "性别" in field:
                content = gender
            else:
                self.log.info(f'===: 有新增字段au_：{field}')
            if content == "":
                continue
            else:
                self.find(MobileBy.XPATH,
                           f'//*[@resource-id="com.tencent.wework:id/au_" and @text="{field}"]/..//*[@resource-id="com.tencent.wework:id/aui"]').click()
                self.wait_for_click((MobileBy.ID, 'com.tencent.wework:id/drb'), 10)
                self.find(MobileBy.XPATH, f'//*[@text="{content}"]').click()
                self.log.info(f"===: 输入成员{element.text}: {content}")

        h5_elements = self.finds(MobileBy.ID, 'com.tencent.wework:id/h5')
        for element in h5_elements:
            content = ""
            field = element.text
            if "地址" in field:
                content = address
            else:
                self.log.info(f'===: 有新增字段h5：{field}')
            if content == "":
                continue
            else:
                self.find(MobileBy.XPATH, f'//*[@resource-id="com.tencent.wework:id/h5" and @text="{field}"]/..//*[@resource-id="com.tencent.wework:id/aui"]').click()
                self.wait_for_click((MobileBy.ID, 'com.tencent.wework:id/h1'), 10)
                self.find(MobileBy.ID, 'com.tencent.wework:id/h1').send_keys(content)
                self.find(MobileBy.ID, 'com.tencent.wework:id/gvk').click()
                self.wait_for_visible((MobileBy.ID, 'com.tencent.wework:id/gv4'), 10)
                self.log.debug(f"===: 输入成员{element.text}: {content}")

        # 部门添加 pass
        # 身份选择
        if identity != "":
            self.find(MobileBy.XPATH, '//*[resource-id="com.tencent.wework:id/bgq"]//*[resource-id="com.tencent.wework:id/avc"]').click()
            self.wait_for_click((MobileBy.ID, 'com.tencent.wework:id/drb'), 10)
            self.find(MobileBy.XPATH, f'//*[@text="{position}"]').click()
            self.log.info(f"===: 输入成员身份: {position}")
            self.wait_for_visible((MobileBy.ID, 'com.tencent.wework:id/gv4'), 10)
        # 保存
        self.find(
            MobileBy.ID, 'com.tencent.wework:id/gvk'
        ).click()
        self.log.info(f"===: 添加成员{username}结束")
        # 抓取toast信息，判断是否添加成功
        status_ele = self.wait_for_present((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'), 10)
        if status_ele.text == "添加成功":
            self.log.info(f"===: 添加成员{username}成功")
            return True
        else:
            self.log.info(f"===: 添加成员{username}失败")
            return False
