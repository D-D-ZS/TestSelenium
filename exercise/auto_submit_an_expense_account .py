#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/7/15 9:56  
# Author  : DanDan Zhao 
# File    : auto_submit_an_expense_account.py
# 
from selenium import webdriver
import xlrd
import xlwt
from xlutils.copy import copy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()


def elements():
    """
    自动登录销售易网页版，并进入费用页面
    :return:
    """
    driver.implicitly_wait(60)
    driver.maximize_window()
    driver.get("https://crm.xiaoshouyi.com/expense.action")
    driver.find_element_by_name("loginName").send_keys("dandan.zhao@datageek.com.cn")
    driver.find_element_by_name("password").send_keys("Zh@od@nd@n123")
    driver.find_element_by_css_selector(
        "#div_main > div.crm-register-bg > div.crm-register-form.crm-login-form.login_box > div.crm-register-footer > a").click()
    driver.find_element_by_class_name("pop_close").click()
    driver.get("https://crm.xiaoshouyi.com/expense.action")


def excel():
    """
    解析Excel表格中填写的报销数据，并自动填写到系统中，填报过内容备注为1，不再填报
    :return:
    """
    wb = xlrd.open_workbook("reimbursement.xlsx")
    st = wb.sheets()[0]
    rn = st.nrows
    for i in range(1, rn):
        status = int(st.cell_value(i, 8))
        if status == 1:
            print("row %d has done" % i)
            continue
        else:
            driver.find_element_by_css_selector(
                "#crm_toolbar > div.grid_tool > div > a.create-entity-btn.dinline-block.no-drop.lfloat").click()
            date = str(xlrd.xldate_as_datetime(st.cell_value(i, 0), 0).date())
            rtype = st.cell_value(i, 1)
            fee = str(st.cell_value(i, 2))
            so = st.cell_value(i, 3)
            if st.cell_value(i, 4) == '':
                start_time = "00:00"
            else:
                start_time = xlrd.xldate_as_datetime(st.cell_value(i, 4), 0).strftime("%H:%M")
            op = st.cell_value(i, 5)
            if st.cell_value(i, 6) == '':
                end_time = "23:59"
            else:
                end_time = xlrd.xldate_as_datetime(st.cell_value(i, 6), 0).strftime("%H:%M")
            ap = st.cell_value(i, 7)
            print(date, rtype, fee, so, start_time, op, end_time, ap)

            e = driver.find_element_by_xpath("//div[@id='expense_relateEntity']/div/div/div/div")
            ActionChains(driver).move_to_element(e).click().perform()
            time.sleep(2)
            dropdownlist = driver.find_elements_by_xpath("//div[@role='option']")
            for j in dropdownlist:
                if j.text == "销售机会":
                    j.click()
                    break
                else:
                    pass
            soe = driver.find_element_by_css_selector(
                "#expense_relateEntity > div.people_name.clear.js-relateEntityDiv > input")
            soe.send_keys(so)
            time.sleep(2)
            soe.send_keys(Keys.DOWN)
            soe.send_keys(Keys.ENTER)
            print("write so")
            rte = driver.find_element_by_css_selector("#expense_expenseType > div > input.text.ui-autocomplete-input")
            rte.send_keys(rtype)
            time.sleep(1)
            rte.send_keys(Keys.DOWN)
            rte.send_keys(Keys.ENTER)
            print("write type")
            driver.find_element_by_css_selector("#expense_money > span > input.ui-spinner-input").send_keys(fee)
            print("write fee")
            driver.find_element_by_xpath("//div[@itemtype='7']/div[2]/input").send_keys(date)
            driver.find_element_by_xpath("//div[@itemtype='7']/div[2]/input").send_keys(Keys.ENTER)
            print("write date")
            driver.find_element_by_css_selector(
                "[itemid='217703331'] > div > input.dtpicker-input.dtpicker-date.hasDatepicker").send_keys(date)
            driver.find_element_by_css_selector(
                "[itemid='217703331'] > div > input.dtpicker-input.dtpicker-date.hasDatepicker").send_keys(Keys.ENTER)
            driver.find_element_by_css_selector(
                "[itemid='217703331'] > div > input.dtpicker-input.dtpicker-time.hasTimepicker").send_keys(start_time)
            driver.find_element_by_css_selector(
                "[itemid='217703331'] > div > input.dtpicker-input.dtpicker-time.hasTimepicker").send_keys(Keys.ENTER)
            driver.find_element_by_css_selector("#expense_dbcVarchar5 > input").send_keys(op)
            print("write start")
            driver.find_element_by_css_selector(
                "[itemid='217703089'] > div > input.dtpicker-input.dtpicker-date.hasDatepicker").send_keys(date)
            driver.find_element_by_css_selector(
                "[itemid='217703089'] > div > input.dtpicker-input.dtpicker-date.hasDatepicker").send_keys(Keys.ENTER)
            driver.find_element_by_css_selector(
                "[itemid='217703089'] > div > input.dtpicker-input.dtpicker-time.hasTimepicker").send_keys(end_time)
            driver.find_element_by_css_selector(
                "[itemid='217703089'] > div > input.dtpicker-input.dtpicker-time.hasTimepicker").send_keys(Keys.ENTER)
            driver.find_element_by_css_selector("#expense_dbcVarchar3 > input").send_keys(ap)
            print("write end")
            time.sleep(1)
            try:
                driver.find_element_by_xpath(
                    "//*[@class='pop_up_02 ui-dialog-content ui-widget-content']/div[2]/div[2]/a[9]").click()
                # ui-id-13 > div.pop_up_bottom > div:nth-child(2) > a:nth-child(9)
            except Exception:
                print(e)
                print("save %d is failed " % i)
            else:
                print("save %d is Succ " % i)
            time.sleep(2)
            # new_xls = copy(wb)
            # ws = new_xls.get_sheet(0)
            # ws.write(i, 8, 1)
            # new_xls.save("reimbursement.xls")
            # xlwt.Worksheet(sheetname="sheet1").write(i, 8, i)


if __name__ == '__main__':
    elements()
    excel()
