#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 10:41
# @Author  : huanghe
# @Site    : 
# @File    : test.py
# @Software: PyCharm


from r2c1_dianliu import get_sessionID



print('请输入要点流的paid')
paid= input()
print('请输入IP地址：')
ip = input()
print('请输入端口号：')
port = int(input())
get_sessionID(ip=ip,port=port,paid=paid)





