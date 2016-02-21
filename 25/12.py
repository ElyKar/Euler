#!/bin/python
s = 0
maxdiv = 0
cur = 0
while (maxdiv < 500):
	count = 1
	s = s+cur
	cur = cur+1
	for i in range(2, s):
		if s%i == 0:
			count = count+1
	if count > maxdiv:
		maxdiv = count
		print "%d" % count
	
	
print "%d" % s