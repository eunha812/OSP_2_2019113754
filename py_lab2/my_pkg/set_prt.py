#!/usr/bin/python
import string

def setprt(str1,str2):
	str1 = str1.replace(",","")
	str1 = str1.replace("[","")
	str1 = str1.replace("]","")
	str1 = str1.replace(" ","")

	str2 = str2.replace(",","")
	str2 = str2.replace("[","")
	str2 = str2.replace("]","")
	str2 = str2.replace(" ","")

	list1 = list(str1)
	list2 = list(str2)

	list1 = list(map(int,list1))
	list2 = list(map(int,list2))

	s1 = set(list1)
	s2 = set(list2)

	print("=> union ",end='')
	print(s1 | s2)
	print("=> intersection ",end='')
	print(s1 & s2)
