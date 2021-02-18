#coding=utf-8
import unittest
import HTMLTestRunner
import time
from Common.function import project_path

if __name__ == '__main__':
    test_dir =project_path() + 'TestCases'
    tests = unittest.defaultTestLoader.discover(test_dir,pattern = 'test*.py',top_level_dir = None)
    now = time.strftime('%Y-%m-%d-%H_%m_%S',time.localtime(time.time()))
    filepath = project_path() + '/Reports/' + now + '.html'
    fp = open(filepath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test_report', description='test_description')
    runner.run(tests)
    fp.close()