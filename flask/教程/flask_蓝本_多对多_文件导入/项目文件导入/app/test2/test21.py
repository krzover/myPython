#coding:utf-8

print 'test文件夹的test21文件也被调用了'
# 从同级的init文件导入变量或者函数名字
from . import eat 

eat()


def play():
    print 'play222..............'