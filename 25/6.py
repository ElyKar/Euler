#!/bin/python
s = 0
square = 0
for i in range(101):
	s += i
	square += i*i


print "%d" % (s*s-square)