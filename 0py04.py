#coding=utf-8

import datetime

wee=["monday:eat","tuesday:drink","wed,go whoring","thu,gambling","fri,smoking"]
print(wee[datetime.datetime.now().weekday()])#datetime.datetime.now()是当前时间
#星期是从0到6,6是周日

print("中超四强球队是：")
team = ['河南建业','上海申花','江苏苏宁','广州恒大']

for i,j in enumerate(team):#枚举
    print(i+1,j) #i+1 从0开始的

#分列展示
print("中超6强球队是：")
team = ['河南建业','上海申花','江苏苏宁','广州恒大','天津泰达','上海上港']

for i,j in enumerate(team):#枚举
    if i%2==0:
        print(j+"\t",end='')
    else:
        print(j,'\n')

#extend用法

sick1=['1紧张','2心慌','睡眠质量差','针扎刺痛感3秒无法呼吸']
sick2=['食欲不振','坐立不安']
sick1.extend(sick2)
print(sick1)
#modify the list element
sick1[0]='莫名紧张'
print(sick1)
sick1.append("肠胃不适")
print(sick1)
#delete element
del sick1[-1]
print(sick1)
value="肠胃不适"
if sick1.count(value)>0:
    sick1.remove(value)
print(sick1)
#print(sick1.index('心慌'))
#print(sick1.count('心慌'))
#print(sick1.sort(key=str.lower,reverse=True))

grade=[98,323,55,11,9867,7,76,88,5345]
grade.sort(reverse=True)
#降序
print(grade)

#列表表达式
import random #output 10 random number
rn=[random.randint(10,100) for i in range(1,10)] #列表推导式中表达式作用是计算新列表中的元素
print(rn)

#生成1到10之间所有偶数的平方

sq=[i*i for i in range(2,11,2)]
print(sq)

gd=[float(i*0.5) for i in grade ]
print(gd)

g=[int(i*0.5) for i in grade if i>100 ]
print(g)

#创建二维列表

arr=[]
for i in range(4):
    arr.append([])
    for j in range(5):
        arr[i].append(j)
print(arr)

arr=[[j for j in range(5)] for i in range(4)]
print(arr[0][4])


#一个酒店总共有4层，每层有7个房间，按楼层输出每个房间的房间号
floor=[[i*1000+100+j for j in range(1,8)] for i in range(1,5)]
print(floor)

#按照不同的板式输出古诗

str1="千山鸟飞绝"
str2="万径人踪灭"
str3="孤舟蓑笠翁"
str4="独钓寒江雪"

SG=[list(str1),list(str2),list(str3),list(str4)]
print(SG)

for i in range(4):
    for j in range(5):
        if j==4:
            print(SG[i][j])
        else:
            print(SG[i][j],end="")

SG.reverse()
print(SG)
print("----竖版----")
for i in range(5):
    for j in range(4):
        if j==3:
            print(SG[j][i])
        else:
            print(SG[j][i],end="")


