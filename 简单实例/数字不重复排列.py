#coding:utf-8
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
程序源代码：

'''


range_x= range (1,6)
def calc():
    #需要排几位数就写几个循环
    count_num = 0
    for a_a in range_x:
        for a_b in range_x:
            for a_c in range_x:                
                if a_a!=a_b and a_a!=a_c and a_b!=a_c:
                    print a_a,a_b,a_c
                    count_num +=1
    print '___总计:',count_num
calc()
        
