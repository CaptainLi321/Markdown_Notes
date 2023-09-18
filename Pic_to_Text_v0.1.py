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


    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件

    params = {"image":s}
    access_token = '24.8159c8a52e5c458a0db1d366828aa206.2592000.1697166443.282335-24585254'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.text)

    str=response.text
    str=re.sub(r".*\"words_result\":\[(.*?)\].*", r'\1,', str)
    str=re.sub(r'\{\"words\":\"(.*?)\"\},', r'\1\n', str)

    path = 'input.png'
    if os.path.isfile(path):
        os.remove(path)

    print(str+'\n')
    pyperclip.copy(str)

    toaster = ToastNotifier()
    toaster.show_toast("Done, Copied",
                    str,
                    duration=10)
else:
    print("No Input")
