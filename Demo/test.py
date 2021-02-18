#coding= utf-8
from ddt import ddt,data,file_data,unpack
from dataexcel import get_data
import unittest
from selenium import webdriver

excel =get_data('',1)
@ddt
class test_se(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://e.chinaums.com/scrm/#/login')

    @data(*excel)
    def test_01(self,dic):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/div/div[1]/input').send_keys(dic.get('username'))
        print(dic.get('username'))
        self.driver.find_element_by_xpath('//*[@id="app"]/div/form/div[3]/div/div/input').send_keys(dic.get('password'))
        print(dic.get('password'))
        self.assertEqual(dic.get('username'),dic.get('password'))

    def tearDown(self) -> None:
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()