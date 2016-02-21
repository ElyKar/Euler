#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

primes = [x for x in range(1000000) if div(x)]

maxSuit = 0
maxPrime = 0
for i in range(len(primes)):
	curI = i+1
	curP = primes[i]
	while curI < len(primes) and curP < 1000000:
		if div(curP) and curI-i > maxSuit:
			maxSuit = curI-i
			maxPrime = curP
			print "%d : %d" % (maxSuit, maxPrime)
		curP += primes[curI]
		curI += 1

print maxPrime