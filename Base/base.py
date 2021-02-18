from Common.log import FrameLog
from selenium import webdriver

'''
对click ,send_keys,clear,等时间的封装
'''
class Base():
    def __init__(self,driver):
        self.driver = driver
        self.log =FrameLog().log()

    #*args 表示接受任意多个非关键字参数
    def findele(self,*args):
        try:
            print(args)
            self.log.info('通过'+args[0]+'元素定位，元素是'+args[1])
            return self.driver.find_element(*args)
        except:
            #定位失败
            self.log.error('元素定位失败')

    #点击元素click
    def click(self,args):
        self.findele(args).click()

    #定位元素，输入值
    def sendkey(self,args,value):
        self.findele(args).send_keys(value)

    #调用js方法
    def js(self,str):
        self.driver.execute_script(str)

    def url(self):
        return self.driver.current_url

    #后退

    def back(self):
        self.driver.back()

    #前进
    def forword(self):
        self.driver.forword()

    #退出
    def quit(self):
        self.driver.quit()