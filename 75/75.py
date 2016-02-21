#!/bin/python

fact = [1,1,1*2,2*3,2*3*4,2*3*4*5,2*3*4*5*6,2*3*4*5*6*7,2*3*4*5*6*7*8,2*3*4*5*6*7*8*9]

def next(x):
	res = 0
	for d in str(x):
		res += fact[int(d)]
	return res

s = 0
for i in range(1000000):
	loop = []
	start = i
	while start not in loop:
		loop.append(start)
		start = next(start)
	if len(loop) == 60: s += 1
print s