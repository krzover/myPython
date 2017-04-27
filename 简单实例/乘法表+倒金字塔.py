#coding:utf-8


#乘法表
# for x in xrange(1,10):
#     for a in xrange(1,x+1):
#         print '%d*%d = %d'%(a,x,a*x)
#     print '\n'


#倒金字塔
floor = input('floor:')
for x in xrange(floor):
    print  ' '*x,'*'*-(2*(x-floor)+1)
