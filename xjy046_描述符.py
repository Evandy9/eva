#coding=utf-8
#描述符就是将某种特殊类型的类的实例指派给另一个类的属性
# class Descriptor:
#     def __get__(self, instance, owner):
#         print("getting",self,instance,owner)
#     def __set__(self, instance, value):
#         print("setting",self,instance,value)
#     def __delete__(self, instance):
#         print("del",self,instance)
#
# class Test:
#     x = Descriptor() #类实例指派给Test类的属性x，Descriptor是x的描述符类、
#
# test=Test() #类实例化
# test.x
# #print(test.x)
# #test
# print(test)
# #Test
# print(Test)
#
# test.x="fuck" #触发到des类中的setting,等号赋值
# del test.x #触发到DES类中的delete
#-----------------------------------------------------------------------------
#
# class Myproperty:
#     def __init__(self,fget=None,fset=None,fdel=None):
#         self.fget=fget #初始化赋值
#         self.fset=fset
#         self.fdel=fdel
#     def __get__(self, instance, owner):#
#         return self.fget(instance)#owner的实例对象
#     def __set__(self, instance, value):
#         self.fset(instance,value)
#     def __delete__(self, instance):
#         self.fdel(instance)
#
# class C:
#     def __init__(self):
#         self._x=None
#     def getX(self):
#         return self._x
#     def setX(self,value):
#         self._x=value
#     def delX(self):
#         del self._x
#     x=Myproperty(getX,setX,delX)
# c=C()
# c.x="xman"
# print(c.x)
# print(c._x)
# del c.x

#---------------------------------------------------------------------------------------
class Celsius:
    def __init__(self,value=20.1):#初始化温度
        self.value=float(value)  #（5）
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value): #（4） #2
        self.value=float(value)
class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel*1.8+32  #4
    def __set__(self, instance, value):
        instance.cel=(float(value)-32)/1.8 #（2）
class Temperature:
    cel=Celsius()     #描述符类描述的cel属性，（3）  #1
    fah=Fahrenheit()   #（1） #3

temp=Temperature()
print(temp.cel) #对象实例的属性cel是celsius的实例对象，用的是celsius的init初始值
temp.cel = 30 #调用路径1234
print(temp.fah)
temp.fah = 100 #调用逻辑12345
print(temp.cel)