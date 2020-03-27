#coding=utf-8

class Countlist:
    def __init__(self,*args):#可变数量
        self.values=[x for x in args] #列表推导式
        self.count={}.fromkeys(range(len(self.values)),0) #初始化字典

    def __len__(self):
        return len(self.value)
    def __getitem__(self, item):
        self.count[item] +=1
        return self.values[item]

c1=Countlist(1,2,2,4,7,89)
c2=Countlist(98,5,6,7,78)
c1[1]
c2[1]
c1[1]+c2[2]
print(c1.count)


