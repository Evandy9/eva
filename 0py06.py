#coding=utf-8
def match(pn):
    import re
    patten=r'^[a-zA-Z][0-9a-zA-z\_]{5,17}@[126|163]+.com$'
    match=re.match(patten,pn)
    print(match)
    if match == None:
        print("illegal email")
    else:
        print("correct email")

pn=input("pls input the mail you want to check:")

match(pn)

#函数默认值
def test(person="luren"):
    print(test.__defaults__)
test()

#可变参数
def coffe(*coffename):
    print("my favorite is :")
    for i in coffename:
        print(i)
list1=["maoshi","matie"]
coffe(*list1)