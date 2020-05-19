#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/6/28 15:25  
# Author  : DanDan Zhao 
# File    : element_operation_test.py  
# 
# 简单元素操作

from selenium import webdriver
from time import sleep
# 导入鼠标点击相关模块，用于PC， H5页面不行
from selenium.webdriver.common.action_chains import ActionChains
# 导入键盘操作类
from selenium.webdriver.common.keys import Keys
# 导入触控操作类，可用于H5页面操作
from selenium.webdriver.common.touch_actions import TouchActions
# 等待
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


def login_email():
    """
    使用到的API：
    switch_to.* : 跳入iframe，切换窗口，切换到告警alert窗口等
    clear(): 清空文本框内容
    """
    driver.get("http://www.126.com")
    # 126邮箱登录
    # 切换到账号密码登录
    driver.find_element_by_xpath('//*[@id="switchAccountLogin"]').click()
    sleep(3)
    # 由于页面嵌入了iframe因此无法直接定位到输入框，需要先转入iframe
    # switch to frame usage:
    # driver.switch_to.frame('frame_name')
    # driver.switch_to.frame(1)
    # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    # 转入第一个iframe
    driver.switch_to.frame(0)
    # 清空输入框文本
    driver.find_element_by_name("email").clear()
    # 模拟输入用户名密码
    driver.find_element_by_name("email").send_keys("username")
    driver.find_element_by_name("password").send_keys("passwd")
    # 模拟点击登录
    driver.find_element_by_id("dologin").click()
    sleep(3)
    driver.quit()


def youdao():
    """
    maximize_window()：窗口最大化
    submit()：触发提交，click()使用较多
    size: 获取元素大小
    text: 获取元素内容
    get_attribute(): 获取某个属性，可以是id、name、type或其他属性
    """
    driver.get("http://youdao.com")
    driver.maximize_window()
    driver.find_element_by_id("translateContent").send_keys("hello")
    driver.find_element_by_id("translateContent").submit()
    sleep(3)
    # driver.switch_to.default_content()
    # driver.refresh()
    # driver.find_element_by_css_selector("body > div.dialog-guide-download.win-download > i > a.close.js_close").click()
    # <a href="javascript:;" data-rlog="search-popup-close-win" class="close js_close"></a>
    # 这种元素class name 取空格后边的内容
    driver.find_element_by_class_name("js_close").click()
    print(driver.find_element_by_class_name("collapse-content").text)
    print(driver.find_element_by_id("query").size)
    print(driver.find_element_by_id("query").get_attribute("onmouseover"))
    sleep(5)
    # driver.quit()


def mouse():
    """
    模拟鼠标操作事件，相关操作封装在ActionChains类中。常用方法如下：
    perform(): 执行所有ActionChains中存储的行为
    将所有操作按顺序放入一个队列里，当调用perform()方式时，队列中的时间会依次执行
    基本用法：生成一个动作（action = ActionChains(driver)） -> 添加动作1(action.方法1) -> 添加动作2(action.方法2) ... -> 调用perform()执行
    context_click(): 右击
    double_click(): 双击
    drag_and_drop(): 拖动
    move_to_element(): 鼠标悬停
    当获取元素不唯一时可能会引起以下错误：AttributeError: 'list' object has no attribute 'id'
    页面放大和操作之间要间隔一下，否则移动鼠标瞬间可能会变位置
    """
    driver.get("https://www.huya.com/")
    driver.maximize_window()
    sleep(5)
    element = driver.find_element_by_id("hy-nav-category")
    game = driver.find_element_by_xpath("//a[@class='clickstat' and @eid='click/navi/game/game3']")
    # 实例化ActionChains，最好不要分开写，分开写有时候后一步的元素找不到就会报错
    # actions = ActionChains(driver)
    # actions.move_to_element(element)
    # actions.click(game)
    # actions.perform()
    ActionChains(driver).move_to_element(element).perform()
    ActionChains(driver).click(game)
    sleep(2)
    ActionChains(driver).click(driver.find_element_by_xpath("//a[@href='https://www.huya.com/saopp']")).perform()
    # WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located(driver.find_element_by_id("J_weekRankList")))
    ActionChains(driver).move_by_offset(1553, 1000).context_click().perform()
    sleep(10)
    driver.quit()


def keyboard():
    """
    模拟键盘类Keys，通过send_keys()方法发送键盘键操作
    """
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("seleniumm")
    sleep(1)
    # 删除一个字符
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
    sleep(1)
    # 输入空格
    driver.find_element_by_id("kw").send_keys(Keys.SPACE)
    driver.find_element_by_id("kw").send_keys("教程")
    sleep(1)
    # ctrl + a 全选输入内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
    sleep(1)
    # ctrl + x 剪切输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
    sleep(1)
    # ctrl + v 粘贴内容到输入框
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
    # 通过回车键来代替单击操作
    driver.find_element_by_id("su").send_keys(Keys.ENTER)
    sleep(5)
    driver.quit()


if __name__ == '__main__':
    keyboard()
