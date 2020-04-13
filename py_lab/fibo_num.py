#!/usr/bin/python

n = int(input("fibonacci number? "))

def fib(n) :
	if n == 1 or n == 2 :
		return 1
	return fib(n - 1) + fib(n - 2)

cnt = n + 1
for i in range(1, cnt, 1) : 
	print(fib(i),end="")
	if (i == n):
		break
	print(",",end="")

print("")
print("F%d = " % n ,end="")
print(fib(n)) 
