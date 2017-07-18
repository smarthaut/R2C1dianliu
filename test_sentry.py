#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/17 13:28
# @Author  : huanghe
# @Site    : 
# @File    : test_sentry.py
# @Software: PyCharm


import requests


url = 'http://10.50.4.151:10000/'
req = requests.get(url=url)

print(req.text)