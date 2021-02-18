from functions import date_n,id,css,class_name,xpath,js,return_driver,open_base_site,click_bank
import time
from selenium.webdriver.common.keys import Keys

'''
函数名：search_tickets
参数：出发站 from_station,到达站 to_station，订票日期 n
'''
def search_tickets(from_station,to_station,n):
    open_base_site('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
    from_station = from_station
    to_station = to_station
    tomorrow = date_n(n)
    #定位出发城市和到达城市
    id('departCityName').send_keys(from_station)
    time.sleep(3)
    id('arriveCityName').send_keys(to_station)
    #移除出发时间的’readonly‘属性
    js('departDate')
    time.sleep(3)
    #清除出发时间的默认内容
    id('departDate').send_keys(Keys.CONTROL, 'a')
    #定义出发日期
    id('departDate').send_keys(tomorrow)
    #鼠标点击空白处，移除时间控件
    click_bank()
    time.sleep(5)
    #点击搜索
    class_name('searchbtn').click()
    time.sleep(3)
