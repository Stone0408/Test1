from Base.base import Base
from selenium.webdriver.common.by import By
import time

'''
搜索火车票页面，出发  到达，日期 js效果，搜索
'''
class SearchPage(Base):

    def search_leave(self):
        return self.findele(By.ID,'departCityName')

    def search_arrive(self):
        return self.findele(By.ID,'arriveCityName')

    def search_date(self):
        return self.findele(By.ID,'departDate')

    def search_btn(self):
        return  self.findele(By.CLASS_NAME,'searchbtn')

    def search_current(self):
        return self.findele(By.CSS_SELECTOR,'#searchtype > li.current')

    def search_js(self,value):
        jsvalue = "document.getElementById('departDate').value = '%s'" % (value)
        time.sleep(3)
        self.js(jsvalue)

    def searc_train(self,leave,arrive,leave_date):
        self.search_leave().send_keys(leave)
        time.sleep(2)
        self.search_arrive().send_keys(arrive)
        self.search_js(leave_date)
        #self.search_current().click()
        self.search_btn().click()
        time.sleep(3)
        return self.url()