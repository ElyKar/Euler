#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

primes = [x for x in range(1000000) if div(x)]
squares = [n*n for n in range(1, 1000)]

print "init"

def goldbach(n):
	if (n-1)%10==0: print n
	if n in primes: return True
	idxP = 0
	p = primes[idxP]
	while p < n:
		idxS = 0
		s = squares[idxS]
		while p+2*s <= n:
			if p + 2*s == n: return True
			idxS += 1
			s = squares[idxS]
		idxP += 1
		p = primes[idxP]
	print n
	return False
	
n = 3
while goldbach(n):
	n += 2
