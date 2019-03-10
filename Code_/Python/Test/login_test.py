# 模拟登录淘宝网页
# 淘宝访问页面必须要求登录 才可以查看信息等，所以需要采用selenium模拟浏览器操作。

# 步骤 （1）先模拟打开淘宝首页，点击登录（使用二维码扫描登陆）
# （2）（获取到cookies,保存并打印出来）

# 想打印cookie

from selenium import webdriver

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout, encoding='utf-8')

driver = webdriver.Chrome()
url = 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F'


def get_page():
