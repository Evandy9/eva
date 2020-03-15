#coding=utf-8

def savefile(boy,girl,count):
    file_name_boy = 'boy_' + str(count) + '.txt'  # 先写名字
    file_name_girl = 'girl_' + str(count) + '.txt'

    boy_file = open(file_name_boy, 'w')  # 写入文件内容
    girl_file = open(file_name_girl, 'w')

    boy_file.writelines(boy)  # 写入序列
    girl_file.writelines(girl)
    boy_file.close()
    girl_file.close()

f=open('/home/evandy/readme.txt')

boy=[]
girl=[]
count=1

for i in f:
    if i[:6]!='======':#字符串分割
        (role,said)=i.split(':',1)
        if role=='A':
            boy.append(said)
        if role=='B':
            girl.append(said)
    else:#文件保存操作
        savefile(boy,girl,count)

        boy=[]
        girl=[]
        count +=1

savefile(boy,girl,count)

f.close()