import time
import unittest
import HTMLTestRunner
from functions import date_n,id,css,class_name,xpath,js,return_driver,open_base_site,click_bank
from functions import read_excel
from functions import log
from search_tickets import search_tickets

class booking_tickets(unittest.TestCase):
    def setUp(self) -> None:
        self.driver =return_driver()

    def tearDown(self) -> None:
        self.driver.quit()
    def test_booking_tickets(self):

        #读取excel数据
        log('Read Eecel Files to get test data.')
        dic1 =read_excel('D:\\testdata.xls',0)
        print(dic1[0][0],dic1[1][0])
        #开始输入起始地
        log('Begin to search tickets')
        search_tickets(dic1[0][0],dic1[1][0],1)
        #获取driver对象
        log('begin to get driver object')


if __name__ =='__main__':
    suit = unittest.TestSuite()
    suit.addTest(booking_tickets('test_booking_tickets'))
    file_name1 = 'D:\\report2.html'
    print('22222')
    fp = open(file_name1, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test_report', description='test_description')
    runner.run(suit)
    fp.close()
    print('pass')
