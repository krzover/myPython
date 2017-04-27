#coding:utf-8

def num_sum():
    x = 0
    y = 1
    while y<1000:
       a = x+y
       x=y
       y=a
       print a
num_sum()