#coding=utf-8

# try:
#     print(int('a'))
# except ValueError as reason:
#     print('出错了'+str(reason))
# else:#不错的情况就执行了
#     print('everything goes well')

# try:
#     f=open('/home/evandy/readme.txt','w')
#     for i in f:
#         print(i)
# except OSError as reason:
#     print('issue happened'+str(reason))
# finally:
#     f.close()

try:
    with open('/home/evandy/readme.txt','w') as f:#不用的时候自动调用f.close()
        print(f.write('bad'))
        for i in f:#注意缩进
            print(i)
except OSError as reason:
    print('issue happened'+str(reason))