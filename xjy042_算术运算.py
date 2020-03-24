#coding=utf-8
# class mathm(int):#inherit int class
#     def __add__(self, other):
#         return int(self)+int(other) #must use int,otherwise it will be always a+b not int(a)+int(b)
#     def __sub__(self, other):
#         return int(self)+int(other)
# a=mathm(3)
# b=mathm(345)
# print(a+b)

#------------------------------------------------------------------------------------------------------

class Test(int):
    def __add__(self, other):
        return int.__sub__(self,other)
    def __sub__(self, other):
        return int.__add__(self,other)
a=Test(3)
b=Test(34534)
print(a+b)
#----------------------------------------------------------------------------------------------------------
反运算。。。