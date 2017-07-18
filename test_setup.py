#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 9:20
# @Author  : huanghe
# @Site    : 
# @File    : test_setup.py
# @Software: PyCharm


from  socket import *
import re

class TcpClient():
	DATA = 'SETUP rtsp://10.50.4.151:554 RTSP/1.0\r\nContent-Type: application/sdp\r\nCSeq: 26243\r\nOnDemandSessionId: c2dcb90100000040800001005e000302\r\nRequire: com.comcast.ngod.r2,com.comcast.ngod.r2.decimal_npts\r\nSessionGroup: 70001-0\r\nStreamControlProto: rtsp\r\nTransport: MP2T/DVBC/UDP;unicast;client=00:19:56:e8:37:5b;bandwidth=3750000;destination=225.25.25.35;client_port=<EOF>;sop_name=SEACnnnnn\r\nVolume: 80222\r\nContent-Length: 175\r\n\r\nv=0\r\no=- c2dcb90100000040800001005e000302 0 IN IP4 10.11.0.22:2931\r\ns=\r\nt=0 0\r\na=X-playlist-item: xor.com CMEftps020170717F001 \r\nc=IN IP4 0.0.0.0\r\nm=video 0 udp MP2T\r\n\r\n\r\n\r\n\r\n'
	def __init__(self,ip,port):
		HOST = ip
		PORT = port
		ADDR = (HOST,PORT)
		self.client = socket(AF_INET,SOCK_STREAM)
		self.client.connect(ADDR)
		self.client.send(self.DATA.encode('utf-8'))
		date = self.client.recv(1024)
		date1 = str(date,encoding='utf-8')
		print(date1)
		sessionid = re.search(r'Session: (\d+)',date1,re.M|re.I).group()
		print(sessionid[9:])
if __name__ == '__main__':
	print('请输入IP地址：')
	ip = input()
	print('请输入端口号：')
	port = int(input())
	client = TcpClient(ip=ip,port=port)


