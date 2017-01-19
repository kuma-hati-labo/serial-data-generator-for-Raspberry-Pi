#! /usr/bin/env python
# -*- coding:utf-8 -*-

#
# シリアルポートから 0x41-0x5A('A'-'Z') の循環データを出力するプログラム
#

import sys
import serial

argvs = sys.argv
argc = len(argvs)
if (argc != 2):
	print u"Error:Need transfar rate"
	sys.exit()

ser = serial.Serial('/dev/ttyAMA0', int(argvs[1]))

for i in range(0,1000000):
	for data in range(65, 91):
		ser.write(chr(data))

ser.close()

