#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import time
import math
import base64
import re
import os
import pyperclip
import subprocess
from win10toast import ToastNotifier

count = 1
workdir = os.getcwd()
print("Pic to LaTeX")
print(workdir)
print("Version: 0.5 ")

if os.path.isfile(".\\input.png"):
    os.remove(".\\input.png")
cmd=r'Snipaste snip -o "%s"' % workdir+r'\input.png'
p=subprocess.Popen(cmd,shell=True)
return_code=p.wait()  #等待子进程结束，并返回状态码；
# os.system()


while not os.path.isfile(".\\input.png"):
    time.sleep(0.1)
    pass


if os.path.isfile(".\\input.png"):

    with open(".\\input.png", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()

    print("Converting Pic No.", end='')
    print(count)

    timestamp = math.floor(time.time()*100)
    url = 'http://www.bing.com/cameraexp/api/v1/getlatex'
    headers = {'Host': 'www.bing.com', 'Content-Type': 'application/json', 'Connection': 'keep-alive', 'Accept': 'application/json',
                'User-Agent': 'Math/1 CFNetwork/1121.2.2 Darwin/19.3.0', 'Content-Length': '10136', 'Accept-Language': 'zh-cn', 'Accept-Encoding': 'gzip, deflate, br'}
    cookies = {}
    data = '{"data":"%s","inputForm":"Image","clientInfo":{"app":"Math","platform":"ios","configuration":"Unknown","version":"1.8.0","mkt":"zh-cn"},"timestamp":%d}' % (
        s, timestamp)
    html = requests.post(url, headers=headers,
                            verify=False, cookies=cookies, data=data,)

    str2 = re.sub(r'.*"latex":"(.*?)".*', r'\1', html.text)
    str2 = re.sub(r'\\\\', r'\\', str2)
    str2 = str2 + "\n"

    def save(filename, contents):
        fh = open(filename, 'a', encoding='utf-8')
        fh.write(contents)
        fh.close()
    save("result.txt", "Result No.")
    save("result.txt", str(count))
    save("result.txt", "\n")
    save("result.txt", str2)

    path = 'input.png'
    if os.path.isfile(path):
        os.remove(path)

    print(str2+'\n')
    pyperclip.copy(str2)

    toaster = ToastNotifier()
    toaster.show_toast("Done, Copied",
                    str2,
                    duration=10)
else:
    print("No Input")
