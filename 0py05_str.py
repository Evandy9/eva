#coding=utf-8

str1="人生苦短,"
print(len(str1.encode()))#utf-8中文占三个字节
#coding=utf-8
print(len(str1.encode('GBK')))

#CHAR 截取
print(str1[1])
print(str1[1:2])#从n-1开始到m不包含m

try:
    print(str1[20])
except IndexError:
    print("error")

# p="do you know my birthday?"
# print("A:",p)
# p1="input your id"
# print("B:",p1)
# p2=input("pls input here:")
# p3=p2[1:2]
# p4=p2[3:4]
# p5=p2[6:8]
# print("A:your birthday is %s 年 %s 月 %s 日" % (p3,p4,p5)) #括号要括上

str2="天,下;无;\n双"
print(str2.split(";"))

st3="#dfajll #23 #000"
p=st3.split(" ")
print(p)
for i in p:
    print(i[1:]) #list all the items without #

#合并字符串
str4=["ming","ri","he","qi","duo"]
s5=" @".join(str4) #合并字符串 strnew=string.join(iterable) 迭代器可以是列表或元祖或其他，string是合并时的分隔符
at="@"+s5
print("the result is :",at)

#检索字符串
str6="天,下;无;\n双"
print(str6.count("tian"))
print(str6.find("tian"))#字符串中出现的位置
print(str6.index("下"))
print(str6.startswith("天"))
print(str6.endswith("天"))

#用户名已存在
# username="|ming|ri|xue|yuan|"
# un1=username.lower()
# regname=input("pls input the name you want:")
# reg2="|"+regname.lower()+"|"
# if reg2 in username:
#     print("the name has been used")
# else:
#     print("congratulations")

#去掉字符串中的特殊字符和空格
st="* www.kengnimade.com \n\t\r"
print(st.strip())
print(st.strip("*"))#去掉指定的特殊符号
print(st.lstrip())#去掉前面的特殊符号
print(st.rstrip())#去掉后面的特殊符号

#格式化输出
temp="编号：{:0>9s}\t 公司名称：{:s}\t website:http://www.{:s}.com"
print(temp.format('5','百度',"baidu"))

#格式化显示
import math
print("以货币形式显示：${:,.2f}".format(1212+999))

#encode
st="竹杖芒鞋轻胜马"
by=st.encode('GBK')
by2=st.encode('UTF-8')
print("the origin str is :",st)
print("after the switch:",by)
print("after the switch:",by2)
sw=by.decode('GBK')
print(sw)

#匹配ip地址,百位是0或1时,[01]{0,1}百位可有可无,\d{0,1}十位可有可无,2[0-4]\d百位是2时十位是0到4中的一个，各位是任意数字，括号括起来是一组，{3}这样的组合重复三次
# print(re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])','192.168.1.1'))
# r'([01]?)'

#匹配字符串,手机号是不是符合标准
import re
patten=r'^1[358]\d{9}$' #以1开头，以9位数字结尾
pn="13867780000"
match=re.match(patten,pn)
print(match)
if match == None:
    print("it is not CMCC")
else:
    print("weclome CMCC")

#匹配身份证件号
import re
patten=r'^[1-9]\d{5}[12]\d{3}(0[1-9]|1[012])(0[1-9]|1[0-9]|2[0-9]|3[01])\d{3}(\d|X|x)$'
pn="410622190012310000"
match=re.match(patten,pn)
print(match)
if match == None:
    print("illegal id")
else:
    print("correct id")

#匹配邮箱
import re
patten=r'^[a-zA-Z][0-9a-zA-z\_]{5,17}@[126|163]+.com$'
pn="andy_shihuanyu@126.com"
match=re.match(patten,pn)
print(match)
if match == None:
    print("illegal email")
else:
    print("correct email")
# 需以字母开头：^[a-zA-Z]
# 可使用字母、数字、下划线：[0-9a-zA-Z\_]
# 6~18个字符:{5,17}
# 后缀：@[126|163].com$’

#匹配IP
import re
patten=r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-5]\d|25[0-5])'
pn="192.168.1.1"
match=re.search(patten,pn)
print(match)
print(match.start())
print(match.end())
if match == None:
    print("illegal ip")
else:
    print("correct ip")

#match从首字母开始开始匹配，string如果包含pattern子串，则匹配成功，返回Match对象，失败则返回None，若要完全匹配，pattern要以$结尾。
#search若string中包含pattern子串，则返回Match对象，否则返回None，注意，如果string中存在多个pattern子串，只返回第一个
#findall返回string中所有与pattern相匹配的全部字串，返回形式为数组
import re
patten=r'(黑客)|(抓包)|(特洛伊)'
pn="我细化看黑客和特洛伊"
match=re.findall(patten,pn)
print(match)
if match == None:
    print("clear")
else:
    print("the website you visit is very dangerous")

#替换字符串
#re.I 不区分大小写，re.A让\w不匹配汉字
#隐藏中奖者手机号
import re
patten=r'1[3456789]\d{9}'
string='中奖号码为5101803，中奖人手机号为13816222960'
match=re.sub(patten,string,)
re.s
#替换危险字符