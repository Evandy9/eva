#coding=utf-8

import re

# print(re.search(r'andy','andy loves sleep'))
#
# print('andy loves fuck'.find('andy'))
#search是返回出现的第一次出现的位置
# print(re.search(r'.','andy loves sleep')) #.是通配符类似于*
#print(re.search(r"[.]",'andy.loves sleep')) 与下面相等
# print(re.search(r'\.','andy.loves sleep')) #\转移符
#
# print(re.search(r'\d','andy loves sleep 3 ladies')) #\d匹配数字
#
# print(re.search(r'\d\d\d','andy loves sleep 123'))  #多个\d代表多个数字
#
# print(re.search(r'[aeiou]','andy loves sleep 3 ladies')) #[]代表范围是中括号中的东西
#
# print(re.search(r'[a-e]','andy loves sleep 3 ladies')) #- is range
#
# print(re.search(r'[2-4]','andy loves sleep 34 ladies'))

print(re.search(r'ab{3,10}','andy abbbbbc')) #{} 代表重复次数,代表次数范围

#匹配188
print(re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','188'))
#匹配ip地址,百位是0或1时,[01]{0,1}百位可有可无,\d{0,1}十位可有可无,2[0-4]\d百位是2时十位是0到4中的一个，各位是任意数字，括号括起来是一组，{3}这样的组合重复三次
print(re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])','192.168.1.1'))

print(re.findall(r"[a-z]","andy is the best")) #返回列表
print(re.findall(r"^[a-z]","andy is the best")) #取反

print(re.findall(r"[\n]","andy is the best\n"))

# * = {0,}
# + = {1,}
# ? = {0,1}

#贪婪模式
s="<html><td><sd>"

print(re.findall(r"<.+>",s)) #.+任意字符出现一次以上

#非贪婪模式
print(re.findall(r"<.+?>",s))
print(re.search(r"<.+?>",s))

p=re.compile(r"[A-Z]") #如果多次应用可以进行编译

print(p.findall("andy loVE YOU"))

#verbose开始详细模式