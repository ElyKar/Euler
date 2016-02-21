#!/bin/python

from math import sqrt

def div(x):
	cur = 2
	while cur <= sqrt(x):
		if x%cur == 0: return False
		cur += 1
	return x != 1

def add(dim):
	for i in range(4):
		n = l[-1]+dim-1
		l.append(n)
		if div(n): primes.append(n)

l = [1]
primes = []
add(3)

dim = 3

while len(primes)*10 > len(l):
	dim += 2	
	add(dim)

print dim