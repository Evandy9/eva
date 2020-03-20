#coding=utf-8

# class Parent:#创建父类
#     def hello(self): #创建父类方法hello
#         print("sn is sb")
# class Child(Parent):#创建子类继承父类
#     pass
# p=Parent() #父类实例化,p为实例对象
# p.hello()#调用父类的方法
# c=Child() #子类实例化
# c.hello()#子类继承父类的方法
# #子类定义与父类同名的方法和属性，那子类会覆盖父类的方法和属性
# class Child(Parent):
#     def hello(self):#hello会覆盖子类中的hello 方法
#         print("sn is very sb")
# d = Child()
# d.hello()

#各类鱼的游走
import random as r
class Fish:
    def __init__(self): #初始化坐标
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
#Python中函数和方法的区别：函数要手动传self，方法不用传self。如果是一个函数，用类名去调用，如果是一个方法，用对象去调用
    def move(self):
        self.x -=1 #一路向西移动
        print("my position is:",self.x,self.y)
class Goldfish(Fish):#继承父类
    pass
class Shark(Fish):
    def __int__(self):#初始化
        super().__init__() #先调用父类中的init方法，如果没有这句的话此处子类的初始化方法会覆盖父类初始化方法
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("so hungry")
            self.hungry = False
        else:
            print("enough")

fish = Fish() #类的实例化，
fish.move()
goldfish = Goldfish()
goldfish.move()
shark = Shark()
#shark.eat()
shark.move() #因为30行的init把父类里的init覆盖掉了，所有会报错，需要添加super（）



