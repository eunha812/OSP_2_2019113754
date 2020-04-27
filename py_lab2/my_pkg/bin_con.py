#!/usr/bin/python

def convert(inb):
	s = str(inb)
	m = '0b'
	s = m + s	

	value = int(s,2)

	o = format(value, 'o')
	h = format(value, 'X')

	print("=> OCT> " + str(o))
	print("=> DEC> " + str(value))
	print("=> HEX> " + str(h))

	print()
	print()	
