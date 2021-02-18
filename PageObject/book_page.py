from Base.base import Base
from selenium.webdriver.common.by import By
import time
'''
火车票预定页面 ，1，预定,2，关闭浮层，3免登陆预定 预定
'''
class BookPage(Base):
    def book(self):
        return self.findele(By.XPATH,"//*[@id='tbody-01-k5260']/div[1]/div[6]/div[4]/a")

    #关闭浮层
    def book_close(self):
        return self.findele(By.CSS_SELECTOR,'#appd_wrap_close')

    #免登陆订票
    def book_nologin(self):
        return self.findele(By.CSS_SELECTOR,'#btn_nologin')

    #预定
    def book_btn(self):
        try:
            time.sleep(5)
            self.book_close().click()
            time.sleep(3)
            self.book().click()
            time.sleep(2)
            self.book_nologin()
        except:
            self.log.error('车次查询失败')
            None
        return self.url()