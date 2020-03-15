#coding=utf-8

# i=10
#
# while i:
#
#     print("i love you")
#     i=i-1;
#

# f=open('/home/evandy/readme.txt')
# for i in f:
#     print(i)

#
# f.seek(45,0)从第45个
# list(f) change f to a list


f=open('/home/evandy/readme.txt','a')
f.write(""+"\n" + "ilove you" + "\n"+ "guy")
f.close()

# f = "lucky.txt"
#
# a =8
# with open(f,"a") as file:   #只需要将之前的”w"改为“a"即可，代表追加内容
#     for i in range(a):
#         file.write(str(i) + "d" + " "+"\n")
#     a +=1