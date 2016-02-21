#!/bin/python

from math import sqrt
from fractions import gcd
import time

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1
	
def firstDiv(n):
	for p in primes:
		if n%p == 0: return p
	return 0

def totient(x):
	if tots[x-1] != 0: return tots[x-1]
	first = firstDiv(x)
	if first == 2:
		div = x/2
		if div%2 == 0: tots[x-1] = 2*totient(div)
		else: 	       tots[x-1] = totient(div)
	else:
		d = gcd(first, x/first)
		if d != 1: 
			tots[x-1] = totient(first)*totient(x/first)*d/totient(d)
		else:
			tots[x-1] = totient(first)*totient(x/first)
	return tots[x-1]
	
def isPerm(i, j):
	x, y = str(i), str(j)
	for letter in x:
		if x.count(letter) != y.count(letter): return False
	return True


primes = [x for x in range(1, 10000000) if div(x)]

tots = [0 for i in range(10000000)]

for p in primes: tots[p-1] = p-1

start = time.time()

minTot = 1000000000
minN = 0
for x in range(2,10000001):
	tot = totient(x)
	if isPerm(x, tot) and x*1./tot < minTot:
		minTot = x*1./tot
		minN = x
print minN
print time.time()-start