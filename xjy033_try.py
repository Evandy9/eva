#coding=utf-8

# try:
#     f = open('/home/evandy/readmea.txt')
#     print(f.read())
#     f.close()
# except (SyntaxError,OSError,TypeError) as reason:
#     print('出错了\n错误的原因是' + str(reason))
# except SyntaxError as reason: #也可以用(oserror,typeerror)
#     print('语法出错了\n错误的原因是' + str(reason))
# except OSError as reason:
#     print('文件出错了\n错误的原因是'+str(reason))
# except TypeError as reason:
#     print('类型出错了\n错误的原因是' + str(reason)) #顺序执行哪个先错先跳哪个,后面的就不会再执行

try:
    f = open('/home/evandy/readme.txt','w')
    print(f.write("why it is correct without error "))
    sum=1+'1'
except TypeError as reason:
    print('类型出错了\n错误的原因是' + str(reason))
finally:
    f.close()