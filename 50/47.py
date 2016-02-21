#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1
	
primes = set([x for x in range(10000) if div(x)])

def fact(x):
	divs = []
	cur = 2
	X = x
	while X != 1:
		if X % cur == 0:
			divs.append(cur)
			X = X / cur
			cur = 2
		else:
			cur += 1
	return divs


def hasFourFact(x):
	factors = set(fact(x))
	if len(factors) != 4: return False
	for f in factors:
		if f not in primes: return False
	return True

flag = True
cur = 68000
while flag:
	if cur % 1000 == 0: print cur
	if hasFourFact(cur) and hasFourFact(cur+1) and hasFourFact(cur+2) and hasFourFact(cur+3):
		flag = False
	else:
		cur = cur+1
		
print cur