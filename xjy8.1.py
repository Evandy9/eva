# -*- coding:utf-8 -*-

score=int(input("pls input the score you want to check:"))

if 90<=score<=100:
	print('A')
elif 80<=score<90:
	print('B')
elif 70<=score<80:
	print('C')
elif 60<=score<70:
	print('D')
elif 0<=score<60:
	print('are you a fool,kaotamazhemedian?')
else:
	print('input error,bro')