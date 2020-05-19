#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# Version : 1.0  
# Time    : 2019/6/27 14:37  
# Author  : DanDan Zhao 
# File    : find_element_test.py
# 
from selenium import webdriver
from time import *

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
# 放大浏览器窗口
driver.maximize_window()
# 从百度首页开始完成API的测试
# 1. 相对简单的定位方法
# 通过name属性定位元素，在当前页面中可以不唯一
# <input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
driver.find_element_by_name("wd").send_keys("selenium")
print("find_element_by_name pass")
sleep(1)

# 通过id定位元素，在HTML中规定id属性唯一（刷新页面id值可能会随机变化）
# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
driver.find_element_by_id("su").click()
print("find_element_by_id pass")
sleep(1)

# 通过指定元素的类名定位元素
# <a class="toindex" href="/">百度首页</a>
# 通过class定位到百度首页并点击回到首页
driver.find_element_by_class_name("toindex").click()
print("find_element_by_class_name pass")
sleep(1)

# 通过tag定位，HTML通过tag来实现定义不同的功能。一个tag往往定义一类功能，所以通过tag识别某个元素的概率很低。
# 因为前端页面中包含大量的<div>, <input>，<a>等tag
# 定位tag名称为input的元素，并打印元素的属性
# 指定tag后获取的是页面中第一个tag
print(driver.find_element_by_tag_name("meta").get_attribute("content"))
sleep(2)
print("find_element_by_tag_name pass")

# 通过元素标签对之间的文本信息来定位元素，专门用来定位文本链接
# <a href="http://news.baidu.com" target="_blank" class="mnav">新闻</a>
driver.find_element_by_link_text("新闻").click()
print("find_element_by_link_text pass")
sleep(2)
# 通过元素标签对之间的部分文本信息来定位元素，对link定位的补充，对于较长文本，可以取文本链接中的一部分定位，只要这一部分信息可以唯一的标识这个链接
# <div class="mine-text">我的关注</div>
driver.find_element_by_partial_link_text("客户端").click()
print("find_element_by_partial_link_text pass")
sleep(1)

# 关闭当前窗口
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.close()

# 复杂情况下id、name等属性值不唯一或者随着页面刷新发生变化时通过以上方法很难定位，因袭需要使用Xpath以及CSS定位。
# 2. Xpath
# 比较慢
# 使用浏览器console可以检验xpath是否正确，$x('xpath')
# Xpath-绝对路径定位
# Xpath主要用标签名的层级关系来定位元素的绝对路径，最外层为HTML语言
# 在body文本内，一级一级往下查找，如果一个层级下有多个相同的标签名，那么就按上下顺序确定第几个，例如div[2]表示当前层第二个div
# <a href="http://news.baidu.com" name="tj_trnews" class="mnav">新闻</a> 百度首页右上角新闻，获取链接“http://news.baidu.com/”
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
print("绝对路径：" + driver.find_element_by_xpath("/html/body/div/div/div/div[3]/a").get_attribute("href"))

# Xpath-利用元素属性定位
# //input[@id='kw']：//表示当前页面某个目录下（所有），input表示定位元素的标签名，[@id='kw']表示这个元素的id属性值等于kw
# 同样以新闻为例
print("利用元素属性，指定标签名：" + driver.find_element_by_xpath("//a[@name='tj_trnews']").get_attribute("href"))
# 如果不指定标签名，则可以用星号*代替
print("利用元素属性，不指定标签名，使用*：" + driver.find_element_by_xpath("//*[@name='tj_trnews']").get_attribute("href"))

# Xpath-层级与属性结合
# 如果一个元素本身没有可以唯一标识这个元素的属性值，那么我们可以找其上一级元素，如果他的上一级有可以唯一标识的属性的值，也可以拿来用
# 仍然以新闻为例，加入本身没有唯一标识，通过找到他的父级然后定位到它
# 如果父级仍然没有，则再向上找，一直到找到，或者到html写出完整的绝对路径
print("通过父级元素定位：" + driver.find_element_by_xpath("//div[@id='u1']/a").get_attribute("href"))

# Xpath-使用逻辑运算符
# 如果一个属性不能定位到元素，可以使用逻辑运算符连接多个属性
# 在属性中通过and连接两个条件
print(driver.find_element_by_xpath("//a[@class='mnav' and @name='tj_trnews']").get_attribute("href"))
print(driver.find_element_by_xpath("//a[@class='mnav' and @name='tj_trhao123']").get_attribute("href"))
# 3. CSS定位(appium 原生不支持)（chrome console 中使用 $('css')）
# CSS可以灵活的选择空间的任意属性，一般情况下定位速度要比Xpath快，以下是CSS常见语法
# | 选择器 | 例子 | 描述 | | --- | --- | --- |
# |.class | .intro | class选择器，选择class="intro"的所有元素|
# |#id| #firstname | id选择器，选择id="firstname"的所有元素|
# | * | * | 选择所有元素 |
# | element | p | 元素，所有<p>元素 |
# | element > element | div > input | 选择所有父元素为<div>的所有<input>元素 |
# | element + element | div + input | 选择同一级中紧接在<div>元素之后的所有<input>元素 |
# | [attribute=value] | [target=_blank] | 选择target="_blank"的所有元素 |
# CSS-通过class属性定位
# 查找百度首页输入框，并输入内容
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
driver.find_element_by_css_selector(".s_ipt").send_keys("test")
# 通过id属性定位
driver.find_element_by_css_selector("#kw").send_keys("test id")
# 通过组合定位 父标签+id
# <span class="bg s_ipt_wr quickdelete-wrap"><span class="soutu-btn"></span><div id="kw_tip"
# style="width: initial; margin-left: 36px; max-width: 399px; display: none;" unselectable="on" onselectstart="return
#  false;" class="s_ipt_tip"></div><input id="kw" name="wd" class="s_ipt" value="" maxlength="255"
# autocomplete="off"><a href="javascript:;" id="quickdelete" title="清空" class="quickdelete" style="top: 0px; right:
# 0px; display: inline;"></a></span>
driver.find_element_by_css_selector("span.bg.s_ipt_wr.quickdelete-wrap>input#kw").send_keys("test")
# 4. 用By定位元素
# 统一调用find_element()方法，通过By来声明定位的方法，并传入对应定位方法的定位参数
driver.find_element(By.ID, "kw").send_keys(": test by")
