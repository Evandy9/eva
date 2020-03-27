#coding=utf-8

for i in "Fish":
    print(i)

links ={'baidu':'www.baidu.com','ali':'alibaba.com','tencent':'tencent.com'}
for each in links:
    print("%s-->%s",(each,links[each]))#打印字典里的键和值
#-----------------------------------------------------------------------------------------------
string="fish"
it=iter(string)  #__iter__()
# print(next(it))  __next__()
# print(next(it))
#iter()and next() next返回下一个值,iter和NEXT成对出现
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)

for each in string:
    print(each)
#------------------------------------------------------------------------------------------------

class Fab:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
fa=Fab()
for i in fa:
    if i < 20:
        print(i)
    else:
        break
#------------------------------------------------------------------------------------------------
class Fbn:
    def __init__(self,n=10):
        self.a=0
        self.b=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > self.n:
            raise StopIteration
        else:
            return self.a
fbn=Fbn()
for each in fbn:
    print(each)

fbm=Fbn(100)
for i in fbm:
    print(i)