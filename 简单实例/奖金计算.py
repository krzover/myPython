#coding:utf-8

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
'''
def calc():
    in_profits = raw_input(' 输入利润(万):')
    in_profits = int(in_profits)
    arr = [100,60,40,20,10,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    r = 0
    for Index_num in range(0,len(arr)):
        #从大开始比较,如果大则算出超额部分奖金,剩下金额=arr[index_num-1]的金额.循环算出剩下金额的奖金并相加
        if in_profits>arr[Index_num]:
            r+= (in_profits-arr[Index_num])*rat[Index_num]/100
            in_profits=arr[Index_num]
            print arr[Index_num]
    print '__',r
calc()