#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 10:33
# @Author  : huanghe
# @Site    : 
# @File    : test_cifs.py
# @Software: PyCharm


import requests


filename = 'cifs_content.xml'
f = open(filename,'r')
URL = 'http://10.50.4.151:8080/TransferContent'
DATA = "".join(f.readlines())


req = requests.post(url=URL,data=DATA)
print(req.status_code)

