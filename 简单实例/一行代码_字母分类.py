a = ['asd', 'dgfhfg', 'asgreth', 'rtb']
b = {}
#filter()方法
# filter(lambda x:b[x[0]].append(x) if x[0] in b else b.setdefault(x[0],[x]),a)
# print b
#if判断
# print [b[x[0]].append(x) if x[0] in b else b.setdefault(x[0],[x]) for x in a]
#三位运算
# print [x[0] in b and b[x[0]].append(x) or b={x[0]:[x]} for x in a]