# -*- coding:utf-8 -*-
import random

#guess = int(input("pls input what you guess:"))

secret = random.randint(1,10) #randin 随机数

while True:
#random.randint(1,10) != secret:
	guess = int(input("pls input what you guess:"))
	if guess == secret:
		print("congratulations,bitch")
		break
	elif guess > secret:
		print("da le")
	else:
		print("xiao le")
print("game over")