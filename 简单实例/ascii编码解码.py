#coding:utf-8
'''
#ascii编码转字符
a = [76,105,102,101,32,83,104,111,114,116,44,85,115,101,32,80,121,116,104,111,110,33]
for x in a:
    # print chr(x),
    pass
#字符转ascii编码
b = 'si shi si,shi shi shi,shi si shi shi si,si shi shi si shi'
c= []
for y in b:
    c.append(ord(y))
print c
'''

#计算字符出现的次数
in_put =str(input(':::'))
list = '11233543516838351683516843183464'
list_num = len(list)-1
count_num = 0
while list_num >=0:
    if in_put == list[list_num]:
        count_num+=1
    list_num-=1
print count_num