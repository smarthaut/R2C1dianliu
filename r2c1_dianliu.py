#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/18 10:33
# @Author  : huanghe
# @Site    : 
# @File    : r2c1_dianliu.py
# @Software: PyCharm


from socket import *
import re


def get_sessionID(ip,port,paid):
	HOST = ip
	PORT = port
	paid = paid
	he = HOST+':'+str(PORT)
	DATA = 'SETUP rtsp://'+HOST+':'+str(PORT)+ 'RTSP/1.0\r\nContent-Type: application/sdp\r\nCSeq: 26243\r\nOnDemandSessionId: c2dcb90100000040800001005e000302\r\nRequire: com.comcast.ngod.r2,com.comcast.ngod.r2.decimal_npts\r\nSessionGroup: 70001-0\r\nStreamControlProto: rtsp\r\nTransport: MP2T/DVBC/UDP;unicast;client=00:19:56:e8:37:5b;bandwidth=3750000;destination=225.25.25.35;client_port=<EOF>;sop_name=SEACnnnnn\r\nVolume: 80222\r\nContent-Length: 175\r\n\r\nv=0\r\no=- c2dcb90100000040800001005e000302 0 IN IP4 10.11.0.22:2931\r\ns=\r\nt=0 0\r\na=X-playlist-item: xor.com '+paid+' \r\nc=IN IP4 0.0.0.0\r\nm=video 0 udp MP2T\r\n\r\n\r\n\r\n\r\n'
	ADDR = (HOST,PORT)
	obj = socket(AF_INET,SOCK_STREAM)
	obj.connect(ADDR)
	obj.send(DATA.encode('utf-8'))
	data = str(obj.recv(1024),encoding='utf-8')
	sessionID = re.search(r'Session: (\d+)',data,re.M|re.I).group()[9:]
	print('SessionID为：'+sessionID)
	num = '0'
	while num != 'q':
		print('PLAY----------------------1')
		print('PAUSE---------------------2')
		print('FF_PLAY-------------------3')
		print('FR_PLAY-------------------4')
		print('请输入选择')
		num = input()
		if num == '1':
			DATA = 'PLAY * RTSP/1.0\r\nCSeq: 2\r\nRequire: com.comcast.ngod.c1,com.comcast.ngod.c1.decimal_npts\r\nSession: '+sessionID+'\r\nUser-Agent: ITVLibrary 1.0; amino\r\nRange: npt=now-\r\nScale: 1.000000\r\n\r\n'
			obj.send(DATA.encode('utf-8'))
			data = str(obj.recv(1024), encoding='utf-8')
			print(data)
		elif num == '2':
			DATA = 'PAUSE * RTSP/1.0\r\nCSeq: 2\r\nRequire: com.comcast.ngod.c1,com.comcast.ngod.c1.decimal_npts\r\nSession: '+sessionID+'\r\nUser-Agent: ITVLibrary 1.0; amino\r\nScale: 1.000000\r\n\r\n'
			obj.send(DATA.encode('utf-8'))
			data = str(obj.recv(1024), encoding='utf-8')
			print(data)
		elif num == '3':
			DATA = 'PLAY * RTSP/1.0\r\nCSeq: 2\r\nRequire: com.comcast.ngod.c1,com.comcast.ngod.c1.decimal_npts\r\nSession: '+sessionID+'\r\nUser-Agent: ITVLibrary 1.0; amino\r\nRange: npt=now-\r\nScale: 2.000000\r\n\r\n'
			obj.send(DATA.encode('utf-8'))
			data = str(obj.recv(1024), encoding='utf-8')
			print(data)
		elif num == '4':
			DATA = 'PLAY * RTSP/1.0\r\nCSeq: 2\r\nRequire: com.comcast.ngod.c1,com.comcast.ngod.c1.decimal_npts\r\nSession: ' + sessionID + '\r\nUser-Agent: ITVLibrary 1.0; amino\r\nRange: npt=now-\r\nScale: -2.000000\r\n\r\n'
			obj.send(DATA.encode('utf-8'))
			data = str(obj.recv(1024), encoding='utf-8')
			print(data)