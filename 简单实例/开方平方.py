#coding:utf-8
import math
'''
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。请看具体分析：
'''


def calc():
    for i in range(10000):
        #i+100开方后得到x,再判断x平方时候等于i+100
        x =int( math.sqrt(i+100))
        y =int( math.sqrt(i+268))
        if (x * x)==(i+100) and (y * y) == (i+268):
            print i

calc()