#coding:utf-8

import urllib2
import requests

url = 'http://www.baidu.com'
#系统自带的方法
content = urllib2.urlopen(url).read()

#requests包的方法(pip install requests)
req_get = requests.get(url)

print req_get.content

#print content

file_1 = open('1.html','w')
file_1.write(req_get.content)
file_1.close