#!/bin/python

from fractions import gcd

lowerBound = 1./3
higherBound = 0.5
count = 0
for d in range(4, 12001):
	start = int(lowerBound/(1./d))+1
	while start*1./d < higherBound:
		if gcd(start, d) == 1:
			count += 1
		start += 1
print count