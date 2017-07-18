#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 17:35
# @Author  : huanghe
# @Site    : 
# @File    : test_ftp.py
# @Software: PyCharm


import requests


filenaem = "ftp_content.xml"
f = open(filenaem)
DATA = "".join(f.readlines())
URl = 'http://10.50.4.151:8080/TransferContent'

r = requests.post(url=URl,data=DATA)
print(r.status_code)

