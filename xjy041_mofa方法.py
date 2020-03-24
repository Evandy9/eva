#coding=utf-8

class changfang:
    def __init__(self,x,y):
        self.x=x  #第一个x是类实例化的局部变量，第二个是赋值
        self.y=y
    def getPera(self):
        return (self.x+self.y)*2
        #print("the pera is %d" % ((self.x+self.y)/2))
    def getArea(self):
        return self.x*self.y
        #print("the pera is %s" % (self.x * self.y))
rect=changfang(2,4) #传入参数

#rect.getPera()
print(rect.getPera())   #print可以显示return结果
----------------------------------------------------------------------------
class A:
    def __init__(self): #返回的只能是空，不能是一个字符串
        return "ca"
        #for init method must not have return value
a=A()
print(a)
__new__重写，继承不可变类型又需要修改时才会重写这个方法
----------------------------------------------------------------------------
class Capstr(str): #inherit str class,str can not be rewrite
    def __new__(cls, string): #rewrite the new method
        string=string.upper()
        return str.__new__(cls,string) #return the rewrite new method value
a=Capstr("i love China") #
print(a) #print the result
----------------------------------------------------------------------------
__del__

class C:
    def __init__(self):
        print("it is me--init")
    def __del__(self):
        print("oh,it is me ---del")
c1=C() #init method was called

c2=c1
c3=c2
del c3
del c2
del c1 #Garbage collection mechanism will be enabled only when all the quotation were deleted

