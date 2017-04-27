#coding:utf-8

#计算字符出现的次数
'''
ab =str(input(':::'))
list = '11233543516838351683516843183464'
list_num = len(list)-1
count_num = 0
while list_num >=0:
    if ab == list[list_num]:
        list[list_num] = '\000'
        count_num+=1
    list_num-=1
print count_num
'''

#计算每个字符串出现的次数
str_list = 'bbsssss'
dic_num=0
for a in str_list:     
    str_num = len(str_list)-1
    dict = {a:0}
    while str_num>=0:
        if  a == str_list[str_num]:
            dict[a] = dict[a]+1            
        str_num-=1
    print dict