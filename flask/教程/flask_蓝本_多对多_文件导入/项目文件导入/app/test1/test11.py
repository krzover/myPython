#coding:utf-8

# 从上一级的test2文件夹导入文件
from   ..test2.test21    import play  as play2
print 'test11/...............................'

# 给导入的文件重命名
from ..test3.test31 import play as play3


play2()
play3()
