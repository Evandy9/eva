

#coding=utf-8

# height=float(input("pls input a number:"))

# if height>2:
#     print("you are not 2")
# else:
#     print("ni ge 2b")

# import keyword
# print(keyword.kwlist)
#
# print("answer the question huangrong")
# none = True
# number=0
# while none:
#     number +=1
#     if number%3==2 and number%5==3 and number%7==2:
#         print("the number is :",number)
#         none = False
#
# print("echo the sum of 1+2+...+100")
# sum = 0
# for i in range(101):
#     sum +=i
# print(sum)
#
for i in range(1,10,2):
    print(i,end=" ") #输出时后面加空格
    print(" ")
#
#
# #猜数字
# import random
# secret = random.randint(1,10)
# while True:
#     number = int(input("pls input a number:"))
#     if number != secret and (number<0 or number>10):
#         print("hi guy pls see the question carefully")
#         print(secret)
#         continue
#     elif number != secret and (0<number<10):
#         print("sorry，it is not correct")
#     else:
#         print("bingo")
#         break

#10086
#
# import random
# yidong=random.randint(1,100)
# yidong1=random.randint(1,100)
# yidong2=random.randint(1,100)
# print("输入1，显示您当前的余额；")
# print("输入2，显示您当前剩余的流量，单位为G；")
# print("输入3，显示您的剩余通话时间，单位为分钟；")
# print("输入0，退出自助查询系统；")
#
# while True:
#     number = int(input("pls input the number you want:"))
#     if number not in (0,1,2,3):
#         print("not a valid number,pls check carefully")
#         continue
#     elif number == 1:
#         print("您当前的余额为%d元"% yidong)
#         continue
#     elif number == 2:
#         print("您当前剩余的流量为%dG"% yidong1)
#         continue
#     elif number == 3:
#         print("您的剩余通话时间为 %d 分钟"% yidong2)
#         continue
#     else:
#         pass
#         break


#乘法表

for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j)+"\t",end="")
    print("")
