#_*_coding:utf-8_*_
import os,sys
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
sys.path.append(os.path.split(os.getcwd())[0])
import time,unittest,HTMLTestRunner
from PageObject.book_page import BookPage
from PageObject.order_page import OrderPage
from PageObject.Search_page import SearchPage
from Common.excel_date import read_excel
from Common.function import config_url
from selenium import webdriver
from Common.function import project_path
import time

class loginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_excel(project_path() + 'Data/testdata.xls',0)
        cls.driver = webdriver.Chrome()
        cls.driver.get(config_url())
        cls.driver.maximize_window()

    def test02(self):
        self.driver.get('https://train.ctrip.com/TrainBooking/SearchTrain.aspx')
        search = SearchPage(self.driver)
        time.sleep(5)
        res = search.searc_train(self.data.get(1)[0],self.data.get(1)[1],self.data.get(1)[2])
        s = res.requests.session()
        s.keep_alive = False
        #本例断言是根据当前页面的url来判断的
        self.assertIn('TrainBooking',res)

    def test_03(self):
        book = BookPage(self.driver)
        res = book.book_btn()
        #断言取当前页面的url是否包含InputPassengers
        self.assertIn('InputPassengers',res)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(loginTest('test02'))
    suiteTest.addTest(loginTest('test03'))
    filepath = project_path() + '/Reports/' + '.html'
    fp = open(filepath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test_report', description='test_description')
    runner.run(suiteTest)
    fp.close()