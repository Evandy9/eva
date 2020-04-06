#coding=utf-8

#python有道翻译
#防止不要过度频繁被认为是机器人

# import urllib.request
# import urllib.parse
# import json
# import time
#
# while True:
#     content = input('pls key in the content which you want to tanslate:')
#     if content == 'q!':
#         break
#     else:
#         url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#         data = {} #字典中要加入key和value
#
#         data['i'] = content
#         data['from'] = 'AUTO'
#         data['to'] = 'AUTO'
#         data['smartresult'] = 'dict'
#         data['client'] = 'fanyideskweb'
#         data['salt'] = '15860131102674'
#         data['sign'] = '2c7258c9ed7171d79b86a5aec0fa0196'
#         data['ts'] = '1586013110267'
#         data['bv'] = '2e73e56db60f3c3df338f1d78a7a2059'
#         data['doctype'] = 'json'
#         data['version'] = '2.1'
#         data['keyfrom'] = 'fanyi.web'
#         data['action'] = 'FY_BY_REALTlME'
#
#         data = urllib.parse.urlencode(data).encode('utf-8')
#
#         req = urllib.request.Request(url, data)
#
#         req.add_header('User-Agent',
#                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')
#         # 隐藏header规避模拟user-agent
#         response = urllib.request.urlopen(url, data)
#
#         html = response.read().decode('utf-8')
#
#         target = json.loads(html)
#
#         print('the result is: %s' % (target['translateResult'][0][0]['tgt']))  # 检索关键字
#         time.sleep(5)
        #print(req.headers)

# #response = urllib.request.urlopen('http://placekitten.com/200/300')
# req=urllib.request.Request('http://placekitten.com/200/300')
# response=urllib.request.urlopen(req)
# #open the url either can be a string or a Request object
# cat_img = response.read()
#
# with open('/home/evandy/cat_b.jpg','wb') as f:
#     f.write(cat_img)
#
# print(response.geturl())
# print(response.info())
# print(response.getcode())

#------------------------------------------------------------------------------------
#代理

import urllib.request
import random
url='https://www.ip138.com/'
iplist=['175.42.123.178:9999','120.83.101.202:9999','183.166.21.230:9999']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)}) #三件套
opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent',
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36')]
urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)

html=response.read().decode('gb2312')

print(html)