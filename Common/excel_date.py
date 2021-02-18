import xlrd,os
'''
读取excel 所有数据放入字典中
filename 文件名
index 为 excel的sheet索引
'''

def read_excel(filename,index):
    xls = xlrd.open_workbook(filename,index)
    sheet = xls.sheet_by_index(index)
    #行数
    print(sheet.nrows)
    #列数
    print(sheet.ncols)
    dic = {}
    for i in range(sheet.ncols):
        data = []
        for j in range(sheet.nrows):
            data.append(sheet.row_values(j)[i])
        dic[i] = data
    return dic

if __name__ =='__main__':
    #读取excel，返回字典
    data = read_excel(os.path.split(os.path.realpath(__file__))[0].split('Co')[0] + 'Data\\testdata.xls',0)
    print(data)
    print(data.get(0))

