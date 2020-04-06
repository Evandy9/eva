#coding=utf-8

import urllib.request #urllib是一个包

response = urllib.request.urlopen("http://www.baidu.com") #获取的内容返回给一个对象response

html = response.read() #对象读取

print(html)
