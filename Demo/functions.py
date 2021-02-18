from datetime import datetime,date,timedelta
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import xlrd
import logging

#打开订票网站
'''启动浏览器'''
driver = webdriver.Chrome()
driver.maximize_window()

'''返回driver对象'''
def return_driver():
    return driver

'''打开地址'''
def open_base_site(url):
    driver = return_driver()
    driver.get(url)


'''返回订票日期'''
def date_n(n):
    return str((date.today() + timedelta(days = +int(n))).strftime('%Y-%m-%d'))

'''id查找元素,并返回'''
def id(element):
    return driver.find_element_by_id(element)

'''class查找元素,并返回'''
def class_name(element):
    return driver.find_element_by_class_name(element)

'''css selector查找元素,并返回'''
def css(element):
    return driver.find_element_by_css_selector(element)

'''xpath查找元素,并返回'''
def xpath(element):
    return driver.find_element_by_xpath(element)

'''js,通过selenium来执行JavaScript语句'''
def js(element):
    driver.execute_script("document.getElementById("+"'"+element+"'"+").removeAttribute('readOnly')")

def click_bank():
    ActionChains(driver).move_by_offset(0,0).click().perform()

'''读取excel文件数据'''
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    print(sheet.nrows)
    print(sheet.ncols)
    #定义一个空字典
    dic = {}
    for j in range(sheet.ncols):
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i)[j])
        dic[j] = data
    return dic


'''定义日志格式 内容'''
def log(str):
    logging.basicConfig(level=logging.INFO,format='(asctime)s%(filename)s%(message)s',datefmt='%a,%d %b %Y %H:%M:%S',filename='log-selenium.log',filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)









