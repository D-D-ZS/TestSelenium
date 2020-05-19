#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/7/16 9:45  
# Author  : DanDan Zhao 
# File    : other_api_test.py  
# 

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def get_elements():
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    driver.maximize_window()
    driver.get("https://crm.xiaoshouyi.com/expense.action")
    driver.find_element_by_name("loginName").send_keys("dandan.zhao@datageek.com.cn")
    driver.find_element_by_name("password").send_keys("Zh@od@nd@n123")
    driver.find_element_by_css_selector(
        "#div_main > div.crm-register-bg > div.crm-register-form.crm-login-form.login_box > div.crm-register-footer > a").click()
    driver.find_element_by_class_name("pop_close").click()
    driver.get("https://crm.xiaoshouyi.com/expense.action")
    sroll = driver.find_element_by_id("jqxScrollThumbverticalScrollBardiv_main_content")
    ActionChains(driver).drag_and_drop_by_offset(sroll, 0, 40).perform()
    sleep(5)
    print("start")
    elements = driver.find_elements_by_xpath("//div[@role='row']/div[1]")

    for e in elements:
        if e.is_displayed():
            # print(e.get_attribute("id"))
            e.click()
            # sleep(1)
        else:
            # 通过js将页面拖动到指定元素
            # driver.execute_script("arguments[0].scrollIntoView(false);", e)
            # 无报错，但是页面数据不显示
            # e.send_keys(Keys.DOWN)
            # ActionChains(driver).drag_and_drop_by_offset(sroll, 0, 100).perform()
            # 元素在页面显示了，但是不能点击选中
            # sleep(10)
            # ActionChains(driver).move_to_element(e).click(e).perform()
            # sleep(10)
            e.click()
    # sleep(30)
    # driver.quit()


if __name__ == '__main__':
    get_elements()