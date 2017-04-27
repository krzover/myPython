#coding:utf-8

#客户端
import socket
#获取socket对象
s = socket.socket()
#获取本地主机名称
host = socket.gethostname()
#设置端口
port = 12345
#连接('主机名或ip地址',端口)
s.connect(('192.168.22.245',port))
#输出接收到的信息
print s.recv(1024)
while True:
    ccc = raw_input('发送:')
    #发送字符串
    s.send(ccc)
s.close


#服务端
import socket
#获取对象
s = socket.socket()
#获取本地主机名称
host = socket.gethostname()
#设置端口
port = 12345
#绑定ip和端口
s.bind(('localhost',port))
#tcp监听
s.listen(5)
#等待接收客户端连接
c,addr = s.accept()
#输出客户端ip
print '连接地址:',addr
#发送欢迎信息
c.send('欢迎访问')
while  True:
    #输出接收到的信息
    print c.recv(1024)
c.close()