#coding = utf-8

# class C(object):
#     def __getattribute__(self, name):#属性被访问时，被调用
#         print("getattribute")
#         return super().__getattribute__(name) #获得用return，不改变原有的，调用基类用super（自动继承父类），没有父类默认找object类
#     def __getattr__(self, name):
#         print("getattr")
#     def __setattr__(self, name, value):#当属性被设置时被调用
#         print("setattr")
#         return super().__setattr__(name,value)
#     def __delattr__(self, name): #当删除时被调用
#         print("delattr")
#         return super().__delattr__(name)
# c=C()
# c.x
# c.x=1
# del c.x
#----------------------------------------------------------------------------------
class Rent:
    def __init__(self,width=0,height=0):#构造函数初始化
        self.width=width
        self.height=height #初始化
    def __setattr__(self, name, value):
        if name=="square":
            self.width=value
            self.height=value
        else:
            #self.name=value #赋值会触发setattr，然后不等于square而是width，然后会调用此句，然后又会去调用init，死循环
            #super().__setattr__(name,value) 相等于下面的方法
            self.__dict__[name]=value
    def getAera(self):
        return self.width * self.height
r=Rent(2,8)
print(r.getAera())

r.square=10
print(r.width)
print(r.height)
print(r.getAera())
print(r.__dict__)
#r是实例化对象，相当于self，square相当于settle里的name，10是value