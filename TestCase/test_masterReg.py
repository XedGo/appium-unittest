#coding=utf-8
import unittest
from appium import webdriver
from config import Getcode
from selenium.webdriver.common.by import By
from time import sleep
desired_caps = {}
author = "MengYuan"
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = '16f7113e'
desired_caps['appPackage'] = 'com.wanshifu.myapplication'
desired_caps['appActivity'] = '.moudle.login.LoginActivity'
desired_caps['automationName'] = 'UiAutomator2'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

class Test_Case1(unittest.TestCase):
    """ 注册模块 """   # 此处用于生成报告时展示的主标题
    def setUp(self):   ### 初始化预置条件
		# 列子：
		self.MasterRegTextCheck = "哈哈"

    def test_Case0001(self):
        """ 进入注册界面"""# 此处用于生成报告时展示的子标题
		#列子：
        MasterReg = driver.find_element_by_id("com.wanshifu.myapplication:id/tv_register")
        MasterReg.click()
        print("点击进入注册界面")
        MasterRegText = driver.find_element_by_id("com.wanshifu.myapplication:id/title").text
        self.assertEqual(MasterRegText, self.MasterRegTextCheck)