#!/usr/bin/python

import string
from my_pkg.bin_con import *
from my_pkg.set_prt import *

while True:
	op = int(input('Select menu: 1)conversion 2)union/intersection 3)exit ? '))
	if op == 1:
		inb = input('input binary number : ')
		convert(inb)

	elif op == 2:
		str1 = input('1st list: ')
		str2 = input('2nd list: ')
		setprt(str1,str2)

	elif op == 3:
		print('exit the program...')
		break

	else:
		print('Error, option is not found\n')
	
