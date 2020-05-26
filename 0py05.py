#conding=utf-8
print("\n"+" "*10+"滁州西涧\n\n独怜幽草涧边生，上有黄鹂深树鸣。\n春潮带雨晚来急，野渡无人舟自横。")

#创建字典的方法有哪些
#（1）
name=["xishi","diaochan","zhaojun","yuhuan"]
constellation=["turus","mojie","juxie","baiyang"]

dic=dict(zip(name,constellation)) #create dictionary
print(dic)
#（2）元祖+列表直接大括号创建字典
#list can not be the key of dictionary,but tuple can
name=("xishi","diaochan","zhaojun","yuhuan")
constellation=["turus","mojie","juxie","baiyang"]
dic={name:constellation}
print(dic)
#(3)字典推导式创建
name=["xishi","diaochan","yifan","yuhuan"]
xingzuo=["jinniu","baiyang","mojie","sheshou"]
dic={i:j for i,j in zip(name,xingzuo)}#名字列表和星座列表组合成一个元祖
print(dic)

#create empty dictionary
dic={}
dic=dict()

dic=dict(xishi="taurus",diaochan="mojie",zhaojun="baiyang")
print(dic)

# dic=dict.fromkeys(name)
# print(dic)
#del dic

# dic.clear() #clear the dictionary
# print(dic)

print(dic["xish"] if "xish"in dic else "not in" )

print(dic.get("xishi"))

print(dic.items())

for items in dic.items():
    print(items) #output tuple

for key,values in dic.items():
    print(key,values)

dic["yifan"]="chunv" #append key,if the key exists,it will update the dictionary
print(dic)

del dic["xishi"]
print(dic)

if "xishi" in dic:
    del dic["xishi"]
print(dic)

#列表、元祖、字典列表推导式，输出5个10到100的随机数

import random
lis=[random.randint(10,100) for i in range(5)]
print(lis)
tup=(random.randint(10,100) for i in range(5))
print(tuple(tup))
dic={i:random.randint(10,100) for i in range(5)}
print(dic)


print("zip")
print(dict(zip(name,xingzuo)))
print(name[1])

str1='ldajlfsdl'
tu=tuple(str1)
print(tu[1])


#创建列表的方法
list=[] #直接写
#写个字符串，然后list（str1） 创建列表
#创建元祖的方法与list相同有两个方法

#创建集合的方法
#集合也用大括号，不重复数字，集合和字典的区别，集合是无序的，无法用索引[]用于索引

name=["xishi","diaochan","yifan","yuhuan"]
xingzuo=["jinniu","baiyang","mojie","sheshou"]
dic={i:j for i,j in zip(name,xingzuo)}#名字列表和星座列表组合成一个元祖
#print(dic[1]) 不能用索引
print(dic.get("xishi")) #字典里不能用dic[]索引值，要用dic.get()函数实现，与列表不同的是[]里是键不是索引号
#遍历字典用items

#创建两个集合分别保存选择python和C语言的学生名字
#集合用大括号{a,b,c}
#dic{a:1,b:2,c:3}
dic={}
set1=set() #create empty set
print(dic)
print(type(set1))
#set函数将列表和元祖转换成集合
name=["xishi","diaochan"]
set1=set(name)
print(name)
print(set1)

python=set(["a","b"])
print(python)