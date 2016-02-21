#!/bin/python

def assertRight(x, y, z, p):
	return x+y+z == p and x*x+y*y == z*z

def number(p):
	count = 0
	for x in range(1, p):
		for y in range(x, p):
			if assertRight(x, y, p-(x+y), p): count+=1
	return count


res = [number(p) for p in range(1, 1001)]
maxp = 0
curp = 0
maxi = 0
for p in res:
	if maxi < p:
		maxi = p
		maxp = curp
	curp += 1

print maxp