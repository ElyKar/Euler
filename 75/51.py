#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

def value(x):
	count = 0
	for i in range(1, 10):
		if div(int(x.replace('*',str(i)))): count += 1
	return count
	
primes = [x for x in range(1000000) if div(x)]

print "init"

for p in primes:
	for i in range(10):
		if str(i) in str(p) and value(str(p).replace(str(i), '*')) == 8: print p
