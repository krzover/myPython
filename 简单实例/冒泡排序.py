#coding:utf-8

def com(list):
    for x in xrange(len(list)-1):
        for y in xrange(x,len(list)-1):
            if list[y]>list[y+1]:
                list[y],list[y+1] = list[y+1],list[y]
                print list
list = [1,9,2,8,3,7,6,4,5,5]
com(list)