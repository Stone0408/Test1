# coding = utf-8
import unittest
import HTMLTestRunner
from selenium import webdriver
import time
import math

class SuiteTest1(unittest.TestCase):
    def testBaiDu(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('python')
        self.driver.find_element_by_id('su').click()
        time.sleep(5)
        assert u'python' in self.driver.page_source,'页面不存在搜索关键字'
        self.driver.quit()


    suite = unittest.TestSuite()
    suite.addTest(SuiteTest1('testBaiDu'))
    file_name = 'D:\\report1.html'
    print('22222')
    fp = open(file_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test_report', description='test_description')
    runner.run(suite)
    fp.close()
    print('pass')
