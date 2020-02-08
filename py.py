# -*- coding:utf-8 -*-

sum=0
for x in range(1,10):
	sum=sum+x
	print(sum)

print("???")

max(1,3)


#定义函数
'''
def andy(x):
	if x>=0:
		return x
	else:
		return -x
print(andy(9))

def nop():
	pass 不带pass会报错
'''

'''python算幂指数及阶乘'''
'''
def pe(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
print(nn(1.00005,70)*28810)

'''
'''
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(100))
	
'''

#列出当前目录下的所有文件和目录名，可以通过一行代码实现
'''
import os
[d for d in os.listdir('.')]
'''

