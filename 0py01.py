#coding=utf-8

# height=float(input("pls input a number:"))

# if height>2:
#     print("you are not 2")
# else:
#     print("ni ge 2b")

import keyword
print(keyword.kwlist)

print("answer the question huangrong")
none = True
number=0
while none:
    number +=1
    if number%3==2 and number%5==3 and number%7==2:
        print("the number is :",number)
        none = False

print("echo the sum of 1+2+...+100")
sum = 0
for i in range(101):
    sum +=i
print(sum)

for i in range(1,10,2):
    print(i,end=' ') #输出时后面加空格

for i in range(1,10):
    for j in range(1,10):
        print(str(i)+"x"+str(j))