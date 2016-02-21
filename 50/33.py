#!/bin/python

den = 1
num = 1
for i in range(1, 10):
	for d in range(1, i):
		for n in range(1, d):
			if (d*(10*n+i) == n*(10*i+d)):
				den *= d
				num *= n

print "%d : %d" % (num, den)