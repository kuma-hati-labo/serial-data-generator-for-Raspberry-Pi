#! /usr/bin/env python
# -*- coding:utf-8 -*-

#
# �V���A���|�[�g���� 0x00-0xFF �̏z�f�[�^���o�͂���v���O����
#

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

ser.close()

