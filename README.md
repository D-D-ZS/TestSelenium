# 介绍
appium、selenium 练习，基于企业微信、雪球的PO实现

# 说明
## 目录结构
- config 配置文件
    - chromedriver.json chrome driver版本mapping
    - config.yml 基础配置
- data 测试数据
    - user.yml 用户信息
    - user_name_list.yml 用户名称列表
- exercise 练习目录
- p_appium APP相关内容
    - wework 企业微信APP
        - page  page代码
        - test_case 用例代码
    - xueqiu 雪球APP 
        - page page代码
        - test_case 用例代码
- utils 工具模块
    - base.py 基类，app、web 的 driver及相关方法封装
    - chromedriver_helper.py 动态获取chrome driver帮助模块
    - common.py 一些共用的常用方法封装
    - except_windows.py 意外弹窗处理装饰器
    - log_helper.py 日志配置模块
- web web页面相关内容
    - page 企业微信web管理后台 page代码
    - test_case 测试用例
- chromedriver chrome driver 存放路径
