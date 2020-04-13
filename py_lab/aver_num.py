#!/usr/bin/python

N = int(input("input number N:"))
list = [0 for _ in range(N)]

cnt = 0
for i in range(N):
	cnt = i+1
	print("input %d th number:" % cnt) 
	list[i] = int(input())

sum = 0
for i in range(0, N, 1):
	sum += list[i]

average = sum/N

print("average is :",end="")
print(average) 

