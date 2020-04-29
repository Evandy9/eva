#coding=utf-8

# import urllib.request
# import re
#
# def open_file(url):
#     req = urllib.request.Request(url)
#     req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36')
#     page = urllib.request.urlopen(url)
#     html = page.read()
import urllib.request
import urllib.error

req = urllib.request.Request("http://www.baidu.comn")

try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as p:
    print(p.code)
    print(p.read())
except urllib.error.URLError as e:
    print(e.reason)
else:
    print("everything is all right")

try:
    urllib.request.urlopen(req)
except urllib.error.URLError as f:
    if hasattr(f,'reason'):
        print("we failed to reach the server")
        print("Reason",f.reason)
    elif hasattr(f,"code"):
        print("the server can not fulfill the request.")
        print("error code",f.code)
else:
    print("everything is all right")