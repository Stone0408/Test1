'''
获取项目路径，测试url等
'''
import os,configparser

#获取项目路径
#os.path.split（）返回文件的路径和文件名
#os.path.realpath() 返回指定文件的标准路径
def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('Co')[0]


#返回config.ini文件中testUrl（获取测试系统地址）
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path() + 'config.ini')
    return config.get('testUrl','url')

if __name__ == '__main__':
    print('项目路径：' + project_path())
    print('测试系统:' + config_url())