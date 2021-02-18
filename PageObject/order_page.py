from Base.base import Base
from selenium.webdriver.common.by import By
import time
'''
订单页面
'''
class OrderPage(Base):
    def detail_name(self):
        return self.findele(By.CSS_SELECTOR,"#pasglistdiv>div>u1>li:nth-child(2)>input")
    def user_info(self,name):
        time.sleep(3)
        self.detail_name().send_keys(name)
        return self.dr_url()