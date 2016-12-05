#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import serial


argvs = sys.argv
argc = len(argvs)
if (argc != 2):
	print u"Error:Need transfar rate"
	sys.exit()

ser = serial.Serial('/dev/ttyAMA0', int(argvs[1]))

while 1:
	for data in range(0, 256):
		ser.write(chr(data))
		print ".",

ser.close()

