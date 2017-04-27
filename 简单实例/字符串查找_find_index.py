#coding:utf-8
s_1 = 'dahfjdhkakjhfdjahsjdpythondkadqnpythondka'
sub = 'python'
# 获取第一个python字符中p相对于整个字符串所在的索引位置
# 假如字符串中没有要查找的子字符串，则输出-1
# 声明变量记录有没有找到该字符索引
is_find = False

for i in range(0,len(s_1)):
    # 判断截取的字符串是否与子串相同
    if s_1[i:i +len(sub)] == sub:
        # 相同，i表示子串中第一个字符的位置
        print 'python中p的索引为%d'%(i)
        is_find = True
        break

if is_find == False:
    print '没有找到该字符,-1'

# find 字符串中查找子串第一个字符所在的索引，找到该字符，输出字符索引位置，没有找到则输出-1
''' 1.要查找的子串内容
    2.查找开始的位置
    3.查找结束的位置
    注：默认查找范围是整个字符串
'''
number =  s_1.find('ppppp',0,len(s_1))
print number
# 查找子串在字符串中 开始的位置，有则输出索引，没有则直接错误异常
''' 1.要查找的子串内容
    2.查找开始的位置
    3.查找结束的位置
    注：默认查找范围是整个字符串
'''
number1 = s_1.index('python')
print s_1[number1:number1+len('python')]



