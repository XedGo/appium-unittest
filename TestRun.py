#coding=utf-8
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
#######      使用时请先打开APPIUM再执行测试    ###########

def creatsuite():
    testunit = unittest.TestSuite()
    # 设置测试文件查找的目录
    test_dir = 'C:\\Users\Administrator\Desktop\WsfTest\TestCase'

    # 定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)

    #discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        testunit.addTests(test_suite)
    print(testunit)
    return testunit

alltestnames = creatsuite()



if __name__ == '__main__':
    report_title = '接单易家庭版自动化测试报告'
    desc = '版本号V1.0 <br/> 作者: 孟园'
    report_file = 'EndTest.html'


    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(alltestnames)
