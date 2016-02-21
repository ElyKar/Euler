#!/bin/python

from math import sqrt

def div(x):
	if (x % 10000) == 0: print x
	if not pan(str(x), len(str(x))): return False
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	print x
	return x != 1
	
def pan(x, p):
	if '0' in x: return False
	flag = True
	for i in range(1, p+1):
		flag = flag and str(i) in x
	return flag and len(x) == p and len(x) == len(set([i for i in x]))

primes = [x for x in range(7660000, 1, -1) if div(x)]