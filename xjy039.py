#coding=utf-8

#组合是把无继承关系的横向的类放到一起，纵向关系是继承

# class Turtle:
#     def __init__(self,x):
#         self.num=x
#
# class Fish:
#     def __init__(self,y):
#         self.num=y
#
# class Pool:
#     def __init__(self,x,y):
#         self.Turtle=Turtle(x) #实例化
#         self.Fish=Fish(y)
#
#     def print_num(self):
#         print("it has %s turtle,and %s fish" %(self.Turtle.num,self.Fish.num)) #self.turtle=p是实例化对象，.num是整型
#
# pool=Pool(1,10)
#
# pool.print_num()

#类，类对象和实例对象

# class C:
#     count=0  #C是个类，定义完这个类之后就是一个类对象
#
# a=C() a是实例化对象
# b=C()
# c=C()
# c.count += 10
# C.count +=100
# #a.count=100而c.count=10
# #实例属性覆盖类属性

class CC:
    def setXY(self,x,y):
        self.x=x
        self.y=y
    def printXY(self):
        print("x,y will be %s,%s" % (self.x,self.y))

dd = CC() 

dd.setXY(1,10) == dd.setXY(dd,1,10)

dd.printXY()

# dd.__dict__
#
# CC.__dict__
#
# del CC
# 之后 dd.printXY(1,10) 依然可以print 因为属性是静态变量，类对象被删除还会存放在内存里，
# 只有程序退出之后才会释放，类属性仅用来追踪与类相关的值d