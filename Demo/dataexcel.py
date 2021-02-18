#coding=utf-8
import xlrd
def get_data(filename,sheetnum):
    path = 'D:\\testdata.xls'
    bookdata = xlrd.open_workbook(path)
    book_sheet = bookdata.sheet_by_index(0)
    '''行数'''
    rows_num = book_sheet.nrows
    '''列数'''
    cols_num = book_sheet.ncols
    '''键值'''
    key_name = book_sheet.row_values(0)
    print(key_name)
    '''定义一个空的列表，存放全部的数据'''
    list = []
    '''定义list 大列表循环次数，除去第一行的标题'''
    for i in range(1,rows_num):
        '''定义一个空字典，存储每一组用户账户 密码'''
        dic = {}
        '''定义字典循环次数。列表总列数cols_num，每一列的value 并与键值key对应'''
        for j in range(0,cols_num):
            dic[key_name[j]] =book_sheet.row_values(i)[j]
        list.append(dic)
    return list
if __name__ == '__main__':
    print(get_data('',1))










