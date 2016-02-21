#!/bin/python
s = 0
for i in range(999) :
	if (i%5==0 and i%3==0) :
		s += i
	elif i%5==0:
		s += i
	elif i%3==0:
		s += i

print "%d" % s