#!/bin/python

from fractions import gcd


high = 3./7
minN = 0
minim = 1
for d in range(10, 1000000):
	n = int(high/(1./d))
	if gcd(n, d) == 1 and high-n*1./d < minim:
		minim = high-n*1./d
		minN = n
	
print minN