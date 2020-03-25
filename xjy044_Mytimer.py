#coding=utf-8
import time as t


# class A:
#     def __str__(self):
#         return "Andy is handsome"
# a=A()
# print(a)
#a 是没有返回字符串的
# class B:
#     def __repr__(self):
#         return "Andy is handsome"
# b=B()
# print(b)

class Mytimer():
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    #开始时间
    def start(self):
        self.start=t.localtime()
    #结束时间
    def stop(self):
        self.stop=t.localtime()
        self._calc() #对象.内部方法
    #内部方法，计算运行时间
    def _calc(self): #内部方法私有
        self.lasted=[] #list要先声明
        self.prompt="It runed x seconds"
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.prompt += str(self.lasted[index])
        print (self.prompt)
