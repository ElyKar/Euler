#!/bin/python

dim = 1001
square = dim*dim
cur = 0
s = 0
while square != 1:
	for i in range(4):
		s += square
		square -= dim-(2*cur+1)
		print square
	cur += 1
s+=1
print "%d" % s