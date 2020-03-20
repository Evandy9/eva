#coding=utf-8
# class Ball:
# 	def __int__(self,name):
# 		self.name = name
# 	def kick(self):
# 		print("my name is %s"%self.name)
# b=Ball('tudou')
# b.kick()

# class Person:  类对象
# 	name="andy"
# p=Person()  类的实例化
# p.name        第一种公有

#公有和私有
name mangling
# class Person:
# 	__name="andy"  变量或者函数名前加双下横线可以将变量私有化
# p=Person()
# p.__name就无法显示了  私有（1）

# class Person:
# 	__name="andy"
# 	def getName(self): 方法
# 		return self.__name
# p=Person()
# p.__name 报错
# p.getName() 得到andy
# p._Person__name 得到andy
# _类名__变量名                   私有（2）伪私有

