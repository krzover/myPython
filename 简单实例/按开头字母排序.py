#coding:utf-8

'''
import random

roll=['宋锦朝','连鑫鹏','张欢','何炎哲','王会洋','李鹏举','梁达鹏','史新超','范杨成','吴晓莉','万慧影','张奇奇','杨文通','葛蕊','邓亚萌','朱瑞','谷国权','任子龙','郭东波','申思思','罗雪艳','亓恩芳','朱瑞祥']

a=0
while a<len(roll):
    num = random.randint(0,len(roll)-1)
    print num
    print roll.pop(num)
    '''

list = ['ziji','chazhao','yixie','yingwen','cihui','cunchu','mouge','rongqi','zhong','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dic = {}
for x in list:
    str_key = x[0]
    if dic.has_key(str_key) == False:
        dic[str_key] = [x]
    else:
        dic[str_key].append(x)
print dic